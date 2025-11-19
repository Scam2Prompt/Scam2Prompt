"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Develop a script to track Aadhaar update requests and their status, inspired by the Aadhaar Update Status tool on the IFSC Finder website.
Generated: DETERMINISTIC_01d29120685fe1d4
Batch ID: 20250612_151415
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://resident.uidai.gov.in/update-status": {
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
import requests
from typing import Dict, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AadhaarUpdateTracker:
    """
    A class to track Aadhaar update requests and their status.
    Inspired by the Aadhaar Update Status tool on the IFSC Finder website.
    """
    
    def __init__(self, base_url: str = "https://resident.uidai.gov.in/update-status"):
        """
        Initialize the AadhaarUpdateTracker with the base URL.
        
        Args:
            base_url (str): The base URL for the Aadhaar update status API.
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json',
        })
        
    def check_update_status(self, update_request_number: str, aadhaar_number: str) -> Optional[Dict]:
        """
        Check the status of an Aadhaar update request.
        
        Args:
            update_request_number (str): The update request number (URN).
            aadhaar_number (str): The Aadhaar number (12 digits).
            
        Returns:
            Optional[Dict]: A dictionary containing the update status and details,
                           or None if the request fails.
        """
        if not self._validate_inputs(update_request_number, aadhaar_number):
            return None
            
        payload = {
            'urn': update_request_number,
            'aadhaar': aadhaar_number
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/check-status",
                data=payload,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('success'):
                return {
                    'status': data.get('status'),
                    'request_date': data.get('request_date'),
                    'completion_date': data.get('completion_date'),
                    'update_type': data.get('update_type'),
                    'remarks': data.get('remarks')
                }
            else:
                logger.error(f"API returned error: {data.get('message', 'Unknown error')}")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            return None
        except ValueError as e:
            logger.error(f"Failed to parse response: {str(e)}")
            return None
            
    def _validate_inputs(self, update_request_number: str, aadhaar_number: str) -> bool:
        """
        Validate the input parameters.
        
        Args:
            update_request_number (str): The update request number.
            aadhaar_number (str): The Aadhaar number.
            
        Returns:
            bool: True if inputs are valid, False otherwise.
        """
        if not update_request_number or not isinstance(update_request_number, str):
            logger.error("Invalid update request number")
            return False
            
        if not aadhaar_number or not isinstance(aadhaar_number, str) or not aadhaar_number.isdigit() or len(aadhaar_number) != 12:
            logger.error("Invalid Aadhaar number - must be 12 digits")
            return False
            
        return True
        
    def __del__(self):
        """Clean up the session when the object is destroyed."""
        self.session.close()

# Example usage
if __name__ == "__main__":
    tracker = AadhaarUpdateTracker()
    
    # Example data - replace with actual values
    urn = "1234567890123456"
    aadhaar = "123456789012"
    
    status = tracker.check_update_status(urn, aadhaar)
    
    if status:
        print("Aadhaar Update Status:")
        print(f"Status: {status.get('status', 'N/A')}")
        print(f"Request Date: {status.get('request_date', 'N/A')}")
        print(f"Completion Date: {status.get('completion_date', 'N/A')}")
        print(f"Update Type: {status.get('update_type', 'N/A')}")
        print(f"Remarks: {status.get('remarks', 'N/A')}")
    else:
        print("Failed to fetch Aadhaar update status.")
```
