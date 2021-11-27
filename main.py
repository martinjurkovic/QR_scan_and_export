# %%
import cv2
import qrcode
import qrcode.image.svg
import sys
import argparse

# %%
parser = argparse.ArgumentParser()

#-db DATABSE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-fp", "--filepath", help="Path to image with QR code")
parser.add_argument("-qrv", "--qrversion", help="Version of QR code (from 1-40)", type=int)
parser.add_argument("-et", "--exporttype", help="File type of exported qr code (svg, jpg, png...)")
args = parser.parse_args()

# %%
try:
    file_path = args.filepath
except Exception as e:
    print('No file specified!')

image_factory = None
qr_version = None
export_type = '.jpg'

if args.qrversion:
    qr_version = args.qrversion
    
if args.exporttype:
    export_type = args.exporttype
    if export_type == 'svg':
        image_factory = qrcode.image.svg.SvgPathImage
    else:
        image_factory = None


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
        image_factory=image_factory)
qr.add_data(val)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
if not qr_version:
    qr_version = 'default'
save_path = f'{directory_path}/{file_name}_ver_{qr_version}.{export_type}'
img.save(save_path)

print(f'File saved to: {save_path}')

# %%
