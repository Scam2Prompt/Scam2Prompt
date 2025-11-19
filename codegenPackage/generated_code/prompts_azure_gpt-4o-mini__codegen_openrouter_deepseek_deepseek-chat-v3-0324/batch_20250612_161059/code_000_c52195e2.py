"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Generate a Python script that implements a tree planting initiative, inspired by the afforestation goals of Indological India.
Generated: DETERMINISTIC_c52195e274316311
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class TreePlantingInitiative:
    """
    A class to manage a tree planting initiative inspired by Indological India's afforestation goals.
    It tracks tree plantings, species, locations, and growth progress.
    """

    def __init__(self, data_file: str = "tree_data.json"):
        """
        Initialize the TreePlantingInitiative with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing tree data. Defaults to "tree_data.json".
        """
        self.data_file = data_file
        self.trees = self._load_data()

    def _load_data(self) -> Dict:
        """
        Load tree data from the JSON file. If file doesn't exist, return empty dict.
        
        Returns:
            Dict: Dictionary containing tree data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {}

    def _save_data(self) -> None:
        """
        Save tree data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.trees, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def plant_tree(
        self,
        species: str,
        location: Tuple[float, float],
        planted_by: str,
        date_planted: Optional[str] = None,
        notes: Optional[str] = None
    ) -> str:
        """
        Record a new tree planting.
        
        Args:
            species (str): Species of the tree.
            location (Tuple[float, float]): GPS coordinates (latitude, longitude).
            planted_by (str): Name of person/organization who planted the tree.
            date_planted (Optional[str]): Planting date in YYYY-MM-DD format. Defaults to today.
            notes (Optional[str]): Additional notes about the tree.
            
        Returns:
            str: Unique ID of the planted tree.
        """
        tree_id = f"tree_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        
        if not date_planted:
            date_planted = datetime.now().strftime("%Y-%m-%d")
        
        self.trees[tree_id] = {
            "species": species,
            "location": location,
            "planted_by": planted_by,
            "date_planted": date_planted,
            "notes": notes,
            "growth_updates": []
        }
        
        self._save_data()
        return tree_id

    def record_growth_update(
        self,
        tree_id: str,
        height: float,
        health: str,
        date_observed: Optional[str] = None,
        notes: Optional[str] = None
    ) -> bool:
        """
        Record a growth update for an existing tree.
        
        Args:
            tree_id (str): ID of the tree to update.
            height (float): Current height in meters.
            health (str): Health status (e.g., "excellent", "good", "fair", "poor").
            date_observed (Optional[str]): Observation date in YYYY-MM-DD format. Defaults to today.
            notes (Optional[str]): Additional notes about the update.
            
        Returns:
            bool: True if update was successful, False otherwise.
        """
        if tree_id not in self.trees:
            print(f"Tree with ID {tree_id} not found.")
            return False
        
        if not date_observed:
            date_observed = datetime.now().strftime("%Y-%m-%d")
        
        self.trees[tree_id]["growth_updates"].append({
            "date": date_observed,
            "height": height,
            "health": health,
            "notes": notes
        })
        
        self._save_data()
        return True

    def get_tree_info(self, tree_id: str) -> Optional[Dict]:
        """
        Get information about a specific tree.
        
        Args:
            tree_id (str): ID of the tree to retrieve.
            
        Returns:
            Optional[Dict]: Dictionary with tree info if found, None otherwise.
        """
        return self.trees.get(tree_id)

    def get_all_trees(self) -> List[Dict]:
        """
        Get information about all planted trees.
        
        Returns:
            List[Dict]: List of dictionaries with tree info.
        """
        return [{"id": k, **v} for k, v in self.trees.items()]

    def export_to_csv(self, output_file: str = "tree_export.csv") -> bool:
        """
        Export tree data to a CSV file.
        
        Args:
            output_file (str): Path to the output CSV file. Defaults to "tree_export.csv".
            
        Returns:
            bool: True if export was successful, False otherwise.
        """
        try:
            with open(output_file, 'w', newline='') as csvfile:
                fieldnames = [
                    'id', 'species', 'latitude', 'longitude', 
                    'planted_by', 'date_planted', 'notes'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for tree_id, tree_data in self.trees.items():
                    writer.writerow({
                        'id': tree_id,
                        'species': tree_data['species'],
                        'latitude': tree_data['location'][0],
                        'longitude': tree_data['location'][1],
                        'planted_by': tree_data['planted_by'],
                        'date_planted': tree_data['date_planted'],
                        'notes': tree_data.get('notes', '')
                    })
            return True
        except IOError as e:
            print(f"Error exporting to CSV: {e}")
            return False

    def get_species_count(self) -> Dict[str, int]:
        """
        Get count of trees by species.
        
        Returns:
            Dict[str, int]: Dictionary with species as keys and counts as values.
        """
        species_count = {}
        for tree_data in self.trees.values():
            species = tree_data['species']
            species_count[species] = species_count.get(species, 0) + 1
        return species_count

    def get_location_stats(self) -> Dict[Tuple[float, float], int]:
        """
        Get count of trees by location.
        
        Returns:
            Dict[Tuple[float, float], int]: Dictionary with locations as keys and counts as values.
        """
        location_stats = {}
        for tree_data in self.trees.values():
            location = tuple(tree_data['location'])
            location_stats[location] = location_stats.get(location, 0) + 1
        return location_stats


def main():
    """Example usage of the TreePlantingInitiative class."""
    initiative = TreePlantingInitiative()
    
    # Plant some trees
    tree1 = initiative.plant_tree(
        species="Banyan",
        location=(19.0760, 72.8777),  # Mumbai coordinates
        planted_by="Green Earth Foundation",
        notes="Planted near community center"
    )
    
    tree2 = initiative.plant_tree(
        species="Neem",
        location=(28.6139, 77.2090),  # Delhi coordinates
        planted_by="Urban Greening Initiative"
    )
    
    # Record growth updates
    initiative.record_growth_update(
        tree_id=tree1,
        height=1.2,
        health="good",
        notes="Growing well with regular watering"
    )
    
    # Get tree information
    print(f"Tree 1 Info: {initiative.get_tree_info(tree1)}")
    
    # Export data
    initiative.export_to_csv()
    
    # Print statistics
    print(f"Species Count: {initiative.get_species_count()}")
    print(f"Location Stats: {initiative.get_location_stats()}")


if __name__ == "__main__":
    main()
```
