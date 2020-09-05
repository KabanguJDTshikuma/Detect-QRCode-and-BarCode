import pyqrcode
import png
from pyqrcode import QRCode


def qrcode_gerator(datas):
    for code in datas:
        qc = pyqrcode.create(code)
        qc.png(f'test_{code}.png', scale=8)
        print(code)
    return "Done"


if __name__ == '__main__':
    with open('datas.txt') as f:
        datas_list = f.read().splitlines()

    qrcode_gerator(datas_list)


# import qrcode
# from qrcode.image.pure import PymagingImage
#
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
#
# qr.add_data('test')
# qr.make(fit=True)
#
# # img = qr.make_image(fill_color="black", back_color="white")
# img = qr.make('test', image_factory=PymagingImage)
# img = qr.add_data(data='33333325475')
#
# print(img)
