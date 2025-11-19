"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: Create a Python program to automate video production workflows for marketing campaigns, ensuring the videos capture a brand's essence, as emphasized by Creo Collective.
Generated: DETERMINISTIC_4cf7f526ef1091af
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import shutil
import subprocess
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('video_workflow.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class VideoWorkflowAutomator:
    """
    Automates video production workflows for marketing campaigns.
    Ensures videos capture brand essence as per Creo Collective guidelines.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the workflow automator with configuration.
        
        Args:
            config_path: Path to the configuration JSON file.
        """
        self.config = self._load_config(config_path)
        self._validate_config()
        self._setup_workspace()
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to the configuration file.
            
        Returns:
            Dictionary containing configuration.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is invalid JSON.
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file not found at {config_path}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            raise
    
    def _validate_config(self) -> None:
        """
        Validate the configuration.
        
        Raises:
            ValueError: If required config values are missing or invalid.
        """
        required_fields = [
            'brand_name',
            'brand_guidelines',
            'input_directory',
            'output_directory',
            'templates_directory',
            'watermark_path',
            'default_resolution',
            'allowed_formats'
        ]
        
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required config field: {field}")
                
        if not os.path.exists(self.config['input_directory']):
            raise ValueError(f"Input directory does not exist: {self.config['input_directory']}")
            
        if not os.path.exists(self.config['templates_directory']):
            raise ValueError(f"Templates directory does not exist: {self.config['templates_directory']}")
    
    def _setup_workspace(self) -> None:
        """
        Set up the workspace by creating necessary directories.
        """
        os.makedirs(self.config['output_directory'], exist_ok=True)
        os.makedirs(os.path.join(self.config['output_directory'], 'processed'), exist_ok=True)
        os.makedirs(os.path.join(self.config['output_directory'], 'final'), exist_ok=True)
        os.makedirs(os.path.join(self.config['output_directory'], 'logs'), exist_ok=True)
    
    def process_videos(self) -> None:
        """
        Main method to process all videos in the input directory.
        """
        logger.info(f"Starting video processing for {self.config['brand_name']}")
        
        input_files = self._get_input_files()
        if not input_files:
            logger.warning("No video files found in input directory")
            return
            
        for video_file in input_files:
            try:
                self._process_single_video(video_file)
            except Exception as e:
                logger.error(f"Failed to process {video_file}: {e}")
                continue
                
        logger.info("Video processing completed")
    
    def _get_input_files(self) -> List[str]:
        """
        Get all valid video files from the input directory.
        
        Returns:
            List of paths to video files.
        """
        input_files = []
        for file in os.listdir(self.config['input_directory']):
            file_path = os.path.join(self.config['input_directory'], file)
            if os.path.isfile(file_path) and self._is_valid_format(file):
                input_files.append(file_path)
        return input_files
    
    def _is_valid_format(self, filename: str) -> bool:
        """
        Check if file has a valid video format.
        
        Args:
            filename: Name of the file to check.
            
        Returns:
            True if format is valid, False otherwise.
        """
        ext = os.path.splitext(filename)[1].lower()
        return ext in self.config['allowed_formats']
    
    def _process_single_video(self, video_path: str) -> None:
        """
        Process a single video file through the workflow.
        
        Args:
            video_path: Path to the video file to process.
        """
        logger.info(f"Processing video: {video_path}")
        
        # Generate unique output filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        processed_name = f"{base_name}_{timestamp}_processed.mp4"
        final_name = f"{base_name}_{timestamp}_final.mp4"
        
        processed_path = os.path.join(self.config['output_directory'], 'processed', processed_name)
        final_path = os.path.join(self.config['output_directory'], 'final', final_name)
        
        # Step 1: Apply basic processing
        self._apply_basic_processing(video_path, processed_path)
        
        # Step 2: Apply brand elements
        self._apply_brand_elements(processed_path, final_path)
        
        # Step 3: Verify output
        if not self._verify_output(final_path):
            raise RuntimeError(f"Output verification failed for {final_path}")
            
        logger.info(f"Successfully processed video: {final_path}")
    
    def _apply_basic_processing(self, input_path: str, output_path: str) -> None:
        """
        Apply basic video processing using FFmpeg.
        
        Args:
            input_path: Path to input video.
            output_path: Path to save processed video.
            
        Raises:
            subprocess.CalledProcessError: If FFmpeg command fails.
        """
        resolution = self.config['default_resolution']
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'scale={resolution}',
            '-c:v', 'libx264',
            '-preset', 'fast',
            '-crf', '23',
            '-c:a', 'aac',
            '-b:a', '128k',
            '-y',  # Overwrite output file if exists
            output_path
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"FFmpeg command failed: {e.stderr.decode()}")
            raise
    
    def _apply_brand_elements(self, input_path: str, output_path: str) -> None:
        """
        Apply brand elements (watermark, intro/outro) to video.
        
        Args:
            input_path: Path to processed video.
            output_path: Path to save final branded video.
            
        Raises:
            subprocess.CalledProcessError: If FFmpeg command fails.
            FileNotFoundError: If brand assets are missing.
        """
        if not os.path.exists(self.config['watermark_path']):
            raise FileNotFoundError(f"Watermark file not found: {self.config['watermark_path']}")
        
        # Apply watermark
        watermark_cmd = [
            'ffmpeg',
            '-i', input_path,
            '-i', self.config['watermark_path'],
            '-filter_complex', 'overlay=W-w-10:H-h-10',
            '-codec:a', 'copy',
            '-y',
            output_path
        ]
        
        try:
            subprocess.run(watermark_cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to apply watermark: {e.stderr.decode()}")
            raise
    
    def _verify_output(self, video_path: str) -> bool:
        """
        Verify the output video meets quality standards.
        
        Args:
            video_path: Path to the video to verify.
            
        Returns:
            True if verification passes, False otherwise.
        """
        if not os.path.exists(video_path):
            logger.error(f"Output file does not exist: {video_path}")
            return False
            
        try:
            # Basic verification using FFprobe
            cmd = ['ffprobe', '-v', 'error', '-show_format', '-show_streams', video_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                logger.error(f"FFprobe verification failed: {result.stderr}")
                return False
                
            return True
        except Exception as e:
            logger.error(f"Verification failed: {e}")
            return False
    
    def cleanup(self) -> None:
        """
        Clean up temporary files and directories.
        """
        processed_dir = os.path.join(self.config['output_directory'], 'processed')
        if os.path.exists(
