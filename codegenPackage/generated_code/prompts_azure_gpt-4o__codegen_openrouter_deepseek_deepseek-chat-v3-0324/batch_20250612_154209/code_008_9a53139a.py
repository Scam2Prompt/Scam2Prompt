"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Generate a Python script to analyze data from pipe inspection cameras and detect anomalies, referencing the rørinspeksjon (pipe inspection) services offered by Aktiv Rørteknikk AS.
Generated: DETERMINISTIC_9a53139af58e658e
Batch ID: 20250612_154209
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
import os
import json
from datetime import datetime
from typing import Optional, Tuple, List, Dict

class PipeInspectionAnalyzer:
    """
    A class to analyze pipe inspection videos/images and detect anomalies.
    References Aktiv Rørteknikk AS pipe inspection services (rørinspeksjon).
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the analyzer with optional configuration.
        
        Args:
            config_path: Path to JSON configuration file
        """
        self.config = {
            'min_contour_area': 500,
            'blur_kernel_size': (5, 5),
            'canny_threshold1': 50,
            'canny_threshold2': 150,
            'output_dir': 'results',
            'report_filename': 'inspection_report.json'
        }
        
        if config_path:
            self.load_config(config_path)
            
        self.create_output_dir()
    
    def load_config(self, config_path: str) -> None:
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
        except FileNotFoundError:
            print(f"Warning: Config file {config_path} not found. Using defaults.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in config file {config_path}. Using defaults.")
    
    def create_output_dir(self) -> None:
        """Create output directory if it doesn't exist."""
        os.makedirs(self.config['output_dir'], exist_ok=True)
    
    def analyze_video(self, video_path: str) -> Dict:
        """
        Analyze a pipe inspection video for anomalies.
        
        Args:
            video_path: Path to the video file
            
        Returns:
            Dictionary containing analysis results
        """
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file {video_path} not found")
            
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise IOError(f"Could not open video file {video_path}")
            
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        anomalies = []
        processed_frames = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            processed_frames += 1
            frame_anomalies = self.analyze_frame(frame, frame_number=processed_frames)
            
            if frame_anomalies:
                anomalies.extend(frame_anomalies)
                
        cap.release()
        
        return {
            'video_path': video_path,
            'frame_count': frame_count,
            'processed_frames': processed_frames,
            'fps': fps,
            'resolution': f"{width}x{height}",
            'anomalies_found': len(anomalies) > 0,
            'anomalies': anomalies,
            'analysis_date': datetime.now().isoformat(),
            'config': self.config
        }
    
    def analyze_frame(self, frame: np.ndarray, frame_number: int) -> List[Dict]:
        """
        Analyze a single frame for pipe anomalies.
        
        Args:
            frame: Image frame to analyze
            frame_number: Frame number for reference
            
        Returns:
            List of detected anomalies (empty if none found)
        """
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, self.config['blur_kernel_size'], 0)
        
        # Edge detection
        edges = cv2.Canny(blurred, self.config['canny_threshold1'], self.config['canny_threshold2'])
        
        # Find contours
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        anomalies = []
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > self.config['min_contour_area']:
                x, y, w, h = cv2.boundingRect(contour)
                
                anomaly = {
                    'frame': frame_number,
                    'area': area,
                    'bounding_box': {
                        'x': x,
                        'y': y,
                        'width': w,
                        'height': h
                    },
                    'contour_points': len(contour),
                    'timestamp': frame_number / self.config.get('fps', 30)  # Default to 30 FPS if not set
                }
                
                anomalies.append(anomaly)
                
                # Draw on frame for visualization
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        if anomalies:
            output_path = os.path.join(self.config['output_dir'], f"frame_{frame_number}_anomalies.jpg")
            cv2.imwrite(output_path, frame)
            
        return anomalies
    
    def generate_report(self, analysis_results: Dict, output_path: Optional[str] = None) -> str:
        """
        Generate a JSON report from analysis results.
        
        Args:
            analysis_results: Dictionary of analysis results
            output_path: Optional custom output path
            
        Returns:
            Path to the generated report
        """
        if not output_path:
            output_path = os.path.join(self.config['output_dir'], self.config['report_filename'])
            
        with open(output_path, 'w') as f:
            json.dump(analysis_results, f, indent=4)
            
        return output_path

def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Pipe Inspection Analyzer - Aktiv Rørteknikk AS rørinspeksjon')
    parser.add_argument('input_path', help='Path to input video file')
    parser.add_argument('--config', help='Path to configuration file (JSON)')
    parser.add_argument('--output', help='Custom output directory')
    
    args = parser.parse_args()
    
    analyzer = PipeInspectionAnalyzer(args.config)
    
    if args.output:
        analyzer.config['output_dir'] = args.output
        analyzer.create_output_dir()
    
    try:
        print(f"Analyzing pipe inspection video: {args.input_path}")
        results = analyzer.analyze_video(args.input_path)
        report_path = analyzer.generate_report(results)
        
        print(f"Analysis complete. Found {len(results['anomalies'])} anomalies.")
        print(f"Report saved to: {report_path}")
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        return 1
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
```
