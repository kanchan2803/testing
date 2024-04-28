import pytesseract
import cv2
#from click import capture_image
#pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

myconfig = r"--psm 11 --oem 3"

def extract_text(image_path):
  img = cv2.imread(image_path)

  # cv2.imshow("img",img)
  # cv2.waitKey(0)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Text extraction
  text = pytesseract.image_to_string(gray,config=myconfig)

  height, width, _ = img.shape

  boxes = pytesseract.image_to_boxes(img, config=myconfig)

  for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height-int(box[2])), (int(box[3]), height-int(box[4])), (0,200,0), 2)

  print("Extracted Text:\n", text)
  return img,text

# capture_image()
# extract_text("captured_image.jpg")
