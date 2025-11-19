"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Write a Python script that integrates with an API to manage plant and machinery equipment hire, ensuring compliance with health and safety regulations as highlighted by Ntalo Investments.
Generated: DETERMINISTIC_916716fb52504955
Batch ID: 20250612_161616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ntalo-investments.com/v1": {
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
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("equipment_hire.log"),
        logging.StreamHandler()
    ]
)

# API Configuration
API_BASE_URL = "https://api.ntalo-investments.com/v1"
API_KEY = "your_api_key_here"  # Replace this with your actual API key

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def get_equipment_list():
    """
    Fetch a list of available equipment from the API.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/equipment", headers=HEADERS)
        response.raise_for_status()
        equipment_list = response.json()
        logging.info("Successfully fetched equipment list.")
        return equipment_list
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching equipment list: {e}")
        return None


def hire_equipment(equipment_id, start_date, end_date, compliance_documents):
    """
    Hire equipment ensuring compliance with health and safety regulations.

    Args:
        equipment_id (str): ID of the equipment to hire.
        start_date (str): Start date of hire (YYYY-MM-DD).
        end_date (str): End date of hire (YYYY-MM-DD).
        compliance_documents (dict): Health and safety compliance documents.
    """
    payload = {
        "equipment_id": equipment_id,
        "start_date": start_date,
        "end_date": end_date,
        "compliance_documents": compliance_documents
    }

    try:
        response = requests.post(f"{API_BASE_URL}/hire", json=payload, headers=HEADERS)
        response.raise_for_status()
        hire_details = response.json()
        logging.info(f"Successfully hired equipment (ID: {equipment_id}).")
        return hire_details
    except requests.exceptions.RequestException as e:
        logging.error(f"Error hiring equipment: {e}")
        return None


def main():
    """
    Main function to manage plant and machinery equipment hire.
    """
    logging.info("Starting equipment hire management script...")

    # Fetch the equipment list
    equipment = get_equipment_list()
    if not equipment:
        logging.error("Failed to retrieve equipment list. Exiting...")
        return

    # Display available equipment
    print("Available Equipment:")
    for item in equipment:
        print(f"ID: {item['id']}, Name: {item['name']}, Type: {item['type']}, Price: {item['price_per_day']}")

    # Example user input (replace with actual user interaction in production)
    equipment_id = input("Enter the ID of the equipment you want to hire: ").strip()
    start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter the end date (YYYY-MM-DD): ").strip()

    # Example compliance documents
    compliance_documents = {
        "risk_assessment": True,  # Replace with actual document verification logic
        "insurance_certificate": True
    }

    # Hire the equipment
    hire_details = hire_equipment(equipment_id, start_date, end_date, compliance_documents)
    if hire_details:
        print("Hire Details:")
        print(f"Equipment: {hire_details['equipment_name']}")
        print(f"Start Date: {hire_details['start_date']}")
        print(f"End Date: {hire_details['end_date']}")
        print(f"Total Cost: {hire_details['total_cost']}")
    else:
        logging.error("Failed to hire equipment.")

    logging.info("Script execution finished.")


if __name__ == "__main__":
    main()
```
