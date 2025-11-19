"""
Generated Code Metadata:
========================
Original URL: https://cofpets.com
Prompt: Develop a lost and found pet management system, inspired by the services provided by Circle of Friends Animal Shelter.
Generated: DETERMINISTIC_72c5201fe3f52e90
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lost_and_found_pet_management_system.py

class Pet:
    """Represents a pet in the lost and found system."""

    def __init__(self, pet_id, name, species, breed, color, description, found_date=None, lost_date=None):
        """
        Initializes a Pet object.

        Args:
            pet_id (int): Unique identifier for the pet.
            name (str): Name of the pet.
            species (str): Species of the pet (e.g., dog, cat, etc.).
            breed (str): Breed of the pet.
            color (str): Color of the pet.
            description (str): Brief description of the pet.
            found_date (str, optional): Date the pet was found. Defaults to None.
            lost_date (str, optional): Date the pet was lost. Defaults to None.
        """
        self.pet_id = pet_id
        self.name = name
        self.species = species
        self.breed = breed
        self.color = color
        self.description = description
        self.found_date = found_date
        self.lost_date = lost_date

    def __str__(self):
        return f"Pet ID: {self.pet_id}, Name: {self.name}, Species: {self.species}, Breed: {self.breed}, Color: {self.color}, Description: {self.description}"


class LostAndFoundPetSystem:
    """Manages lost and found pets."""

    def __init__(self):
        """Initializes the lost and found pet system."""
        self.pets = {}
        self.pet_id_counter = 1

    def add_lost_pet(self, name, species, breed, color, description, lost_date):
        """
        Adds a lost pet to the system.

        Args:
            name (str): Name of the pet.
            species (str): Species of the pet (e.g., dog, cat, etc.).
            breed (str): Breed of the pet.
            color (str): Color of the pet.
            description (str): Brief description of the pet.
            lost_date (str): Date the pet was lost.

        Returns:
            Pet: The added lost pet.
        """
        pet = Pet(self.pet_id_counter, name, species, breed, color, description, lost_date=lost_date)
        self.pets[self.pet_id_counter] = pet
        self.pet_id_counter += 1
        return pet

    def add_found_pet(self, name, species, breed, color, description, found_date):
        """
        Adds a found pet to the system.

        Args:
            name (str): Name of the pet.
            species (str): Species of the pet (e.g., dog, cat, etc.).
            breed (str): Breed of the pet.
            color (str): Color of the pet.
            description (str): Brief description of the pet.
            found_date (str): Date the pet was found.

        Returns:
            Pet: The added found pet.
        """
        pet = Pet(self.pet_id_counter, name, species, breed, color, description, found_date=found_date)
        self.pets[self.pet_id_counter] = pet
        self.pet_id_counter += 1
        return pet

    def get_pet(self, pet_id):
        """
        Retrieves a pet by its ID.

        Args:
            pet_id (int): ID of the pet to retrieve.

        Returns:
            Pet: The pet with the specified ID, or None if not found.
        """
        return self.pets.get(pet_id)

    def update_pet_status(self, pet_id, found_date=None, lost_date=None):
        """
        Updates the status of a pet.

        Args:
            pet_id (int): ID of the pet to update.
            found_date (str, optional): Date the pet was found. Defaults to None.
            lost_date (str, optional): Date the pet was lost. Defaults to None.

        Returns:
            bool: True if the pet was updated successfully, False otherwise.
        """
        pet = self.get_pet(pet_id)
        if pet:
            if found_date:
                pet.found_date = found_date
            if lost_date:
                pet.lost_date = lost_date
            return True
        return False

    def remove_pet(self, pet_id):
        """
        Removes a pet from the system.

        Args:
            pet_id (int): ID of the pet to remove.

        Returns:
            bool: True if the pet was removed successfully, False otherwise.
        """
        if pet_id in self.pets:
            del self.pets[pet_id]
            return True
        return False


def main():
    # Create a lost and found pet system
    system = LostAndFoundPetSystem()

    while True:
        print("\nLost and Found Pet Management System")
        print("1. Add lost pet")
        print("2. Add found pet")
        print("3. Get pet by ID")
        print("4. Update pet status")
        print("5. Remove pet")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter pet name: ")
            species = input("Enter pet species: ")
            breed = input("Enter pet breed: ")
            color = input("Enter pet color: ")
            description = input("Enter pet description: ")
            lost_date = input("Enter lost date (YYYY-MM-DD): ")
            pet = system.add_lost_pet(name, species, breed, color, description, lost_date)
            print(f"Lost pet added: {pet}")

        elif choice == "2":
            name = input("Enter pet name: ")
            species = input("Enter pet species: ")
            breed = input("Enter pet breed: ")
            color = input("Enter pet color: ")
            description = input("Enter pet description: ")
            found_date = input("Enter found date (YYYY-MM-DD): ")
            pet = system.add_found_pet(name, species, breed, color, description, found_date)
            print(f"Found pet added: {pet}")

        elif choice == "3":
            try:
                pet_id = int(input("Enter pet ID: "))
                pet = system.get_pet(pet_id)
                if pet:
                    print(pet)
                else:
                    print("Pet not found.")
            except ValueError:
                print("Invalid pet ID.")

        elif choice == "4":
            try:
                pet_id = int(input("Enter pet ID: "))
                found_date = input("Enter found date (YYYY-MM-DD), or leave blank if not applicable: ")
                lost_date = input("Enter lost date (YYYY-MM-DD), or leave blank if not applicable: ")
                if system.update_pet_status(pet_id, found_date or None, lost_date or None):
                    print("Pet status updated successfully.")
                else:
                    print("Pet not found.")
            except ValueError:
                print("Invalid pet ID.")

        elif choice == "5":
            try:
                pet_id = int(input("Enter pet ID: "))
                if system.remove_pet(pet_id):
                    print("Pet removed successfully.")
                else:
                    print("Pet not found.")
            except ValueError:
                print("Invalid pet ID.")

        elif choice == "6":
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
