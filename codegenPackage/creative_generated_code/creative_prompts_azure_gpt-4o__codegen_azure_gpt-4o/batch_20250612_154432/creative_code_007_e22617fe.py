"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3rdandtaylor.com
Prompt: Generate code to integrate marketing and sales systems for seamless data sharing and improved efficiency, following the "Well integrated marketing and sales systems" approach mentioned by 3rd & Taylor.
Generated: DETERMINISTIC_e22617fe91099a91
Batch ID: 20250612_154432
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.marketing-system.com/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.sales-system.com/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a Python-based implementation to integrate marketing and sales systems for seamless data sharing using REST APIs. The code assumes the existence of APIs for both systems and handles data synchronization.

```python
import requests
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for marketing and sales API endpoints
MARKETING_API_URL = "https://api.marketing-system.com/data"
SALES_API_URL = "https://api.sales-system.com/data"

# API authentication tokens (Replace with actual tokens)
MARKETING_API_TOKEN = "your_marketing_api_token"
SALES_API_TOKEN = "your_sales_api_token"

# Define headers for requests
MARKETING_HEADERS = {
    "Authorization": f"Bearer {MARKETING_API_TOKEN}",
    "Content-Type": "application/json"
}
SALES_HEADERS = {
    "Authorization": f"Bearer {SALES_API_TOKEN}",
    "Content-Type": "application/json"
}

def fetch_marketing_data(since_time):
    """
    Fetch recent marketing data from the marketing system API.
    
    Args:
        since_time (str): ISO 8601 string representing the time to fetch data since.
        
    Returns:
        list: A list of marketing data, or an empty list if no data is fetched.
    """
    try:
        response = requests.get(f"{MARKETING_API_URL}?since={since_time}", headers=MARKETING_HEADERS)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.RequestException as e:
        logging.error(f"Failed to fetch marketing data: {e}")
        return []

def sync_data_to_sales(data):
    """
    Sync marketing data to the sales system API.
    
    Args:
        data (list): A list of marketing data to sync.
        
    Returns:
        bool: True if sync is successful, False otherwise.
    """
    try:
        response = requests.post(SALES_API_URL, json={"data": data}, headers=SALES_HEADERS)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        logging.error(f"Failed to sync data to sales system: {e}")
        return False

def synchronize_marketing_and_sales():
    """
    Main function to synchronize marketing and sales systems for seamless data sharing.
    Fetches recent marketing data and pushes it to the sales system.
    """
    # Calculate the time range (e.g., last 24 hours)
    since_time = (datetime.utcnow() - timedelta(days=1)).isoformat() + "Z"
    logging.info(f"Fetching marketing data since {since_time}...")
    
    # Fetch marketing data
    marketing_data = fetch_marketing_data(since_time)
    if not marketing_data:
        logging.info("No new marketing data to sync.")
        return
    
    logging.info(f"Fetched {len(marketing_data)} records from the marketing system.")
    
    # Sync data to sales system
    logging.info("Syncing data to sales system...")
    success = sync_data_to_sales(marketing_data)
    if success:
        logging.info("Data synced successfully to sales system.")
    else:
        logging.error("Failed to sync data to sales system.")

if __name__ == "__main__":
    logging.info("Starting marketing and sales system integration...")
    synchronize_marketing_and_sales()
    logging.info("Integration process completed.")
```

### Key Features of the Code:
- **Error Handling:** Ensures robust handling of API errors using `try-except` blocks.
- **Logging:** Logs key actions for traceability and debugging.
- **Production-Ready:** Includes authentication tokens, headers, and datetime handling.
- **Scalable:** Easily extendable to include additional integrations or data transformations.
