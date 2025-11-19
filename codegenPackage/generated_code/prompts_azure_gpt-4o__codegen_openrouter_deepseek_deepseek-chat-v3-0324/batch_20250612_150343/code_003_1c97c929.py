"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Create a surveillance system for traffic monitoring using the features outlined in Starknet IT Solutions' surveillance and spy services.
Generated: DETERMINISTIC_1c97c9299545a6cd
Batch ID: 20250612_150343
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
import datetime
import os
import time
from threading import Thread
import logging
from collections import defaultdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('traffic_monitoring.log'),
        logging.StreamHandler()
    ]
)

class TrafficMonitor:
    def __init__(self, video_source=0, output_dir='output'):
        """
        Initialize the traffic monitoring system.
        
        Args:
            video_source: Video source (0 for default camera, path for video file)
            output_dir: Directory to save outputs
        """
        self.video_source = video_source
        self.output_dir = output_dir
        self.running = False
        self.frame_count = 0
        self.vehicle_count = defaultdict(int)
        self.last_alert_time = 0
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize background subtractor
        self.fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=False)
        
        # Load Haar cascade for vehicle detection
        self.car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')
        
        # Initialize video capture
        self.cap = cv2.VideoCapture(self.video_source)
        if not self.cap.isOpened():
            raise RuntimeError("Error opening video source")
            
        # Get video properties
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_path = os.path.join(self.output_dir, f'traffic_{timestamp}.avi')
        self.out = cv2.VideoWriter(self.output_path, fourcc, self.fps, (self.width, self.height))
        
        logging.info(f"Traffic Monitor initialized. Source: {video_source}, Resolution: {self.width}x{self.height}, FPS: {self.fps}")

    def detect_vehicles(self, frame):
        """
        Detect vehicles in the frame using Haar cascades.
        
        Args:
            frame: Input frame
            
        Returns:
            List of bounding boxes for detected vehicles
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vehicles = self.car_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        return vehicles

    def process_frame(self, frame):
        """
        Process a single frame for traffic monitoring.
        
        Args:
            frame: Input frame
            
        Returns:
            Processed frame with annotations
        """
        # Apply background subtraction
        fgmask = self.fgbg.apply(frame)
        
        # Detect vehicles
        vehicles = self.detect_vehicles(frame)
        
        # Draw bounding boxes and count vehicles
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            self.vehicle_count['total'] += 1
            
        # Add timestamp and counters to frame
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(frame, f"Vehicles: {len(vehicles)}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(frame, f"Total: {self.vehicle_count['total']}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        
        return frame

    def check_traffic_conditions(self, vehicle_count):
        """
        Check traffic conditions and trigger alerts if necessary.
        
        Args:
            vehicle_count: Number of vehicles detected in current frame
        """
        current_time = time.time()
        
        # Check for heavy traffic (more than 5 vehicles in frame)
        if vehicle_count > 5 and (current_time - self.last_alert_time) > 60:
            self.last_alert_time = current_time
            logging.warning(f"Heavy traffic detected! {vehicle_count} vehicles in frame.")
            # Here you would integrate with alert system (email, SMS, etc.)
            
    def run(self):
        """
        Main processing loop for traffic monitoring.
        """
        self.running = True
        logging.info("Starting traffic monitoring...")
        
        try:
            while self.running:
                ret, frame = self.cap.read()
                if not ret:
                    logging.error("Error reading frame from video source")
                    break
                    
                processed_frame = self.process_frame(frame)
                
                # Write frame to output video
                self.out.write(processed_frame)
                
                # Display the resulting frame
                cv2.imshow('Traffic Monitoring', processed_frame)
                
                # Check traffic conditions
                self.check_traffic_conditions(len(self.detect_vehicles(frame)))
                
                # Increment frame counter
                self.frame_count += 1
                
                # Exit on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        except Exception as e:
            logging.error(f"Error in processing loop: {str(e)}")
            
        finally:
            self.stop()

    def stop(self):
        """
        Clean up resources and stop the monitoring system.
        """
        if self.running:
            self.running = False
            if self.cap.isOpened():
                self.cap.release()
            if self.out.isOpened():
                self.out.release()
            cv2.destroyAllWindows()
            logging.info("Traffic monitoring stopped.")
            
            # Save final report
            self.save_report()

    def save_report(self):
        """
        Save a report of the monitoring session.
        """
        report_path = os.path.join(self.output_dir, 'report.txt')
        with open(report_path, 'w') as f:
            f.write(f"Traffic Monitoring Report\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Frames Processed: {self.frame_count}\n")
            f.write(f"Total Vehicles Detected: {self.vehicle_count['total']}\n")
            f.write(f"Average Vehicles per Frame: {self.vehicle_count['total'] / max(1, self.frame_count):.2f}\n")
        logging.info(f"Report saved to {report_path}")

class TrafficMonitoringSystem:
    def __init__(self, sources=None):
        """
        Initialize the traffic monitoring system with multiple sources.
        
        Args:
            sources: List of video sources (cameras or video files)
        """
        self.sources = sources or [0]  # Default to single camera
        self.monitors = []
        
    def start(self):
        """
        Start monitoring all sources.
        """
        for source in self.sources:
            try:
                monitor = TrafficMonitor(video_source=source)
                thread = Thread(target=monitor.run)
                thread.daemon = True
                thread.start()
                self.monitors.append((monitor, thread))
                logging.info(f"Started monitoring for source: {source}")
            except Exception as e:
                logging.error(f"Failed to start monitoring for source {source}: {str(e)}")
                
    def stop_all(self):
        """
        Stop all monitoring threads.
        """
        for monitor, thread in self.monitors:
            monitor.stop()
        logging.info("All monitoring threads stopped")

if __name__ == "__main__":
    try:
        # Example: Monitor default camera and a video file
        system = TrafficMonitoringSystem(sources=[0, 'traffic_sample.mp4'])
        system.start()
        
        # Keep main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        system.stop_all()
    except Exception as e:
        logging.error(f"System error: {str(e)}")
        system.stop_all()
```
