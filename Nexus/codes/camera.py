import cv2


def shape(img):
    _, thrash = cv2.threshold(img, 200, 200, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv2.approxPolyDP(
            contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 4:
            cv2.putText(img, "rectangle", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        elif len(approx) > 8:
            cv2.putText(img, "Circle", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    return img

cam = cv2.VideoCapture(0)
while(cam.isOpened()):
    aval, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img=shape(gray)
    cv2.imshow('frame', img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
