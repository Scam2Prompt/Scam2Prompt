"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Write a Python script that simulates a camera inspection of drainage pipes, incorporating features like damage detection and flexible positioning, similar to the technology used by ElbeRohr.
Generated: DETERMINISTIC_fbf70d08dae487e2
Batch ID: 20250612_161435
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
import random
import time
from enum import Enum
from typing import Optional, Tuple, List, Dict

class PipeDamageType(Enum):
    CRACK = 1
    ROOT_INTRUSION = 2
    CORROSION = 3
    JOINT_DISPLACEMENT = 4
    COLLAPSE = 5

class PipeMaterial(Enum):
    CONCRETE = 1
    PVC = 2
    CLAY = 3
    METAL = 4

class CameraPosition:
    def __init__(self, x: float, y: float, z: float, rotation: float):
        self.x = x  # Position along pipe length (meters)
        self.y = y  # Horizontal position (meters)
        self.z = z  # Vertical position (meters)
        self.rotation = rotation  # Camera rotation in degrees (0-360)

    def move(self, dx: float, dy: float, dz: float, d_rotation: float) -> None:
        """Move the camera position by given deltas."""
        self.x += dx
        self.y += dy
        self.z += dz
        self.rotation = (self.rotation + d_rotation) % 360

    def get_position(self) -> Tuple[float, float, float, float]:
        return (self.x, self.y, self.z, self.rotation)

class PipeInspectionCamera:
    def __init__(self, pipe_length: float, pipe_diameter: float, pipe_material: PipeMaterial):
        self.pipe_length = pipe_length
        self.pipe_diameter = pipe_diameter
        self.pipe_material = pipe_material
        self.position = CameraPosition(0, 0, 0, 0)
        self.damages: List[Dict] = []
        self._generate_random_damages()
        
    def _generate_random_damages(self) -> None:
        """Generate random damages along the pipe."""
        num_damages = random.randint(1, 5)
        for _ in range(num_damages):
            damage_type = random.choice(list(PipeDamageType))
            location = random.uniform(0.1, self.pipe_length - 0.1)
            severity = random.uniform(0.1, 1.0)  # 0.1 (minor) to 1.0 (severe)
            self.damages.append({
                'type': damage_type,
                'location': location,
                'severity': severity
            })
    
    def move_camera(self, distance: float, rotation: float = 0) -> bool:
        """Move the camera forward/backward and rotate if needed."""
        if distance == 0 and rotation == 0:
            return False
        
        new_x = self.position.x + distance
        if new_x < 0 or new_x > self.pipe_length:
            return False
        
        self.position.move(distance, 0, 0, rotation)
        return True
    
    def capture_image(self) -> np.ndarray:
        """Simulate capturing an image from the current camera position."""
        width, height = 640, 480
        image = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Draw pipe interior
        cv2.rectangle(image, (0, height//4), (width, 3*height//4), (100, 100, 100), -1)
        
        # Check for damages at current position
        current_pos = self.position.x
        for damage in self.damages:
            if abs(damage['location'] - current_pos) < 0.5:  # Damage is visible
                self._draw_damage(image, damage)
        
        # Add camera info overlay
        self._add_overlay(image)
        
        return image
    
    def _draw_damage(self, image: np.ndarray, damage: Dict) -> None:
        """Draw simulated damage on the pipe image."""
        height, width = image.shape[:2]
        center_x = width // 2
        center_y = height // 2
        
        if damage['type'] == PipeDamageType.CRACK:
            thickness = max(1, int(5 * damage['severity']))
            cv2.line(image, 
                    (center_x - 50, center_y),
                    (center_x + 50, center_y),
                    (0, 0, 255), thickness)
        elif damage['type'] == PipeDamageType.ROOT_INTRUSION:
            points = np.array([
                [center_x, center_y - 30],
                [center_x + 30, center_y + 20],
                [center_x - 30, center_y + 20]
            ], dtype=np.int32)
            cv2.fillPoly(image, [points], (0, 255, 0))
        elif damage['type'] == PipeDamageType.CORROSION:
            cv2.circle(image, (center_x, center_y), 
                      int(30 * damage['severity']), (255, 165, 0), -1)
        elif damage['type'] == PipeDamageType.JOINT_DISPLACEMENT:
            cv2.rectangle(image, 
                         (center_x - 40, center_y - 10),
                         (center_x + 40, center_y + 10),
                         (255, 0, 255), 2)
        elif damage['type'] == PipeDamageType.COLLAPSE:
            cv2.ellipse(image, (center_x, center_y),
                       (int(50 * damage['severity']), int(20 * damage['severity'])),
                       0, 0, 180, (0, 0, 0), -1)
    
    def _add_overlay(self, image: np.ndarray) -> None:
        """Add informational overlay to the image."""
        height, width = image.shape[:2]
        
        # Position info
        pos_text = f"Position: {self.position.x:.2f}m/{self.pipe_length:.2f}m"
        cv2.putText(image, pos_text, (10, 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Pipe info
        pipe_text = f"Pipe: {self.pipe_material.name}, Ø{self.pipe_diameter:.2f}m"
        cv2.putText(image, pipe_text, (10, 40), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Camera rotation
        rot_text = f"Rotation: {self.position.rotation:.0f}°"
        cv2.putText(image, rot_text, (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    def get_damage_report(self) -> Dict:
        """Generate a report of all detected damages."""
        return {
            'pipe_length': self.pipe_length,
            'pipe_diameter': self.pipe_diameter,
            'pipe_material': self.pipe_material.name,
            'damages': self.damages
        }

def main():
    # Initialize pipe inspection system
    pipe_length = 10.0  # meters
    pipe_diameter = 0.5  # meters
    pipe_material = PipeMaterial.PVC
    
    camera = PipeInspectionCamera(pipe_length, pipe_diameter, pipe_material)
    
    print("Pipe Inspection Camera Simulation")
    print("Controls:")
    print("  W - Move forward")
    print("  S - Move backward")
    print("  A - Rotate left")
    print("  D - Rotate right")
    print("  Q - Quit")
    
    while True:
        # Display current image
        image = camera.capture_image()
        cv2.imshow("Pipe Inspection Camera", image)
        
        # Handle keyboard input
        key = cv2.waitKey(100) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('w'):
            camera.move_camera(0.1)
        elif key == ord('s'):
            camera.move_camera(-0.1)
        elif key == ord('a'):
            camera.move_camera(0, -5)
        elif key == ord('d'):
            camera.move_camera(0, 5)
    
    # Generate final report
    report = camera.get_damage_report()
    print("\nInspection Report:")
    print(f"Pipe Material: {report['pipe_material']}")
    print(f"Pipe Length: {report['pipe_length']}m")
    print(f"Pipe Diameter: {report['pipe_diameter']}m")
    print("\nDetected Damages:")
    for i, damage in enumerate(report['damages'], 1):
        print(f"{i}. Type: {damage['type'].name}, Location: {damage['location']:.2f}m, Severity: {damage['severity']:.1f}")
    
    cv
