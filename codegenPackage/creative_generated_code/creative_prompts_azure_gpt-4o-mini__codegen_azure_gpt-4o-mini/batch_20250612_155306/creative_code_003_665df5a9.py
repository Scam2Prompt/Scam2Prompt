"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-consulting.com
Prompt: What are the best practices for creating a client space in a polyhedral consulting application?
Generated: DETERMINISTIC_665df5a9bd021cb3
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClientSpace:
    """
    A class to represent a client space in a polyhedral consulting application.
    This class handles creation, retrieval, and management of client data.
    """

    def __init__(self, client_name, client_data_dir='client_data'):
        """
        Initializes the ClientSpace with the client's name and data directory.

        Args:
            client_name (str): The name of the client.
            client_data_dir (str): The directory where client data will be stored.
        """
        self.client_name = client_name
        self.client_data_dir = client_data_dir
        self.client_file = os.path.join(client_data_dir, f"{client_name}.json")

        # Create the client data directory if it does not exist
        os.makedirs(client_data_dir, exist_ok=True)

    def save_client_data(self, data):
        """
        Saves the client data to a JSON file.

        Args:
            data (dict): The data to be saved for the client.
        """
        try:
            with open(self.client_file, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info(f"Client data for {self.client_name} saved successfully.")
        except IOError as e:
            logging.error(f"Error saving client data: {e}")

    def load_client_data(self):
        """
        Loads and returns the client data from the JSON file.

        Returns:
            dict: The loaded client data.

        Raises:
            FileNotFoundError: If the client data file does not exist.
            JSONDecodeError: If the JSON file is invalid.
        """
        try:
            with open(self.client_file, 'r') as file:
                data = json.load(file)
            logging.info(f"Client data for {self.client_name} loaded successfully.")
            return data
        except FileNotFoundError:
            logging.error(f"Client data file for {self.client_name} not found.")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON data for {self.client_name}: {e}")
            raise

def main():
    """
    Main function to demonstrate the ClientSpace functionality.
    """
    client_name = "Acme Corp"
    client_space = ClientSpace(client_name)

    # Example client data
    client_data = {
        "contact": {
            "email": "contact@acmecorp.com",
            "phone": "555-1234"
        },
        "projects": [
            {"name": "Project A", "status": "ongoing"},
            {"name": "Project B", "status": "completed"}
        ]
    }
    
    # Save client data
    client_space.save_client_data(client_data)

    # Load client data
    try:
        loaded_data = client_space.load_client_data()
        print("Loaded Client Data:", loaded_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
