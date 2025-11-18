"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Develop a Python script for managing habitats in a game like Genopets, including features for renting, terraforming, and refining crystals.
Generated: DETERMINISTIC_fa70beac3e87d012
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class HabitatManager:
    """
    HabitatManager class for managing operations like renting, terraforming, and refining crystals.
    """

    def __init__(self):
        # Initialize habitats dictionary to store habitat data
        self.habitats = {}

    def create_habitat(self, habitat_id, owner, habitat_type):
        """
        Create a new habitat and store it in the habitats dictionary.

        :param habitat_id: Unique identifier for the habitat
        :param owner: Owner of the habitat
        :param habitat_type: Type of the habitat (e.g., "Fire", "Water", "Earth")
        """
        if habitat_id in self.habitats:
            raise ValueError(f"Habitat {habitat_id} already exists.")
        self.habitats[habitat_id] = {
            "owner": owner,
            "type": habitat_type,
            "is_rented": False,
            "rented_to": None,
            "terraforming": False,
            "refining_crystals": False,
            "last_refined": None,
        }

    def rent_habitat(self, habitat_id, renter):
        """
        Rent a habitat to a player.

        :param habitat_id: Habitat ID to be rented
        :param renter: Player renting the habitat
        """
        if habitat_id not in self.habitats:
            raise ValueError(f"Habitat {habitat_id} does not exist.")
        habitat = self.habitats[habitat_id]
        if habitat["is_rented"]:
            raise ValueError(f"Habitat {habitat_id} is already rented.")
        habitat["is_rented"] = True
        habitat["rented_to"] = renter

    def end_rental(self, habitat_id):
        """
        End the rental of a habitat.

        :param habitat_id: Habitat ID to end the rental
        """
        if habitat_id not in self.habitats:
            raise ValueError(f"Habitat {habitat_id} does not exist.")
        habitat = self.habitats[habitat_id]
        if not habitat["is_rented"]:
            raise ValueError(f"Habitat {habitat_id} is not currently rented.")
        habitat["is_rented"] = False
        habitat["rented_to"] = None

    def start_terraforming(self, habitat_id):
        """
        Begin terraforming a habitat.

        :param habitat_id: Habitat ID to terraform
        """
        if habitat_id not in self.habitats:
            raise ValueError(f"Habitat {habitat_id} does not exist.")
        habitat = self.habitats[habitat_id]
        if habitat["terraforming"]:
            raise ValueError(f"Habitat {habitat_id} is already being terraformed.")
        habitat["terraforming"] = True

    def complete_terraforming(self, habitat_id):
        """
        Complete the terraforming process for a habitat.

        :param habitat_id: Habitat ID that has been terraformed
        """
        if habitat_id not in self.habitats:
            raise ValueError(f"Habitat {habitat_id} does not exist.")
        habitat = self.habitats[habitat_id]
        if not habitat["terraforming"]:
            raise ValueError(f"Habitat {habitat_id} is not currently being terraformed.")
        habitat["terraforming"] = False

    def start_refining_crystals(self, habitat_id):
        """
        Begin refining crystals in a habitat.

        :param habitat_id: Habitat ID to refine crystals
        """
        if habitat_id not in self.habitats:
            raise ValueError(f"Habitat {habitat_id} does not exist.")
        habitat = self.habitats[habitat_id]
        if habitat["refining_crystals"]:
            raise ValueError(f"Habitat {habitat_id} is already refining crystals.")
        habitat["refining_crystals"] = True

    def complete_refining_crystals(self, habitat_id):
        """
        Complete the crystal refining process for a habitat.

        :param habitat_id: Habitat ID that has completed refining crystals
        """
        if habitat_id not in self.habitats:
            raise ValueError(f"Habitat {habitat_id} does not exist.")
        habitat = self.habitats[habitat_id]
        if not habitat["refining_crystals"]:
            raise ValueError(f"Habitat {habitat_id} is not currently refining crystals.")
        habitat["refining_crystals"] = False
        habitat["last_refined"] = datetime.datetime.now()

    def get_habitat_status(self, habitat_id):
        """
        Retrieve the status of a habitat.

        :param habitat_id: Habitat ID to retrieve status for
        :return: Dictionary containing the status of the habitat
        """
        if habitat_id not in self.habitats:
            raise ValueError(f"Habitat {habitat_id} does not exist.")
        return self.habitats[habitat_id]


# Example usage
if __name__ == "__main__":
    manager = HabitatManager()

    try:
        # Create a new habitat
        manager.create_habitat("habitat_1", "Player1", "Fire")
        print("Habitat created successfully.")

        # Rent the habitat
        manager.rent_habitat("habitat_1", "Player2")
        print("Habitat rented successfully.")

        # Start terraforming
        manager.start_terraforming("habitat_1")
        print("Terraforming started.")

        # Complete terraforming
        manager.complete_terraforming("habitat_1")
        print("Terraforming completed.")

        # Start refining crystals
        manager.start_refining_crystals("habitat_1")
        print("Crystal refining started.")

        # Complete refining crystals
        manager.complete_refining_crystals("habitat_1")
        print("Crystal refining completed.")

        # Get habitat status
        status = manager.get_habitat_status("habitat_1")
        print("Habitat Status:", status)

        # End the rental
        manager.end_rental("habitat_1")
        print("Rental ended successfully.")
    except ValueError as e:
        print(f"Error: {e}")
```
