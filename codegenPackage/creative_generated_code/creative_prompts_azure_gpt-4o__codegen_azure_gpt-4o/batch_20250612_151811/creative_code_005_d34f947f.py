"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Create a program to simulate land acquisition and disposition scenarios, incorporating the operational expertise highlighted by Carolina Capital.
Generated: DETERMINISTIC_d34f947f79d7f0f2
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# land_acquisition_simulation.py

import uuid
import json

class LandParcel:
    """
    Represents a land parcel with details such as ID, owner, value, and status.
    """
    def __init__(self, owner, value, status="Available"):
        self.id = str(uuid.uuid4())  # Generate a unique ID for the land parcel
        self.owner = owner           # Current owner of the parcel
        self.value = value           # Monetary value of the parcel
        self.status = status         # Status (Available, Acquired, Disposed)

    def to_dict(self):
        """
        Convert the object to a dictionary for serialization.
        """
        return {
            "id": self.id,
            "owner": self.owner,
            "value": self.value,
            "status": self.status
        }


class LandTransactionManager:
    """
    Manages land acquisition and disposition scenarios.
    """
    def __init__(self):
        self.land_parcels = {}  # Dictionary to store land parcels by ID

    def create_land_parcel(self, owner, value):
        """
        Create a new land parcel with the given owner and value.
        """
        parcel = LandParcel(owner, value)
        self.land_parcels[parcel.id] = parcel
        return parcel

    def acquire_land(self, parcel_id, new_owner):
        """
        Acquire a land parcel by transferring ownership.
        """
        try:
            parcel = self.land_parcels[parcel_id]
            if parcel.status != "Available":
                raise ValueError(f"Parcel {parcel_id} is not available for acquisition.")
            
            parcel.owner = new_owner
            parcel.status = "Acquired"
            return parcel
        except KeyError:
            raise KeyError(f"Parcel with ID {parcel_id} does not exist.")
        except ValueError as e:
            raise ValueError(str(e))

    def dispose_land(self, parcel_id):
        """
        Dispose of a land parcel (mark it as disposed).
        """
        try:
            parcel = self.land_parcels[parcel_id]
            if parcel.status != "Acquired":
                raise ValueError(f"Parcel {parcel_id} is not acquired and cannot be disposed.")
            
            parcel.status = "Disposed"
            return parcel
        except KeyError:
            raise KeyError(f"Parcel with ID {parcel_id} does not exist.")
        except ValueError as e:
            raise ValueError(str(e))

    def get_parcel_details(self, parcel_id):
        """
        Retrieve details of a specific land parcel.
        """
        try:
            parcel = self.land_parcels[parcel_id]
            return parcel.to_dict()
        except KeyError:
            raise KeyError(f"Parcel with ID {parcel_id} does not exist.")

    def list_all_parcels(self):
        """
        List all land parcels with their details.
        """
        return [parcel.to_dict() for parcel in self.land_parcels.values()]


# Example usage
if __name__ == "__main__":
    manager = LandTransactionManager()

    # Create new parcels
    parcel1 = manager.create_land_parcel(owner="Alice", value=100000)
    parcel2 = manager.create_land_parcel(owner="Bob", value=150000)

    print("Created parcels:", manager.list_all_parcels())

    # Acquire a parcel
    acquired_parcel = manager.acquire_land(parcel1.id, new_owner="Carolina Capital")
    print("Acquired parcel details:", acquired_parcel.to_dict())

    # Dispose of a parcel
    disposed_parcel = manager.dispose_land(parcel1.id)
    print("Disposed parcel details:", disposed_parcel.to_dict())

    # List all parcels
    print("All parcels after operations:", manager.list_all_parcels())
```
