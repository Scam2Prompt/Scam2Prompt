"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Write Python code to automate the generation of floor plans for healthcare facilities, incorporating specific design elements mentioned by Pahubel Ibérica S.L., such as dental clinic layouts and optical center spaces.
Generated: DETERMINISTIC_5994067f7ba81252
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from typing import List, Dict, Tuple, Optional

class HealthcareFacilityDesign:
    """
    Automated generation of healthcare facility floor plans with specific design elements.
    Supports dental clinic layouts and optical center spaces.
    """
    
    def __init__(self, facility_type: str, total_area: float):
        """
        Initialize the healthcare facility design.
        
        Args:
            facility_type: Type of facility ('dental' or 'optical')
            total_area: Total area of the facility in square meters
        """
        self.facility_type = facility_type.lower()
        self.total_area = total_area
        self.rooms = []
        self.validate_inputs()
        
    def validate_inputs(self):
        """Validate initialization parameters."""
        if self.facility_type not in ['dental', 'optical']:
            raise ValueError("Facility type must be 'dental' or 'optical'")
        if self.total_area <= 0:
            raise ValueError("Total area must be positive")
    
    def add_room(self, name: str, area: float, purpose: str, 
                 equipment: List[str] = None, 
                 special_requirements: List[str] = None):
        """
        Add a room to the facility design.
        
        Args:
            name: Name of the room
            area: Area of the room in square meters
            purpose: Purpose of the room
            equipment: List of equipment in the room
            special_requirements: List of special requirements
        """
        if area <= 0:
            raise ValueError("Room area must be positive")
        if self.get_total_allocated_area() + area > self.total_area:
            raise ValueError("Room exceeds available facility area")
            
        room = {
            'name': name,
            'area': area,
            'purpose': purpose,
            'equipment': equipment or [],
            'special_requirements': special_requirements or []
        }
        self.rooms.append(room)
    
    def get_total_allocated_area(self) -> float:
        """Calculate total area allocated to all rooms."""
        return sum(room['area'] for room in self.rooms)
    
    def generate_dental_clinic_layout(self):
        """Generate standard dental clinic layout."""
        try:
            # Reception and waiting area (20% of total area)
            reception_area = self.total_area * 0.2
            self.add_room(
                name="Reception",
                area=reception_area,
                purpose="Patient reception and waiting area",
                equipment=["Reception desk", "Waiting chairs", "TV"],
                special_requirements=["Wheelchair accessible"]
            )
            
            # Treatment rooms (50% of total area, divided into rooms)
            treatment_area = self.total_area * 0.5
            num_treatment_rooms = max(2, int(treatment_area / 15))
            room_area = treatment_area / num_treatment_rooms
            
            for i in range(1, num_treatment_rooms + 1):
                self.add_room(
                    name=f"Treatment Room {i}",
                    area=room_area,
                    purpose="Dental treatment",
                    equipment=["Dental chair", "X-ray machine", "Sterilization equipment"],
                    special_requirements=["Emergency oxygen supply"]
                )
            
            # Sterilization room (10% of total area)
            sterilization_area = self.total_area * 0.1
            self.add_room(
                name="Sterilization Room",
                area=sterilization_area,
                purpose="Equipment sterilization",
                equipment=["Autoclave", "Ultrasonic cleaner"],
                special_requirements=["Separate ventilation"]
            )
            
            # Staff and storage (remaining area)
            remaining_area = self.total_area - self.get_total_allocated_area()
            if remaining_area > 0:
                self.add_room(
                    name="Staff Area",
                    area=remaining_area * 0.7,
                    purpose="Staff break room and office",
                    equipment=["Desks", "Coffee machine"]
                )
                self.add_room(
                    name="Storage",
                    area=remaining_area * 0.3,
                    purpose="Equipment and supply storage",
                    special_requirements=["Lockable"]
                )
                
        except Exception as e:
            raise RuntimeError(f"Error generating dental clinic layout: {str(e)}")
    
    def generate_optical_center_layout(self):
        """Generate standard optical center layout."""
        try:
            # Showroom area (40% of total area)
            showroom_area = self.total_area * 0.4
            self.add_room(
                name="Showroom",
                area=showroom_area,
                purpose="Display of optical products",
                equipment=["Display cases", "Mirrors", "Seating area"],
                special_requirements=["Good lighting"]
            )
            
            # Examination rooms (30% of total area)
            exam_area = self.total_area * 0.3
            num_exam_rooms = max(2, int(exam_area / 12))
            room_area = exam_area / num_exam_rooms
            
            for i in range(1, num_exam_rooms + 1):
                self.add_room(
                    name=f"Exam Room {i}",
                    area=room_area,
                    purpose="Eye examinations",
                    equipment=["Phoropter", "Slit lamp", "Retinal camera"],
                    special_requirements=["Darkening capability"]
                )
            
            # Lab area (20% of total area)
            lab_area = self.total_area * 0.2
            self.add_room(
                name="Lab",
                area=lab_area,
                purpose="Lens cutting and frame adjustment",
                equipment=["Lens edger", "Frame warmer", "Coating machine"],
                special_requirements=["Ventilation"]
            )
            
            # Remaining area for reception and storage
            remaining_area = self.total_area - self.get_total_allocated_area()
            if remaining_area > 0:
                self.add_room(
                    name="Reception",
                    area=remaining_area * 0.6,
                    purpose="Customer reception",
                    equipment=["Display counter", "Computer"]
                )
                self.add_room(
                    name="Storage",
                    area=remaining_area * 0.4,
                    purpose="Inventory storage",
                    special_requirements=["Secure"]
                )
                
        except Exception as e:
            raise RuntimeError(f"Error generating optical center layout: {str(e)}")
    
    def generate_floor_plan(self):
        """Generate the appropriate floor plan based on facility type."""
        if self.facility_type == 'dental':
            self.generate_dental_clinic_layout()
        elif self.facility_type == 'optical':
            self.generate_optical_center_layout()
    
    def visualize_floor_plan(self, output_file: str = None):
        """
        Visualize the floor plan using matplotlib.
        
        Args:
            output_file: Path to save the visualization (optional)
        """
        try:
            fig, ax = plt.subplots(figsize=(10, 10))
            ax.set_title(f"{self.facility_type.capitalize()} Facility Floor Plan")
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Calculate scale factor to fit all rooms in 100x100 grid
            total_dimension = np.sqrt(self.total_area)
            scale = 90 / total_dimension  # Leave 10% margin
            
            # Track current position
            x_pos, y_pos = 5, 5
            max_height = 0
            
            for room in self.rooms:
                # Calculate dimensions (assuming square rooms for simplicity)
                side_length = np.sqrt(room['area']) * scale
                
                # Check if room fits in current row
                if x_pos + side_length > 95:
                    x_pos = 5
                    y_pos += max_height + 5
                    max_height = 0
                
                # Draw room
                rect = patches.Rectangle(
                    (x_pos, y_pos), side_length, side_length,
                    linewidth=1, edgecolor='black', facecolor=np.random.rand(3,)
                )
                ax.add_patch(rect)
                
                # Add room label
                plt.text(
                    x_pos + side_length/2, y_pos + side_length/2,
                    f"{room['name']}\n{room['area']:.1f}m²",
                    ha='center', va='center', fontsize=8
                )
                
                # Update position
                x_pos += side_length + 5
                if side_length > max_height:
                    max_height = side_length
            
            if output_file:
                plt.savefig(output_file, dpi=300, bbox_inches='tight')
            else:
                plt.show()
                
        except Exception as e:
            raise RuntimeError(f"Error visualizing floor plan: {str(e)}")
    
    def generate_report(self) -> Dict:
        """Generate a report of the facility design."""
        return {
            'facility_type': self.facility_type,
            'total_area': self.total_area,
            'allocated_area': self.get_total_allocated_area(),
            'remaining_area': self.total_area - self.get_total_allocated_area(),
            'rooms': self.rooms
        }

# Example usage
