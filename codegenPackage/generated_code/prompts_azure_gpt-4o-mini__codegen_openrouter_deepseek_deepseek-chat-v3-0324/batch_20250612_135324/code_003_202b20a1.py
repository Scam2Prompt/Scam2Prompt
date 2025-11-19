"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Write a script to set up a surveillance system using CCTV and IP cameras, as outlined by Starknet IT Solutions.
Generated: DETERMINISTIC_202b20a1e0d4ba49
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CCTV and IP Camera Surveillance System Setup Script
Starknet IT Solutions
"""

import os
import sys
import subprocess
import configparser
import logging
from datetime import datetime
import shutil
import argparse
import platform
import requests
import json
import cv2
import time

# Constants
CONFIG_FILE = 'surveillance_config.ini'
LOG_FILE = 'surveillance_system.log'
DEFAULT_RECORDING_DIR = 'recordings'
DEFAULT_FRAME_RATE = 30
DEFAULT_RESOLUTION = '1920x1080'
DEFAULT_RETENTION_DAYS = 30

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SurveillanceSystem:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.cameras = []
        self.is_running = False
        self.load_config()

    def load_config(self):
        """Load configuration from file or create default if not exists"""
        if not os.path.exists(CONFIG_FILE):
            self.create_default_config()
        
        try:
            self.config.read(CONFIG_FILE)
            self.validate_config()
            self.load_camera_configs()
        except Exception as e:
            logger.error(f"Error loading configuration: {str(e)}")
            raise

    def create_default_config(self):
        """Create default configuration file"""
        self.config['DEFAULT'] = {
            'recording_directory': DEFAULT_RECORDING_DIR,
            'frame_rate': str(DEFAULT_FRAME_RATE),
            'resolution': DEFAULT_RESOLUTION,
            'retention_days': str(DEFAULT_RETENTION_DAYS),
            'motion_detection': 'false',
            'alert_email': '',
            'alert_threshold': '0.5'
        }
        
        self.config['CAMERA1'] = {
            'name': 'Front Door',
            'type': 'ip',
            'source': 'rtsp://username:password@ip_address:port/stream',
            'enabled': 'true'
        }
        
        with open(CONFIG_FILE, 'w') as configfile:
            self.config.write(configfile)
        
        logger.info(f"Created default configuration file at {CONFIG_FILE}")

    def validate_config(self):
        """Validate the loaded configuration"""
        required_sections = ['DEFAULT']
        for section in required_sections:
            if section not in self.config:
                raise ValueError(f"Missing required section in config: {section}")

    def load_camera_configs(self):
        """Load all camera configurations from the config file"""
        self.cameras = []
        for section in self.config.sections():
            if section.startswith('CAMERA'):
                camera_config = {
                    'name': self.config.get(section, 'name', fallback=f'Camera {section}'),
                    'type': self.config.get(section, 'type', fallback='ip'),
                    'source': self.config.get(section, 'source'),
                    'enabled': self.config.getboolean(section, 'enabled', fallback=True)
                }
                self.cameras.append(camera_config)
        
        if not self.cameras:
            logger.warning("No cameras configured in the system")

    def setup_directories(self):
        """Create necessary directories for the surveillance system"""
        recording_dir = self.config['DEFAULT'].get('recording_directory', DEFAULT_RECORDING_DIR)
        
        try:
            os.makedirs(recording_dir, exist_ok=True)
            logger.info(f"Created recording directory at {recording_dir}")
        except OSError as e:
            logger.error(f"Failed to create recording directory: {str(e)}")
            raise

    def check_dependencies(self):
        """Check for required dependencies"""
        required_packages = ['opencv-python', 'numpy', 'requests']
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package)
            except ImportError:
                missing_packages.append(package)
        
        if missing_packages:
            logger.error(f"Missing required packages: {', '.join(missing_packages)}")
            raise ImportError(f"Please install missing packages: {', '.join(missing_packages)}")

    def test_camera_connection(self, camera_config):
        """Test connection to a camera"""
        try:
            cap = cv2.VideoCapture(camera_config['source'])
            if not cap.isOpened():
                logger.error(f"Failed to connect to camera: {camera_config['name']}")
                return False
            
            ret, frame = cap.read()
            cap.release()
            
            if ret:
                logger.info(f"Successfully connected to camera: {camera_config['name']}")
                return True
            else:
                logger.error(f"Failed to receive frame from camera: {camera_config['name']}")
                return False
        except Exception as e:
            logger.error(f"Error testing camera connection: {str(e)}")
            return False

    def cleanup_old_recordings(self):
        """Clean up old recordings based on retention policy"""
        recording_dir = self.config['DEFAULT'].get('recording_directory', DEFAULT_RECORDING_DIR)
        retention_days = self.config['DEFAULT'].getint('retention_days', DEFAULT_RETENTION_DAYS)
        cutoff_time = time.time() - (retention_days * 86400)
        
        try:
            for root, dirs, files in os.walk(recording_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_time = os.path.getmtime(file_path)
                    
                    if file_time < cutoff_time:
                        try:
                            os.remove(file_path)
                            logger.debug(f"Removed old recording: {file_path}")
                        except OSError as e:
                            logger.error(f"Failed to remove old recording {file_path}: {str(e)}")
        except Exception as e:
            logger.error(f"Error during recording cleanup: {str(e)}")

    def record_camera(self, camera_config):
        """Record video from a single camera"""
        recording_dir = self.config['DEFAULT'].get('recording_directory', DEFAULT_RECORDING_DIR)
        frame_rate = self.config['DEFAULT'].getint('frame_rate', DEFAULT_FRAME_RATE)
        resolution = self.config['DEFAULT'].get('resolution', DEFAULT_RESOLUTION)
        width, height = map(int, resolution.split('x'))
        
        camera_name = camera_config['name'].replace(' ', '_')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(recording_dir, f"{camera_name}_{timestamp}.avi")
        
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_file, fourcc, frame_rate, (width, height))
        
        try:
            cap = cv2.VideoCapture(camera_config['source'])
            if not cap.isOpened():
                logger.error(f"Failed to open camera: {camera_config['name']}")
                return
            
            logger.info(f"Started recording from {camera_config['name']} to {output_file}")
            
            while self.is_running:
                ret, frame = cap.read()
                if not ret:
                    logger.warning(f"Failed to read frame from {camera_config['name']}")
                    break
                
                resized_frame = cv2.resize(frame, (width, height))
                out.write(resized_frame)
                
                # Small delay to prevent high CPU usage
                time.sleep(1/frame_rate)
            
        except Exception as e:
            logger.error(f"Error recording from {camera_config['name']}: {str(e)}")
        finally:
            cap.release()
            out.release()
            logger.info(f"Stopped recording from {camera_config['name']}")

    def start_surveillance(self):
        """Start the surveillance system"""
        if self.is_running:
            logger.warning("Surveillance system is already running")
            return
        
        self.is_running = True
        logger.info("Starting surveillance system")
        
        try:
            self.setup_directories()
            self.cleanup_old_recordings()
            
            for camera in self.cameras:
                if camera['enabled']:
                    if not self.test_camera_connection(camera):
                        logger.error(f"Skipping camera {camera['name']} due to connection issues")
                        continue
                    
                    # Start recording in a separate thread for each camera
                    import threading
                    thread = threading.Thread(target=self.record_camera, args=(camera,))
                    thread.daemon = True
                    thread.start()
            
            # Keep main thread alive
            while self.is_running:
                time.sleep(1)
                
        except KeyboardInterrupt:
            logger.info("Received keyboard interrupt, shutting down...")
            self.stop_surveillance()
        except Exception as e:
            logger.error(f"Error
