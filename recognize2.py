import cv2
import sys
storage = cv2.CreateMemStorage()
image_path = "yusei.jpg"
img = cv2.imread(image_path)

hc = cv2.Load("../data/haarcascades/haarcascade_frontalface_default.xml")
faces = cv2.HaarDetectObjects(img, hc, storage, 1.1, 3, 0, (0, 0))

max=0
maxh=0
maxw=0
resx=0
resy=0
for (x, y, w, h), n in faces:
  if max<w*h:
    maxw=w
    maxh=h
    resx=x
    resy=y
    max=w*h

sub = cv2.GetSubRect(img, (resx,resy,maxw,maxh))
cv2.SaveImage("face_"+sys.argv[1], sub)
