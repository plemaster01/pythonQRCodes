# Creating and Reading From QR Codes with Python!
import pyqrcode
import cv2
# pip install pyqrcode
# pip install opencv-python
# pip install pypng
# import png
data = 'https://www.youtube.com/channel/UCV5Ab39YnXvTZ6Grar9URxQ?sub_confirmation=1'
url = pyqrcode.create(data)
# create and save qr code as image files
url.png('myQR2.png', scale=6)
url.svg('myQR2.svg', scale=8)
img = cv2.imread('myQR1.png')
det = cv2.QRCodeDetector()
val, pts, st_code = det.detectAndDecode(img)
print(val)