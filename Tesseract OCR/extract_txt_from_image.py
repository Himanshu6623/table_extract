import pytesseract
from PIL import Image
import cv2
img=Image.open("marks.png")
myconfig=r"--psm 11 --oem 3"
pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text=pytesseract.image_to_string(img,config=myconfig)
print(text)
#rows=text.split('\n')
#table_data=[row.split('\t') for row in rows]
#for row in table_data:
#    print(row)
#img1=cv2.imread("marksheet.png")
#height,width,_=img1.shape
#boxes=pytesseract.image_to_boxes(img1,config=myconfig)
#for box in boxes.splitlines():
#    box=box.split(" ")
#    img1=cv2.rectangle(img1,(int(box[1]),height-int(box[2])),(int(box[3]),height-int(box[4])),(0,255,0),2)
#    
#cv2.imshow("img",img1)
#cv2.waitKey(0)
