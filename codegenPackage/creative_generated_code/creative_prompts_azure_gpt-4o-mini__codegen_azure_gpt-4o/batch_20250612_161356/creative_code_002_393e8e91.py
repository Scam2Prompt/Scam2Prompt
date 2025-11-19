"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://revs-rmrk.shop
Prompt: What API can I use to monitor domain status and prevent suspension issues?
Generated: DETERMINISTIC_393e8e9128dc9824
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script using the `whois` library to monitor domain status. Note that you need to install the `whois` Python library before running this code (`pip install python-whois`). Additionally, this example includes error handling and logging for production readiness.

```python
import whois
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    filename='domain_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_domain_status(domain_name: str):
    """
    Check the status of a domain and log issues like expiration warnings.
    
    Args:
        domain_name (str): The domain name to check (e.g., "example.com").
        
    Returns:
        dict: A dictionary containing domain information like expiration status.
    """
    try:
        # Fetch domain information using the whois library
        domain_info = whois.whois(domain_name)
        
        # Extract expiration date
        expiration_date = domain_info.expiration_date
        
        # Handle multiple expiration dates (e.g., for multiple registrars)
        if isinstance(expiration_date, list):
            expiration_date = min(expiration_date)
        
        # Check if expiration date is valid
        if expiration_date is None:
            logging.error(f"Unable to retrieve expiration date for domain: {domain_name}")
            return {"status": "error", "message": "Expiration date not found."}
        
        # Calculate the time left until expiration
        days_until_expiration = (expiration_date - datetime.now()).days
        if days_until_expiration < 0:
            logging.warning(f"Domain {domain_name} has already expired on {expiration_date}.")
            return {"status": "expired", "expiration_date": expiration_date}
        elif days_until_expiration <= 30:
            logging.warning(f"Domain {domain_name} is expiring soon ({expiration_date}). Only {days_until_expiration} days left.")
            return {"status": "warning", "days_until_expiration": days_until_expiration, "expiration_date": expiration_date}
        
        logging.info(f"Domain {domain_name} is active. Expiration date: {expiration_date}.")
        return {"status": "active", "days_until_expiration": days_until_expiration, "expiration_date": expiration_date}
    
    except Exception as e:
        logging.error(f"An error occurred while checking the domain {domain_name}: {str(e)}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # Example of usage: Replace with your domain name
    domain_to_check = "example.com"
    result = check_domain_status(domain_to_check)
    print(result)
```

### Requirements:
Install the `python-whois` library by running:
```bash
pip install python-whois
```

This script is designed for production use, complete with logging to track domain statuses and error handling for robustness.
