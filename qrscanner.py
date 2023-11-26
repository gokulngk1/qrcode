import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr =qrcode.make("https://chat.openai.com/c/7ecc1143-0e8d-4219-a9f1-6d426376f9b5")
myqr.save("myqr.png" ,scale =8)
phone =qrcode.make("9360332436")
phone.save("phone.png")

b= decode(Image.open("phone.png"))
d = decode(Image.open("myqr.png"))
print(d[0].data.decode("ascii"))
print(b[0].data.decode("ascii"))