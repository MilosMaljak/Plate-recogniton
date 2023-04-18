import cv2
import pytesseract
import imutils

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
cars = cv2.imread("HS9A5645.jpg")


plate = cascade.detectMultiScale(cars, 1.1, 6)
for(x,y,w,h) in plate:
    plateImg = cars[y:y+h,x:x+w]
    cars = cv2.rectangle(cars,(x,y), (x+w, y+h),(255, 0, 0), 3)

cv2.imshow("image", cars)
cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(plateImg, lang='eng')
print("registration number is", text)
cv2.waitKey(0)