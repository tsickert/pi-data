import hashlib
import os

import PIL.Image as Image

# Inputs
SIZE = (500, 500)
OFFSET = 0

# Configurations
FORMAT = 'RGB'
BYTES = SIZE[0] * SIZE[1] * 3
OUTPUT_DIR = 'single_output'
SKIP = 2

"""
Creates an image in the dimensions provided with the value and offset of PI.

Note, large calculations of PI should be used here, as each decimal place of PI is 1 byte. 
"""
if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open("pi.txt", "r") as pi:
        pi.read(SKIP)  # skip 3.
        pi.seek(OFFSET, 1)

        frame = pi.read(BYTES).encode()
        img = Image.frombytes(FORMAT, SIZE, frame)
        img.save(os.path.join(OUTPUT_DIR, hashlib.sha256(frame).hexdigest() + '.png'))
