"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-gpu.pages.dev
Prompt: Write a program to simulate the onboarding process for new nodes in the GPUnet ecosystem, including validating Node License Keys.
Generated: DETERMINISTIC_a2b71980b21e4dc5
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import uuid
from datetime import datetime

class NodeOnboarding:
    """
    A class to simulate the onboarding of new nodes into the GPUnet ecosystem.
    """
    def __init__(self):
        # Stores onboarded nodes in the format {node_id: {"license_key", "onboard_time"}}
        self.nodes = {}

    def validate_license_key(self, license_key):
        """
        Validates the license key.

        A valid license key should:
        1. Be a non-empty string of length 16.
        2. Match the pattern: 4 groups of alphanumeric characters separated by hyphens (e.g., XXXX-XXXX-XXXX-XXXX).

        Args:
            license_key (str): The license key to validate.

        Returns:
            bool: True if the license key is valid, False otherwise.
        """
        if not isinstance(license_key, str) or len(license_key) != 19:
            return False
        pattern = r"^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$"
        return bool(re.match(pattern, license_key))

    def onboard_node(self, license_key):
        """
        Onboards a new node into the GPUnet ecosystem after validating the license key.

        Args:
            license_key (str): The license key of the node.

        Returns:
            dict: A dictionary containing the onboarding status and details.
        """
        # Validate the license key first
        if not self.validate_license_key(license_key):
            return {
                "status": "failed",
                "message": "Invalid license key format. Must be XXXX-XXXX-XXXX-XXXX."
            }

        # Generate a unique Node ID
        node_id = str(uuid.uuid4())

        # Record the onboarding time
        onboarding_time = datetime.now().isoformat()

        # Store the node details in the registry
        self.nodes[node_id] = {
            "license_key": license_key,
            "onboard_time": onboarding_time
        }

        return {
            "status": "success",
            "node_id": node_id,
            "onboard_time": onboarding_time
        }

    def list_nodes(self):
        """
        Lists all onboarded nodes in the GPUnet ecosystem.

        Returns:
            dict: A dictionary of all onboarded nodes.
        """
        return self.nodes

# Example usage of the NodeOnboarding class
if __name__ == "__main__":
    # Initialize the onboarding system
    onboarding_system = NodeOnboarding()

    # Example license keys
    license_key_valid = "ABCD-1234-EFGH-5678"
    license_key_invalid = "INVALID-LICENSE-KEY"

    # Onboard a node with a valid license key
    print("Onboarding with valid license key:")
    result_valid = onboarding_system.onboard_node(license_key_valid)
    print(result_valid)

    # Attempt to onboard with an invalid license key
    print("\nOnboarding with invalid license key:")
    result_invalid = onboarding_system.onboard_node(license_key_invalid)
    print(result_invalid)

    # List all onboarded nodes
    print("\nListing all onboarded nodes:")
    nodes = onboarding_system.list_nodes()
    print(nodes)
```
