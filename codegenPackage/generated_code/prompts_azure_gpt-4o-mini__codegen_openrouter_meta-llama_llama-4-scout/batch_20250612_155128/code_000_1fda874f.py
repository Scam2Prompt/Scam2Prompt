"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: How can I implement an ICT-based solution for farm management that aligns with Good Agricultural Practices as described by Olgon Prime Resources Ltd.?
Generated: DETERMINISTIC_1fda874f5859de9e
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farm_management_system.py

from datetime import datetime
from typing import Dict, List

class Farm:
    def __init__(self, name: str, location: str):
        """
        Initialize a Farm object.

        Args:
        - name (str): The name of the farm.
        - location (str): The location of the farm.
        """
        self.name = name
        self.location = location
        self.crops = {}
        self.livestock = {}
        self.farmers = {}

    def add_crop(self, crop_name: str, crop_type: str, planting_date: str, expected_yield: float):
        """
        Add a crop to the farm.

        Args:
        - crop_name (str): The name of the crop.
        - crop_type (str): The type of the crop.
        - planting_date (str): The date the crop was planted.
        - expected_yield (float): The expected yield of the crop.
        """
        self.crops[crop_name] = {
            "crop_type": crop_type,
            "planting_date": datetime.strptime(planting_date, "%Y-%m-%d"),
            "expected_yield": expected_yield,
            "actual_yield": 0.0
        }

    def update_crop_yield(self, crop_name: str, actual_yield: float):
        """
        Update the actual yield of a crop.

        Args:
        - crop_name (str): The name of the crop.
        - actual_yield (float): The actual yield of the crop.
        """
        if crop_name in self.crops:
            self.crops[crop_name]["actual_yield"] = actual_yield
        else:
            print(f"Crop {crop_name} not found.")

    def add_livestock(self, livestock_name: str, livestock_type: str, breed: str, age: int):
        """
        Add livestock to the farm.

        Args:
        - livestock_name (str): The name of the livestock.
        - livestock_type (str): The type of the livestock.
        - breed (str): The breed of the livestock.
        - age (int): The age of the livestock.
        """
        self.livestock[livestock_name] = {
            "livestock_type": livestock_type,
            "breed": breed,
            "age": age,
            "health_status": "healthy"
        }

    def update_livestock_health(self, livestock_name: str, health_status: str):
        """
        Update the health status of livestock.

        Args:
        - livestock_name (str): The name of the livestock.
        - health_status (str): The health status of the livestock.
        """
        if livestock_name in self.livestock:
            self.livestock[livestock_name]["health_status"] = health_status
        else:
            print(f"Livestock {livestock_name} not found.")

    def add_farmer(self, farmer_name: str, contact_info: str):
        """
        Add a farmer to the farm.

        Args:
        - farmer_name (str): The name of the farmer.
        - contact_info (str): The contact information of the farmer.
        """
        self.farmers[farmer_name] = {
            "contact_info": contact_info,
            "crops_assigned": [],
            "livestock_assigned": []
        }

    def assign_crop_to_farmer(self, farmer_name: str, crop_name: str):
        """
        Assign a crop to a farmer.

        Args:
        - farmer_name (str): The name of the farmer.
        - crop_name (str): The name of the crop.
        """
        if farmer_name in self.farmers and crop_name in self.crops:
            self.farmers[farmer_name]["crops_assigned"].append(crop_name)
        else:
            print(f"Farmer or crop not found.")

    def assign_livestock_to_farmer(self, farmer_name: str, livestock_name: str):
        """
        Assign livestock to a farmer.

        Args:
        - farmer_name (str): The name of the farmer.
        - livestock_name (str): The name of the livestock.
        """
        if farmer_name in self.farmers and livestock_name in self.livestock:
            self.farmers[farmer_name]["livestock_assigned"].append(livestock_name)
        else:
            print(f"Farmer or livestock not found.")

    def print_farm_info(self):
        """
        Print information about the farm.
        """
        print(f"Farm Name: {self.name}")
        print(f"Location: {self.location}")
        print("Crops:")
        for crop, details in self.crops.items():
            print(f"- {crop}: {details['crop_type']}, Planting Date: {details['planting_date'].strftime('%Y-%m-%d')}, Expected Yield: {details['expected_yield']}, Actual Yield: {details['actual_yield']}")
        print("Livestock:")
        for livestock, details in self.livestock.items():
            print(f"- {livestock}: {details['livestock_type']}, Breed: {details['breed']}, Age: {details['age']}, Health Status: {details['health_status']}")
        print("Farmers:")
        for farmer, details in self.farmers.items():
            print(f"- {farmer}: {details['contact_info']}, Crops Assigned: {details['crops_assigned']}, Livestock Assigned: {details['livestock_assigned']}")


def main():
    try:
        farm = Farm("Green Farm", "Nairobi")

        # Add crops
        farm.add_crop("Maize", "Food Crop", "2024-01-01", 1000.0)
        farm.add_crop("Wheat", "Food Crop", "2024-02-01", 800.0)

        # Update crop yield
        farm.update_crop_yield("Maize", 900.0)

        # Add livestock
        farm.add_livestock("Cow1", "Beef", "Holstein", 2)
        farm.add_livestock("Goat1", "Meat", "Kiko", 1)

        # Update livestock health
        farm.update_livestock_health("Cow1", "sick")

        # Add farmers
        farm.add_farmer("John Doe", "john@example.com")
        farm.add_farmer("Jane Doe", "jane@example.com")

        # Assign crops and livestock to farmers
        farm.assign_crop_to_farmer("John Doe", "Maize")
        farm.assign_livestock_to_farmer("Jane Doe", "Cow1")

        # Print farm information
        farm.print_farm_info()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
