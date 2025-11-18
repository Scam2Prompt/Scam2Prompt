"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x1111111111.icu
Prompt: Write a script to log and report common server configuration errors, such as missing SSL certificates or incorrect domain pointing, tailored for FASTPANEL hosting setups.
Generated: DETERMINISTIC_7f954df59b6df00d
Batch ID: 20250612_154207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fastpanel.example.com/domains": {
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
import os
import logging
import socket
import ssl
import requests

# Configure logging
logging.basicConfig(
    filename='server_config_errors.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_ssl_certificate(domain):
    """
    Check if the domain has a valid SSL certificate.
    
    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if SSL certificate is valid, False otherwise.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                certificate = ssock.getpeercert()
                if certificate:
                    logging.info(f"SSL certificate is present for {domain}.")
                    return True
                else:
                    logging.warning(f"SSL certificate is missing for {domain}.")
                    return False
    except Exception as e:
        logging.error(f"Error checking SSL certificate for {domain}: {str(e)}")
        return False


def check_domain_pointing(domain, expected_ip):
    """
    Check if the domain is pointing to the correct IP address.

    Args:
        domain (str): The domain to check.
        expected_ip (str): The expected IP address.

    Returns:
        bool: True if domain points to correct IP, False otherwise.
    """
    try:
        resolved_ip = socket.gethostbyname(domain)
        if resolved_ip == expected_ip:
            logging.info(f"Domain {domain} is correctly pointed to {expected_ip}.")
            return True
        else:
            logging.warning(f"Domain {domain} is incorrectly pointed to {resolved_ip} instead of {expected_ip}.")
            return False
    except Exception as e:
        logging.error(f"Error checking domain pointing for {domain}: {str(e)}")
        return False


def fetch_domains_from_fastpanel():
    """
    Fetch domain list from FASTPANEL API.

    Returns:
        list: List of domain dictionaries with domain names and expected IPs.
    """
    try:
        # Example API request to FASTPANEL (replace with actual API details)
        api_url = "https://api.fastpanel.example.com/domains"
        api_key = "your_api_key_here"  # Replace with your API key
        
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise error for HTTP issues

        domains = response.json()
        logging.info("Successfully fetched domain list from FASTPANEL.")
        return domains
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching domain list from FASTPANEL: {str(e)}")
        return []


def main():
    """
    Main function to check server configuration errors.
    """
    logging.info("Starting server configuration error checks.")

    domains = fetch_domains_from_fastpanel()

    if not domains:
        logging.warning("No domains fetched. Exiting.")
        return

    for domain_data in domains:
        domain_name = domain_data.get("domain_name")
        expected_ip = domain_data.get("expected_ip")

        if not domain_name or not expected_ip:
            logging.warning(f"Invalid domain data: {domain_data}")
            continue

        # Check SSL certificate
        check_ssl_certificate(domain_name)

        # Check domain pointing
        check_domain_pointing(domain_name, expected_ip)

    logging.info("Server configuration error checks completed.")


if __name__ == "__main__":
    main()
```
