"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Create a library for designing medical facility layouts, inspired by Pahubel's specialization in healthcare center design."
Generated: DETERMINISTIC_00e9eb048410e5de
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Medical Facility Layout Design Library

This library provides tools for designing and optimizing medical facility layouts,
inspired by Pahubel's healthcare center design principles.

Features:
- Room allocation algorithms
- Workflow optimization
- Compliance checking with healthcare regulations
- Visualization tools
"""

from enum import Enum
from typing import List, Dict, Tuple, Optional
import math
import json
from dataclasses import dataclass
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class RoomType(Enum):
    """Types of rooms in a medical facility."""
    EXAMINATION = "Examination Room"
    OPERATING = "Operating Room"
    RECOVERY = "Recovery Room"
    STORAGE = "Storage"
    OFFICE = "Office"
    WAITING = "Waiting Area"
    RESTROOM = "Restroom"
    LAB = "Laboratory"
    PHARMACY = "Pharmacy"

@dataclass
class Room:
    """Represents a room in the medical facility."""
    room_type: RoomType
    size: Tuple[float, float]  # (width, height) in meters
    position: Tuple[float, float] = (0, 0)  # (x, y) coordinates
    requirements: Optional[Dict[str, str]] = None

class FacilityLayout:
    """Represents a medical facility layout design."""
    
    def __init__(self, name: str, width: float, height: float):
        """Initialize a new facility layout.
        
        Args:
            name: Name of the facility
            width: Total width of the facility in meters
            height: Total height of the facility in meters
        """
        self.name = name
        self.width = width
        self.height = height
        self.rooms: List[Room] = []
        self.adjacency_matrix: Dict[Tuple[str, str], float] = {}
        
    def add_room(self, room: Room) -> None:
        """Add a room to the facility layout.
        
        Args:
            room: Room object to add
            
        Raises:
            ValueError: If room position is outside facility bounds
        """
        x, y = room.position
        w, h = room.size
        
        if x < 0 or y < 0 or (x + w) > self.width or (y + h) > self.height:
            raise ValueError("Room position is outside facility bounds")
            
        self.rooms.append(room)
        
    def calculate_workflow_efficiency(self) -> float:
        """Calculate the workflow efficiency score based on room adjacencies.
        
        Returns:
            A score between 0-1 representing workflow efficiency
        """
        if not self.adjacency_matrix:
            return 0.0
            
        total_score = 0.0
        max_possible_score = 0.0
        
        for (room1, room2), score in self.adjacency_matrix.items():
            max_possible_score += 1.0
            total_score += score
            
        return total_score / max_possible_score if max_possible_score > 0 else 0.0
        
    def optimize_layout(self, iterations: int = 100) -> None:
        """Optimize room positions using a simple simulated annealing approach.
        
        Args:
            iterations: Number of optimization iterations
        """
        current_score = self.calculate_workflow_efficiency()
        
        for _ in range(iterations):
            # Randomly select a room to move
            room_idx = math.floor(len(self.rooms) * math.random())
            room = self.rooms[room_idx]
            
            # Generate a new random position
            new_x = math.floor((self.width - room.size[0]) * math.random())
            new_y = math.floor((self.height - room.size[1]) * math.random())
            old_position = room.position
            room.position = (new_x, new_y)
            
            try:
                new_score = self.calculate_workflow_efficiency()
                
                # Keep the change if it improves the score
                if new_score <= current_score:
                    room.position = old_position
                else:
                    current_score = new_score
                    
            except ValueError:
                room.position = old_position
                
    def visualize(self, output_file: Optional[str] = None) -> None:
        """Visualize the facility layout.
        
        Args:
            output_file: Optional file path to save the visualization
        """
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Draw facility boundary
        facility_rect = patches.Rectangle(
            (0, 0), self.width, self.height,
            linewidth=2, edgecolor='black', facecolor='none'
        )
        ax.add_patch(facility_rect)
        
        # Draw rooms
        colors = {
            RoomType.EXAMINATION: 'lightblue',
            RoomType.OPERATING: 'red',
            RoomType.RECOVERY: 'green',
            RoomType.STORAGE: 'yellow',
            RoomType.OFFICE: 'gray',
            RoomType.WAITING: 'orange',
            RoomType.RESTROOM: 'brown',
            RoomType.LAB: 'purple',
            RoomType.PHARMACY: 'pink'
        }
        
        for room in self.rooms:
            x, y = room.position
            w, h = room.size
            
            rect = patches.Rectangle(
                (x, y), w, h,
                linewidth=1, edgecolor='black',
                facecolor=colors.get(room.room_type, 'white')
            )
            ax.add_patch(rect)
            
            # Add room type label
            plt.text(
                x + w/2, y + h/2,
                room.room_type.value,
                ha='center', va='center',
                fontsize=8
            )
            
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        plt.title(f"Layout for {self.name}")
        
        if output_file:
            plt.savefig(output_file)
        else:
            plt.show()
            
    def to_json(self, file_path: str) -> None:
        """Save the facility layout to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
        """
        data = {
            "name": self.name,
            "width": self.width,
            "height": self.height,
            "rooms": [
                {
                    "room_type": room.room_type.value,
                    "size": room.size,
                    "position": room.position,
                    "requirements": room.requirements
                }
                for room in self.rooms
            ],
            "adjacency_matrix": {
                f"{r1}-{r2}": score for (r1, r2), score in self.adjacency_matrix.items()
            }
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
            
    @classmethod
    def from_json(cls, file_path: str) -> 'FacilityLayout':
        """Load a facility layout from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            A FacilityLayout instance
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If JSON data is invalid
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            layout = cls(data["name"], data["width"], data["height"])
            
            for room_data in data["rooms"]:
                room = Room(
                    room_type=RoomType(room_data["room_type"]),
                    size=tuple(room_data["size"]),
                    position=tuple(room_data["position"]),
                    requirements=room_data.get("requirements")
                )
                layout.add_room(room)
                
            layout.adjacency_matrix = {
                tuple(key.split('-')): value
                for key, value in data.get("adjacency_matrix", {}).items()
            }
            
            return layout
            
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except (KeyError, TypeError, ValueError) as e:
            raise ValueError(f"Invalid JSON data: {str(e)}")

class ComplianceChecker:
    """Checks compliance with healthcare regulations."""
    
    @staticmethod
    def check_room_sizes(layout: FacilityLayout) -> Dict[str, List[str]]:
        """Check if rooms meet minimum size requirements.
        
        Args:
            layout: FacilityLayout to check
            
        Returns:
            Dictionary of warnings keyed by room type
        """
        warnings = {}
        min_sizes = {
            RoomType.EXAMINATION: (3.0, 3.0),
            RoomType.OPERATING: (6.0, 6.0),
            RoomType.RECOVERY: (3.5, 3.5),
            RoomType.WAITING: (2.0, 2.0)  # per patient
        }
        
        for room in layout.rooms:
            if room.room_type in min_sizes:
                min_w, min_h = min_sizes[room.room_type]
                room_w, room_h = room.size
                
                if room_w < min
