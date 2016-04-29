import numpy as np
import cv2

CAMERA_ID = 0

cap = cv2.VideoCapture(CAMERA_ID)
#out = cv2.VideoWriter('test.avi', cv2.cv.CV_FOURCC(*'XVID'), 20.0, (640, 480))

print('Press \'s\' to save image')
print('Press \'q\' to quit')

i = 1
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
    cv2.imshow('frame', frame)
    #out.write(frame)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
      print('Closing')
      break
    elif k == ord('s'):
      filename = str(i) + '.png'
      print('Saving to ' + filename)
      cv2.imwrite(filename, frame)
      i = i + 1
  else:
    break

cap.release()
#out.release()
cv2.destroyAllWindows()

