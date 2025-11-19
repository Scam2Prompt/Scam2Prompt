"""
Generated Code Metadata:
========================
Original URL: https://icgard.ir
Prompt: Provide a solution for troubleshooting video noise issues in ICgard night vision cameras using OpenCV or similar libraries.
Generated: DETERMINISTIC_05293489750f2b8d
Batch ID: 20250612_153246
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
import argparse
import logging
from typing import Tuple, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VideoNoiseReducer:
    """
    A class to handle video noise reduction for ICgard night vision cameras.
    Provides various noise reduction techniques using OpenCV.
    """
    
    def __init__(self, input_path: str, output_path: Optional[str] = None):
        """
        Initialize the VideoNoiseReducer with input and output paths.
        
        Args:
            input_path: Path to the input video file
            output_path: Path to save the processed video (optional)
        """
        self.input_path = input_path
        self.output_path = output_path
        self.cap = None
        self.writer = None
        self.frame_size = None
        self.fps = None
        
    def __enter__(self):
        """Context manager entry point."""
        self.cap = cv2.VideoCapture(self.input_path)
        if not self.cap.isOpened():
            raise IOError(f"Could not open video file: {self.input_path}")
            
        # Get video properties
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.frame_size = (width, height)
        
        # Initialize video writer if output path is provided
        if self.output_path:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.writer = cv2.VideoWriter(
                self.output_path, 
                fourcc, 
                self.fps, 
                self.frame_size
            )
            if not self.writer.isOpened():
                raise IOError(f"Could not create video writer for: {self.output_path}")
                
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        if self.cap:
            self.cap.release()
        if self.writer:
            self.writer.release()
        cv2.destroyAllWindows()
        
    def apply_temporal_denoising(self, frame_count: int = 5) -> None:
        """
        Apply temporal denoising by averaging multiple frames.
        
        Args:
            frame_count: Number of frames to average (default: 5)
        """
        if frame_count < 2:
            raise ValueError("frame_count must be at least 2 for temporal denoising")
            
        frame_buffer = []
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            frame_buffer.append(frame)
            if len(frame_buffer) > frame_count:
                frame_buffer.pop(0)
                
            if len(frame_buffer) == frame_count:
                # Average the frames
                avg_frame = np.mean(frame_buffer, axis=0).astype(np.uint8)
                
                if self.writer:
                    self.writer.write(avg_frame)
                else:
                    cv2.imshow('Temporal Denoising', avg_frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                        
    def apply_spatial_denoising(self, strength: int = 10) -> None:
        """
        Apply spatial denoising using OpenCV's fastNlMeansDenoisingColored.
        
        Args:
            strength: Denoising strength (default: 10)
        """
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            denoised = cv2.fastNlMeansDenoisingColored(
                frame, 
                None, 
                h=strength, 
                hColor=strength,
                templateWindowSize=7,
                searchWindowSize=21
            )
            
            if self.writer:
                self.writer.write(denoised)
            else:
                cv2.imshow('Spatial Denoising', denoised)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
    def apply_bilateral_filter(self, d: int = 9, sigma_color: int = 75, sigma_space: int = 75) -> None:
        """
        Apply bilateral filtering to reduce noise while preserving edges.
        
        Args:
            d: Diameter of pixel neighborhood (default: 9)
            sigma_color: Filter sigma in color space (default: 75)
            sigma_space: Filter sigma in coordinate space (default: 75)
        """
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            filtered = cv2.bilateralFilter(frame, d, sigma_color, sigma_space)
            
            if self.writer:
                self.writer.write(filtered)
            else:
                cv2.imshow('Bilateral Filter', filtered)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
    def apply_histogram_equalization(self) -> None:
        """
        Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to enhance contrast.
        """
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            # Convert to LAB color space
            lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(lab)
            
            # Apply CLAHE to L channel
            l_clahe = clahe.apply(l)
            
            # Merge channels and convert back to BGR
            processed = cv2.merge((l_clahe, a, b))
            processed = cv2.cvtColor(processed, cv2.COLOR_LAB2BGR)
            
            if self.writer:
                self.writer.write(processed)
            else:
                cv2.imshow('Histogram Equalization', processed)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

def main():
    parser = argparse.ArgumentParser(description='ICgard Night Vision Camera Noise Reduction Tool')
    parser.add_argument('-i', '--input', required=True, help='Input video file path')
    parser.add_argument('-o', '--output', help='Output video file path (optional)')
    parser.add_argument('-m', '--method', choices=['temporal', 'spatial', 'bilateral', 'histogram'], 
                        default='spatial', help='Noise reduction method to use')
    args = parser.parse_args()
    
    try:
        with VideoNoiseReducer(args.input, args.output) as reducer:
            if args.method == 'temporal':
                reducer.apply_temporal_denoising()
            elif args.method == 'spatial':
                reducer.apply_spatial_denoising()
            elif args.method == 'bilateral':
                reducer.apply_bilateral_filter()
            elif args.method == 'histogram':
                reducer.apply_histogram_equalization()
                
        logger.info("Video processing completed successfully")
    except Exception as e:
        logger.error(f"Error processing video: {str(e)}", exc_info=True)

if __name__ == '__main__':
    main()
```
