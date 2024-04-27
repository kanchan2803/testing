import cv2

def capture_image():
  cam = cv2.VideoCapture(0)
  cv2.namedWindow("Webcam")

  captured = False

  while True:
    ret, frame = cam.read()

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1)

    if key % 256 == ord('c'):
      captured = True
      break

    if key % 256 == ord('q'):
      break

  if captured:
    cv2.imwrite("captured_image.jpg", frame)
    print("Image captured!")
    
  cam.release()
  cv2.destroyAllWindows()

