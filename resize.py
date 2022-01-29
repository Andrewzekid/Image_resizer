import cv2 as cv
import PIL
import pathlib

basepath = pathlib.Path(".")
image_files = basepath.glob("*.jpg")

for image in image_files:
    img = cv.imread(str(image), cv.IMREAD_UNCHANGED)
    
    print('Original Dimensions : ',img.shape)
    
    scale_percent = 50 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    
    print('Resized Dimensions : ',resized.shape)
    
    cv.imshow("Resized image", resized)
    cv.waitKey(0)
    cv.imwrite(str(image)[:-4] + "_resized_50.jpg",resized)
    cv.destroyAllWindows()