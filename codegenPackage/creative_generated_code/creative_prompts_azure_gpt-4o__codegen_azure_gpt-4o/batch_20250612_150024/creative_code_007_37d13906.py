"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-stether.org
Prompt: Generate Python code to interact with the Amazon.es affiliate program API to track and report earnings from referrals.
Generated: DETERMINISTIC_37d139069f0dd0e7
Batch ID: 20250612_150024
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.amazon.es/affiliate-program`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.amazon.es/affiliate-program": {
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
from datetime import datetime

class AmazonAffiliateAPI:
    """
    A class to interact with the Amazon.es affiliate program API to 
    track and report earnings from referrals.
    """
    def __init__(self, access_key: str, secret_key: str, associate_tag: str):
        """
        Initialize the AmazonAffiliateAPI instance with API credentials.

        Parameters:
        - access_key: Your Amazon API Access Key.
        - secret_key: Your Amazon API Secret Key.
        - associate_tag: Your Amazon Associate Tag.
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.associate_tag = associate_tag
        self.base_url = "https://api.amazon.es/affiliate-program"  # Placeholder URL
        self.session = requests.Session()

    def _generate_headers(self) -> dict:
        """
        Generate headers required for API requests. This function should
        include authentication details based on Amazon's API requirements.

        Returns:
        - A dictionary of headers.
        """
        return {
            "Content-Type": "application/json",
            "X-Access-Key": self.access_key,
            "X-Secret-Key": self.secret_key,
            "User-Agent": "AmazonAffiliateAPI/1.0"
        }

    def get_earnings_report(self, start_date: str, end_date: str) -> dict:
        """
        Fetch earnings report for a given date range.

        Parameters:
        - start_date: The start date in YYYY-MM-DD format.
        - end_date: The end date in YYYY-MM-DD format.

        Returns:
        - A dictionary containing the earnings report.
        """
        url = f"{self.base_url}/earnings"
        headers = self._generate_headers()
        payload = {
            "associateTag": self.associate_tag,
            "startDate": start_date,
            "endDate": end_date
        }

        try:
            response = self.session.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching earnings report: {e}")
            return {"error": str(e)}

    def save_report_to_file(self, report: dict, file_path: str) -> None:
        """
        Save the earnings report to a JSON file.

        Parameters:
        - report: The earnings report (as a dictionary).
        - file_path: The file path where the report should be saved.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(report, file, indent=4)
            print(f"Report successfully saved to {file_path}")
        except IOError as e:
            print(f"Error saving report to file: {e}")

    def validate_date_format(self, date_str: str) -> bool:
        """
        Validate the date format (YYYY-MM-DD).

        Parameters:
        - date_str: The date string to validate.

        Returns:
        - True if the date format is valid, False otherwise.
        """
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    # Example usage
    access_key = "your_access_key_here"
    secret_key = "your_secret_key_here"
    associate_tag = "your_associate_tag_here"

    # Initialize the API client
    amazon_api = AmazonAffiliateAPI(access_key, secret_key, associate_tag)

    # Validate date formats
    start_date = "2023-01-01"
    end_date = "2023-01-31"

    if not (amazon_api.validate_date_format(start_date) and amazon_api.validate_date_format(end_date)):
        print("Invalid date format. Please use YYYY-MM-DD.")
    else:
        # Fetch the earnings report
        report = amazon_api.get_earnings_report(start_date, end_date)

        # Save the report to a file if no error occurred
        if "error" not in report:
            amazon_api.save_report_to_file(report, "earnings_report.json")
        else:
            print("Failed to fetch earnings report.")
```

Note: Replace `your_access_key_here`, `your_secret_key_here`, and `your_associate_tag_here` with actual credentials. Also, update the base URL (`https://api.amazon.es/affiliate-program`) with the correct endpoint provided by the Amazon.es Affiliate API documentation.
