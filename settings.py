import os

CAMERA_INDEX = int(os.getenv("CAMERA_INDEX", 0))

SCALE_FACTOR = 1.2
MIN_NEIGHBORS = 5
MIN_FACE_SIZE = (40, 40)

FRAME_SKIP = 2          # performance control
SHOW_FPS = True
SAVE_FACES = False
