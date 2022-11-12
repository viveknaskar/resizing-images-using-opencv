# Python script to resize multiple images in batch

import cv2
import glob

# glob module is used to retrieve files/pathnames matching a specified pattern.
images = glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    resized_img=cv2.resize(img,(350,250))
    cv2.imshow("Resized Image",resized_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("batch_resized_"+image,resized_img)