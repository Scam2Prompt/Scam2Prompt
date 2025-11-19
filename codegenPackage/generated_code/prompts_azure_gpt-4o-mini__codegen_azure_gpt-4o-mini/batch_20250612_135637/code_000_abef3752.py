"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Generate a Python script that utilizes MS Power BI for dynamic data reporting as described by GLOW Consultants.
Generated: DETERMINISTIC_abef37522785d4f9
Batch ID: 20250612_135637
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.powerbi.com/v1.0/myorg/groups/{self.workspace_id}/reports/{self.report_id}/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://analysis.windows.net/powerbi/api/.default": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import pandas as pd
import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PowerBIReport:
    def __init__(self, client_id, client_secret, tenant_id, workspace_id, report_id):
        """
        Initialize the PowerBIReport class with necessary credentials and identifiers.

        :param client_id: Azure AD application client ID
        :param client_secret: Azure AD application client secret
        :param tenant_id: Azure AD tenant ID
        :param workspace_id: Power BI workspace ID
        :param report_id: Power BI report ID
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id
        self.report_id = report_id
        self.access_token = None

    def authenticate(self):
        """
        Authenticate with Azure AD and obtain an access token for Power BI API.

        :raises Exception: If authentication fails
        """
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'https://analysis.windows.net/powerbi/api/.default'
        }
        
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            self.access_token = response.json().get('access_token')
            logging.info("Authentication successful.")
        except requests.exceptions.HTTPError as err:
            logging.error(f"Authentication failed: {err}")
            raise Exception("Authentication failed") from err

    def get_report_data(self):
        """
        Retrieve data from the specified Power BI report.

        :return: DataFrame containing the report data
        :raises Exception: If data retrieval fails
        """
        if not self.access_token:
            raise Exception("Access token is not available. Please authenticate first.")

        url = f"https://api.powerbi.com/v1.0/myorg/groups/{self.workspace_id}/reports/{self.report_id}/data"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            logging.info("Data retrieval successful.")
            return pd.DataFrame(data['value'])  # Assuming the data is in 'value' key
        except requests.exceptions.HTTPError as err:
            logging.error(f"Data retrieval failed: {err}")
            raise Exception("Data retrieval failed") from err

def main():
    # Replace with your actual credentials and identifiers
    CLIENT_ID = 'your_client_id'
    CLIENT_SECRET = 'your_client_secret'
    TENANT_ID = 'your_tenant_id'
    WORKSPACE_ID = 'your_workspace_id'
    REPORT_ID = 'your_report_id'

    # Create an instance of PowerBIReport
    powerbi_report = PowerBIReport(CLIENT_ID, CLIENT_SECRET, TENANT_ID, WORKSPACE_ID, REPORT_ID)

    try:
        # Authenticate and retrieve report data
        powerbi_report.authenticate()
        report_data = powerbi_report.get_report_data()
        print(report_data)  # Display the report data
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
