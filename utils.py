import time

class FPSCounter:
    def __init__(self):
        self.prev = time.time()

    def get_fps(self):
        now = time.time()
        fps = int(1 / (now - self.prev))
        self.prev = now
        return fps
