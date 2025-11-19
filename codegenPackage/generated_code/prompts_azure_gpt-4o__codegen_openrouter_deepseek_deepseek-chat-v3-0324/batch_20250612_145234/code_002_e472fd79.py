"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Generate code to create a real-time AV system that integrates immersive technologies, similar to the solutions demonstrated at Pro Integration Future Asia.
Generated: DETERMINISTIC_e472fd79c85e33df
Batch ID: 20250612_145234
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
import open3d as o3d
import threading
import queue
import time
from typing import Optional, Tuple, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RealTimeAVSystem:
    """
    Real-time Audio-Visual system integrating immersive technologies with Intel RealSense depth cameras.
    """
    
    def __init__(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.align = rs.align(rs.stream.color)
        self.running = False
        self.frame_queue = queue.Queue(maxsize=10)
        self.pointcloud = None
        self.visualizer = None
        
        # Configure streams
        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        
    def start(self) -> None:
        """Start the AV system pipeline."""
        try:
            self.pipeline.start(self.config)
            self.running = True
            logger.info("AV System started successfully")
            
            # Start processing threads
            threading.Thread(target=self._capture_frames, daemon=True).start()
            threading.Thread(target=self._process_frames, daemon=True).start()
            
        except Exception as e:
            logger.error(f"Failed to start AV system: {str(e)}")
            raise
            
    def stop(self) -> None:
        """Stop the AV system pipeline."""
        self.running = False
        self.pipeline.stop()
        if self.visualizer:
            self.visualizer.destroy_window()
        logger.info("AV System stopped")
        
    def _capture_frames(self) -> None:
        """Capture frames from RealSense camera and add to processing queue."""
        try:
            while self.running:
                frames = self.pipeline.wait_for_frames()
                aligned_frames = self.align.process(frames)
                
                if self.frame_queue.full():
                    self.frame_queue.get_nowait()  # Discard oldest frame if queue full
                    
                self.frame_queue.put(aligned_frames)
                
        except Exception as e:
            logger.error(f"Frame capture error: {str(e)}")
            self.running = False
            
    def _process_frames(self) -> None:
        """Process frames from queue for visualization and analysis."""
        try:
            while self.running or not self.frame_queue.empty():
                if self.frame_queue.empty():
                    time.sleep(0.01)
                    continue
                    
                frames = self.frame_queue.get()
                
                # Get depth and color frames
                depth_frame = frames.get_depth_frame()
                color_frame = frames.get_color_frame()
                
                if not depth_frame or not color_frame:
                    continue
                    
                # Process depth data
                depth_image = np.asanyarray(depth_frame.get_data())
                color_image = np.asanyarray(color_frame.get_data())
                
                # Generate point cloud
                self._generate_pointcloud(depth_frame, color_frame)
                
                # Display color image
                cv2.imshow('Real-time AV System', color_image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False
                    
        except Exception as e:
            logger.error(f"Frame processing error: {str(e)}")
            self.running = False
            
    def _generate_pointcloud(self, depth_frame: rs.frame, color_frame: rs.frame) -> None:
        """Generate and visualize 3D point cloud from depth and color frames."""
        try:
            # Create point cloud object
            pc = rs.pointcloud()
            points = pc.calculate(depth_frame)
            pc.map_to(color_frame)
            
            # Convert to Open3D format
            v, t = points.get_vertices(), points.get_texture_coordinates()
            verts = np.asanyarray(v).view(np.float32).reshape(-1, 3)
            texcoords = np.asanyarray(t).view(np.float32).reshape(-1, 2)
            
            # Create Open3D point cloud
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(verts)
            
            # Add color if available
            if color_frame:
                color_image = np.asanyarray(color_frame.get_data())
                colors = []
                for coord in texcoords:
                    u = min(max(int(coord[0] * color_image.shape[1]), 0), color_image.shape[1] - 1)
                    v = min(max(int(coord[1] * color_image.shape[0]), 0), color_image.shape[0] - 1)
                    colors.append(color_image[v, u] / 255.0)
                pcd.colors = o3d.utility.Vector3dVector(colors)
                
            self.pointcloud = pcd
            
            # Visualize if not already running
            if not self.visualizer:
                self.visualizer = o3d.visualization.Visualizer()
                self.visualizer.create_window(window_name='3D Point Cloud')
                self.visualizer.add_geometry(pcd)
                
            else:
                self.visualizer.update_geometry(pcd)
                self.visualizer.poll_events()
                self.visualizer.update_renderer()
                
        except Exception as e:
            logger.error(f"Point cloud generation error: {str(e)}")
            
    def get_latest_pointcloud(self) -> Optional[o3d.geometry.PointCloud]:
        """Get the latest generated point cloud."""
        return self.pointcloud
        
    def get_system_status(self) -> bool:
        """Get current system running status."""
        return self.running


def main():
    """Main function to run the AV system."""
    av_system = RealTimeAVSystem()
    
    try:
        av_system.start()
        
        # Keep main thread alive while system runs
        while av_system.get_system_status():
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        logger.info("Shutting down AV system...")
        
    finally:
        av_system.stop()


if __name__ == "__main__":
    main()
```
