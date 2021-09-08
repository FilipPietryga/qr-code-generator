import qrcode
import cv2
import sys

d = cv2.QRCodeDetector()

while True:
    choice = int(input("""Welcome to the qr-code-generator program!
1. create 
2. analyze
3. quit
select your option
>"""))

    if(choice == 1):
        data = input("Insert data to put into qrcode!\n>")
        img = qrcode.make(data)
        filename = input("How would you like to call your file?\n>")
        filename += ".jpg"
        img.save(filename)
        print("The image has been saved successfully!!")
    if(choice == 2):
        url = input("insert file name\n>")
        url += ".jpg"
        val, _, _ = d.detectAndDecode(cv2.imread(url))
        print("The qr-code contains:", val)
    if(choice == 3):
        sys.exit()
