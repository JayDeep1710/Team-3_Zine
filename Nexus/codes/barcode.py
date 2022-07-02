import numpy as np
import cv2

img = cv2.imread('bar.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
val, thresh = cv2.threshold(img, 120, 200, cv2.THRESH_BINARY)
contours, val = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
s = ""
i = 0
for contour in contours:
    approx = cv2.approxPolyDP(
        contour, 0.02 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (150, 150, 150), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 4:
        i += 1
        if(cv2.contourArea(contour) in range(18000, 25000)):
            s += "0"
            cv2.putText(img, "0", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif(cv2.contourArea(contour) in range(45000, 50000)):
            s += "1"
            cv2.putText(img, "1", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

print(s[::-1])
number = 0
for i in range(len(s)):
    if s[i] == "1":
        number = number+pow(2, i)
print(number)

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
