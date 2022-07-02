from turtle import distance, width
import cv2
from cv2 import sqrt
import serial
import struct
import time


def distance(x1, y1, x2, y2):
    print(x2, y2)
    return round(sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))[0][0], 2)


arduino = serial.Serial('COM6', 9600)
time.sleep(2)

img = cv2.imread('shape.png')
h, w, channel = img.shape
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
val, thresh = cv2.threshold(img, 220, 250, cv2.THRESH_BINARY)
cv2.imshow("threshold", thresh)
contours, val = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
dic = {}
min = 500
for contour in contours:
    approx = cv2.approxPolyDP(
        contour, 0.03 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 1)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        d = distance(h/2, w/2, x, y)
        print(d)
        dic[d] = ("t", (x, y))
        if d < min:
            min = d
        cv2.putText(img, "Triangle", (x, y),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 4:
        d = distance(h/2, w/2, x, y)
        dic[d] = ("r", (x, y))
        if d < min:
            min = d
        cv2.putText(img, "rectangle", (x, y),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (150, 150, 160))

    elif len(approx) > 7:
        d = distance(h/2, w/2, x, y)
        print(d)
        dic[d] = ("c", (x, y))
        if d < min:
            min = d
        # cv2.putText(img, "Circle", (x, y),
            #   cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
print("closest", dic[min])
close = dic[min]

if(close[0] == 'c'):
    speeda = 50*(close[1][0]-h)
    speedb = 50*(close[1][1]-w)
    blink = 0

if(close[0] == 'r'):
    speeda = 50*(close[1][0]-h)
    speedb = -120
    blink = 1

if(close[0] == 't'):
    speeda = -120
    speedb = 50*(close[1][1]-w)
    blink = 2

arduino.write(struct.pack('>BBB', speeda, speedb, blink))
cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
