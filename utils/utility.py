import cv2
import imutils
import numpy as np
def lane(frame):
    image = imutils.resize(frame, width=1000)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 3)
    edge = cv2.Canny(blur, 10, 255)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    # eroded=cv2.erode(edge,kernel,iterations=1)
    dilate = cv2.dilate(edge, kernel, iterations=2)

    lines = cv2.HoughLinesP(dilate, 1, np.pi / 180, threshold=10, lines=np.array([]), minLineLength=85,
                            maxLineGap=10)


    for line in lines[:2]:
        (a, b, c, d) = line[0]

        cv2.line(image, (a, b), (c, d), (0, 255, 0), 4)

    return image