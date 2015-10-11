import cv2

cascade_path = "../lib/haarcascades/haarcascade_frontalface_alt.xml"
image_path = "img/yusei2.png"

color = (255, 255, 255)

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_path)

facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

if len(facerect) > 0:
  for rect in facerect:
    cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
else:
  print("no face")

cv2.imshow("detected.jpg", image)

while(1):
  if cv2.waitKey(10) > 0:
    break
