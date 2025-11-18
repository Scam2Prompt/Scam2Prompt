"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-en.pages.dev
Prompt: Develop a Python script using the Certik API to perform a security audit on a smart contract for a decentralized betting platform, inspired by Blockchain Bets' audit process.
Generated: DETERMINISTIC_8a7350c9c836a7e8
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.certik.com/v1/audit": {
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
import time

class CertikAPIClient:
    """
    A client to interact with the Certik API for smart contract audits.
    """

    BASE_URL = "https://api.certik.com/v1/audit"

    def __init__(self, api_key):
        """
        Initializes the Certik API client.

        :param api_key: Your Certik API key for authentication.
        """
        self.api_key = api_key

    def submit_audit_request(self, contract_address, platform_name):
        """
        Submits a request for a security audit on a given smart contract.

        :param contract_address: Ethereum address of the smart contract.
        :param platform_name: Name of the decentralized betting platform.
        :return: Response from the Certik API.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        payload = {
            'contract_address': contract_address,
            'platform_name': platform_name,
        }
        try:
            response = requests.post(self.BASE_URL, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad HTTP response
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def check_audit_status(self, audit_id):
        """
        Checks the status of a submitted audit request.

        :param audit_id: The ID of the submitted audit.
        :return: The current status of the audit.
        """
        status_url = f"{self.BASE_URL}/{audit_id}/status"

        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        
        try:
            response = requests.get(status_url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred while checking status: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

def main():
    """
    Main function to execute the audit process.
    """
    api_key = "YOUR_API_KEY"  # Replace with your Certik API key
    contract_address = "0xYourContractAddress"  # Replace with the smart contract address
    platform_name = "Blockchain Bets"  # Name of the decentralized betting platform

    client = CertikAPIClient(api_key)

    # Step 1: Submit the audit request
    print("Submitting audit request...")
    audit_response = client.submit_audit_request(contract_address, platform_name)

    if audit_response and 'audit_id' in audit_response:
        audit_id = audit_response['audit_id']
        print(f"Audit submitted successfully. Audit ID: {audit_id}")

        # Step 2: Poll for audit status
        print("Checking audit status...")
        while True:
            status_response = client.check_audit_status(audit_id)
            if status_response:
                status = status_response.get('status', 'unknown')
                print(f"Current audit status: {status}")

                if status in ['completed', 'failed']:
                    print(f"Final audit status: {status}")
                    break
                else:
                    time.sleep(30)  # Wait before polling again
            else:
                print("Failed to retrieve audit status.")
                break
    else:
        print("Failed to submit audit request.")

if __name__ == "__main__":
    main()
```

**Note**: Replace `"YOUR_API_KEY"` and `"0xYourContractAddress"` with your actual Certik API key and the smart contract address you want to audit.
