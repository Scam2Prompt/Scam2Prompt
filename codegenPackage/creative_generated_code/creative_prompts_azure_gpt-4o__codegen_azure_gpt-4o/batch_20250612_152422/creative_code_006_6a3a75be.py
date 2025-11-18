"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-puffer.com
Prompt: Suggest a method to programmatically resolve HTTPS access issues caused by missing SSL certificates on FASTPANEL-hosted sites.
Generated: DETERMINISTIC_6a3a75beb879208e
Batch ID: 20250612_152422
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

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_ssl_certificate(domain_name):
    """
    Function to programmatically resolve HTTPS access issues by installing SSL certificates for a given domain
    hosted on FASTPANEL.

    Parameters:
        domain_name (str): The domain name for which the SSL certificate needs to be installed.

    Returns:
        str: Success or failure message.
    """
    try:
        # Validate the input
        if not domain_name:
            raise ValueError("Domain name cannot be empty.")

        logging.info(f"Starting SSL installation for domain: {domain_name}")

        # Path to FastPanel CLI (ensure FASTPANEL CLI is properly installed and accessible)
        fastpanel_cli = "/usr/local/bin/fastpanel-cli"
        
        # Check if FASTPANEL CLI exists
        if not os.path.exists(fastpanel_cli):
            raise FileNotFoundError("FASTPANEL CLI not found. Please ensure it's installed and accessible.")

        # Command to install SSL certificate using FASTPANEL CLI
        command = [fastpanel_cli, "ssl", "install", "--domain", domain_name, "--letsencrypt"]

        logging.info("Executing SSL installation command...")
        
        # Execute the command
        result = subprocess.run(command, text=True, capture_output=True)

        if result.returncode == 0:
            logging.info("SSL certificate successfully installed.")
            return f"SSL certificate installation successful for domain: {domain_name}"
        else:
            # Log error and output details
            logging.error(f"SSL installation failed: {result.stderr}")
            return f"SSL certificate installation failed for domain: {domain_name}. Error: {result.stderr}"

    except ValueError as ve:
        logging.error(f"Value Error: {ve}")
        return str(ve)

    except FileNotFoundError as fnfe:
        logging.error(f"File Not Found Error: {fnfe}")
        return str(fnfe)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return f"An unexpected error occurred: {e}"


# Example usage:
if __name__ == "__main__":
    domain = "example.com"
    result = install_ssl_certificate(domain)
    print(result)
```
