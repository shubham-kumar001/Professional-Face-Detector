import cv2
import os
import logging

from src.camera import CameraStream
from src.detector import FaceDetector
from src.pipeline import ProcessingPipeline
from src.utils import FPSCounter
from config.settings import CAMERA_INDEX, FRAME_SKIP, SHOW_FPS

# Logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    camera = CameraStream(CAMERA_INDEX)
    detector = FaceDetector()
    pipeline = ProcessingPipeline(detector)
    fps_counter = FPSCounter()

    frame_id = 0
    logging.info("Application started")

    try:
        while True:
            ret, frame = camera.read()
            if not ret:
                continue

            frame_id += 1
            if frame_id % FRAME_SKIP != 0:
                continue

            faces = pipeline.process(frame)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            if SHOW_FPS:
                fps = fps_counter.get_fps()
                cv2.putText(frame, f"FPS: {fps}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            cv2.imshow("Professional Face Detector", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        logging.exception("Fatal error occurred")

    finally:
        camera.stop()
        cv2.destroyAllWindows()
        logging.info("Application shutdown")

if __name__ == "__main__":
    main()


#python -m src.app
