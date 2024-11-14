import numpy as np
import cv2

cap = cv2.VideoCapture('assets/destiny_icebreaker.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    smaller_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)

    # Source Image, Number of best corners, quality of corner, min euclidean distance between two corners 
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    smaller_gray_img = cv2.resize(gray_img, (0, 0), fx = 0.5, fy = 0.5)
    corners = cv2.goodFeaturesToTrack(gray_img, 1000, 0.01, 10)
    corners = np.int_(corners)
    # Corner Image
    corner_img = np.zeros(frame.shape, np.uint8)
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(corner_img, (x, y), 5, (255, 0, 0), -1)
    smaller_corner_img = cv2.resize(corner_img, (0, 0), fx = 0.5, fy = 0.5)

    # Frame Corner Image
    frame_corner_img = frame.copy()
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(frame_corner_img, (x, y), 5, (255, 0, 0), -1)
    smaller_frame_corner_img = cv2.resize(frame_corner_img, (0, 0), fx = 0.5, fy = 0.5)

    # Chose a font
    font = cv2.FONT_ITALIC

    # Empty Image for both originl and corner image
    img = np.zeros(frame.shape, np.uint8)

    # Adding the original to img
    smaller_frame = cv2.putText(smaller_frame, "Original", (0, height//2 - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    img[:height//2, :width//2] = smaller_frame

    # Adding the gray img to img
    smaller_gray_img = cv2.putText(smaller_gray_img, "Greyscale", (0, height//2 - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    img[:height//2, width//2:] = cv2.cvtColor(smaller_gray_img, cv2.COLOR_GRAY2BGR)

    # Adding the corner img to img
    smaller_corner_img = cv2.putText(smaller_corner_img, "Corners", (0, height//2 - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    img[height//2:, :width//2] = smaller_corner_img

    # Adding the combined corner img and original
    smaller_frame_corner_img = cv2.putText(smaller_frame_corner_img, "Original+Corners", (0, height//2 - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    img[height//2:, width//2:] = smaller_frame_corner_img

    img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)

    cv2.imshow('Frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()