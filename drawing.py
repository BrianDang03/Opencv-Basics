import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Image to draw, start, end location, color, thickness
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.line(img, (width//2, 0), (width//2, height), (0, 0, 255), 1)

    # Image to draw, Top Left, Bottom Right, color, thickness: -1 fills the entire thing    
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)

    # Image to draw, center, radius, color, thickness: -1 filles entire shape    
    img = cv2.circle(img, (300, 300), 60, (234, 102, 45), -1)

    # Chose a font
    font = cv2.FONT_ITALIC
    # Image to draw, msg, bottom left, font, scale of the font, color, thickness,  
    img = cv2.putText(img, "Hello World!", (200, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2. waitKey(1) == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()