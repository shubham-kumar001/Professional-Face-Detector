class ProcessingPipeline:
    def __init__(self, detector):
        self.detector = detector
        self.frame_count = 0

    def process(self, frame):
        self.frame_count += 1
        return self.detector.detect(frame)
