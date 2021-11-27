# %%
import cv2
import qrcode
import qrcode.image.svg
import sys

# %%
try:
    file_path = sys.argv[1]
except Exception as e:
    print('No file specified!')

if len(sys.argv) > 2:
    qr_version = sys.argv[2]
else:
    qr_version = 18

# %%
splitted = file_path.rsplit("/", 1)
directory_path = splitted[0]
file_name = splitted[1].rsplit(".")[0]


# %%
print('Reading file...')
try:
    img=cv2.imread(file_path)
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
except Exception as e:
    sys.exit('Cant read QR code from image file!')

print('File read successfully!')
print(f'QR code value:\n{val}\n')

# %%
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=qr_version,
        box_size=10,
        border=5,
        image_factory=qrcode.image.svg.SvgPathImage)
qr.add_data(val)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
save_path = f'{directory_path}/{file_name}_ver{qr_version}.svg'
img.save(save_path)

print(f'File saved to: {save_path}')

# %%
