"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: Generate a script to automate certification tracking for commercial personnel, including credit managers, based on the training services mentioned on SIF's webpage.
Generated: DETERMINISTIC_afd9c958b0ac07e5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# certification_tracker.py

import datetime
import json
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CertificationTracker:
    def __init__(self, training_services: List[Dict]):
        """
        Initialize the CertificationTracker with a list of training services.

        Args:
        - training_services (List[Dict]): A list of dictionaries containing training service information.
            Each dictionary should have the following keys:
                - 'id' (str): Unique identifier for the training service.
                - 'name' (str): Name of the training service.
                - 'credits' (int): Number of credits associated with the training service.
                - 'expiration_date' (str): Expiration date of the training service in 'YYYY-MM-DD' format.
        """
        self.training_services = training_services
        self.certifications = {}

    def add_certification(self, personnel_id: str, training_service_id: str, completion_date: str):
        """
        Add a certification for a personnel.

        Args:
        - personnel_id (str): Unique identifier for the personnel.
        - training_service_id (str): Unique identifier for the training service.
        - completion_date (str): Date of completion in 'YYYY-MM-DD' format.

        Raises:
        - ValueError: If the training service ID is not found in the training services list.
        """
        training_service = next((ts for ts in self.training_services if ts['id'] == training_service_id), None)
        if training_service is None:
            raise ValueError(f"Training service ID '{training_service_id}' not found")

        if personnel_id not in self.certifications:
            self.certifications[personnel_id] = []

        self.certifications[personnel_id].append({
            'training_service_id': training_service_id,
            'completion_date': completion_date,
            'expiration_date': training_service['expiration_date']
        })

    def get_certifications(self, personnel_id: str):
        """
        Get the certifications for a personnel.

        Args:
        - personnel_id (str): Unique identifier for the personnel.

        Returns:
        - List[Dict]: A list of dictionaries containing certification information.
        """
        return self.certifications.get(personnel_id, [])

    def check_expiration(self, personnel_id: str):
        """
        Check the expiration status of certifications for a personnel.

        Args:
        - personnel_id (str): Unique identifier for the personnel.

        Returns:
        - List[Dict]: A list of dictionaries containing certification information with expiration status.
        """
        certifications = self.get_certifications(personnel_id)
        expired_certifications = []

        for certification in certifications:
            expiration_date = datetime.datetime.strptime(certification['expiration_date'], '%Y-%m-%d')
            if expiration_date < datetime.datetime.now():
                certification['expired'] = True
                expired_certifications.append(certification)
            else:
                certification['expired'] = False

        return expired_certifications

def load_training_services(file_path: str) -> List[Dict]:
    """
    Load training services from a JSON file.

    Args:
    - file_path (str): Path to the JSON file.

    Returns:
    - List[Dict]: A list of dictionaries containing training service information.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON: {e}")
        return []

def main():
    # Load training services from JSON file
    training_services = load_training_services('training_services.json')

    # Create a CertificationTracker instance
    tracker = CertificationTracker(training_services)

    # Add certifications for personnel
    tracker.add_certification('personnel1', 'service1', '2022-01-01')
    tracker.add_certification('personnel1', 'service2', '2022-06-01')
    tracker.add_certification('personnel2', 'service1', '2022-03-01')

    # Get certifications for personnel
    print("Certifications for personnel1:")
    print(tracker.get_certifications('personnel1'))

    # Check expiration status
    print("\nExpired certifications for personnel1:")
    print(tracker.check_expiration('personnel1'))

if __name__ == '__main__':
    main()
```

```json
// training_services.json

[
    {
        "id": "service1",
        "name": "Service 1",
        "credits": 10,
        "expiration_date": "2024-01-01"
    },
    {
        "id": "service2",
        "name": "Service 2",
        "credits": 20,
        "expiration_date": "2024-06-01"
    }
]
```
