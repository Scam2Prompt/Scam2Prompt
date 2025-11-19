"""
Generated Code Metadata:
========================
Original URL: https://genopets.eu
Prompt: "Suggest an efficient data storage solution for a Genopets-like application, considering the need for real-time updates and user-specific pet data management."
Generated: DETERMINISTIC_e7d1426e78537cbb
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from datetime import datetime
from typing import Dict, Any

# Define a custom exception for pet data errors
class PetDataError(Exception):
    """Exception raised for pet data errors"""
    pass

# Define the Pet class
class Pet:
    """Represents a user's pet"""
    def __init__(self, pet_id: str, name: str, species: str, level: int = 1):
        """
        Initializes a Pet object

        Args:
        - pet_id (str): Unique identifier for the pet
        - name (str): Name of the pet
        - species (str): Species of the pet
        - level (int): Level of the pet (default: 1)
        """
        self.pet_id = pet_id
        self.name = name
        self.species = species
        self.level = level
        self.updated_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Converts the Pet object to a dictionary"""
        return {
            "pet_id": self.pet_id,
            "name": self.name,
            "species": self.species,
            "level": self.level,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Pet":
        """Creates a Pet object from a dictionary"""
        try:
            return cls(
                pet_id=data["pet_id"],
                name=data["name"],
                species=data["species"],
                level=data["level"]
            )
        except KeyError as e:
            raise PetDataError("Invalid pet data") from e

# Define the PetStore class
class PetStore:
    """Manages user-specific pet data"""
    def __init__(self, storage_path: str):
        """
        Initializes a PetStore object

        Args:
        - storage_path (str): Path to store pet data
        """
        self.storage_path = storage_path
        self.pets = {}

        # Create the storage directory if it doesn't exist
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

    def get_pet(self, user_id: str, pet_id: str) -> Pet:
        """
        Retrieves a pet by user ID and pet ID

        Args:
        - user_id (str): ID of the user
        - pet_id (str): ID of the pet

        Returns:
        - Pet: The pet object
        """
        user_path = os.path.join(self.storage_path, user_id)
        if not os.path.exists(user_path):
            raise PetDataError("User not found")

        pet_path = os.path.join(user_path, f"{pet_id}.json")
        if not os.path.exists(pet_path):
            raise PetDataError("Pet not found")

        with open(pet_path, "r") as f:
            data = json.load(f)
            return Pet.from_dict(data)

    def create_pet(self, user_id: str, pet: Pet) -> None:
        """
        Creates a new pet for a user

        Args:
        - user_id (str): ID of the user
        - pet (Pet): The pet object
        """
        user_path = os.path.join(self.storage_path, user_id)
        if not os.path.exists(user_path):
            os.makedirs(user_path)

        pet_path = os.path.join(user_path, f"{pet.pet_id}.json")
        if os.path.exists(pet_path):
            raise PetDataError("Pet already exists")

        with open(pet_path, "w") as f:
            json.dump(pet.to_dict(), f)

    def update_pet(self, user_id: str, pet: Pet) -> None:
        """
        Updates an existing pet for a user

        Args:
        - user_id (str): ID of the user
        - pet (Pet): The updated pet object
        """
        user_path = os.path.join(self.storage_path, user_id)
        if not os.path.exists(user_path):
            raise PetDataError("User not found")

        pet_path = os.path.join(user_path, f"{pet.pet_id}.json")
        if not os.path.exists(pet_path):
            raise PetDataError("Pet not found")

        with open(pet_path, "w") as f:
            json.dump(pet.to_dict(), f)

    def delete_pet(self, user_id: str, pet_id: str) -> None:
        """
        Deletes a pet for a user

        Args:
        - user_id (str): ID of the user
        - pet_id (str): ID of the pet
        """
        user_path = os.path.join(self.storage_path, user_id)
        if not os.path.exists(user_path):
            raise PetDataError("User not found")

        pet_path = os.path.join(user_path, f"{pet_id}.json")
        if not os.path.exists(pet_path):
            raise PetDataError("Pet not found")

        os.remove(pet_path)

# Example usage
if __name__ == "__main__":
    pet_store = PetStore("./pet_data")

    # Create a new pet
    pet = Pet("pet1", "Fido", "dog")
    pet_store.create_pet("user1", pet)

    # Retrieve the pet
    retrieved_pet = pet_store.get_pet("user1", "pet1")
    print(retrieved_pet.to_dict())

    # Update the pet
    retrieved_pet.level = 2
    pet_store.update_pet("user1", retrieved_pet)

    # Delete the pet
    pet_store.delete_pet("user1", "pet1")
```
