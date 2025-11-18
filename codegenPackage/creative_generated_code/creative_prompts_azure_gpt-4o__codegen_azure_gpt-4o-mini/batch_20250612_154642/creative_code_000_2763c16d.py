"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syntera.pro
Prompt: Write Python code to integrate Syntera's AI manager with a CRM system like Altegio using API endpoints for syncing customer data and appointment history.
Generated: DETERMINISTIC_2763c16d1d3f3dcf
Batch ID: 20250612_154642
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.altegio.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.syntera.com": {
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
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SynteraCRMIntegration:
    def __init__(self, syntera_api_url, altegio_api_url, syntera_api_key, altegio_api_key):
        """
        Initialize the integration with API URLs and keys.

        :param syntera_api_url: Base URL for Syntera's API
        :param altegio_api_url: Base URL for Altegio's API
        :param syntera_api_key: API key for accessing Syntera's API
        :param altegio_api_key: API key for accessing Altegio's API
        """
        self.syntera_api_url = syntera_api_url
        self.altegio_api_url = altegio_api_url
        self.syntera_api_key = syntera_api_key
        self.altegio_api_key = altegio_api_key

    def sync_customer_data(self):
        """
        Sync customer data from Syntera to Altegio.
        """
        try:
            syntera_customers = self.fetch_syntera_customers()
            for customer in syntera_customers:
                self.create_or_update_altegio_customer(customer)
        except Exception as e:
            logging.error(f"Error syncing customer data: {e}")

    def fetch_syntera_customers(self):
        """
        Fetch customer data from Syntera's API.

        :return: List of customers
        """
        headers = {'Authorization': f'Bearer {self.syntera_api_key}'}
        response = requests.get(f"{self.syntera_api_url}/customers", headers=headers)
        
        if response.status_code != 200:
            logging.error(f"Failed to fetch customers from Syntera: {response.text}")
            raise Exception("Failed to fetch customers from Syntera")

        return response.json()

    def create_or_update_altegio_customer(self, customer):
        """
        Create or update a customer in Altegio based on Syntera data.

        :param customer: Customer data from Syntera
        """
        headers = {
            'Authorization': f'Bearer {self.altegio_api_key}',
            'Content-Type': 'application/json'
        }
        
        # Check if customer exists in Altegio
        altegio_customer_id = self.get_altegio_customer_id(customer['email'])
        if altegio_customer_id:
            # Update existing customer
            response = requests.put(f"{self.altegio_api_url}/customers/{altegio_customer_id}",
                                    headers=headers, data=json.dumps(customer))
        else:
            # Create new customer
            response = requests.post(f"{self.altegio_api_url}/customers",
                                     headers=headers, data=json.dumps(customer))

        if response.status_code not in (200, 201):
            logging.error(f"Failed to create/update customer in Altegio: {response.text}")
            raise Exception("Failed to create/update customer in Altegio")

    def get_altegio_customer_id(self, email):
        """
        Retrieve the customer ID from Altegio based on email.

        :param email: Email of the customer
        :return: Customer ID or None
        """
        headers = {'Authorization': f'Bearer {self.altegio_api_key}'}
        response = requests.get(f"{self.altegio_api_url}/customers?email={email}", headers=headers)

        if response.status_code != 200:
            logging.error(f"Failed to retrieve customer ID from Altegio: {response.text}")
            raise Exception("Failed to retrieve customer ID from Altegio")

        customers = response.json()
        return customers[0]['id'] if customers else None

    def sync_appointment_history(self):
        """
        Sync appointment history from Syntera to Altegio.
        """
        try:
            syntera_appointments = self.fetch_syntera_appointments()
            for appointment in syntera_appointments:
                self.create_or_update_altegio_appointment(appointment)
        except Exception as e:
            logging.error(f"Error syncing appointment history: {e}")

    def fetch_syntera_appointments(self):
        """
        Fetch appointment history from Syntera's API.

        :return: List of appointments
        """
        headers = {'Authorization': f'Bearer {self.syntera_api_key}'}
        response = requests.get(f"{self.syntera_api_url}/appointments", headers=headers)

        if response.status_code != 200:
            logging.error(f"Failed to fetch appointments from Syntera: {response.text}")
            raise Exception("Failed to fetch appointments from Syntera")

        return response.json()

    def create_or_update_altegio_appointment(self, appointment):
        """
        Create or update an appointment in Altegio based on Syntera data.

        :param appointment: Appointment data from Syntera
        """
        headers = {
            'Authorization': f'Bearer {self.altegio_api_key}',
            'Content-Type': 'application/json'
        }
        
        # Check if appointment exists in Altegio
        altegio_appointment_id = self.get_altegio_appointment_id(appointment['id'])
        if altegio_appointment_id:
            # Update existing appointment
            response = requests.put(f"{self.altegio_api_url}/appointments/{altegio_appointment_id}",
                                    headers=headers, data=json.dumps(appointment))
        else:
            # Create new appointment
            response = requests.post(f"{self.altegio_api_url}/appointments",
                                     headers=headers, data=json.dumps(appointment))

        if response.status_code not in (200, 201):
            logging.error(f"Failed to create/update appointment in Altegio: {response.text}")
            raise Exception("Failed to create/update appointment in Altegio")

    def get_altegio_appointment_id(self, syntera_appointment_id):
        """
        Retrieve the appointment ID from Altegio based on Syntera appointment ID.

        :param syntera_appointment_id: Appointment ID from Syntera
        :return: Appointment ID or None
        """
        headers = {'Authorization': f'Bearer {self.altegio_api_key}'}
        response = requests.get(f"{self.altegio_api_url}/appointments?syntera_id={syntera_appointment_id}", headers=headers)

        if response.status_code != 200:
            logging.error(f"Failed to retrieve appointment ID from Altegio: {response.text}")
            raise Exception("Failed to retrieve appointment ID from Altegio")

        appointments = response.json()
        return appointments[0]['id'] if appointments else None

if __name__ == "__main__":
    # Replace with your actual API endpoints and keys
    SYNTERA_API_URL = "https://api.syntera.com"
    ALTEGIO_API_URL = "https://api.altegio.com"
    SYNTERA_API_KEY = "your_syntera_api_key"
    ALTEGIO_API_KEY = "your_altegio_api_key"

    integration = SynteraCRMIntegration(SYNTERA_API_URL, ALTEGIO_API_URL, SYNTERA_API_KEY, ALTEGIO_API_KEY)
    integration.sync_customer_data()
    integration.sync_appointment_history()
```
