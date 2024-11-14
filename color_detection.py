import numpy as np
import cv2

cap = cv2.VideoCapture('assets/destiny_icebreaker.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    smaller_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    smaller_hsv = cv2.resize(hsv, (0, 0), fx = 0.5, fy = 0.5)

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    smaller_mask = cv2.resize(mask, (0, 0), fx = 0.5, fy = 0.5)

    result = cv2.bitwise_and(frame, frame, mask = mask)
    smaller_result = cv2.resize(result, (0, 0), fx = 0.5, fy = 0.5)
       
    image = np.zeros(frame.shape, np.uint8)   

    # Chose a font
    font = cv2.FONT_ITALIC
        
    # Image to draw, msg, bottom left, font, scale of the font, color, thickness, 
    smaller_frame = cv2.putText(smaller_frame, "Original", (0, height//2 - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    image[:height//2, :width//2] = smaller_frame

    # Image to draw, msg, bottom left, font, scale of the font, color, thickness, 
    smaller_hsv = cv2.putText(smaller_hsv, "HSV", (0, height//2 - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    image[:height//2, width//2:] = smaller_hsv


    # Image to draw, msg, bottom left, font, scale of the font, color, thickness, 
    smaller_mask = cv2.putText(smaller_mask, "Mask", (0, height//2 - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    image[height//2:, :width//2] = cv2.cvtColor(smaller_mask, cv2.COLOR_GRAY2BGR)

    # Image to draw, msg, bottom left, font, scale of the font, color, thickness, 
    smaller_result = cv2.putText(smaller_result, "Original+Mask", (0, height//2 - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    image[height//2:, width//2:] = smaller_result
    
    image = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)

    cv2.imshow('frame', image)  

    if cv2.waitKey(int(1000/100)) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# BGR_color = np.array([[[255, 0, 0]]])
# print(cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV))
# [[[hsv value]]]

# x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV
# x[0][0] is on pixel 