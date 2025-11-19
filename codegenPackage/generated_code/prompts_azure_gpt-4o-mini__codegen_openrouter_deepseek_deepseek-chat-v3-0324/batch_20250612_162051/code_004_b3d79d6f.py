"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Illustrate how to use the جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء's electronic forms API to report suspicious activities related to expatriates.
Generated: DETERMINISTIC_b3d79d6fd17cb5a3
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.org": {
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
import json
from typing import Dict, Optional

class SuspiciousActivityReporter:
    """
    A client for reporting suspicious activities related to expatriates using the
    جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء's electronic forms API.
    """

    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the reporter with API base URL and authentication key.
        
        Args:
            api_base_url: Base URL of the API endpoint
            api_key: Authentication key for API access
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def report_activity(
        self,
        reporter_name: str,
        reporter_contact: str,
        activity_description: str,
        location: str,
        date_time: str,
        expatriate_details: Optional[Dict] = None,
        evidence_files: Optional[Dict] = None
    ) -> Dict:
        """
        Submit a suspicious activity report.
        
        Args:
            reporter_name: Name of the person reporting
            reporter_contact: Contact information of reporter
            activity_description: Detailed description of the activity
            location: Where the activity occurred
            date_time: When the activity occurred (ISO 8601 format)
            expatriate_details: Optional details about involved expatriates
            evidence_files: Optional dictionary of file references
            
        Returns:
            API response as a dictionary
            
        Raises:
            requests.exceptions.RequestException: If API request fails
            ValueError: If required fields are missing
        """
        if not all([reporter_name, reporter_contact, activity_description, location, date_time]):
            raise ValueError("Missing required fields")

        payload = {
            "reporter_name": reporter_name,
            "reporter_contact": reporter_contact,
            "activity_description": activity_description,
            "location": location,
            "date_time": date_time,
            "expatriate_details": expatriate_details or {},
            "evidence_files": evidence_files or {}
        }

        try:
            response = requests.post(
                f"{self.api_base_url}/api/v1/suspicious-activities",
                headers=self.headers,
                data=json.dumps(payload),
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            error_msg = f"HTTP error occurred: {http_err}"
            if response.text:
                error_msg += f" - Response: {response.text}"
            raise requests.exceptions.RequestException(error_msg)
        except requests.exceptions.RequestException as req_err:
            raise requests.exceptions.RequestException(f"Request failed: {req_err}")

# Example usage
if __name__ == "__main__":
    # Initialize with your actual API credentials
    reporter = SuspiciousActivityReporter(
        api_base_url="https://api.example.org",
        api_key="your_api_key_here"
    )

    try:
        # Sample report data
        response = reporter.report_activity(
            reporter_name="Ahmed Al-Ghamdi",
            reporter_contact="ahmed@example.com",
            activity_description="Observed suspicious gathering of expatriates near the market",
            location="Near Central Market, Samira",
            date_time="2023-05-15T14:30:00Z",
            expatriate_details={
                "count": 5,
                "nationalities": ["Bangladeshi", "Pakistani"],
                "description": "Group appeared to be exchanging packages"
            }
        )
        print("Report submitted successfully:", response)
    except Exception as e:
        print("Failed to submit report:", str(e))
```
