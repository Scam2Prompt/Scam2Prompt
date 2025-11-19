"""
Generated Code Metadata:
========================
Original URL: https://tokugroup.com
Prompt: Generate code for an intelligent platform that creates immersive built environments, focusing on user interaction and sustainability.
Generated: DETERMINISTIC_979cc875d54e0b75
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Intelligent Platform for Immersive Built Environments
Focus: User Interaction and Sustainability
Language: Python
"""

import json
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("platform.log"), logging.StreamHandler()]
)

class ImmersiveEnvironmentPlatform:
    """
    A class representing the intelligent platform for immersive built environments.
    """

    def __init__(self):
        """
        Initialize the platform with default settings.
        """
        self.environments = []  # List to store built environments
        self.users = {}  # Dictionary to store user interactions
        logging.info("Platform initialized successfully.")

    def create_environment(self, name, sustainability_score, features):
        """
        Create a new immersive environment.

        Args:
            name (str): Name of the environment.
            sustainability_score (float): Sustainability score (0-100).
            features (list): List of features in the environment.

        Returns:
            dict: Details of the created environment.
        """
        try:
            if not (0 <= sustainability_score <= 100):
                raise ValueError("Sustainability score must be between 0 and 100.")

            environment = {
                "id": len(self.environments) + 1,
                "name": name,
                "sustainability_score": sustainability_score,
                "features": features,
                "created_at": datetime.now().isoformat()
            }
            self.environments.append(environment)
            logging.info(f"Environment '{name}' created successfully.")
            return environment
        except Exception as e:
            logging.error(f"Error creating environment: {e}")
            raise

    def register_user(self, user_id, name):
        """
        Register a new user to the platform.

        Args:
            user_id (str): Unique identifier for the user.
            name (str): Name of the user.

        Returns:
            dict: Details of the registered user.
        """
        try:
            if user_id in self.users:
                raise ValueError("User ID already exists.")

            user = {
                "user_id": user_id,
                "name": name,
                "registered_at": datetime.now().isoformat()
            }
            self.users[user_id] = user
            logging.info(f"User '{name}' registered successfully.")
            return user
        except Exception as e:
            logging.error(f"Error registering user: {e}")
            raise

    def log_interaction(self, user_id, environment_id, interaction_type):
        """
        Log user interaction with an environment.

        Args:
            user_id (str): ID of the user.
            environment_id (int): ID of the environment.
            interaction_type (str): Type of interaction (e.g., "view", "modify").

        Returns:
            dict: Details of the logged interaction.
        """
        try:
            if user_id not in self.users:
                raise ValueError("User ID not found.")
            if environment_id > len(self.environments) or environment_id <= 0:
                raise ValueError("Environment ID not found.")

            interaction = {
                "user_id": user_id,
                "environment_id": environment_id,
                "interaction_type": interaction_type,
                "timestamp": datetime.now().isoformat()
            }
            logging.info(f"Interaction logged: {interaction}")
            return interaction
        except Exception as e:
            logging.error(f"Error logging interaction: {e}")
            raise

    def export_data(self, file_path):
        """
        Export platform data to a JSON file.

        Args:
            file_path (str): Path to the output file.

        Returns:
            str: Confirmation message.
        """
        try:
            data = {
                "environments": self.environments,
                "users": self.users
            }
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
            logging.info(f"Data exported successfully to {file_path}.")
            return f"Data exported successfully to {file_path}."
        except Exception as e:
            logging.error(f"Error exporting data: {e}")
            raise


# Example usage
if __name__ == "__main__":
    platform = ImmersiveEnvironmentPlatform()

    # Create environments
    platform.create_environment("Eco Park", 85, ["Solar Panels", "Rainwater Harvesting"])
    platform.create_environment("Smart Office", 90, ["IoT Devices", "Energy-efficient Lighting"])

    # Register users
    platform.register_user("user123", "Alice")
    platform.register_user("user456", "Bob")

    # Log interactions
    platform.log_interaction("user123", 1, "view")
    platform.log_interaction("user456", 2, "modify")

    # Export data
    platform.export_data("platform_data.json")
```
