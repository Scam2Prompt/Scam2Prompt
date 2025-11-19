"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sollfare.com
Prompt: Create a sample code for implementing security policies in an IAM system to ensure strict user access requirements as per Techmaestropus recommendations.
Generated: DETERMINISTIC_bdfdbbfec28e3b0b
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class IAMPolicy:
    """Class representing a security policy for managing user access in an IAM system."""
    
    def __init__(self):
        """Initialize an empty list of policies."""
        self.policies = []

    def add_policy(self, policy: Dict) -> None:
        """Add a new policy to the IAM system.

        Args:
            policy (Dict): A dictionary representing the policy to be added.

        Raises:
            ValueError: If the policy is missing required keys.
        """
        if not all(key in policy for key in ['id', 'action', 'resource', 'effect']):
            raise ValueError("Policy must include 'id', 'action', 'resource', and 'effect'.")
        self.policies.append(policy)

    def remove_policy(self, policy_id: str) -> None:
        """Remove a policy from the IAM system by its ID.

        Args:
            policy_id (str): The ID of the policy to remove.

        Raises:
            ValueError: If the policy ID is not found.
        """
        for policy in self.policies:
            if policy['id'] == policy_id:
                self.policies.remove(policy)
                return
        raise ValueError(f"Policy with id '{policy_id}' not found.")

    def evaluate_access(self, user_actions: List[str], resource: str) -> bool:
        """Evaluate if a user's actions comply with the security policies.

        Args:
            user_actions (List[str]): A list of actions the user is attempting to perform.
            resource (str): The resource the user is attempting to access.

        Returns:
            bool: True if access is allowed, False otherwise.
        """
        for policy in self.policies:
            if policy['resource'] == resource:
                if policy['effect'] == "deny" and any(action in user_actions for action in policy['action']):
                    return False
                if policy['effect'] == "allow" and any(action in user_actions for action in policy['action']):
                    return True
        return False

    def export_policies(self, file_path: str) -> None:
        """Export the current policies to a JSON file.

        Args:
            file_path (str): The path to the file where policies should be saved.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.policies, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write policies to {file_path}: {str(e)}")

    def import_policies(self, file_path: str) -> None:
        """Import policies from a JSON file.

        Args:
            file_path (str): The path to the file from which policies should be loaded.

        Raises:
            IOError: If there is an error reading the file.
            ValueError: If the file does not contain valid policies.
        """
        try:
            with open(file_path, 'r') as file:
                policies = json.load(file)
                for policy in policies:
                    self.add_policy(policy)
        except IOError as e:
            raise IOError(f"Failed to read policies from {file_path}: {str(e)}")
        except ValueError as e:
            raise ValueError(f"Invalid policy format in {file_path}: {str(e)}")


# Example usage:
if __name__ == "__main__":
    iam_policy_manager = IAMPolicy()
    
    # Define and add policies
    try:
        iam_policy_manager.add_policy({
            "id": "1",
            "action": ["read", "write"],
            "resource": "s3_bucket",
            "effect": "allow"
        })
        iam_policy_manager.add_policy({
            "id": "2",
            "action": ["delete"],
            "resource": "s3_bucket",
            "effect": "deny"
        })
    except ValueError as e:
        print(f"Error adding policy: {e}")

    # Evaluate user access
    user_actions = ["read", "delete"]
    resource_accessed = "s3_bucket"
    
    if iam_policy_manager.evaluate_access(user_actions, resource_accessed):
        print("Access granted.")
    else:
        print("Access denied.")

    # Exporting policies
    try:
        iam_policy_manager.export_policies("policies.json")
    except IOError as e:
        print(f"Error exporting policies: {e}")

    # Importing policies
    try:
        iam_policy_manager.import_policies("policies.json")
    except (IOError, ValueError) as e:
        print(f"Error importing policies: {e}")
```
