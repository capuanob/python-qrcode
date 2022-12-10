#!/usr/bin/env python3
import atheris
import logging
import sys

with atheris.instrument_imports(include=[
    'qrcode'
    #'qrcode.constants',
    #'qrcode.exceptions',
    #'qrcode.util',
    #'qrcode.LUT',
    #'qrcode.base',
    #'qrcode.image',
    #'qrcode.image-base',
    #'qrcode.image.styles',
    #'qrcode.image.styles.moduledrawers',
    #'qrcode.image.styles.moduledrawers.pil',
    #'qrcode.compat',
    #'qrcode.compat.util',
    #'qrcode.image.styles.moduledrawers.base',
    #'qrcode.image.pure'
   ],
   exclude=[
       'qrcode.compat.pil',
       'qrcode.image.styles.moduledrawers.pil',
       'qrcode.constants',
       'qrcode.exceptions',
       'qrcode.util',
       'qrcode.LUT',
       'qrcode.image',
       'qrcode.image-base',
       'qrcode.image.styles',
       'qrcode.image.styles.moduledrawers',
       'qrcode.image.styles.moduledrawers.pil',
       'qrcode.compat',
       'qrcode.compat.util',
       'qrcode.image.styles.moduledrawers.base',
       'qrcode.image.pure'
       ]):
    import qrcode

# No logging
logging.disable(logging.CRITICAL)

error_correction_opts = [qrcode.constants.ERROR_CORRECT_L,
                         qrcode.constants.ERROR_CORRECT_M,
                         qrcode.constants.ERROR_CORRECT_Q,
                         qrcode.constants.ERROR_CORRECT_H]


def TestOneInput(data):
    try:
        # img = qrcode.make(data)
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=1, border=0)
        qr.add_data(data)
        qr.make(fit=True)
    except ValueError as e:
        if 'glog' in str(e):
            return -1
        raise

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
