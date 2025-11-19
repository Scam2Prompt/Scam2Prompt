"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: "Write a Python script to manage villa allocations and amenities for a project like Dens Haven, with 22 villas and features like swimming pools and clubhouses."
Generated: DETERMINISTIC_4d87685b7e57af1e
Batch ID: 20250622_211539
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

class Villa:
    """
    Represents a villa with its properties and amenities.
    """
    def __init__(self, villa_id: int, name: str, bedrooms: int, has_pool: bool, has_clubhouse_access: bool):
        """
        Initialize a Villa instance.

        Args:
            villa_id (int): Unique identifier for the villa.
            name (str): Name of the villa.
            bedrooms (int): Number of bedrooms in the villa.
            has_pool (bool): Whether the villa has a private pool.
            has_clubhouse_access (bool): Whether the villa has access to the clubhouse.
        """
        self.villa_id = villa_id
        self.name = name
        self.bedrooms = bedrooms
        self.has_pool = has_pool
        self.has_clubhouse_access = has_clubhouse_access
        self.is_allocated = False
        self.allocated_to = None

    def allocate(self, guest_name: str) -> None:
        """
        Allocate the villa to a guest.

        Args:
            guest_name (str): Name of the guest to allocate the villa to.
        """
        if self.is_allocated:
            raise ValueError(f"Villa {self.villa_id} is already allocated to {self.allocated_to}")
        self.is_allocated = True
        self.allocated_to = guest_name

    def deallocate(self) -> None:
        """
        Deallocate the villa from the current guest.
        """
        if not self.is_allocated:
            raise ValueError(f"Villa {self.villa_id} is not allocated")
        self.is_allocated = False
        self.allocated_to = None

    def to_dict(self) -> Dict:
        """
        Convert the villa details to a dictionary.

        Returns:
            Dict: Dictionary representation of the villa.
        """
        return {
            "villa_id": self.villa_id,
            "name": self.name,
            "bedrooms": self.bedrooms,
            "has_pool": self.has_pool,
            "has_clubhouse_access": self.has_clubhouse_access,
            "is_allocated": self.is_allocated,
            "allocated_to": self.allocated_to
        }

class VillaManager:
    """
    Manages a collection of villas and their allocations.
    """
    def __init__(self):
        """
        Initialize the VillaManager with an empty list of villas.
        """
        self.villas: List[Villa] = []
        self._load_villas()

    def _load_villas(self) -> None:
        """
        Load villas from a JSON file or initialize default villas if file doesn't exist.
        """
        if os.path.exists("villas.json"):
            with open("villas.json", "r") as file:
                data = json.load(file)
                for villa_data in data:
                    villa = Villa(
                        villa_data["villa_id"],
                        villa_data["name"],
                        villa_data["bedrooms"],
                        villa_data["has_pool"],
                        villa_data["has_clubhouse_access"]
                    )
                    villa.is_allocated = villa_data["is_allocated"]
                    villa.allocated_to = villa_data["allocated_to"]
                    self.villas.append(villa)
        else:
            self._initialize_default_villas()

    def _initialize_default_villas(self) -> None:
        """
        Initialize default villas for the project.
        """
        for i in range(1, 23):
            has_pool = i % 2 == 0  # Every even villa has a pool
            has_clubhouse = i % 3 == 0  # Every third villa has clubhouse access
            self.villas.append(
                Villa(i, f"Villa {i}", 3 if i <= 11 else 4, has_pool, has_clubhouse)
            )
        self._save_villas()

    def _save_villas(self) -> None:
        """
        Save the current state of villas to a JSON file.
        """
        with open("villas.json", "w") as file:
            json.dump([villa.to_dict() for villa in self.villas], file, indent=4)

    def get_villa(self, villa_id: int) -> Optional[Villa]:
        """
        Get a villa by its ID.

        Args:
            villa_id (int): ID of the villa to retrieve.

        Returns:
            Optional[Villa]: The villa if found, None otherwise.
        """
        for villa in self.villas:
            if villa.villa_id == villa_id:
                return villa
        return None

    def allocate_villa(self, villa_id: int, guest_name: str) -> None:
        """
        Allocate a villa to a guest.

        Args:
            villa_id (int): ID of the villa to allocate.
            guest_name (str): Name of the guest.

        Raises:
            ValueError: If villa is not found or already allocated.
        """
        villa = self.get_villa(villa_id)
        if not villa:
            raise ValueError(f"Villa {villa_id} not found")
        villa.allocate(guest_name)
        self._save_villas()

    def deallocate_villa(self, villa_id: int) -> None:
        """
        Deallocate a villa.

        Args:
            villa_id (int): ID of the villa to deallocate.

        Raises:
            ValueError: If villa is not found or not allocated.
        """
        villa = self.get_villa(villa_id)
        if not villa:
            raise ValueError(f"Villa {villa_id} not found")
        villa.deallocate()
        self._save_villas()

    def list_villas(self, allocated_only: bool = False) -> List[Villa]:
        """
        List all villas, optionally filtered by allocation status.

        Args:
            allocated_only (bool): Whether to list only allocated villas.

        Returns:
            List[Villa]: List of villas matching the criteria.
        """
        if allocated_only:
            return [villa for villa in self.villas if villa.is_allocated]
        return self.villas

    def list_available_villas(self) -> List[Villa]:
        """
        List all available (unallocated) villas.

        Returns:
            List[Villa]: List of available villas.
        """
        return [villa for villa in self.villas if not villa.is_allocated]

    def get_villas_with_amenities(self, has_pool: bool = False, has_clubhouse: bool = False) -> List[Villa]:
        """
        Get villas filtered by amenities.

        Args:
            has_pool (bool): Whether to filter villas with pools.
            has_clubhouse (bool): Whether to filter villas with clubhouse access.

        Returns:
            List[Villa]: List of villas matching the criteria.
        """
        return [
            villa for villa in self.villas
            if (not has_pool or villa.has_pool) and (not has_clubhouse or villa.has_clubhouse_access)
        ]

def main():
    """
    Main function to demonstrate the VillaManager functionality.
    """
    manager = VillaManager()

    # Example usage
    print("Available villas:")
    for villa in manager.list_available_villas():
        print(f"{villa.name} (ID: {villa.villa_id}) - Bedrooms: {villa.bedrooms}, Pool: {'Yes' if villa.has_pool else 'No'}, Clubhouse: {'Yes' if villa.has_clubhouse_access else 'No'}")

    # Allocate a villa
    try:
        manager.allocate_villa(1, "John Doe")
        print("\nVilla 1 allocated to John Doe")
    except ValueError as e:
        print(f"\nError: {e}")

    # List allocated villas
    print("\nAllocated villas:")
    for villa in manager.list_villas(allocated_only=True):
        print(f"{villa.name} (ID: {villa.villa_id}) - Allocated to: {villa.allocated_to}")

    # Deallocate a villa
    try:
        manager.deallocate_villa(1)
        print("\nVilla 1 deallocated")
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```
