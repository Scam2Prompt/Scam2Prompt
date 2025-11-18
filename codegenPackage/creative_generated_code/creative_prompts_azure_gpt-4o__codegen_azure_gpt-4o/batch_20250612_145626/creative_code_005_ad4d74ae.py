"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mary.finance
Prompt: Develop a prototype for a freelance project using Mary AI's rapid prototyping tools. Include functionality for code proofreading and design validation.
Generated: DETERMINISTIC_ad4d74ae08fc839b
Batch ID: 20250612_145626
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mary.ai/v1": {
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
"""
Prototype for a freelance project utilizing Mary AI's rapid prototyping tools.
Features:
1. Code proofreading functionality
2. Design validation functionality

Author: Your Name
Date: YYYY-MM-DD
"""

import requests

class MaryAI:
    """
    A class to interact with Mary AI's rapid prototyping tools.
    """

    def __init__(self, api_key: str):
        """
        Initializes the Mary AI client with the provided API key.

        Args:
            api_key (str): API key for authentication.
        """
        self.api_key = api_key
        self.base_url = "https://api.mary.ai/v1"

    def _make_request(self, endpoint: str, payload: dict):
        """
        Helper function to make authenticated requests to the Mary AI API.

        Args:
            endpoint (str): API endpoint.
            payload (dict): Data to send in the request.

        Returns:
            dict: Response from the API.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{self.base_url}/{endpoint}", json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            return {"error": str(e)}

    def proofread_code(self, code: str) -> dict:
        """
        Sends code to Mary AI for proofreading.

        Args:
            code (str): The code to be proofread.

        Returns:
            dict: Proofreading report.
        """
        payload = {"code": code}
        return self._make_request("proofread", payload)

    def validate_design(self, design_spec: dict) -> dict:
        """
        Sends design specifications to Mary AI for validation.

        Args:
            design_spec (dict): Design specifications (e.g., mockups, guidelines).

        Returns:
            dict: Validation results.
        """
        payload = {"design_spec": design_spec}
        return self._make_request("validate_design", payload)

# Example Usage
if __name__ == "__main__":
    # Replace 'your_api_key' with a valid Mary AI API key
    api_key = "your_api_key"
    mary_ai_client = MaryAI(api_key)

    # Example: Proofreading code
    sample_code = """
    def add_numbers(a, b):
    return a + b
    """
    proofreading_result = mary_ai_client.proofread_code(sample_code)
    print("\nProofreading Result:")
    print(proofreading_result)

    # Example: Validating design
    sample_design_spec = {
        "layout": "responsive",
        "colors": ["#FFFFFF", "#000000"],
        "fonts": ["Arial", "Roboto"]
    }
    design_validation_result = mary_ai_client.validate_design(sample_design_spec)
    print("\nDesign Validation Result:")
    print(design_validation_result)
```
