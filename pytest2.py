import cv2

stitcher = cv2.Stitcher.create(0)
ImageLeft = cv2.imread("1.jpg")
ImageMid = cv2.imread("2.jpg")
ImageRight = cv2.imread("3.jpg")
result = stitcher.stitch((ImageLeft,ImageMid,ImageRight))

cv2.imwrite("D:/result.jpg", result[1])