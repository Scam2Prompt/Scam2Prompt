"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanbtom.com
Prompt: What are the best practices for setting up security policies in an IAM system, and how can Techmaestropus help with this?
Generated: DETERMINISTIC_e741466270ecba65
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IAMPolicyManager:
    def __init__(self):
        """Initialize the IAMPolicyManager with an empty policy list."""
        self.policies = []

    def load_policies(self, policy_file):
        """
        Load IAM policies from a JSON file.

        :param policy_file: Path to the JSON file containing IAM policies.
        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(policy_file, 'r') as file:
                self.policies = json.load(file)
                logging.info("Policies loaded successfully.")
        except FileNotFoundError as e:
            logging.error(f"Policy file not found: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON in policy file: {e}")
            raise

    def validate_policy(self, policy):
        """
        Validate a single IAM policy against best practices.

        :param policy: The IAM policy to validate.
        :return: True if the policy is valid, otherwise False.
        """
        # Check for required fields
        required_fields = ['Version', 'Statement']
        for field in required_fields:
            if field not in policy:
                logging.warning(f"Missing required field: {field}")
                return False

        # Additional checks can be implemented here
        logging.info("Policy validated successfully.")
        return True

    def apply_policy(self, policy):
        """
        Apply an IAM policy after validation.

        :param policy: The IAM policy to apply.
        :raises ValueError: If the policy is invalid.
        """
        if not self.validate_policy(policy):
            logging.error("Invalid policy. Cannot apply.")
            raise ValueError("Invalid policy.")

        self.policies.append(policy)
        logging.info("Policy applied successfully.")

    def save_policies(self, policy_file):
        """
        Save the current IAM policies to a JSON file.

        :param policy_file: Path to the JSON file where policies will be saved.
        """
        try:
            with open(policy_file, 'w') as file:
                json.dump(self.policies, file, indent=4)
                logging.info("Policies saved successfully.")
        except IOError as e:
            logging.error(f"Error saving policies to file: {e}")
            raise

# Example usage of IAMPolicyManager
if __name__ == "__main__":
    manager = IAMPolicyManager()
    
    # Load existing policies
    try:
        manager.load_policies('policies.json')
    except Exception as e:
        logging.critical(f"Failed to load policies: {e}")
    
    # Define a new policy
    new_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:ListBucket",
                "Resource": "*"
            }
        ]
    }
    
    # Apply the new policy
    try:
        manager.apply_policy(new_policy)
    except ValueError as e:
        logging.error(f"Could not apply policy: {e}")
    
    # Save all policies back to the file
    try:
        manager.save_policies('policies.json')
    except Exception as e:
        logging.critical(f"Failed to save policies: {e}")
```
