import numpy as np
import cv2

# For camera or cap = cv2.VideoCapture('Video Name for Video')
cap = cv2.VideoCapture("assets/destiny_icebreaker.mp4")

while True:
    # ret is a checker, frame is the Image itself
    ret, frame = cap.read() 
    width = int(cap.get(3))
    height = int(cap.get(4)) 

    smaller_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5) 

    # Empty image with the shape of the frame
    image = np.zeros(frame.shape, np.uint8)  

    # img = cv2.rotate(img, cv2.ROTATE_180)

    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[height//2:, width//2:] = smaller_frame


    # Display the frame  
    cv2.imshow('frame', image)

    # If q is pressed, break
    if cv2.waitKey(1) == ord('q'):
        break

# release the camera resource and destory all windows
cap.release()
cv2.destroyAllWindows()    