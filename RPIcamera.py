import cv2
import numpy as np
import picamera
import io

stream = io.BytesIO()

cam = picamera.PiCamera()

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
cam.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)
count = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (CAMERA_HEIGHT,CAMERA_WIDTH))


while(1):
    cam.capture(stream, format='jpeg')
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    frame = cv2.imdecode(data, 1)
    cv2.imshow('frame',frame)
    out.write(frame)
    count += 1
    print(count)
    stream.seek(0)
    key = cv2.waitKey(20)
    if key == ord('q'):
        break
out.release()
cv2.destroyAllWindows()

