"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Explain how to set up cron jobs for automated MailerLite data fetching as indicated in the `cron_jobs` directory.
Generated: DETERMINISTIC_22bb279635ba5eb8
Batch ID: 20250612_162535
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mailerlite.com/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
Script to set up a cron job for automated MailerLite data fetching.
Place this script in the `cron_jobs` directory and configure the cron job to run it periodically.
"""

import os
import requests
import logging
from datetime import datetime

# Configure logging
LOG_FILE = os.path.join(os.path.dirname(__file__), "mailerlite_fetch.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# MailerLite API configuration
API_KEY = os.getenv("MAILERLITE_API_KEY")  # Ensure the API key is set in environment variables
BASE_URL = "https://api.mailerlite.com/api/v2"

# Output directory for fetched data
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Create the directory if it doesn't exist

def fetch_mailerlite_data(endpoint):
    """
    Fetch data from the MailerLite API.

    Args:
        endpoint (str): The API endpoint to fetch data from.

    Returns:
        dict: The JSON response from the API.
    """
    url = f"{BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch data from {endpoint}: {e}")
        return None

def save_data_to_file(data, filename):
    """
    Save data to a file in the output directory.

    Args:
        data (dict): The data to save.
        filename (str): The name of the file to save the data to.
    """
    try:
        file_path = os.path.join(OUTPUT_DIR, filename)
        with open(file_path, "w") as file:
            file.write(data)
        logging.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save data to {filename}: {e}")

def main():
    """
    Main function to fetch MailerLite data and save it locally.
    """
    if not API_KEY:
        logging.error("MailerLite API key is not set. Please set the MAILERLITE_API_KEY environment variable.")
        return

    logging.info("Starting MailerLite data fetch...")

    # Example: Fetch subscribers data
    endpoint = "subscribers"
    data = fetch_mailerlite_data(endpoint)

    if data:
        # Save the fetched data to a file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"subscribers_{timestamp}.json"
        save_data_to_file(data, filename)

    logging.info("MailerLite data fetch completed.")

if __name__ == "__main__":
    main()
```

### Cron Job Setup
To set up the cron job, add the following line to your crontab file (`crontab -e`):

```bash
# Run the MailerLite data fetch script every day at midnight
0 0 * * * /usr/bin/python3 /path/to/cron_jobs/mailerlite_fetch.py
```

Ensure the script has execute permissions:

```bash
chmod +x /path/to/cron_jobs/mailerlite_fetch.py
```
