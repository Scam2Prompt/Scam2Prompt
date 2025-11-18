"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bake-4kd.pages.dev
Prompt: Write a tutorial on how to build a "Smart Bundle" affiliate program using Bake's community features and APIs.
Generated: DETERMINISTIC_f209542abd8098e4
Batch ID: 20250612_145711
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.bakeplatform.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://affiliate.yourdomain.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python tutorial code example for creating a "Smart Bundle" affiliate program using APIs. This assumes we’re interfacing with Bake’s APIs (fictional for this example) and community features.

```python
import requests
from typing import List, Dict

# Constants for Bake API
BAKE_API_BASE_URL = "https://api.bakeplatform.com/v1"
API_KEY = "your_api_key_here"  # Replace with your API key
AFFILIATE_BASE_URL = "https://affiliate.yourdomain.com"

# Headers for authenticated API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# Custom exception for API errors
class APIError(Exception):
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

# Function to create a new affiliate program
def create_affiliate_program(name: str, description: str) -> Dict:
    """
    Create a new affiliate program.

    Args:
        name (str): The name of the affiliate program.
        description (str): A brief description of the affiliate program.

    Returns:
        dict: Details of the created affiliate program.

    Raises:
        APIError: If the API call fails.
    """
    url = f"{BAKE_API_BASE_URL}/affiliate-programs"
    payload = {
        "name": name,
        "description": description,
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code != 201:
        raise APIError(f"Failed to create affiliate program: {response.text}", response.status_code)
    return response.json()

# Function to create a new "Smart Bundle"
def create_smart_bundle(name: str, product_ids: List[str], discount: float) -> Dict:
    """
    Create a new smart bundle.

    Args:
        name (str): The name of the bundle.
        product_ids (List[str]): List of product IDs to include in the bundle.
        discount (float): Discount percentage for the bundle.

    Returns:
        dict: Details of the created smart bundle.

    Raises:
        APIError: If the API call fails.
    """
    url = f"{BAKE_API_BASE_URL}/smart-bundles"
    payload = {
        "name": name,
        "products": product_ids,
        "discount": discount,
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code != 201:
        raise APIError(f"Failed to create smart bundle: {response.text}", response.status_code)
    return response.json()

# Function to generate referral links for affiliates
def generate_referral_link(affiliate_id: str, bundle_id: str) -> str:
    """
    Generate a referral link for an affiliate.

    Args:
        affiliate_id (str): The affiliate's ID.
        bundle_id (str): The bundle's ID.

    Returns:
        str: The referral link.

    Raises:
        APIError: If the API call fails.
    """
    return f"{AFFILIATE_BASE_URL}/referral/{affiliate_id}?bundle={bundle_id}"

# Function to assign an affiliate to a program
def assign_affiliate_to_program(affiliate_id: str, program_id: str) -> Dict:
    """
    Assign an affiliate to a specific program.

    Args:
        affiliate_id (str): The affiliate's ID.
        program_id (str): The ID of the affiliate program.

    Returns:
        dict: Response from the server.

    Raises:
        APIError: If the API call fails.
    """
    url = f"{BAKE_API_BASE_URL}/affiliate-programs/{program_id}/affiliates"
    payload = {
        "affiliate_id": affiliate_id,
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code != 200:
        raise APIError(f"Failed to assign affiliate to program: {response.text}", response.status_code)
    return response.json()

# Main function to demonstrate the workflow
def main():
    try:
        # Step 1: Create an affiliate program
        program = create_affiliate_program(
            name="Smart Bundle Program",
            description="A program for promoting smart product bundles.",
        )
        program_id = program["id"]
        print(f"Affiliate Program Created: {program}")

        # Step 2: Create a smart bundle
        bundle = create_smart_bundle(
            name="Ultimate Productivity Bundle",
            product_ids=["prod123", "prod456", "prod789"],
            discount=20.0,  # 20% discount
        )
        bundle_id = bundle["id"]
        print(f"Smart Bundle Created: {bundle}")

        # Step 3: Register an affiliate and assign to the program
        affiliate_id = "affiliate_001"  # Replace with actual affiliate ID
        assignment_response = assign_affiliate_to_program(affiliate_id, program_id)
        print(f"Affiliate Assigned to Program: {assignment_response}")

        # Step 4: Generate a referral link for the affiliate
        referral_link = generate_referral_link(affiliate_id, bundle_id)
        print(f"Referral Link Generated: {referral_link}")

    except APIError as e:
        print(f"An error occurred: {e}")
        if e.status_code:
            print(f"HTTP Status Code: {e.status_code}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```

This code includes:
1. API calls to create an affiliate program, smart bundle, and assign affiliates.
2. Proper error handling with custom exceptions.
3. Comments and clear separation of functionality for readability.

Replace the `your_api_key_here` with your actual Bake API key.
