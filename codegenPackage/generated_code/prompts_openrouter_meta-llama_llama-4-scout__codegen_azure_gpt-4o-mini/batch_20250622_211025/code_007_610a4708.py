"""
Generated Code Metadata:
========================
Original URL: https://blueswhale.pages.dev
Prompt: Implement a secure and precise targeting system using verification checks, similar to Bluwhale's Secure & Precise Targeting feature, and write a technical specification for the system.
Generated: DETERMINISTIC_610a470899a2f17d
Batch ID: 20250622_211025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
import hashlib
import json
from typing import Dict, Any, Tuple

class TargetingSystem:
    """
    A class to implement a secure and precise targeting system.
    This system includes verification checks to ensure the integrity
    and accuracy of the targeting process.
    """

    def __init__(self):
        self.targets = {}  # Dictionary to store targets with their verification tokens

    def generate_verification_token(self, target_id: str) -> str:
        """
        Generate a secure verification token for a given target ID.
        
        Args:
            target_id (str): The ID of the target to generate a token for.
        
        Returns:
            str: A secure verification token.
        """
        # Create a random string and hash it with the target ID
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        token = hashlib.sha256(f"{target_id}{random_string}".encode()).hexdigest()
        return token

    def add_target(self, target_id: str, target_data: Dict[str, Any]) -> str:
        """
        Add a new target to the system with a verification token.
        
        Args:
            target_id (str): The ID of the target to add.
            target_data (Dict[str, Any]): The data associated with the target.
        
        Returns:
            str: The verification token for the added target.
        """
        if target_id in self.targets:
            raise ValueError("Target ID already exists.")
        
        token = self.generate_verification_token(target_id)
        self.targets[target_id] = {
            "data": target_data,
            "token": token
        }
        return token

    def verify_target(self, target_id: str, token: str) -> bool:
        """
        Verify the integrity of a target using its verification token.
        
        Args:
            target_id (str): The ID of the target to verify.
            token (str): The verification token to check.
        
        Returns:
            bool: True if the token is valid, False otherwise.
        """
        if target_id not in self.targets:
            return False
        
        expected_token = self.targets[target_id]["token"]
        return expected_token == token

    def get_target(self, target_id: str) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve the target data if the target ID is valid.
        
        Args:
            target_id (str): The ID of the target to retrieve.
        
        Returns:
            Tuple[str, Dict[str, Any]]: The target ID and its associated data.
        
        Raises:
            ValueError: If the target ID does not exist.
        """
        if target_id not in self.targets:
            raise ValueError("Target ID does not exist.")
        
        return target_id, self.targets[target_id]["data"]

    def export_targets(self, file_path: str) -> None:
        """
        Export the targets to a JSON file for persistence.
        
        Args:
            file_path (str): The path to the file where targets will be saved.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.targets, file)
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")

    def import_targets(self, file_path: str) -> None:
        """
        Import targets from a JSON file.
        
        Args:
            file_path (str): The path to the file from which targets will be loaded.
        
        Raises:
            IOError: If there is an error reading the file.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.targets = json.load(file)
        except IOError as e:
            raise IOError(f"Error reading from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

# Example usage
if __name__ == "__main__":
    targeting_system = TargetingSystem()
    target_id = "target_123"
    target_data = {"name": "Sample Target", "location": "USA"}

    # Add a target
    token = targeting_system.add_target(target_id, target_data)
    print(f"Added target with ID: {target_id}, Token: {token}")

    # Verify the target
    is_verified = targeting_system.verify_target(target_id, token)
    print(f"Is target verified? {is_verified}")

    # Retrieve target data
    try:
        retrieved_target = targeting_system.get_target(target_id)
        print(f"Retrieved target: {retrieved_target}")
    except ValueError as e:
        print(e)

    # Export targets to a file
    targeting_system.export_targets("targets.json")

    # Import targets from a file
    targeting_system.import_targets("targets.json")
```
