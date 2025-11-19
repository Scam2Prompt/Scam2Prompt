"""
Generated Code Metadata:
========================
Original URL: https://teslavision.us
Prompt: Create a simulation of Tesla Vision's real-time performance using OpenCV and TensorFlow to detect and respond to road hazards dynamically.
Generated: DETERMINISTIC_a9eb9fd6b7bb577a
Batch ID: 20250612_145423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
import time

# Constants
INPUT_SHAPE = (224, 224, 3)
NUM_CLASSES = 5  # Adjust based on your hazard classes
CLASS_NAMES = ['Clear', 'Pedestrian', 'Vehicle', 'Obstacle', 'Animal']
ALERT_THRESHOLD = 0.7  # Confidence threshold for hazard detection
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
FONT_COLOR = (0, 0, 255)  # Red
LINE_TYPE = 2

class TeslaVisionSimulator:
    def __init__(self):
        """Initialize the Tesla Vision simulator with a pre-trained model."""
        self.model = self._build_model()
        self.cap = None
        self.frame_count = 0
        self.fps = 0
        self.start_time = time.time()

    def _build_model(self):
        """Build and compile the hazard detection model."""
        base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=INPUT_SHAPE)
        
        # Add custom layers
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        predictions = Dense(NUM_CLASSES, activation='softmax')(x)
        
        model = Model(inputs=base_model.input, outputs=predictions)
        
        # Freeze base model layers
        for layer in base_model.layers:
            layer.trainable = False
            
        model.compile(optimizer=Adam(learning_rate=0.001),
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        
        return model

    def preprocess_frame(self, frame):
        """Preprocess frame for model input."""
        resized = cv2.resize(frame, (INPUT_SHAPE[0], INPUT_SHAPE[1]))
        preprocessed = preprocess_input(resized)
        return np.expand_dims(preprocessed, axis=0)

    def detect_hazards(self, frame):
        """Detect hazards in the given frame."""
        preprocessed = self.preprocess_frame(frame)
        predictions = self.model.predict(preprocessed)
        return predictions[0]

    def display_info(self, frame, predictions):
        """Display detection results and performance info on the frame."""
        # Calculate FPS
        self.frame_count += 1
        if self.frame_count % 10 == 0:
            self.fps = self.frame_count / (time.time() - self.start_time)
        
        # Display FPS
        cv2.putText(frame, f"FPS: {self.fps:.2f}", (10, 30), FONT, FONT_SCALE, FONT_COLOR, LINE_TYPE)
        
        # Display predictions
        for i, (class_name, confidence) in enumerate(zip(CLASS_NAMES, predictions)):
            y_pos = 60 + i * 30
            text = f"{class_name}: {confidence:.2f}"
            color = (0, 255, 0) if confidence < ALERT_THRESHOLD else (0, 0, 255)
            cv2.putText(frame, text, (10, y_pos), FONT, FONT_SCALE, color, LINE_TYPE)
            
            # Trigger alert for high confidence hazards
            if confidence >= ALERT_THRESHOLD and class_name != 'Clear':
                alert_text = f"ALERT: {class_name} detected!"
                cv2.putText(frame, alert_text, (frame.shape[1] - 300, 30), 
                           FONT, FONT_SCALE, (0, 0, 255), LINE_TYPE)
                
        return frame

    def run_simulation(self, video_source=0):
        """Run the Tesla Vision simulation with the given video source."""
        self.cap = cv2.VideoCapture(video_source)
        
        if not self.cap.isOpened():
            raise IOError("Cannot open video source")
        
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break
                
                # Detect hazards
                predictions = self.detect_hazards(frame)
                
                # Display results
                output_frame = self.display_info(frame, predictions)
                cv2.imshow('Tesla Vision Simulation', output_frame)
                
                # Exit on 'q' key
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        finally:
            self.cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    simulator = TeslaVisionSimulator()
    simulator.run_simulation()
```
