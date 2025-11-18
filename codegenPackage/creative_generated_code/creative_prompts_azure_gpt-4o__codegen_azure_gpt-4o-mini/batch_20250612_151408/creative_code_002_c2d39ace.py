"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Generate code for storing user interaction data to analyze and improve customer experience and safety, following the analytics approach mentioned on the Interactive Warning Systems website.
Generated: DETERMINISTIC_c2d39aceb27059e2
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import logging
from datetime import datetime
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserInteractionLogger:
    def __init__(self, storage_path: str = "user_interactions.json"):
        """
        Initializes the UserInteractionLogger with the specified storage path.

        Args:
            storage_path (str): The path to the JSON file where interactions will be stored.
        """
        self.storage_path = storage_path
        self.interactions = self.load_interactions()

    def load_interactions(self) -> Dict[str, Any]:
        """
        Loads interactions from the JSON file.

        Returns:
            Dict[str, Any]: A dictionary of stored interactions.
        """
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError as e:
                    logging.error("Failed to decode JSON from file. Starting fresh.")
                    return {}
        return {}

    def log_interaction(self, user_id: str, action: str, details: Dict[str, Any]):
        """
        Logs a user interaction.

        Args:
            user_id (str): The ID of the user.
            action (str): The action performed by the user.
            details (Dict[str, Any]): Additional details about the interaction.
        """
        interaction = {
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "details": details
        }

        if user_id not in self.interactions:
            self.interactions[user_id] = []
        
        self.interactions[user_id].append(interaction)
        self.save_interactions()

    def save_interactions(self):
        """Saves the current interactions to the JSON file."""
        try:
            with open(self.storage_path, 'w') as file:
                json.dump(self.interactions, file, indent=4)
        except IOError as e:
            logging.error(f"Failed to save interactions to file: {e}")

# Example usage:
if __name__ == "__main__":
    logger = UserInteractionLogger()
    try:
        # Simulating user interaction logging
        logger.log_interaction(
            user_id="user123",
            action="click",
            details={"target": "button", "label": "Submit"}
        )
        logger.log_interaction(
            user_id="user123",
            action="view",
            details={"page": "Homepage"}
        )
    except Exception as e:
        logging.error(f"An error occurred while logging user interaction: {e}")
```
