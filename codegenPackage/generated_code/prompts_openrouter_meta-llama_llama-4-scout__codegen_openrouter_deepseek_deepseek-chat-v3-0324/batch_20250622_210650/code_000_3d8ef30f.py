"""
Generated Code Metadata:
========================
Original URL: https://knitplusltd.com
Prompt: "Write a Python code to manage the production process of a sustainable garment company like Knit Plus Ltd, including sections for sewing, cutting, quality, and finishing."
Generated: DETERMINISTIC_3d8ef30f6dcec297
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
import json
import os

class ProductionStage(Enum):
    CUTTING = "Cutting"
    SEWING = "Sewing"
    QUALITY = "Quality Control"
    FINISHING = "Finishing"

class GarmentStatus(Enum):
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED_QC = "Failed Quality Control"
    HOLD = "On Hold"

class Garment:
    def __init__(self, garment_id: str, style: str, material: str, quantity: int):
        self.garment_id = garment_id
        self.style = style
        self.material = material
        self.quantity = quantity
        self.status = GarmentStatus.IN_PROGRESS
        self.current_stage = ProductionStage.CUTTING
        self.history = []
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
    def update_stage(self, new_stage: ProductionStage, notes: str = "") -> None:
        """Update the production stage of the garment."""
        if new_stage not in ProductionStage:
            raise ValueError("Invalid production stage")
            
        self.current_stage = new_stage
        self.updated_at = datetime.datetime.now()
        self.history.append({
            "timestamp": datetime.datetime.now(),
            "stage": new_stage.value,
            "notes": notes
        })
        
    def update_status(self, new_status: GarmentStatus, notes: str = "") -> None:
        """Update the status of the garment."""
        if new_status not in GarmentStatus:
            raise ValueError("Invalid garment status")
            
        self.status = new_status
        self.updated_at = datetime.datetime.now()
        self.history.append({
            "timestamp": datetime.datetime.now(),
            "status": new_status.value,
            "notes": notes
        })

class ProductionManager:
    def __init__(self):
        self.garments: Dict[str, Garment] = {}
        self.stage_counts = {stage: 0 for stage in ProductionStage}
        
    def add_garment(self, garment: Garment) -> None:
        """Add a new garment to production."""
        if garment.garment_id in self.garments:
            raise ValueError("Garment ID already exists")
            
        self.garments[garment.garment_id] = garment
        self.stage_counts[ProductionStage.CUTTING] += 1
        
    def move_to_stage(self, garment_id: str, new_stage: ProductionStage, notes: str = "") -> None:
        """Move a garment to a new production stage."""
        if garment_id not in self.garments:
            raise ValueError("Garment not found")
            
        garment = self.garments[garment_id]
        old_stage = garment.current_stage
        
        garment.update_stage(new_stage, notes)
        self.stage_counts[old_stage] -= 1
        self.stage_counts[new_stage] += 1
        
    def update_garment_status(self, garment_id: str, new_status: GarmentStatus, notes: str = "") -> None:
        """Update the status of a garment."""
        if garment_id not in self.garments:
            raise ValueError("Garment not found")
            
        self.garments[garment_id].update_status(new_status, notes)
        
    def get_garment(self, garment_id: str) -> Optional[Garment]:
        """Retrieve a garment by ID."""
        return self.garments.get(garment_id)
        
    def get_production_report(self) -> Dict:
        """Generate a production report."""
        return {
            "total_garments": len(self.garments),
            "stage_counts": {stage.value: count for stage, count in self.stage_counts.items()},
            "status_counts": {
                status.value: sum(1 for g in self.garments.values() if g.status == status)
                for status in GarmentStatus
            }
        }
        
    def save_to_file(self, filename: str) -> None:
        """Save production data to a JSON file."""
        data = {
            "garments": [
                {
                    "garment_id": g.garment_id,
                    "style": g.style,
                    "material": g.material,
                    "quantity": g.quantity,
                    "status": g.status.value,
                    "current_stage": g.current_stage.value,
                    "history": [
                        {
                            "timestamp": h["timestamp"].isoformat(),
                            "stage": h.get("stage", ""),
                            "status": h.get("status", ""),
                            "notes": h["notes"]
                        } for h in g.history
                    ],
                    "created_at": g.created_at.isoformat(),
                    "updated_at": g.updated_at.isoformat()
                } for g in self.garments.values()
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            
    def load_from_file(self, filename: str) -> None:
        """Load production data from a JSON file."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")
            
        with open(filename, 'r') as f:
            data = json.load(f)
            
        self.garments = {}
        self.stage_counts = {stage: 0 for stage in ProductionStage}
        
        for g_data in data["garments"]:
            garment = Garment(
                g_data["garment_id"],
                g_data["style"],
                g_data["material"],
                g_data["quantity"]
            )
            
            garment.status = GarmentStatus(g_data["status"])
            garment.current_stage = ProductionStage(g_data["current_stage"])
            garment.created_at = datetime.datetime.fromisoformat(g_data["created_at"])
            garment.updated_at = datetime.datetime.fromisoformat(g_data["updated_at"])
            
            for h in g_data["history"]:
                entry = {
                    "timestamp": datetime.datetime.fromisoformat(h["timestamp"]),
                    "notes": h["notes"]
                }
                if "stage" in h and h["stage"]:
                    entry["stage"] = h["stage"]
                if "status" in h and h["status"]:
                    entry["status"] = h["status"]
                garment.history.append(entry)
                
            self.garments[garment.garment_id] = garment
            self.stage_counts[garment.current_stage] += 1

def main_menu():
    print("\nSustainable Garment Production Management")
    print("1. Add New Garment")
    print("2. Update Production Stage")
    print("3. Update Garment Status")
    print("4. View Garment Details")
    print("5. Generate Production Report")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")

def get_user_input(prompt: str, input_type=str):
    """Helper function to get user input with validation."""
    while True:
        try:
            user_input = input(prompt)
            if input_type == int:
                return int(user_input)
            elif input_type == float:
                return float(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    manager = ProductionManager()
    
    while True:
        main_menu()
        choice = get_user_input("Enter your choice (1-8): ", int)
        
        if choice == 1:
            try:
                garment_id = get_user_input("Enter garment ID: ")
                style = get_user_input("Enter style: ")
                material = get_user_input("Enter material: ")
                quantity = get_user_input("Enter quantity: ", int)
                
                garment = Garment(garment_id, style, material, quantity)
                manager.add_garment(garment)
                print(f"Garment {garment_id} added to production.")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == 2:
            garment_id = get_user_input("Enter garment ID: ")
            print("Available stages:")
            for i, stage in enumerate(ProductionStage, 1):
                print(f"{i}. {stage.value}")
            stage_choice = get_user_input("Select stage (1-4): ", int)
            
            if 1 <= stage_choice <= 4:
                notes = get_user_input("Enter notes (optional): ")
                try:
                    manager.move_to_stage(
                        garment_id,
                        list(ProductionStage)[stage_choice - 1],
                        notes
                    )
                    print(f"Garment {garment_id} moved to {list(ProductionStage)[stage_choice - 1].value}.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid stage selection.")
                
        elif choice == 3:
            garment_id = get_user_input("Enter garment ID: ")
            print("Available statuses:")
            for i, status in enumerate(GarmentStatus, 1):
                print(f"{i}. {status.value}")
            status_choice = get_user_input("Select status (1-4): ", int)
            
            if 1 <= status
