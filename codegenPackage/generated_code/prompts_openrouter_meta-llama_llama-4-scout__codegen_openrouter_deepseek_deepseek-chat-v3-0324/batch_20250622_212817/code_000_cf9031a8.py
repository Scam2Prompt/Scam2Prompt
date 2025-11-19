"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write a Python script to track and manage car modifications, including performance upgrades and feature additions, for a Chevrolet Cobalt SS/TC.
Generated: DETERMINISTIC_cf9031a8e02b1255
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

class CarModificationTracker:
    """
    A class to track and manage car modifications for a Chevrolet Cobalt SS/TC.
    """
    
    def __init__(self, car_model: str = "Chevrolet Cobalt SS/TC", data_file: str = "modifications.json"):
        """
        Initialize the tracker with car model and data file.
        
        Args:
            car_model (str): The car model being tracked.
            data_file (str): File to store modification data.
        """
        self.car_model = car_model
        self.data_file = data_file
        self.modifications = self._load_data()
        
    def _load_data(self) -> Dict[str, List[Dict[str, Union[str, float, datetime]]]]:
        """
        Load modification data from JSON file.
        
        Returns:
            Dict: Dictionary containing modification data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")
                return {"performance": [], "features": []}
        return {"performance": [], "features": []}
    
    def _save_data(self) -> None:
        """
        Save modification data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.modifications, file, indent=4, default=str)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_performance_upgrade(
        self,
        upgrade_name: str,
        cost: float,
        horsepower_gain: float,
        torque_gain: float,
        date_installed: Optional[str] = None
    ) -> None:
        """
        Add a performance upgrade to the tracker.
        
        Args:
            upgrade_name (str): Name of the upgrade.
            cost (float): Cost of the upgrade.
            horsepower_gain (float): Horsepower gain from upgrade.
            torque_gain (float): Torque gain from upgrade.
            date_installed (str, optional): Installation date (YYYY-MM-DD). Defaults to current date.
        """
        if not date_installed:
            date_installed = datetime.now().strftime("%Y-%m-%d")
            
        upgrade = {
            "name": upgrade_name,
            "cost": cost,
            "horsepower_gain": horsepower_gain,
            "torque_gain": torque_gain,
            "date_installed": date_installed
        }
        
        self.modifications["performance"].append(upgrade)
        self._save_data()
    
    def add_feature_addition(
        self,
        feature_name: str,
        cost: float,
        description: str,
        date_installed: Optional[str] = None
    ) -> None:
        """
        Add a feature addition to the tracker.
        
        Args:
            feature_name (str): Name of the feature.
            cost (float): Cost of the feature.
            description (str): Description of the feature.
            date_installed (str, optional): Installation date (YYYY-MM-DD). Defaults to current date.
        """
        if not date_installed:
            date_installed = datetime.now().strftime("%Y-%m-%d")
            
        feature = {
            "name": feature_name,
            "cost": cost,
            "description": description,
            "date_installed": date_installed
        }
        
        self.modifications["features"].append(feature)
        self._save_data()
    
    def get_total_cost(self) -> float:
        """
        Calculate total cost of all modifications.
        
        Returns:
            float: Total cost of modifications.
        """
        total = 0.0
        for category in self.modifications.values():
            for mod in category:
                total += mod["cost"]
        return round(total, 2)
    
    def get_performance_gains(self) -> Dict[str, float]:
        """
        Calculate total performance gains.
        
        Returns:
            Dict: Total horsepower and torque gains.
        """
        hp_gain = 0.0
        torque_gain = 0.0
        
        for upgrade in self.modifications["performance"]:
            hp_gain += upgrade["horsepower_gain"]
            torque_gain += upgrade["torque_gain"]
            
        return {
            "total_horsepower_gain": round(hp_gain, 2),
            "total_torque_gain": round(torque_gain, 2)
        }
    
    def list_modifications(self) -> None:
        """
        Print all modifications in a readable format.
        """
        print(f"\nModifications for {self.car_model}:")
        print("\nPerformance Upgrades:")
        for i, upgrade in enumerate(self.modifications["performance"], 1):
            print(f"{i}. {upgrade['name']} - "
                  f"+{upgrade['horsepower_gain']} HP, "
                  f"+{upgrade['torque_gain']} lb-ft, "
                  f"${upgrade['cost']}, "
                  f"Installed: {upgrade['date_installed']}")
        
        print("\nFeature Additions:")
        for i, feature in enumerate(self.modifications["features"], 1):
            print(f"{i}. {feature['name']} - "
                  f"${feature['cost']}, "
                  f"Installed: {feature['date_installed']}\n"
                  f"   Description: {feature['description']}")
        
        print(f"\nTotal Cost: ${self.get_total_cost()}")
        gains = self.get_performance_gains()
        print(f"Total Performance Gains: +{gains['total_horsepower_gain']} HP, +{gains['total_torque_gain']} lb-ft")

# Example usage
if __name__ == "__main__":
    tracker = CarModificationTracker()
    
    # Add some example modifications
    tracker.add_performance_upgrade(
        "Stage 1 Tune",
        500.00,
        30.0,
        25.0,
        "2023-01-15"
    )
    
    tracker.add_performance_upgrade(
        "Cold Air Intake",
        250.00,
        10.0,
        8.0
    )
    
    tracker.add_feature_addition(
        "LED Headlights",
        300.00,
        "Upgraded to bright LED headlights for better visibility"
    )
    
    tracker.add_feature_addition(
        "Performance Gauges",
        400.00,
        "Added boost, oil pressure, and AFR gauges",
        "2023-02-20"
    )
    
    # List all modifications
    tracker.list_modifications()
```
