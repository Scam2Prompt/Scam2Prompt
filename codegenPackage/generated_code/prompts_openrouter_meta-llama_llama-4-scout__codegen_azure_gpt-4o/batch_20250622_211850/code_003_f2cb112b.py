"""
Generated Code Metadata:
========================
Original URL: https://gift-mantra.net
Prompt: "Design a basic algorithm for a 'like-minded members' connection feature, similar to what is described on the Stumble! ® website."
Generated: DETERMINISTIC_f2cb112bc34ce646
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class LikeMindedMembers:
    """
    A class to manage and find like-minded members based on shared interests.
    """

    def __init__(self):
        """
        Initialize the LikeMindedMembers class with an empty database of members.
        """
        self.members = {}  # Dictionary to store member data in the format {member_id: {"name": str, "interests": List[str]}}

    def add_member(self, member_id: str, name: str, interests: List[str]) -> None:
        """
        Add a new member to the database.

        :param member_id: Unique identifier for the member.
        :param name: Name of the member.
        :param interests: List of interests for the member.
        """
        if member_id in self.members:
            raise ValueError(f"Member with ID {member_id} already exists.")
        self.members[member_id] = {"name": name, "interests": interests}

    def find_like_minded_members(self, member_id: str) -> List[Dict[str, Any]]:
        """
        Find members with shared interests.

        :param member_id: The ID of the member for whom to find like-minded members.
        :return: A list of dictionaries containing like-minded members' IDs, names, and shared interests.
        """
        if member_id not in self.members:
            raise ValueError(f"Member with ID {member_id} does not exist.")

        target_member = self.members[member_id]
        target_interests = set(target_member["interests"])

        like_minded = []
        for other_id, other_data in self.members.items():
            if other_id == member_id:
                continue  # Skip the target member itself

            shared_interests = target_interests.intersection(other_data["interests"])
            if shared_interests:
                like_minded.append({
                    "member_id": other_id,
                    "name": other_data["name"],
                    "shared_interests": list(shared_interests)
                })

        return like_minded

    def save_to_file(self, file_path: str) -> None:
        """
        Save the members database to a JSON file.

        :param file_path: Path to the file where the database will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.members, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save data to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Load the members database from a JSON file.

        :param file_path: Path to the file from which the database will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.members = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load data from file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the system
        system = LikeMindedMembers()

        # Add members
        system.add_member("1", "Alice", ["reading", "traveling", "coding"])
        system.add_member("2", "Bob", ["traveling", "sports", "coding"])
        system.add_member("3", "Charlie", ["reading", "music", "sports"])

        # Find like-minded members for Alice
        like_minded_for_alice = system.find_like_minded_members("1")
        print("Like-minded members for Alice:")
        for member in like_minded_for_alice:
            print(member)

        # Save the database to a file
        system.save_to_file("members.json")

        # Load the database from a file
        system.load_from_file("members.json")
        print("Database loaded successfully.")

    except Exception as e:
        print(f"Error: {e}")
```
