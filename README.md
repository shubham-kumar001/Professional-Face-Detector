# Professional Face Detector 👤

A high-performance, real-time face detection application built with OpenCV and Python. Features a modular architecture, configurable settings, and smooth performance optimization.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![Real-time](https://img.shields.io/badge/Real--time-Processing-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🎯 Core Detection
- **Real-time Face Detection** using Haar Cascade classifier
- **Multi-face Detection** in single frame
- **Performance Optimized** with frame skipping
- **Smooth FPS Display** with real-time monitoring

### ⚙️ Configuration
- **Adjustable Parameters** (scale factor, neighbors, min size)
- **Camera Configuration** support for multiple sources
- **Performance Tuning** with frame skip control
- **Feature Flags** for FPS display and face saving

### 📊 Monitoring & Logging
- **Comprehensive Logging** with timestamped events
- **FPS Counter** for performance monitoring
- **Error Handling** with exception logging
- **Application State Tracking**

### 🏗️ Architecture
- **Modular Design** with clear separation of concerns
- **Pipeline Processing** for extensibility
- **Thread-safe Camera Stream** for smooth video capture
- **Clean Code Structure** following best practices

## 📁 Project Structure

```
Professional_Face_Detector/
├── app.py                    # Main application entry point
├── requirements.txt          # Dependencies
├── config/
│   └── settings.py          # Configuration parameters
├── src/                      # Source modules
│   ├── camera.py            # Camera stream management
│   ├── detector.py          # Face detection logic
│   ├── pipeline.py          # Processing pipeline
│   ├── utils.py             # Utility functions
│   └── __init__.py          # Package initialization
├── logs/                     # Application logs
│   └── app.log              # Log file
└── README.md                # This documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Webcam or camera device
- pip (Python package manager)

### Installation

1. **Clone or download the project:**
```bash
git clone <repository-url>
cd Professional_Face_Detector
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python app.py
```

### Alternative: Run as module
```bash
python -m src.app
```

## ⚙️ Configuration

Edit `config/settings.py` to customize the application:

```python
# Camera settings
CAMERA_INDEX = 0  # 0 for default webcam, 1 for external camera

# Detection parameters
SCALE_FACTOR = 1.2    # How much the image size is reduced at each scale
MIN_NEIGHBORS = 5     # How many neighbors each candidate rectangle should have
MIN_FACE_SIZE = (40, 40)  # Minimum possible face size

# Performance settings
FRAME_SKIP = 2        # Process every Nth frame (higher = better performance)
SHOW_FPS = True       # Display FPS counter
SAVE_FACES = False    # Save detected faces to disk
```

## 🎮 How to Use

### Basic Operation
1. Run the application: `python app.py`
2. A window titled "Professional Face Detector" will open
3. Faces will be highlighted with green rectangles
4. Press `q` to quit the application

### Camera Selection
To use a different camera source:
1. Edit `config/settings.py`
2. Change `CAMERA_INDEX` to:
   - `0`: Default webcam
   - `1`: External USB camera
   - `2`: Second camera, etc.

### Performance Tuning
- Increase `FRAME_SKIP` for better performance on slower hardware
- Adjust `SCALE_FACTOR` for different face sizes
- Modify `MIN_NEIGHBORS` to reduce false positives

## 📊 Understanding Parameters

### Detection Parameters
- **SCALE_FACTOR (1.2)**: 
  - Lower values = better detection, slower performance
  - Higher values = faster processing, might miss faces
  
- **MIN_NEIGHBORS (5)**:
  - Higher values = fewer detections, higher quality
  - Lower values = more detections, more false positives
  
- **MIN_FACE_SIZE (40, 40)**:
  - Minimum size of faces to detect in pixels
  - Adjust based on distance from camera

### Performance Parameters
- **FRAME_SKIP (2)**: 
  - Processes every 2nd frame
  - Increases FPS, reduces CPU usage
  - Trade-off: slightly less smooth detection

## 🧪 Testing the Setup

Create a test script to verify camera access:

**test_camera.py:**
```python
import cv2

def test_camera(index=0):
    cap = cv2.VideoCapture(index)
    
    if not cap.isOpened():
        print(f"❌ Camera {index} not accessible")
        return False
    
    print(f"✅ Camera {index} is working")
    
    # Test read
    ret, frame = cap.read()
    if ret:
        print(f"✅ Frame captured: {frame.shape}")
    else:
        print("❌ Failed to capture frame")
    
    cap.release()
    return ret

if __name__ == "__main__":
    for i in range(3):
        print(f"\nTesting camera {i}...")
        test_camera(i)
```

Run with:
```bash
python test_camera.py
```

## 🔧 Troubleshooting

### Common Issues

**Issue**: `RuntimeError: Camera not accessible`
**Solution**:
```bash
# Check camera index
python -c "import cv2; print([cv2.VideoCapture(i).isOpened() for i in range(3)])"

# Try different camera index in settings.py
CAMERA_INDEX = 1  # or 2, 3, etc.
```

**Issue**: Low FPS or laggy detection
**Solution**:
```python
# Increase FRAME_SKIP in settings.py
FRAME_SKIP = 3  # or higher

# Adjust detection parameters
SCALE_FACTOR = 1.3
MIN_NEIGHBORS = 4
```

**Issue**: No faces detected
**Solution**:
```python
# Adjust detection sensitivity
SCALE_FACTOR = 1.1  # More sensitive
MIN_NEIGHBORS = 3   # More detections
MIN_FACE_SIZE = (30, 30)  # Smaller faces
```

### Windows Specific
```bash
# If OpenCV has DLL issues
pip uninstall opencv-python
pip install opencv-python-headless

# For better camera support
pip install opencv-contrib-python
```

### Linux Specific
```bash
# Install camera dependencies
sudo apt-get install libopencv-dev python3-opencv
sudo apt-get install v4l-utils

# Check available cameras
v4l2-ctl --list-devices
```

## 📈 Performance Optimization

### For High Performance (Gaming PC)
```python
# config/settings.py
FRAME_SKIP = 1        # Process every frame
SCALE_FACTOR = 1.1    # High accuracy
MIN_NEIGHBORS = 5     # Balanced quality
```

### For Low Performance (Raspberry Pi)
```python
# config/settings.py
FRAME_SKIP = 3        # Process every 3rd frame
SCALE_FACTOR = 1.3    # Faster processing
MIN_NEIGHBORS = 4     # Slightly more sensitive
RESIZE_FACTOR = 0.5   # Downscale frames
```

### Adding Resize for Extra Performance
Add to `app.py` before processing:
```python
# After capturing frame
frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
# Remember to scale coordinates back if needed
```

## 🛠️ Development

### Extending the Application

**Adding Face Recognition:**
```python
# In src/detector.py or new module
class FaceRecognizer:
    def __init__(self):
        self.known_faces = {}
    
    def recognize(self, face_image):
        # Add recognition logic
        pass
```

**Adding Face Saving:**
```python
# Modify app.py to save faces
if SAVE_FACES:
    for i, (x, y, w, h) in enumerate(faces):
        face_img = frame[y:y+h, x:x+w]
        cv2.imwrite(f"faces/face_{frame_id}_{i}.jpg", face_img)
```

### Running Tests
```bash
# Basic functionality test
python -c "import cv2; print('OpenCV version:', cv2.__version__)"

# Test individual modules
python -c "from src.detector import FaceDetector; print('Detector loaded')"
```

## 📊 Logging

The application logs to `logs/app.log`:
- Application start/stop times
- Errors and exceptions
- Performance metrics

View logs:
```bash
# View last 10 lines
tail -n 10 logs/app.log

# View in real-time
tail -f logs/app.log
```

## 🎯 Use Cases

### Security & Surveillance
- Real-time face monitoring
- Access control systems
- Attendance tracking

### Research & Education
- Computer vision projects
- Machine learning training
- Performance benchmarking

### Personal Projects
- Smart mirror applications
- Photo organization
- Interactive installations

## 🔄 Future Enhancements

Planned features:
- [ ] **Face Recognition** with known persons database
- [ ] **Emotion Detection** using deep learning
- [ ] **Age & Gender Estimation**
- [ ] **Multi-threaded Processing** for higher FPS
- [ ] **Web Interface** for remote monitoring
- [ ] **Mobile App Integration**
- [ ] **Cloud Storage** for detected faces
- [ ] **API Endpoints** for integration

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For issues and questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the logs in `logs/app.log`
3. Create an issue with:
   - Camera model and OS
   - Error messages from logs
   - Steps to reproduce

## 🙏 Acknowledgments

- Built with **OpenCV** computer vision library
- Uses **Haar Cascade** classifiers for face detection
- Inspired by real-time vision applications
- Thanks to all contributors and testers

---

**Happy Face Detecting!** 👤 → ✅

*"Seeing faces where others see pixels"*
