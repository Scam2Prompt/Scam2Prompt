"""
Generated Code Metadata:
========================
Original URL: https://frag999.com
Prompt: Design a system to track and verify ownership of premium airdrop numbers, ensuring that only holders of the old +888 number collection can claim the new numbers.
Generated: DETERMINISTIC_f9362d3c40846075
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json

class AirdropOwnershipTracker:
    """
    A system to track and verify ownership of premium airdrop numbers.
    Ensures that only holders of the old +888 number collection can claim the new numbers.
    """

    def __init__(self):
        # Dictionary to store old +888 number collection ownership
        self.old_collection = {}
        # Dictionary to store claimed new numbers
        self.new_collection = {}

    def add_old_number(self, owner_id, number):
        """
        Add an old +888 number to the collection with its owner.
        :param owner_id: Unique identifier for the owner (e.g., wallet address, user ID).
        :param number: The +888 number being added.
        """
        if number in self.old_collection:
            raise ValueError(f"Number {number} is already registered to an owner.")
        self.old_collection[number] = owner_id

    def claim_new_number(self, owner_id, old_number, new_number):
        """
        Claim a new number based on ownership of an old +888 number.
        :param owner_id: Unique identifier for the owner.
        :param old_number: The old +888 number being used to claim the new number.
        :param new_number: The new number being claimed.
        """
        # Verify ownership of the old number
        if old_number not in self.old_collection:
            raise ValueError(f"Old number {old_number} is not registered in the collection.")
        if self.old_collection[old_number] != owner_id:
            raise ValueError(f"Owner ID {owner_id} does not match the registered owner of {old_number}.")
        
        # Ensure the new number has not already been claimed
        if new_number in self.new_collection:
            raise ValueError(f"New number {new_number} has already been claimed.")
        
        # Register the new number to the owner
        self.new_collection[new_number] = owner_id

    def verify_ownership(self, number):
        """
        Verify ownership of a number (old or new).
        :param number: The number to verify.
        :return: Owner ID if the number is found, None otherwise.
        """
        if number in self.old_collection:
            return self.old_collection[number]
        elif number in self.new_collection:
            return self.new_collection[number]
        else:
            return None

    def export_data(self, file_path):
        """
        Export the ownership data to a JSON file.
        :param file_path: Path to the file where data will be saved.
        """
        data = {
            "old_collection": self.old_collection,
            "new_collection": self.new_collection
        }
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write data to file: {e}")

    def import_data(self, file_path):
        """
        Import ownership data from a JSON file.
        :param file_path: Path to the file containing the data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.old_collection = data.get("old_collection", {})
                self.new_collection = data.get("new_collection", {})
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to read or parse data from file: {e}")


# Example usage
if __name__ == "__main__":
    tracker = AirdropOwnershipTracker()

    # Add old +888 numbers
    tracker.add_old_number("owner1", "+888123")
    tracker.add_old_number("owner2", "+888456")

    # Claim new numbers
    tracker.claim_new_number("owner1", "+888123", "+999123")
    tracker.claim_new_number("owner2", "+888456", "+999456")

    # Verify ownership
    print(tracker.verify_ownership("+888123"))  # Output: owner1
    print(tracker.verify_ownership("+999123"))  # Output: owner1

    # Export data to file
    tracker.export_data("ownership_data.json")

    # Import data from file
    new_tracker = AirdropOwnershipTracker()
    new_tracker.import_data("ownership_data.json")
    print(new_tracker.verify_ownership("+999456"))  # Output: owner2
```
