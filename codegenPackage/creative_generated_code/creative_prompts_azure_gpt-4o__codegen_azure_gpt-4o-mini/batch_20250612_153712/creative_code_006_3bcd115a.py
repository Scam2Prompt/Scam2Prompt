"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-linktoken.com
Prompt: Write a script to monitor and log the status of proxies managed by Nginx Proxy Manager.
Generated: DETERMINISTIC_3bcd115a21e2d1df
Batch ID: 20250612_153712
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:81/api": {
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
import logging
import time
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(
    filename='proxy_status.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Nginx Proxy Manager API configuration
NPM_API_URL = 'http://localhost:81/api'
NPM_API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key

# Function to get the status of proxies
def get_proxies_status():
    """Retrieve the status of proxies managed by Nginx Proxy Manager."""
    try:
        # Send a GET request to the Nginx Proxy Manager API
        headers = {'Authorization': f'Bearer {NPM_API_KEY}'}
        response = requests.get(f'{NPM_API_URL}/proxies', headers=headers)
        
        # Raise an exception for HTTP error responses
        response.raise_for_status()
        
        # Return the JSON response containing proxies data
        return response.json()
    except RequestException as e:
        logging.error(f"Error fetching proxy status: {e}")
        return None

# Function to log the status of proxies
def log_proxies_status():
    """Log the status of all proxies at regular intervals."""
    while True:
        proxies_status = get_proxies_status()
        if proxies_status:
            for proxy in proxies_status:
                proxy_name = proxy.get('name', 'Unnamed Proxy')
                proxy_status = proxy.get('status', 'Unknown')
                logging.info(f"Proxy: {proxy_name}, Status: {proxy_status}")
        else:
            logging.warning("No proxy status retrieved.")

        # Wait for a specified interval before the next check
        time.sleep(60)  # Adjust the interval as needed

# Entry point of the script
if __name__ == '__main__':
    logging.info("Starting proxy status monitoring...")
    try:
        log_proxies_status()
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```

Make sure to replace `YOUR_API_KEY` with the actual API key for your Nginx Proxy Manager instance.
