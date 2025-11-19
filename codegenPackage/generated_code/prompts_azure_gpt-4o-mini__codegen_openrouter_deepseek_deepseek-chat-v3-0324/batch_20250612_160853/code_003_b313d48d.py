"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Explain the significance of the Electronic Identity of Buildings (ΗΤΚ) and how it tracks changes over time.
Generated: DETERMINISTIC_b313d48dfee5bfff
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electronic Identity of Buildings (ΗΤΚ) Tracker

This module provides functionality to track changes to a building's electronic identity (ΗΤΚ) over time.
It includes methods to register new buildings, update their information, and retrieve historical data.
"""

from datetime import datetime
from typing import Dict, List, Optional
import uuid

class BuildingHTK:
    """
    Represents the Electronic Identity of a Building (ΗΤΚ) with change tracking capabilities.
    
    Attributes:
        building_id (str): Unique identifier for the building
        current_data (Dict): Current building information
        history (List[Dict]): List of historical changes
    """
    
    def __init__(self, initial_data: Dict):
        """
        Initialize a new building HTK record.
        
        Args:
            initial_data: Dictionary containing initial building data
        """
        self.building_id = str(uuid.uuid4())
        self.current_data = initial_data.copy()
        self.history = [{
            'timestamp': datetime.utcnow(),
            'data': initial_data.copy(),
            'change_description': 'Initial registration'
        }]
    
    def update(self, new_data: Dict, change_description: str) -> bool:
        """
        Update the building's information and track the change.
        
        Args:
            new_data: Dictionary containing updated fields
            change_description: Human-readable description of the change
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        if not isinstance(new_data, dict):
            return False
            
        try:
            # Update current data
            self.current_data.update(new_data)
            
            # Record change in history
            self.history.append({
                'timestamp': datetime.utcnow(),
                'data': new_data.copy(),
                'change_description': change_description
            })
            return True
        except Exception as e:
            print(f"Error updating building HTK: {e}")
            return False
    
    def get_history(self) -> List[Dict]:
        """
        Retrieve the complete change history of the building.
        
        Returns:
            List of dictionaries containing historical changes
        """
        return self.history.copy()
    
    def get_snapshot(self, timestamp: Optional[datetime] = None) -> Optional[Dict]:
        """
        Retrieve building data as it was at a specific time.
        
        Args:
            timestamp: Optional datetime to get historical snapshot.
                      If None, returns current data.
                      
        Returns:
            Dictionary of building data at requested time, or None if not found
        """
        if timestamp is None:
            return self.current_data.copy()
            
        for record in reversed(self.history):
            if record['timestamp'] <= timestamp:
                return record['data'].copy()
                
        return None


class HTKRegistry:
    """
    Registry for managing multiple BuildingHTK instances.
    """
    
    def __init__(self):
        self.buildings: Dict[str, BuildingHTK] = {}
    
    def register_building(self, initial_data: Dict) -> str:
        """
        Register a new building in the HTK system.
        
        Args:
            initial_data: Initial building data
            
        Returns:
            str: The generated building ID
        """
        new_building = BuildingHTK(initial_data)
        self.buildings[new_building.building_id] = new_building
        return new_building.building_id
    
    def get_building(self, building_id: str) -> Optional[BuildingHTK]:
        """
        Retrieve a building's HTK record by ID.
        
        Args:
            building_id: The building ID to retrieve
            
        Returns:
            BuildingHTK instance if found, None otherwise
        """
        return self.buildings.get(building_id)
    
    def update_building(self, building_id: str, new_data: Dict, change_description: str) -> bool:
        """
        Update a building's information in the registry.
        
        Args:
            building_id: ID of building to update
            new_data: New data to merge
            change_description: Description of the change
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        building = self.get_building(building_id)
        if building:
            return building.update(new_data, change_description)
        return False
```
