"""
Generated Code Metadata:
========================
Original URL: https://f0fozvn18.ukit.me
Prompt: Write a Python script using the `requests` library to programmatically check if a uKit website is still in its trial period or has expired.
Generated: DETERMINISTIC_8c11932753936442
Batch ID: 20250622_204634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from datetime import datetime
from typing import Optional, Dict, Any

class UKitTrialChecker:
    """
    A class to check the trial status of a uKit website.
    """

    def __init__(self, website_url: str):
        """
        Initialize the checker with the website URL.
        
        Args:
            website_url (str): The URL of the uKit website to check.
        """
        self.website_url = website_url.rstrip('/')
        self.api_url = f"{self.website_url}/api/v1/site/info"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json'
        }

    def _make_request(self) -> Optional[Dict[str, Any]]:
        """
        Make a GET request to the uKit API endpoint.
        
        Returns:
            Optional[Dict[str, Any]]: The JSON response if successful, None otherwise.
        """
        try:
            response = requests.get(
                self.api_url,
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None

    def check_trial_status(self) -> Optional[str]:
        """
        Check the trial status of the uKit website.
        
        Returns:
            Optional[str]: The trial status message or None if there was an error.
        """
        data = self._make_request()
        if not data:
            return None

        try:
            trial_end_date_str = data.get('trialEndDate')
            if not trial_end_date_str:
                return "No trial information available."

            trial_end_date = datetime.strptime(trial_end_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            current_date = datetime.utcnow()

            if current_date > trial_end_date:
                return "Trial has expired."
            else:
                days_remaining = (trial_end_date - current_date).days
                return f"Trial is active. {days_remaining} days remaining."
        except Exception as e:
            print(f"Error processing trial data: {e}")
            return None

if __name__ == "__main__":
    website_url = input("Enter the uKit website URL: ").strip()
    checker = UKitTrialChecker(website_url)
    status = checker.check_trial_status()
    
    if status:
        print(status)
    else:
        print("Failed to check trial status.")
```
