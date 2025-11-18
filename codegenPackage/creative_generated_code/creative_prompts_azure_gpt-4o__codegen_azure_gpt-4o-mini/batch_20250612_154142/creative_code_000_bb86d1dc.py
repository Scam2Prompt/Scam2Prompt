"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: Write Python code to check the eligibility of a GPU for connection to the Aethir decentralized cloud network, referencing the steps outlined in the Aethir documentation.
Generated: DETERMINISTIC_bb86d1dc9dbb4b23
Batch ID: 20250612_154142
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aethir.io/v1/check_gpu": {
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

# Constants for Aethir API
AETHIR_API_URL = "https://api.aethir.io/v1/check_gpu"

class GPUEligibilityChecker:
    def __init__(self, gpu_id):
        """
        Initialize the GPUEligibilityChecker with the provided GPU ID.
        
        :param gpu_id: str - Unique identifier for the GPU
        """
        self.gpu_id = gpu_id

    def check_eligibility(self):
        """
        Check the eligibility of the GPU for connection to the Aethir decentralized cloud network.
        
        :return: dict - A dictionary containing eligibility status and details
        :raises Exception: If there's an error during the API request
        """
        try:
            response = requests.post(AETHIR_API_URL, json={"gpu_id": self.gpu_id})
            response.raise_for_status()  # Raise an error for bad responses
            eligibility_data = response.json()
            return self._parse_response(eligibility_data)
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Raise HTTP errors
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle other request errors

    def _parse_response(self, eligibility_data):
        """
        Parse the response from the Aethir API and return relevant details.
        
        :param eligibility_data: dict - Parsed JSON response from the API
        :return: dict - Detailed eligibility information
        """
        result = {
            "eligible": eligibility_data.get("eligible", False),
            "details": eligibility_data.get("details", "No details available.")
        }
        return result

# Example usage
if __name__ == "__main__":
    gpu_id = "YOUR_GPU_ID"  # Replace with the actual GPU ID
    checker = GPUEligibilityChecker(gpu_id)

    try:
        eligibility_info = checker.check_eligibility()
        print(f"Eligibility Status: {eligibility_info['eligible']}")
        print(f"Details: {eligibility_info['details']}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
