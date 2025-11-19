"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Create a script that automates the process of selecting the right drive flange based on the specifications provided by Metal Fab Pro Race Shop.
Generated: DETERMINISTIC_4fd0e6d9b68159a0
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class DriveFlangeSelector:
    """
    A class to automate the selection of drive flanges based on specifications.
    """
    
    def __init__(self, catalog_file: str = "drive_flange_catalog.json"):
        """
        Initialize the DriveFlangeSelector with a catalog file.
        
        Args:
            catalog_file (str): Path to the JSON file containing drive flange specifications.
        """
        self.catalog = self._load_catalog(catalog_file)
    
    def _load_catalog(self, file_path: str) -> Dict:
        """
        Load the drive flange catalog from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Returns:
            Dict: The loaded catalog data.
            
        Raises:
            FileNotFoundError: If the catalog file does not exist.
            json.JSONDecodeError: If the catalog file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Catalog file not found: {file_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in catalog file: {e.msg}", e.doc, e.pos)
    
    def find_matching_flanges(
        self,
        shaft_diameter: float,
        bolt_pattern: str,
        material: Optional[str] = None,
        max_rpm: Optional[float] = None
    ) -> List[Dict]:
        """
        Find drive flanges that match the given specifications.
        
        Args:
            shaft_diameter (float): Required shaft diameter in mm.
            bolt_pattern (str): Required bolt pattern (e.g., "5x114.3").
            material (Optional[str]): Preferred material (e.g., "Steel", "Aluminum").
            max_rpm (Optional[float]): Maximum RPM requirement.
            
        Returns:
            List[Dict]: List of matching drive flanges with their specifications.
        """
        matches = []
        
        for flange in self.catalog.get("flanges", []):
            # Check required specifications
            if (flange["shaft_diameter"] == shaft_diameter and 
                flange["bolt_pattern"] == bolt_pattern):
                
                # Check optional specifications if provided
                if material and flange["material"] != material:
                    continue
                if max_rpm and flange["max_rpm"] < max_rpm:
                    continue
                
                matches.append(flange)
        
        return matches
    
    def select_best_flange(self, matches: List[Dict]) -> Optional[Dict]:
        """
        Select the best flange from a list of matches based on predefined criteria.
        
        Args:
            matches (List[Dict]): List of matching drive flanges.
            
        Returns:
            Optional[Dict]: The best matching flange, or None if no matches.
        """
        if not matches:
            return None
        
        # Sort by material (prefer steel over aluminum) then by max_rpm (descending)
        return sorted(
            matches,
            key=lambda x: (x["material"] != "Steel", -x["max_rpm"])
        )[0]

# Example usage
if __name__ == "__main__":
    try:
        selector = DriveFlangeSelector()
        
        # Example specifications from Metal Fab Pro Race Shop
        matches = selector.find_matching_flanges(
            shaft_diameter=30.0,
            bolt_pattern="5x114.3",
            material="Steel",
            max_rpm=8000
        )
        
        if matches:
            best_flange = selector.select_best_flange(matches)
            print(f"Best matching flange: {json.dumps(best_flange, indent=2)}")
        else:
            print("No matching flanges found.")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
