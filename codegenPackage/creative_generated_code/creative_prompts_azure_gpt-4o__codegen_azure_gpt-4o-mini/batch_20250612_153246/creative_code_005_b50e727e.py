"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myhealthcarebilling.com
Prompt: Write a program to manage provider enrollment and re-credentialing processes, ensuring compliance with payer requirements, as described in My Healthcare Billing's insurance credentialing services.
Generated: DETERMINISTIC_b50e727e1d1e2fdc
Batch ID: 20250612_153246
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
from datetime import datetime
from typing import List, Dict, Optional

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Provider:
    """
    Class representing a healthcare provider.
    Attributes include provider ID, name, enrollment status, and credentialing details.
    """
    
    def __init__(self, provider_id: str, name: str):
        self.provider_id = provider_id
        self.name = name
        self.enrollment_status = 'Pending'
        self.credentialing_details = {}
    
    def update_enrollment_status(self, status: str):
        """Update the enrollment status of the provider."""
        logging.info(f"Updating enrollment status for provider {self.provider_id} to {status}.")
        self.enrollment_status = status

    def add_credentialing_detail(self, key: str, value: str):
        """Add credentialing detail to the provider's record."""
        logging.info(f"Adding credentialing detail for provider {self.provider_id}: {key} = {value}.")
        self.credentialing_details[key] = value

class ProviderManager:
    """
    Class to manage provider enrollment and re-credentialing processes.
    """
    
    def __init__(self):
        self.providers: Dict[str, Provider] = {}
    
    def add_provider(self, provider_id: str, name: str) -> None:
        """Add a new provider to the management system."""
        if provider_id in self.providers:
            logging.error(f"Provider ID {provider_id} already exists.")
            raise ValueError(f"Provider ID {provider_id} already exists.")
        self.providers[provider_id] = Provider(provider_id, name)
        logging.info(f"Provider {name} with ID {provider_id} added successfully.")

    def update_provider_status(self, provider_id: str, status: str) -> None:
        """Update the enrollment status of an existing provider."""
        if provider_id not in self.providers:
            logging.error(f"Provider ID {provider_id} not found.")
            raise ValueError(f"Provider ID {provider_id} not found.")
        self.providers[provider_id].update_enrollment_status(status)

    def add_provider_credentialing_detail(self, provider_id: str, key: str, value: str) -> None:
        """Add credentialing detail to a provider's record."""
        if provider_id not in self.providers:
            logging.error(f"Provider ID {provider_id} not found.")
            raise ValueError(f"Provider ID {provider_id} not found.")
        self.providers[provider_id].add_credentialing_detail(key, value)

    def get_provider_info(self, provider_id: str) -> Optional[Dict]:
        """Retrieve information about a provider."""
        if provider_id not in self.providers:
            logging.error(f"Provider ID {provider_id} not found.")
            return None
        provider = self.providers[provider_id]
        return {
            "provider_id": provider.provider_id,
            "name": provider.name,
            "enrollment_status": provider.enrollment_status,
            "credentialing_details": provider.credentialing_details
        }

    def save_to_file(self, file_path: str) -> None:
        """Save the current provider data to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump({id: provider.__dict__ for id, provider in self.providers.items()}, file)
            logging.info(f"Provider data saved to {file_path}.")
        except IOError as e:
            logging.error(f"Error saving provider data to file: {e}")
            raise

    def load_from_file(self, file_path: str) -> None:
        """Load provider data from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for provider_id, provider_data in data.items():
                    provider = Provider(provider_data['provider_id'], provider_data['name'])
                    provider.enrollment_status = provider_data['enrollment_status']
                    provider.credentialing_details = provider_data['credentialing_details']
                    self.providers[provider_id] = provider
            logging.info(f"Provider data loaded from {file_path}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading provider data from file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    provider_manager = ProviderManager()
    
    # Adding providers
    provider_manager.add_provider("123", "Dr. John Doe")
    provider_manager.add_provider("456", "Dr. Jane Smith")
    
    # Updating enrollment status
    provider_manager.update_provider_status("123", "Active")
    
    # Adding credentialing details
    provider_manager.add_provider_credentialing_detail("123", "NPI", "1234567890")
    
    # Saving to file
    provider_manager.save_to_file("providers.json")
    
    # Loading from file
    provider_manager.load_from_file("providers.json")
    
    # Retrieving provider info
    provider_info = provider_manager.get_provider_info("123")
    logging.info(f"Provider Info: {provider_info}")
```
