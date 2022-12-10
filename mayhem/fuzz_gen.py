#!/usr/bin/python3
import atheris
import logging
import sys

with atheris.instrument_imports(include=[
    'qrcode.constants',
    'qrcode.exceptions',
    'qrcode.util',
    'qrcode.LUT',
    'qrcode.base',
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


@atheris.instrument_func
def TestOneInput(data):
    try:
        img = qrcode.make(data)
    except ValueError as e:
        if 'glog' in str(e):
            return -1
        raise

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
