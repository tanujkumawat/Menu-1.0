import cv2

cap = cv2.VideoCapture(0)

ret , photo = cap.read()

print(ret)

cv2.imwrite('/root/Desktop/capAk.png',photo)

cap.release()

