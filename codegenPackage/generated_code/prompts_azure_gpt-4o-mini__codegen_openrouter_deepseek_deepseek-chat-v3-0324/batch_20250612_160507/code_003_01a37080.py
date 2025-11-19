"""
Generated Code Metadata:
========================
Original URL: https://appbalancer.pages.dev
Prompt: Develop a script that lists delivery areas for a takeaway service, inspired by the delivery areas mentioned for Rob N Roll in Kirkcudbright and Auchenlarie.
Generated: DETERMINISTIC_01a370802b211ab3
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class DeliveryAreaService:
    """
    A service to manage and list delivery areas for a takeaway service.
    """

    def __init__(self, areas_file: Optional[str] = None):
        """
        Initialize the DeliveryAreaService.

        Args:
            areas_file (str, optional): Path to a JSON file containing delivery areas.
                                       Defaults to None (uses default areas).
        """
        self.areas_file = areas_file
        self.delivery_areas = self._load_areas()

    def _load_areas(self) -> List[Dict[str, str]]:
        """
        Load delivery areas from the specified file or use default areas.

        Returns:
            List[Dict[str, str]]: List of delivery areas with their details.
        
        Raises:
            FileNotFoundError: If the specified areas file does not exist.
            json.JSONDecodeError: If the areas file is not valid JSON.
        """
        default_areas = [
            {"name": "Kirkcudbright", "postcode": "DG6", "delivery_time": "30-45 mins"},
            {"name": "Auchenlarie", "postcode": "DG7", "delivery_time": "45-60 mins"}
        ]

        if not self.areas_file:
            return default_areas

        try:
            with open(self.areas_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Delivery areas file not found: {self.areas_file}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in areas file: {e.msg}", e.doc, e.pos)

    def list_areas(self) -> List[Dict[str, str]]:
        """
        Get the list of delivery areas.

        Returns:
            List[Dict[str, str]]: List of delivery areas with their details.
        """
        return self.delivery_areas

    def add_area(self, name: str, postcode: str, delivery_time: str) -> None:
        """
        Add a new delivery area.

        Args:
            name (str): Name of the area.
            postcode (str): Postcode of the area.
            delivery_time (str): Estimated delivery time.
        """
        self.delivery_areas.append({
            "name": name,
            "postcode": postcode,
            "delivery_time": delivery_time
        })

    def save_areas(self, file_path: str) -> None:
        """
        Save delivery areas to a JSON file.

        Args:
            file_path (str): Path to save the delivery areas.

        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.delivery_areas, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save areas to file: {e}")


def main():
    """
    Example usage of the DeliveryAreaService.
    """
    try:
        # Initialize with default areas
        service = DeliveryAreaService()
        
        # List all delivery areas
        areas = service.list_areas()
        print("Delivery Areas:")
        for area in areas:
            print(f"- {area['name']} ({area['postcode']}): {area['delivery_time']}")

        # Add a new area
        service.add_area("New Area", "DG8", "50-70 mins")
        
        # Save to a file
        service.save_areas("delivery_areas.json")
        print("\nAreas saved to 'delivery_areas.json'")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
