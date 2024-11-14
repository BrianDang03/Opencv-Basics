import numpy as np
import cv2

def FindObject(img, template, object_name, method, method_name):
    height, width = template.shape
    img_copy = img.copy()
    grey_img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    object_result = cv2.matchTemplate(grey_img_copy, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(object_result)

    if method in [cv2.TM_SQDIFF, cv2.TM_CCORR_NORMED]:
        location = min_loc        
    else:
        location = max_loc   

    bottom_right = (location[0] + width, location[1] + height) 
    cv2.rectangle(img_copy, location, bottom_right, (0, 204, 0), 5)
    img_copy = cv2.resize(img_copy, (0, 0), fx = 0.5, fy = 0.5)  

    img_copy = WriteText(img_copy, f"Find: {object_name}, {method_name}")

    return img_copy

def WriteText(img, text):
    font = cv2.FONT_ITALIC
    height = img.shape[0]
    # Adding the combined corner img and original
    img = cv2.putText(img, text, (0, height - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return img

def CombineImage(img, img2):
    combined_img = np.zeros(img.shape, np.uint8)
    combined_img = cv2.resize(combined_img, (0, 0), fx = 2, fy = 1)
    height = combined_img.shape[0]
    width = combined_img.shape[1]

    combined_img[:height, :width//2] = img
    combined_img[:height, width//2:] = img2

    return combined_img

def main():

    img = cv2.imread("assets/traveler.png", 1)
    sitting_titan_template = cv2.imread("assets/sitting_titan.png", 0)
    blue_ghost_template = cv2.imread("assets/blue_ghost.png", 0)
   
    # Chose a font
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    method_names = {cv2.TM_CCOEFF:"TM_CCOEFF", cv2.TM_CCOEFF_NORMED:"TM_CCOEFF_NORMED", cv2.TM_CCORR:"TM_CCORR", cv2.TM_CCORR_NORMED:"TM_CCORR_NORMED", cv2.TM_SQDIFF:"TM_SQDIFF", cv2.TM_SQDIFF_NORMED:"TM_SQDIFF_NORMED"}

    for method in methods:   
        
        sitting_titan_img = FindObject(img, sitting_titan_template, "Sitting Titan" , method, method_names[method], )
        blue_ghost_img = FindObject(img, blue_ghost_template, "Blue Ghost" , method, method_names[method])
        
        combined_img = CombineImage(sitting_titan_img, blue_ghost_img)
        combined_img = cv2.resize(combined_img, (0, 0), fx = 0.8, fy = 0.8)

        cv2.imshow("Match", combined_img) 
                    
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

main()        