"""
Generated Code Metadata:
========================
Original URL: https://jitodaily.com
Prompt: Generate a Python script to manage multiple betting IDs, ensuring functionality for creating, resetting, and listing IDs as described on JitoDaily.
Generated: DETERMINISTIC_f538f67c7e3b168b
Batch ID: 20250612_154147
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
from typing import Dict, List, Optional

class BettingIDManager:
    """
    A class to manage multiple betting IDs with functionalities to create, reset, and list IDs.
    """
    
    def __init__(self, storage_file: str = "betting_ids.json"):
        """
        Initialize the BettingIDManager with a storage file.
        
        Args:
            storage_file (str): Path to the JSON file storing betting IDs. Defaults to "betting_ids.json".
        """
        self.storage_file = storage_file
        self.betting_ids: Dict[str, Dict] = {}
        self._load_ids()

    def _load_ids(self) -> None:
        """
        Load betting IDs from the storage file. If the file doesn't exist, initialize an empty dict.
        """
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as file:
                    self.betting_ids = json.load(file)
            else:
                self.betting_ids = {}
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load betting IDs: {e}")

    def _save_ids(self) -> None:
        """
        Save the current betting IDs to the storage file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump(self.betting_ids, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save betting IDs: {e}")

    def create_id(self, id_name: str, initial_data: Optional[Dict] = None) -> None:
        """
        Create a new betting ID with optional initial data.
        
        Args:
            id_name (str): Name of the betting ID to create.
            initial_data (Dict, optional): Initial data for the betting ID. Defaults to None.
        
        Raises:
            ValueError: If the betting ID already exists.
        """
        if id_name in self.betting_ids:
            raise ValueError(f"Betting ID '{id_name}' already exists.")
        
        self.betting_ids[id_name] = initial_data if initial_data is not None else {}
        self._save_ids()

    def reset_id(self, id_name: str) -> None:
        """
        Reset a betting ID by clearing its data.
        
        Args:
            id_name (str): Name of the betting ID to reset.
        
        Raises:
            ValueError: If the betting ID does not exist.
        """
        if id_name not in self.betting_ids:
            raise ValueError(f"Betting ID '{id_name}' does not exist.")
        
        self.betting_ids[id_name] = {}
        self._save_ids()

    def delete_id(self, id_name: str) -> None:
        """
        Delete a betting ID.
        
        Args:
            id_name (str): Name of the betting ID to delete.
        
        Raises:
            ValueError: If the betting ID does not exist.
        """
        if id_name not in self.betting_ids:
            raise ValueError(f"Betting ID '{id_name}' does not exist.")
        
        del self.betting_ids[id_name]
        self._save_ids()

    def list_ids(self) -> List[str]:
        """
        List all existing betting IDs.
        
        Returns:
            List[str]: List of betting ID names.
        """
        return list(self.betting_ids.keys())

    def get_id_data(self, id_name: str) -> Dict:
        """
        Get the data associated with a betting ID.
        
        Args:
            id_name (str): Name of the betting ID.
        
        Returns:
            Dict: Data associated with the betting ID.
        
        Raises:
            ValueError: If the betting ID does not exist.
        """
        if id_name not in self.betting_ids:
            raise ValueError(f"Betting ID '{id_name}' does not exist.")
        
        return self.betting_ids[id_name]

    def update_id_data(self, id_name: str, data: Dict) -> None:
        """
        Update the data associated with a betting ID.
        
        Args:
            id_name (str): Name of the betting ID.
            data (Dict): New data to associate with the betting ID.
        
        Raises:
            ValueError: If the betting ID does not exist.
        """
        if id_name not in self.betting_ids:
            raise ValueError(f"Betting ID '{id_name}' does not exist.")
        
        self.betting_ids[id_name].update(data)
        self._save_ids()


# Example usage
if __name__ == "__main__":
    manager = BettingIDManager()
    
    # Create a new betting ID
    manager.create_id("id1", {"balance": 100, "bets": []})
    
    # List all betting IDs
    print("Betting IDs:", manager.list_ids())
    
    # Get data for a betting ID
    print("ID1 data:", manager.get_id_data("id1"))
    
    # Update data for a betting ID
    manager.update_id_data("id1", {"balance": 150})
    print("Updated ID1 data:", manager.get_id_data("id1"))
    
    # Reset a betting ID
    manager.reset_id("id1")
    print("Reset ID1 data:", manager.get_id_data("id1"))
    
    # Delete a betting ID
    manager.delete_id("id1")
    print("Betting IDs after deletion:", manager.list_ids())
```
