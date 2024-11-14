import cv2

img = cv2.imread('assets/forest.jpg', 1)

# Resizing image
# img = cv2.resize(img, (400, 400))
# Scaling Image
img = cv2.resize(img, (0, 0), fx = 0.1, fy=0.1)

# Rotate image
img = cv2.rotate(img, cv2.ROTATE_180)

# Save an Adjuest Image
cv2.imwrite('new_assets/new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()