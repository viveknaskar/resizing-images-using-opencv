# Python script to resize an image

import cv2

# the second parameter is specified the get the color band
# of the image where 0 is for grayscale

img=cv2.imread("potrait.jpg", 0)

# python stores the image as Numpy array
print(type(img))

# fetching the size of the image, which (1080, 1920) in this case
print(img.shape)

# resizing images using the resize method
resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# displaying the image
cv2.imshow("Potrait", resized_image)

cv2.imwrite("NewPotrait.jpg", resized_image)

# waitkey will wait for n seconds & then closes automatically
cv2.waitKey(2000)

cv2.destroyAllWindows()