"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://repositorio.sip.cl
Prompt: Provide an example of how to use the "Sistema Alexia Classroom" API to fetch classroom attendance records, based on the system's documentation from repositorio.sip.cl.
Generated: DETERMINISTIC_328d135a5c6afde8
Batch ID: 20250612_154721
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sistemaalexia.cl/v1": {
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

class SistemaAlexiaAPI:
    """
    A client for interacting with the Sistema Alexia Classroom API.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the API client with the base URL and API key.

        :param base_url: The base URL of the Sistema Alexia API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def fetch_attendance_records(self, classroom_id, date):
        """
        Fetches attendance records for a specified classroom on a specific date.

        :param classroom_id: The ID of the classroom to fetch records for.
        :param date: The date for which to fetch attendance records (format: YYYY-MM-DD).
        :return: A list of attendance records.
        :raises ValueError: If the response is not successful or if the data is malformed.
        """
        url = f"{self.base_url}/attendance/{classroom_id}/{date}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            data = response.json()  # Convert response to JSON
            if 'records' not in data:
                raise ValueError("Malformed response: 'records' key not found")

            return data['records']

        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise  # Re-raise the error after logging
        except Exception as err:
            print(f"An error occurred: {err}")
            raise  # Re-raise the error after logging

# Example usage
if __name__ == "__main__":
    BASE_URL = "https://api.sistemaalexia.cl/v1"  # Replace with the actual API endpoint
    API_KEY = "your_api_key"  # Replace with your actual API key

    classroom_id = "12345"  # Replace with the actual classroom ID
    date = "2023-10-01"  # Replace with the desired date

    api_client = SistemaAlexiaAPI(BASE_URL, API_KEY)

    try:
        attendance_records = api_client.fetch_attendance_records(classroom_id, date)
        print(attendance_records)  # Output the fetched attendance records
    except Exception as e:
        print(f"Failed to fetch attendance records: {e}")
```
