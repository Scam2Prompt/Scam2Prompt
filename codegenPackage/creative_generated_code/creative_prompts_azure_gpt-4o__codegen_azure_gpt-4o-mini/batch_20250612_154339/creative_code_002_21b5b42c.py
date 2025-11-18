"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: Generate code for automating Real Time Information (RTI) filing with HMRC in a managed payroll service, referencing the features provided by Perfect Payrolls.
Generated: DETERMINISTIC_21b5b42cca09bc5d
Batch ID: 20250612_154339
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hmrc.gov.uk": {
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
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HMRCRealTimeInformation:
    def __init__(self, api_base_url, auth_token):
        """
        Initializes the RTI filing service.

        :param api_base_url: Base URL for HMRC API
        :param auth_token: Authentication token for HMRC API access
        """
        self.api_base_url = api_base_url
        self.auth_token = auth_token

    def submit_rti(self, payroll_data):
        """
        Submits real-time information to HMRC.

        :param payroll_data: A dictionary containing payroll information
        :return: Response from the HMRC API
        """
        url = f"{self.api_base_url}/rti"
        headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Content-Type": "application/json"
        }

        try:
            # Sending the POST request to submit payroll data
            response = requests.post(url, headers=headers, data=json.dumps(payroll_data))
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            logging.info("RTI submission successful.")
            return response.json()  # Return the response in JSON format

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request error occurred: {req_err}")
            raise
        except json.JSONDecodeError as json_err:
            logging.error(f"JSON decode error: {json_err}")
            raise

def create_payroll_data(employee, pay_period, earnings):
    """
    Creates a structured payroll data dictionary for RTI submission.

    :param employee: Employee data (name, NI number, etc.)
    :param pay_period: The pay period for this payroll submission
    :param earnings: The earnings details for this payroll submission
    :return: A structured dictionary ready for RTI submission
    """
    return {
        "employee": {
            "name": employee["name"],
            "ni_number": employee["ni_number"],
            "payroll_id": employee["payroll_id"]
        },
        "pay_period": pay_period,
        "earnings": earnings,
        "submission_date": datetime.now().isoformat()
    }

if __name__ == "__main__":
    # Example configuration for HMRC API
    API_BASE_URL = "https://api.hmrc.gov.uk"
    AUTH_TOKEN = "your_auth_token_here"  # Replace with your actual token

    # Example employee and payroll data
    employee_info = {
        "name": "John Doe",
        "ni_number": "QQ123456C",
        "payroll_id": "JD2023"
    }
    
    pay_period_info = "2023-10"
    earnings_info = {
        "gross_pay": 3000,
        "tax_deduction": 500,
        "ni_deduction": 250
    }

    # Create an instance of the HMRC Real Time Information class
    rti_service = HMRCRealTimeInformation(API_BASE_URL, AUTH_TOKEN)

    # Create payroll data for submission
    payroll_data = create_payroll_data(employee_info, pay_period_info, earnings_info)

    # Submit the RTI to HMRC
    try:
        response = rti_service.submit_rti(payroll_data)
        logging.info("RTI response received: %s", response)
    except Exception as e:
        logging.error("Failed to submit RTI: %s", e)
``` 

Make sure to replace `"your_auth_token_here"` with your actual HMRC API authentication token before running the code.
