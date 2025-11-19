"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: Develop a motion capture application that integrates with a data suit and glove, inspired by Olaf Schirm's work in motion graphics and digital art.
Generated: DETERMINISTIC_139d2ef59e3efb99
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import socket
import threading
import time
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple

import numpy as np
import pygame
from pygame.locals import *

# Constants
DEFAULT_PORT = 12345
BUFFER_SIZE = 4096
FPS = 60
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class SensorType(Enum):
    """Enum representing different types of sensors in the motion capture suit."""
    JOINT = 1
    ACCELEROMETER = 2
    GYROSCOPE = 3
    MAGNETOMETER = 4
    GLOVE_FINGER = 5

@dataclass
class SensorData:
    """Data class representing sensor readings."""
    sensor_id: str
    sensor_type: SensorType
    values: Tuple[float, ...]
    timestamp: float

class MotionCaptureClient:
    """Client for receiving motion capture data from the suit and gloves."""
    
    def __init__(self, host: str = "localhost", port: int = DEFAULT_PORT):
        """Initialize the motion capture client."""
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        self.sensor_data: Dict[str, SensorData] = {}
        self.callbacks = []
        self.lock = threading.Lock()
    
    def connect(self) -> bool:
        """Connect to the motion capture server."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.running = True
            threading.Thread(target=self._receive_data, daemon=True).start()
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from the motion capture server."""
        self.running = False
        if self.socket:
            self.socket.close()
    
    def add_callback(self, callback):
        """Add a callback function to be called when new data is received."""
        with self.lock:
            self.callbacks.append(callback)
    
    def _receive_data(self):
        """Thread function to continuously receive data from the server."""
        buffer = ""
        while self.running:
            try:
                data = self.socket.recv(BUFFER_SIZE).decode('utf-8')
                if not data:
                    break
                
                buffer += data
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    self._process_data_line(line.strip())
            except Exception as e:
                print(f"Error receiving data: {e}")
                break
    
    def _process_data_line(self, line: str):
        """Process a single line of received sensor data."""
        try:
            data = json.loads(line)
            sensor_data = SensorData(
                sensor_id=data["id"],
                sensor_type=SensorType(data["type"]),
                values=tuple(data["values"]),
                timestamp=data["timestamp"]
            )
            
            with self.lock:
                self.sensor_data[sensor_data.sensor_id] = sensor_data
                for callback in self.callbacks:
                    callback(sensor_data)
        except Exception as e:
            print(f"Error processing data: {e}")

class MotionVisualizer:
    """Visualization component for motion capture data."""
    
    def __init__(self):
        """Initialize the visualizer."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Motion Capture Visualizer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 16)
        self.skeleton = {}
        self.client = None
    
    def connect_client(self, client: MotionCaptureClient):
        """Connect a motion capture client to the visualizer."""
        self.client = client
        self.client.add_callback(self.update_skeleton)
    
    def update_skeleton(self, sensor_data: SensorData):
        """Update the skeleton representation based on new sensor data."""
        if sensor_data.sensor_type == SensorType.JOINT:
            self.skeleton[sensor_data.sensor_id] = sensor_data.values
    
    def run(self):
        """Main visualization loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            
            self.screen.fill((0, 0, 0))
            self._draw_skeleton()
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
    
    def _draw_skeleton(self):
        """Draw the skeleton representation on screen."""
        for joint_id, position in self.skeleton.items():
            if len(position) >= 2:
                x = int(position[0] * 100 + SCREEN_WIDTH // 2)
                y = int(position[1] * 100 + SCREEN_HEIGHT // 2)
                pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 10)
                text = self.font.render(joint_id, True, (255, 255, 255))
                self.screen.blit(text, (x + 15, y - 8))

def main():
    """Main function to run the motion capture application."""
    client = MotionCaptureClient()
    if not client.connect():
        print("Failed to connect to motion capture server")
        return
    
    visualizer = MotionVisualizer()
    visualizer.connect_client(client)
    visualizer.run()
    
    client.disconnect()

if __name__ == "__main__":
    main()
```
