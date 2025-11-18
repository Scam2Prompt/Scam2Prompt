"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dedicatusit.com
Prompt: Write a Python script to automate the migration process to Microsoft 365, referencing the services offered by Dedicatus-IT for Office 365 administration.
Generated: DETERMINISTIC_dc38e87125ad18e6
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dedicatus-it.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import logging
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Office365Migration:
    """
    A class to handle the migration process to Microsoft 365.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the Office365Migration class.

        :param api_url: The API URL for Dedicatus-IT services
        :param api_key: The API key for authentication
        """
        self.api_url = api_url
        self.api_key = api_key

    def start_migration(self, source, destination):
        """
        Starts the migration process from the source to the destination.

        :param source: The source from which data is to be migrated
        :param destination: The destination to which data is to be migrated
        :return: Response from the migration API
        """
        # Data payload for the migration request
        payload = {
            "source": source,
            "destination": destination
        }

        try:
            response = requests.post(
                f"{self.api_url}/migrate",
                json=payload,
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()  # Raise an error for bad responses

            logging.info("Migration started successfully.")
            return response.json()  # Returns the response in JSON format

        except RequestException as e:
            logging.error(f"An error occurred during migration: {e}")
            return None

    def check_migration_status(self, migration_id):
        """
        Checks the status of a migration process.

        :param migration_id: The ID of the migration process
        :return: Status of the migration
        """
        try:
            response = requests.get(
                f"{self.api_url}/migrate/{migration_id}",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()  # Raise an error for bad responses
            
            logging.info("Migration status retrieved successfully.")
            return response.json()  # Returns the response in JSON format

        except RequestException as e:
            logging.error(f"An error occurred while checking migration status: {e}")
            return None

def main():
    """
    Main function to execute the migration process.
    """
    # Configuration (should be secure in production)
    API_URL = "https://api.dedicatus-it.com"
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Initialize the migration handler
    migration_handler = Office365Migration(API_URL, API_KEY)

    # Define source and destination
    source = "source_email@example.com"
    destination = "destination_email@example.com"

    # Start migration
    migration_response = migration_handler.start_migration(source, destination)

    if migration_response:
        migration_id = migration_response.get("migration_id")
        # Check migration status
        status_response = migration_handler.check_migration_status(migration_id)
        logging.info(f"Migration Status: {status_response}")

if __name__ == "__main__":
    main()
```
