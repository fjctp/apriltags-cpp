import numpy as np
import cv2

cap = cv2.VideoCapture(0)
i = 1
#out = cv2.VideoWriter('test.avi', cv2.cv.CV_FOURCC(*'XVID'), 20.0, (640, 480))

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
    cv2.imshow('frame', frame)
    #out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      print('Closing')
      break
    if cv2.waitKey(1) & 0xFF == ord('s'):
      filename = str(i) + '.png'
      print('Savingi to ' + filename)
      cv2.imwrite(filename, frame)
      i = i + 1
  else:
    break

cap.release()
#out.release()
cv2.destroyAllWindows()

