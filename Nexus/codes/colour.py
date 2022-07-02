import cv2
import numpy as np


def shape(img):
    _, thrash = cv2.threshold(img, 0, 120, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv2.approxPolyDP(
            contour, 0.03 * cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (255, 255, 255), 1)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 0))
        elif len(approx) == 4:
            cv2.putText(img, "rectangle", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 0))
        else:
            cv2.putText(img, "circle", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 0))

    return img


# Reading the image
img = cv2.imread('shape.png')
# Showing the output
cv2.imshow("Image", img)
# convert to hsv colorspace
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower bound and upper bound for Green color
lower_bound_green = np.array([50, 20, 20])
upper_bound_green = np.array([100, 255, 255])
lower_bound_black = np.array([0, 0, 0])
upper_bound_black = np.array([50, 50, 50])
lower_bound_yellow = np.array([20, 80, 80])
upper_bound_yellow = np.array([30, 255, 255])

# find the colors within the boundaries
mask = cv2.inRange(hsv, lower_bound_green, upper_bound_green)
mask1 = cv2.inRange(hsv, lower_bound_yellow, upper_bound_yellow)
mask3 = cv2.add(mask, mask1)
mask4 = cv2.inRange(hsv, lower_bound_black, upper_bound_black)
mask3 = cv2.add(mask3, mask4)
cv2.imshow("Image", shape(mask3))
cv2.waitKey(0)
cv2.destroyAllWindows()
