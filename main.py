import cv2
import argparse
from utils.utility import lane

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=False, help='input image')
ap.add_argument('-v', '--video', required=False, help='video file')
args = vars(ap.parse_args())

if not args.get('image'):
    if not args.get('video'):
        camera = cv2.VideoCapture(0)
    else:
        camera = cv2.VideoCapture(args["video"])
    camera.set(3, 640)
    camera.set(4, 480)

    while True:
        ret, frame = camera.read()
        fourcc = cv2.VideoWriter_fourcc(*'FMP4')
        out = cv2.VideoWriter('video/output.mp4', 0x7634706d, 20.0, (640, 480))
        if ret is None:
            break

        output = lane(frame)
        out.write(output)
        cv2.imshow("output", output)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
else:
    image = cv2.imread(args["image"])
    output = lane(image)
    cv2.imwrite('image/output.jpg')
    cv2.imshow("output", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
