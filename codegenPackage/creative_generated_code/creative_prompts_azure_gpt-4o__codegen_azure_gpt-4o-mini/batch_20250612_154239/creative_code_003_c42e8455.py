"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Create a script using Python to simulate urban agriculture practices for food security, including modules for tracking crop growth and sharing resources, inspired by CEGEduc's focus on sustainable living.
Generated: DETERMINISTIC_c42e8455ffa3257a
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

class Crop:
    """A class to represent a crop in the urban agriculture simulation."""
    
    def __init__(self, name: str, growth_time: int, yield_amount: float):
        """
        Initialize a new crop with its name, growth time in days, and yield amount.
        
        Args:
            name (str): The name of the crop.
            growth_time (int): The growth time in days before harvest.
            yield_amount (float): The amount of produce per harvest.
        """
        self.name = name
        self.growth_time = growth_time
        self.yield_amount = yield_amount
        self.planted_date = None
    
    def plant(self) -> None:
        """Plant the crop by recording the current date."""
        self.planted_date = datetime.now()
    
    def is_ready_to_harvest(self) -> bool:
        """Check if the crop is ready to be harvested based on the growth time."""
        if self.planted_date is None:
            return False
        return datetime.now() >= self.planted_date + timedelta(days=self.growth_time)
    
    def harvest(self) -> float:
        """Harvest the crop if it's ready and return the yield amount."""
        if not self.is_ready_to_harvest():
            raise ValueError("Crop is not ready to harvest.")
        self.planted_date = None  # Reset for the next planting
        return self.yield_amount


class ResourceSharing:
    """A class to manage shared resources among urban farmers."""
    
    def __init__(self):
        """Initialize an empty resource sharing system."""
        self.resources: Dict[str, List[str]] = {}
    
    def add_resource(self, resource_name: str, owner: str) -> None:
        """Add a resource to the sharing system with an owner."""
        if resource_name not in self.resources:
            self.resources[resource_name] = []
        self.resources[resource_name].append(owner)
    
    def get_resources(self) -> Dict[str, List[str]]:
        """Retrieve the current list of shared resources."""
        return self.resources


class UrbanAgricultureSimulator:
    """A class to simulate urban agriculture practices."""
    
    def __init__(self):
        """Initialize the agriculture simulator with resources and crops."""
        self.crops: List[Crop] = []
        self.resource_sharing = ResourceSharing()
    
    def add_crop(self, crop: Crop) -> None:
        """Add a crop to the simulation."""
        self.crops.append(crop)
    
    def plant_crop(self, crop_name: str) -> None:
        """Plant a crop if it exists in the simulation."""
        for crop in self.crops:
            if crop.name == crop_name:
                crop.plant()
                return
        raise ValueError(f"Crop '{crop_name}' not found in simulation.")
    
    def harvest_crops(self) -> Dict[str, float]:
        """Harvest all ready crops and return their yields."""
        harvested_yields = {}
        for crop in self.crops:
            if crop.is_ready_to_harvest():
                try:
                    yield_amount = crop.harvest()
                    harvested_yields[crop.name] = yield_amount
                except ValueError as e:
                    print(e)
        return harvested_yields

    def share_resource(self, resource_name: str, owner: str) -> None:
        """Share a resource among urban farmers."""
        self.resource_sharing.add_resource(resource_name, owner)

    def export_data(self, filename: str) -> None:
        """Export current crop and resource data to a JSON file."""
        data = {
            "crops": [
                {
                    "name": crop.name,
                    "planted_date": crop.planted_date.isoformat() if crop.planted_date else None,
                    "growth_time": crop.growth_time,
                    "yield_amount": crop.yield_amount
                } for crop in self.crops
            ],
            "resources": self.resource_sharing.get_resources()
        }
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except IOError as e:
            print(f"Error saving data to file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a simulator instance
    simulator = UrbanAgricultureSimulator()
    
    # Add crops
    simulator.add_crop(Crop(name="Tomato", growth_time=90, yield_amount=10.0))
    simulator.add_crop(Crop(name="Lettuce", growth_time=30, yield_amount=5.0))
    
    # Plant a crop
    try:
        simulator.plant_crop("Tomato")
        # Simulate time passing for demonstration (in practice, this would be automated)
        import time; time.sleep(2)  # Mocking delay for testing purposes
    except ValueError as e:
        print(e)
    
    # Harvest crops
    harvested = simulator.harvest_crops()
    print("Harvested crops:", harvested)
    
    # Share resources
    simulator.share_resource("Compost", "Alice")
    
    # Export data
    simulator.export_data("urban_agriculture_data.json")
```
