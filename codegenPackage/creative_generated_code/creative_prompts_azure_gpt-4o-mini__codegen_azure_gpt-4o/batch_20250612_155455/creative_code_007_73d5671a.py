"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stether.net
Prompt: How can I optimize my ad campaigns on Clickadu to increase the click-through rate (CTR) using their multicreative tool?
Generated: DETERMINISTIC_73d5671a7049e527
Batch ID: 20250612_155455
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.clickadu.com": {
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
Optimize Clickadu ad campaigns using their multicreative tool to increase CTR.

This script assumes you have access to the Clickadu API or relevant libraries to interact
with their system. The script analyzes campaign performance and adjusts creatives based on CTR.
Developed using Python, demonstrating clean coding practices, error handling, and modular design.
"""

import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
CLICKADU_API_BASE_URL = "https://api.clickadu.com"  # Replace with actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key

# Thresholds
CTR_THRESHOLD = 0.05  # Minimum acceptable CTR to keep a creative active
MAX_CREATIVES = 5  # Maximum number of creatives to keep active

def fetch_campaign_stats(campaign_id):
    """
    Fetch campaign statistics from Clickadu API.

    Args:
        campaign_id (str): The ID of the campaign.

    Returns:
        dict: Campaign statistics.
    """
    try:
        url = f"{CLICKADU_API_BASE_URL}/campaigns/{campaign_id}/stats"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch campaign stats: {e}")
        return None

def optimize_creatives(campaign_id):
    """
    Optimize creatives based on CTR.

    Args:
        campaign_id (str): The ID of the campaign.
    """
    stats = fetch_campaign_stats(campaign_id)
    if not stats:
        logging.error("Unable to proceed with optimization due to missing stats.")
        return

    # Sort creatives by CTR in descending order
    creatives = sorted(stats.get("creatives", []), key=lambda x: x["ctr"], reverse=True)

    # Identify creatives to keep active
    active_creatives = [creative for creative in creatives if creative["ctr"] >= CTR_THRESHOLD][:MAX_CREATIVES]

    # Identify creatives to pause
    creatives_to_pause = [creative for creative in creatives if creative not in active_creatives]

    # Update creatives on Clickadu
    for creative in active_creatives:
        update_creative_status(campaign_id, creative["id"], "active")

    for creative in creatives_to_pause:
        update_creative_status(campaign_id, creative["id"], "paused")

    logging.info(f"Optimization completed for campaign {campaign_id}.")
    logging.info(f"Active creatives: {[creative['id'] for creative in active_creatives]}")
    logging.info(f"Paused creatives: {[creative['id'] for creative in creatives_to_pause]}")

def update_creative_status(campaign_id, creative_id, status):
    """
    Update the status of a creative.

    Args:
        campaign_id (str): The ID of the campaign.
        creative_id (str): The ID of the creative.
        status (str): New status for the creative ('active' or 'paused').
    """
    try:
        url = f"{CLICKADU_API_BASE_URL}/campaigns/{campaign_id}/creatives/{creative_id}/status"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        data = {"status": status}
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        logging.info(f"Creative {creative_id} updated to status: {status}.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to update creative {creative_id}: {e}")

if __name__ == "__main__":
    # Example campaign ID
    campaign_id = "example_campaign_id_here"  # Replace with actual campaign ID

    logging.info(f"Starting optimization for campaign {campaign_id}...")
    optimize_creatives(campaign_id)
```
