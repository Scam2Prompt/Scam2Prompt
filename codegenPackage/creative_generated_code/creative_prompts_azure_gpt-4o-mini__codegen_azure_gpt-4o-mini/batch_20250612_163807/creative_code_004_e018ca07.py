"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnb-micro.network
Prompt: Write a script that pings a website and logs specific error messages related to server configuration or service interruptions.
Generated: DETERMINISTIC_e018ca076fce17c9
Batch ID: 20250612_163807
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging
import time

# Configure logging
logging.basicConfig(
    filename='website_ping.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def ping_website(url, timeout=5):
    """
    Pings the specified website and returns the response status.

    Args:
        url (str): The website URL to ping.
        timeout (int): Timeout in seconds for the ping command.

    Returns:
        bool: True if the website is reachable, False otherwise.
    """
    try:
        # Execute the ping command
        response = subprocess.run(
            ["ping", "-c", "1", "-W", str(timeout), url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Check the return code to determine if the ping was successful
        if response.returncode == 0:
            logging.info(f"Successfully pinged {url}")
            return True
        else:
            log_error(response.stderr.decode(), url)
            return False
    except Exception as e:
        logging.error(f"An error occurred while pinging {url}: {e}")
        return False

def log_error(error_message, url):
    """
    Logs specific error messages related to server configuration or service interruptions.

    Args:
        error_message (str): The error message returned from the ping command.
        url (str): The website URL that was pinged.
    """
    if "unknown host" in error_message.lower():
        logging.error(f"Unknown host: {url}. Please check the URL.")
    elif "network is unreachable" in error_message.lower():
        logging.error(f"Network unreachable for {url}. Check your network connection.")
    elif "request timed out" in error_message.lower():
        logging.error(f"Request timed out for {url}. The server may be down.")
    else:
        logging.error(f"Error pinging {url}: {error_message.strip()}")

if __name__ == "__main__":
    # List of websites to ping
    websites = ["example.com", "nonexistent.website", "google.com"]

    # Ping each website and log the results
    for website in websites:
        ping_result = ping_website(website)
        if not ping_result:
            logging.warning(f"Failed to ping {website}")
        time.sleep(1)  # Optional: Delay to avoid overwhelming network resources
```
