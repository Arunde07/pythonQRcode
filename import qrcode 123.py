import qrcode
print("QR code generator")
print("created by arun")

data = input("enter input>>  ")

qr = qrcode.make(data)
qr.save("C:/ARUN VS CODE/grnew1.png")

print("QR code generation done")