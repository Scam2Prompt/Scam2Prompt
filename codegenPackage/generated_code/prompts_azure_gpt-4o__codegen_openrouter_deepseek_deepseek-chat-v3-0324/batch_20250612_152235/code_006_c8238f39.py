"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Create a Python script to integrate AR content into a commercial application, inspired by Sprout Studios' AR project for DEWA.
Generated: DETERMINISTIC_c8238f39d8c37001
Batch ID: 20250612_152235
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
import pyrealsense2 as rs
from pyzbar.pyzbar import decode
import os
import json
import threading
import time
from typing import Optional, Dict, Any

class ARContentIntegrator:
    """
    AR Content Integrator for commercial applications.
    Integrates AR content based on QR code detection and RealSense camera input.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the AR integrator with configuration.
        
        Args:
            config_path: Path to the configuration JSON file.
        """
        self.config = self._load_config(config_path)
        self.pipeline = rs.pipeline()
        self.config_realsense()
        self.ar_objects = {}
        self.running = False
        self.current_qr_data = None
        self.lock = threading.Lock()
        
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to the configuration file.
            
        Returns:
            Loaded configuration dictionary.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is malformed.
        """
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at {config_path}")
            
        with open(config_path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Invalid JSON in config file: {e}", e.doc, e.pos)
    
    def config_realsense(self) -> None:
        """Configure the RealSense camera pipeline."""
        config = rs.config()
        config.enable_stream(rs.stream.color, 
                           self.config['camera']['width'], 
                           self.config['camera']['height'], 
                           rs.format.bgr8, 
                           self.config['camera']['fps'])
        config.enable_stream(rs.stream.depth, 
                           self.config['camera']['width'], 
                           self.config['camera']['height'], 
                           rs.format.z16, 
                           self.config['camera']['fps'])
        
        self.pipeline.start(config)
    
    def load_ar_objects(self) -> None:
        """Load AR objects from configured directory."""
        ar_dir = self.config['ar_objects']['directory']
        if not os.path.exists(ar_dir):
            raise FileNotFoundError(f"AR objects directory not found at {ar_dir}")
            
        for obj_file in os.listdir(ar_dir):
            if obj_file.endswith('.obj'):
                obj_name = os.path.splitext(obj_file)[0]
                self.ar_objects[obj_name] = os.path.join(ar_dir, obj_file)
    
    def detect_qr_code(self, frame: np.ndarray) -> Optional[str]:
        """
        Detect and decode QR codes in the frame.
        
        Args:
            frame: Input image frame.
            
        Returns:
            Decoded QR data if found, None otherwise.
        """
        decoded_objects = decode(frame)
        if decoded_objects:
            return decoded_objects[0].data.decode('utf-8')
        return None
    
    def process_frame(self) -> None:
        """Main processing loop for AR content integration."""
        try:
            while self.running:
                frames = self.pipeline.wait_for_frames()
                color_frame = frames.get_color_frame()
                if not color_frame:
                    continue
                    
                frame = np.asanyarray(color_frame.get_data())
                qr_data = self.detect_qr_code(frame)
                
                if qr_data and qr_data != self.current_qr_data:
                    with self.lock:
                        self.current_qr_data = qr_data
                        self.display_ar_content(qr_data)
                
                # Display the frame with AR content
                cv2.imshow('AR Integration', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.stop()
                    
        except Exception as e:
            print(f"Error in processing loop: {e}")
            self.stop()
    
    def display_ar_content(self, qr_data: str) -> None:
        """
        Display AR content based on QR code data.
        
        Args:
            qr_data: Decoded data from QR code.
        """
        if qr_data in self.ar_objects:
            print(f"Displaying AR content for: {qr_data}")
            # Here you would integrate with your AR rendering system
            # For example: load and display the 3D model
        else:
            print(f"No AR content found for QR data: {qr_data}")
    
    def start(self) -> None:
        """Start the AR integration system."""
        if self.running:
            print("System is already running")
            return
            
        self.running = True
        self.load_ar_objects()
        processing_thread = threading.Thread(target=self.process_frame)
        processing_thread.daemon = True
        processing_thread.start()
    
    def stop(self) -> None:
        """Stop the AR integration system."""
        self.running = False
        cv2.destroyAllWindows()
        self.pipeline.stop()
    
    def __enter__(self):
        """Context manager entry."""
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop()

def main():
    try:
        with ARContentIntegrator() as ar_integrator:
            print("AR Integration System Running. Press 'q' to quit.")
            while ar_integrator.running:
                time.sleep(0.1)
                
    except Exception as e:
        print(f"Error in AR Integration System: {e}")

if __name__ == "__main__":
    main()
```
