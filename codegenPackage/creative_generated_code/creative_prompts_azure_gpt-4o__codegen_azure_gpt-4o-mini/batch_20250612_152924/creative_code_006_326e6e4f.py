"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Develop a script to assist employers in Spain with verifying if a job position qualifies for hiring a non-EU worker under the shortage occupation list provided by the Servicio Público de Empleo.
Generated: DETERMINISTIC_326e6e4f35fc2e65
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/shortage-occupations": {
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

class JobPositionVerifier:
    """
    A class to verify if a job position qualifies for hiring a non-EU worker
    under the shortage occupation list provided by the Servicio Público de Empleo in Spain.
    """

    def __init__(self, api_url):
        """
        Initializes the JobPositionVerifier with the provided API URL.

        :param api_url: URL of the API providing the shortage occupation list
        """
        self.api_url = api_url
        self.shortage_occupations = self.fetch_shortage_occupations()

    def fetch_shortage_occupations(self):
        """
        Fetches the shortage occupation list from the API.

        :return: A set of shortage occupations
        :raises Exception: If the API request fails
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raises an error for bad responses
            return set(response.json())   # Assume the API returns a list of occupations
        except requests.RequestException as e:
            raise Exception(f"Error fetching shortage occupations: {e}")

    def is_position_shortage_occupation(self, job_position):
        """
        Checks if the provided job position is in the shortage occupation list.

        :param job_position: The job position to check
        :return: True if the job position is in the shortage list, False otherwise
        """
        return job_position in self.shortage_occupations

def main():
    """
    Main function to execute the job position verification process.
    """
    # URL of the API providing the shortage occupation list
    api_url = "https://api.example.com/shortage-occupations"

    verifier = JobPositionVerifier(api_url)

    # Example job positions to check
    job_positions = [
        "Software Developer",
        "Civil Engineer",
        "Data Scientist"
    ]

    for position in job_positions:
        if verifier.is_position_shortage_occupation(position):
            print(f"The job position '{position}' qualifies for hiring a non-EU worker.")
        else:
            print(f"The job position '{position}' does NOT qualify for hiring a non-EU worker.")

if __name__ == "__main__":
    main()
```
