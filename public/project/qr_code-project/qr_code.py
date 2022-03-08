import qrcode

#Create QR Code for some text, kanji, etc.
data = 'www.kylejeffreyreese.com'
img = qrcode.make(data)
#img.save(r'C:\Users\gregg\Desktop\QR Code\website_qr_code.png')

#Create QR Code with additional parameters (color, size, etc.)
qr = qrcode.QRCode(version = 1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'green', back_color = 'blue')

img.save(r'C:\Users\gregg\Desktop\QR Code\website_qr_code1.png')
