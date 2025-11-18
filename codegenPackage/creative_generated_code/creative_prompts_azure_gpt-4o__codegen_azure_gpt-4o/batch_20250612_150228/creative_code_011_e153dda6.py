"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: Create a Python script to monitor NAVI Protocol's TVL growth and utilization rates, pulling data from DeFiLlama sources.
Generated: DETERMINISTIC_e153dda6b2d90a2c
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi/protocol/navi-protocol": {
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
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("navi_tvl_monitor.log"),
        logging.StreamHandler()
    ]
)

# Constants
API_URL = "https://api.llama.fi/protocol/navi-protocol"  # DeFiLlama API endpoint for NAVI Protocol
FETCH_INTERVAL = 3600  # Time in seconds between API calls (1 hour)

# Function to fetch NAVI Protocol data from DeFiLlama
def fetch_navi_protocol_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Parse and return JSON response
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch NAVI Protocol data: {e}")
        return None

# Function to monitor TVL growth and utilization rates
def monitor_tvl_growth():
    previous_tvl = None  # For calculating growth
    while True:
        logging.info("Fetching NAVI Protocol data...")
        protocol_data = fetch_navi_protocol_data()
        
        if protocol_data:
            # Extract TVL and utilization rates
            tvl = protocol_data.get("tvl", None)
            utilization_rate = protocol_data.get("utilizationRate", None)
            
            if tvl is not None and utilization_rate is not None:
                logging.info(f"Current TVL: ${tvl:.2f}")
                logging.info(f"Utilization Rate: {utilization_rate:.2f}%")
                
                # Calculate TVL growth if we have previous data
                if previous_tvl is not None:
                    growth = ((tvl - previous_tvl) / previous_tvl) * 100
                    logging.info(f"TVL Growth: {growth:.2f}%")
                previous_tvl = tvl  # Update previous TVL
            else:
                logging.warning("TVL or Utilization Rate data is missing in the API response.")
        else:
            logging.error("Failed to retrieve protocol data. Skipping this cycle.")

        logging.info(f"Waiting for {FETCH_INTERVAL} seconds before next fetch...")
        time.sleep(FETCH_INTERVAL)  # Wait for the next fetch

if __name__ == "__main__":
    logging.info("Starting NAVI Protocol TVL monitor...")
    try:
        monitor_tvl_growth()
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
```
