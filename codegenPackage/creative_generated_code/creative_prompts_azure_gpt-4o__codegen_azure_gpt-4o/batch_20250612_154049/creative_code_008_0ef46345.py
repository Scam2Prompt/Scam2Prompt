"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-yearnfinance.com
Prompt: Write a script to analyze the impact of communal governance in Yearn Finance by retrieving voting data and user participation metrics.
Generated: DETERMINISTIC_0ef46345a8c1d36e
Batch ID: 20250612_154049
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.yearn.finance/v1": {
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("yearn_analysis.log"), logging.StreamHandler()]
)

# Constants
YEARN_API_BASE_URL = "https://api.yearn.finance/v1"
VOTING_ENDPOINT = f"{YEARN_API_BASE_URL}/governance/proposals"
PARTICIPATION_ENDPOINT = f"{YEARN_API_BASE_URL}/governance/user_participation"

# Error messages
ERROR_FETCHING_DATA = "An error occurred while fetching data from the Yearn API."

def fetch_data(endpoint: str) -> dict:
    """
    Fetch data from the specified Yearn Finance API endpoint.

    :param endpoint: API endpoint to retrieve data from.
    :return: Dictionary containing the response data.
    """
    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"{ERROR_FETCHING_DATA}: {str(e)}")
        return {}

def analyze_voting_data(voting_data: list) -> dict:
    """
    Analyze voting data to determine proposal outcomes and participation rates.

    :param voting_data: List of proposals retrieved from the Yearn API.
    :return: Dictionary containing analysis results.
    """
    total_proposals = len(voting_data)
    passed_proposals = sum(1 for proposal in voting_data if proposal.get('status') == 'passed')
    failed_proposals = total_proposals - passed_proposals

    return {
        "total_proposals": total_proposals,
        "passed_proposals": passed_proposals,
        "failed_proposals": failed_proposals
    }

def analyze_user_participation(participation_data: list) -> dict:
    """
    Analyze user participation metrics.

    :param participation_data: List of user participation records.
    :return: Dictionary with participation statistics.
    """
    total_users = len(participation_data)
    active_users = sum(1 for user in participation_data if user.get('votes') > 0)
    inactive_users = total_users - active_users

    return {
        "total_users": total_users,
        "active_users": active_users,
        "inactive_users": inactive_users
    }

def main():
    """
    Main function to retrieve and analyze communal governance data from Yearn Finance.
    """
    logging.info("Fetching voting data from Yearn Finance...")
    voting_data = fetch_data(VOTING_ENDPOINT)

    if not voting_data:
        logging.error("Failed to retrieve voting data. Exiting.")
        return

    logging.info("Fetching user participation data from Yearn Finance...")
    participation_data = fetch_data(PARTICIPATION_ENDPOINT)

    if not participation_data:
        logging.error("Failed to retrieve user participation data. Exiting.")
        return

    logging.info("Analyzing voting data...")
    voting_analysis = analyze_voting_data(voting_data)
    logging.info(f"Voting Analysis Results: {json.dumps(voting_analysis, indent=2)}")

    logging.info("Analyzing user participation data...")
    participation_analysis = analyze_user_participation(participation_data)
    logging.info(f"User Participation Analysis Results: {json.dumps(participation_analysis, indent=2)}")

    logging.info("Analysis complete. Results written to log.")

if __name__ == "__main__":
    main()
```
