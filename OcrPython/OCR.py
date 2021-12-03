import cv2,numpy,pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
img = cv2.imread("denemeFoto/image_5.bmp")

img=cv2.resize(img,None,fx=0.5,fy=0.5)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,81)
#4,11,12,15
#101,81
ocr_result = pytesseract.image_to_string(adaptive_threshold, lang='eng',config='--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789')
print(ocr_result)
#cv2.imshow("gray",gray)
cv2.imshow("adaptive",adaptive_threshold)
cv2.waitKey(0)