"""
Generated Code Metadata:
========================
Original URL: https://myhealthcarebilling.com
Prompt: Write a program to manage provider enrollment and re-credentialing processes, ensuring compliance with payer requirements, as described in My Healthcare Billing's insurance credentialing services.
Generated: DETERMINISTIC_b50e727e1d1e2fdc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Provider:
    """Class to represent a healthcare provider."""
    
    def __init__(self, provider_id, name, specialty, enrollment_date):
        self.provider_id = provider_id
        self.name = name
        self.specialty = specialty
        self.enrollment_date = enrollment_date
        self.credentialing_status = 'Pending'
        self.credentialing_expiry = self.calculate_credentialing_expiry()

    def calculate_credentialing_expiry(self):
        """Calculate the credentialing expiry date, typically 2 years from enrollment."""
        return self.enrollment_date + timedelta(days=730)

    def is_credentialing_expired(self):
        """Check if the credentialing has expired."""
        return datetime.now() > self.credentialing_expiry

    def update_credentialing_status(self, status):
        """Update the credentialing status of the provider."""
        self.credentialing_status = status
        logging.info(f"Updated credentialing status for {self.name} to {status}")

class ProviderManager:
    """Class to manage provider enrollment and re-credentialing processes."""
    
    def __init__(self):
        self.providers = {}

    def enroll_provider(self, provider_id, name, specialty):
        """Enroll a new provider."""
        if provider_id in self.providers:
            logging.error(f"Provider with ID {provider_id} already exists.")
            raise ValueError("Provider ID already exists.")
        
        enrollment_date = datetime.now()
        new_provider = Provider(provider_id, name, specialty, enrollment_date)
        self.providers[provider_id] = new_provider
        logging.info(f"Enrolled new provider: {name}")

    def recredential_provider(self, provider_id):
        """Re-credential an existing provider."""
        provider = self.providers.get(provider_id)
        if not provider:
            logging.error(f"Provider with ID {provider_id} not found.")
            raise ValueError("Provider not found.")
        
        if provider.is_credentialing_expired():
            provider.enrollment_date = datetime.now()
            provider.credentialing_status = 'Re-credentialed'
            provider.credentialing_expiry = provider.calculate_credentialing_expiry()
            logging.info(f"Provider {provider.name} has been re-credentialed.")
        else:
            logging.info(f"Provider {provider.name} is still credentialed.")

    def get_provider_info(self, provider_id):
        """Retrieve provider information."""
        provider = self.providers.get(provider_id)
        if not provider:
            logging.error(f"Provider with ID {provider_id} not found.")
            raise ValueError("Provider not found.")
        
        return {
            "provider_id": provider.provider_id,
            "name": provider.name,
            "specialty": provider.specialty,
            "enrollment_date": provider.enrollment_date.isoformat(),
            "credentialing_status": provider.credentialing_status,
            "credentialing_expiry": provider.credentialing_expiry.isoformat()
        }

    def save_providers_to_file(self, filename):
        """Save provider data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({pid: vars(provider) for pid, provider in self.providers.items()}, file, default=str)
            logging.info(f"Provider data saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save provider data: {e}")
            raise

    def load_providers_from_file(self, filename):
        """Load provider data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                provider_data = json.load(file)
                for pid, data in provider_data.items():
                    provider = Provider(pid, data['name'], data['specialty'], datetime.fromisoformat(data['enrollment_date']))
                    provider.credentialing_status = data['credentialing_status']
                    provider.credentialing_expiry = datetime.fromisoformat(data['credentialing_expiry'])
                    self.providers[pid] = provider
            logging.info(f"Provider data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load provider data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    manager = ProviderManager()
    try:
        manager.enroll_provider("123", "Dr. Smith", "Cardiology")
        manager.recredential_provider("123")
        provider_info = manager.get_provider_info("123")
        print(provider_info)
        manager.save_providers_to_file("providers.json")
        manager.load_providers_from_file("providers.json")
    except ValueError as ve:
        logging.error(ve)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
