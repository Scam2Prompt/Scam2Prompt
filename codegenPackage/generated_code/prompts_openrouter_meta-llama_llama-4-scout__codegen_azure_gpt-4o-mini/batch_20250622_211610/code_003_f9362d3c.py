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
import json
from typing import List, Dict, Optional

class AirdropManager:
    def __init__(self):
        # Initialize a dictionary to store ownership of old airdrop numbers
        self.old_airdrop_owners: Dict[str, str] = {}  # Maps old number to owner's address
        self.new_airdrop_claims: Dict[str, str] = {}  # Maps new number to owner's address

    def add_old_airdrop_owner(self, old_number: str, owner_address: str) -> None:
        """
        Add an owner for an old airdrop number.

        :param old_number: The old airdrop number
        :param owner_address: The address of the owner
        """
        if old_number in self.old_airdrop_owners:
            raise ValueError(f"Old airdrop number {old_number} already has an owner.")
        self.old_airdrop_owners[old_number] = owner_address

    def claim_new_airdrop(self, new_number: str, owner_address: str) -> bool:
        """
        Allow an owner of an old airdrop number to claim a new airdrop number.

        :param new_number: The new airdrop number to claim
        :param owner_address: The address of the owner claiming the new number
        :return: True if the claim is successful, False otherwise
        """
        if new_number in self.new_airdrop_claims:
            raise ValueError(f"New airdrop number {new_number} has already been claimed.")

        # Check if the owner has an old airdrop number
        if not self.is_owner_of_old_number(owner_address):
            raise PermissionError(f"Address {owner_address} does not own an old airdrop number.")

        # Claim the new airdrop number
        self.new_airdrop_claims[new_number] = owner_address
        return True

    def is_owner_of_old_number(self, owner_address: str) -> bool:
        """
        Check if the given address owns any old airdrop number.

        :param owner_address: The address to check
        :return: True if the address owns an old airdrop number, False otherwise
        """
        return owner_address in self.old_airdrop_owners.values()

    def get_old_owners(self) -> List[str]:
        """
        Get a list of all old airdrop owners.

        :return: List of owner addresses
        """
        return list(self.old_airdrop_owners.values())

    def get_new_claims(self) -> Dict[str, str]:
        """
        Get a dictionary of new airdrop claims.

        :return: Dictionary mapping new airdrop numbers to owner addresses
        """
        return self.new_airdrop_claims

    def save_state(self, filename: str) -> None:
        """
        Save the current state of the airdrop manager to a JSON file.

        :param filename: The name of the file to save the state
        """
        state = {
            'old_airdrop_owners': self.old_airdrop_owners,
            'new_airdrop_claims': self.new_airdrop_claims
        }
        with open(filename, 'w') as f:
            json.dump(state, f)

    def load_state(self, filename: str) -> None:
        """
        Load the state of the airdrop manager from a JSON file.

        :param filename: The name of the file to load the state from
        """
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
                self.old_airdrop_owners = state.get('old_airdrop_owners', {})
                self.new_airdrop_claims = state.get('new_airdrop_claims', {})
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} does not exist.")
        except json.JSONDecodeError:
            raise ValueError(f"The file {filename} contains invalid JSON.")

# Example usage:
if __name__ == "__main__":
    manager = AirdropManager()
    manager.add_old_airdrop_owner("888-001", "0x123abc")
    manager.add_old_airdrop_owner("888-002", "0x456def")

    try:
        manager.claim_new_airdrop("new-001", "0x123abc")
        print("Claim successful!")
    except Exception as e:
        print(f"Error: {e}")

    # Save the state to a file
    manager.save_state("airdrop_state.json")

    # Load the state from a file
    new_manager = AirdropManager()
    new_manager.load_state("airdrop_state.json")
    print(new_manager.get_new_claims())
```
