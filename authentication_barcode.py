import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('datas.txt') as f:
    datas_list = f.read().splitlines()

print(datas_list)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        mydata = barcode.data.decode('utf-8')
        print(mydata)

        if mydata in datas_list:
            print("Successful Authenticated")
        else:
            print("Failed to authenticate!!!")

        # build a shape around the detected barcode.
        pts = np.array([barcode.polygon], np.int32)
        pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)

        # show the data of the barcode
        pts2 = barcode.rect
        cv2.putText(img, mydata, (pts2[0], pts2[1]),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(1)
