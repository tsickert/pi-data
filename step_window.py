import hashlib
import os

import PIL.Image as Image

FORMAT = 'RGB'
SIZE = (8, 8)
BYTES = SIZE[0] * SIZE[1] * 3
OUTPUT_DIR = 'step_window'
FILENAME = "pi.txt"

"""
This iterates through the value of PI as provided in the pi.txt file and creates images of the size in the configuration
The outputs are PNGs.
"""
if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(FILENAME, "r") as pi:
        pi.read(2)  # skip 3.
        frame = pi.read(BYTES).encode()
        while frame is not None:
            try:
                img = Image.frombytes(FORMAT, SIZE, frame)
                img.save(os.path.join(OUTPUT_DIR, hashlib.sha256(frame).hexdigest() + '.png'))
                frame = pi.read(BYTES).encode()
            except ValueError as e:
                print('Done')
                break
