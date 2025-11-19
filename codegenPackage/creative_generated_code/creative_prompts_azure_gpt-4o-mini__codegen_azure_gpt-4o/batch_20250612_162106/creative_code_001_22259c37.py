"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paypalreferralcode.com
Prompt: Write a Python script that integrates with PayPal's referral system to track referrals and earnings.
Generated: DETERMINISTIC_22259c374c8a082a
Batch ID: 20250612_162106
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api-m.paypal.com": {
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
PayPal Referral Tracker Script
This Python script integrates with PayPal's referral system to track referrals and earnings. 
Ensure you have proper API credentials before using this script.
"""

import requests
import logging
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("paypal_referral_tracker.log"),
        logging.StreamHandler()
    ]
)

# PayPal API credentials and endpoint
PAYPAL_API_BASE_URL = "https://api-m.paypal.com"
CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")  # Stored in .env file
CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")  # Stored in .env file

# Function to get PayPal API access token
def get_access_token():
    """
    Obtain access token from PayPal API.
    Returns:
        str: Access token for PayPal API.
    Raises:
        Exception: If the token retrieval fails.
    """
    url = f"{PAYPAL_API_BASE_URL}/v1/oauth2/token"
    headers = {"Accept": "application/json", "Accept-Language": "en_US"}
    data = {"grant_type": "client_credentials"}

    try:
        response = requests.post(url, headers=headers, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
        response.raise_for_status()  # Raise an exception for HTTP errors
        token_data = response.json()
        return token_data["access_token"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve access token: {e}")
        raise Exception("Could not retrieve PayPal access token.") from e

# Function to retrieve referral data
def get_referrals(access_token):
    """
    Fetch referral data from PayPal API.
    Args:
        access_token (str): Access token for PayPal API.
    Returns:
        list: List of referral objects.
    Raises:
        Exception: If the referral retrieval fails.
    """
    url = f"{PAYPAL_API_BASE_URL}/v1/marketing/referrals"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        referrals_data = response.json()
        return referrals_data.get("referrals", [])
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve referrals: {e}")
        raise Exception("Could not retrieve referral data.") from e

# Function to calculate total earnings from referrals
def calculate_total_earnings(referrals):
    """
    Calculate total earnings from referral data.
    Args:
        referrals (list): List of referral objects.
    Returns:
        float: Total earnings from referrals.
    """
    total_earnings = 0.0 

    for referral in referrals:
        earnings = referral.get("earnings", 0.0)
        total_earnings += earnings
    return total_earnings

# Main function
def main():
    """
    Main function to track PayPal referrals and earnings.
    """
    try:
        logging.info("Starting PayPal referral tracking...")
        
        # Step 1: Authenticate and get access token
        access_token = get_access_token()
        logging.info("Successfully retrieved access token.")

        # Step 2: Retrieve referral data
        referrals = get_referrals(access_token)
        logging.info(f"Retrieved {len(referrals)} referrals.")

        # Step 3: Calculate total earnings
        total_earnings = calculate_total_earnings(referrals)
        logging.info(f"Total earnings from referrals: ${total_earnings:.2f}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
