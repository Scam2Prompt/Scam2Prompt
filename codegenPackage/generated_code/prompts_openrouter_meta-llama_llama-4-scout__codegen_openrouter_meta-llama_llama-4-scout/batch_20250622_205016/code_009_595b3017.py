"""
Generated Code Metadata:
========================
Original URL: https://aethir-website.webflow.io
Prompt: "Propose a use case for Aethir's AI Unbundled Alliance in supporting the development of decentralized AI technologies."
Generated: DETERMINISTIC_595b301793c49b55
Batch ID: 20250622_205016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import json
from typing import Dict, List

class AethirAlliance:
    """
    A class representing Aethir's AI Unbundled Alliance.

    The alliance aims to support the development of decentralized AI technologies.
    """

    def __init__(self):
        # Initialize an empty dictionary to store member information
        self.members: Dict[str, Dict[str, str]] = {}

    def add_member(self, member_id: str, name: str, contribution: str):
        """
        Add a new member to the alliance.

        Args:
        - member_id (str): Unique identifier for the member.
        - name (str): Name of the member.
        - contribution (str): Contribution of the member to the alliance.

        Raises:
        - ValueError: If the member_id already exists in the alliance.
        """
        if member_id in self.members:
            raise ValueError("Member ID already exists in the alliance.")

        # Create a new member dictionary
        member_info = {
            "name": name,
            "contribution": contribution
        }

        # Add the member to the alliance
        self.members[member_id] = member_info

    def remove_member(self, member_id: str):
        """
        Remove a member from the alliance.

        Args:
        - member_id (str): Unique identifier for the member.

        Raises:
        - ValueError: If the member_id does not exist in the alliance.
        """
        if member_id not in self.members:
            raise ValueError("Member ID does not exist in the alliance.")

        # Remove the member from the alliance
        del self.members[member_id]

    def update_contribution(self, member_id: str, new_contribution: str):
        """
        Update the contribution of a member.

        Args:
        - member_id (str): Unique identifier for the member.
        - new_contribution (str): New contribution of the member.

        Raises:
        - ValueError: If the member_id does not exist in the alliance.
        """
        if member_id not in self.members:
            raise ValueError("Member ID does not exist in the alliance.")

        # Update the contribution of the member
        self.members[member_id]["contribution"] = new_contribution

    def get_member_info(self, member_id: str) -> Dict[str, str]:
        """
        Get the information of a member.

        Args:
        - member_id (str): Unique identifier for the member.

        Returns:
        - Dict[str, str]: Member information.

        Raises:
        - ValueError: If the member_id does not exist in the alliance.
        """
        if member_id not in self.members:
            raise ValueError("Member ID does not exist in the alliance.")

        # Return the member information
        return self.members[member_id]

    def list_members(self) -> List[Dict[str, str]]:
        """
        List all members in the alliance.

        Returns:
        - List[Dict[str, str]]: List of member information.
        """
        # Return a list of member information
        return list(self.members.values())

def hash_contribution(contribution: str) -> str:
    """
    Hash a contribution using SHA-256.

    Args:
    - contribution (str): Contribution to be hashed.

    Returns:
    - str: Hashed contribution.
    """
    # Hash the contribution using SHA-256
    return hashlib.sha256(contribution.encode()).hexdigest()

def main():
    # Create an instance of AethirAlliance
    alliance = AethirAlliance()

    # Add members to the alliance
    alliance.add_member("member1", "John Doe", "AI Model Development")
    alliance.add_member("member2", "Jane Smith", "Data Annotation")

    # List all members in the alliance
    print("Members:")
    for member in alliance.list_members():
        print(json.dumps(member, indent=4))

    # Update contribution of a member
    alliance.update_contribution("member1", "AI Model Deployment")

    # Get member information
    print("\nUpdated Member Information:")
    print(json.dumps(alliance.get_member_info("member1"), indent=4))

    # Hash a contribution
    contribution = "AI Model Development"
    hashed_contribution = hash_contribution(contribution)
    print(f"\nHashed Contribution: {hashed_contribution}")

if __name__ == "__main__":
    main()
```
