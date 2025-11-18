"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappchainweb.rf.gd
Prompt: Create a script to enable SSL certificates for a website hosted on a platform offering free and simple SSL, like iFastNet hosting.
Generated: DETERMINISTIC_8318687ec3d2ec6e
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import os
from subprocess import run, CalledProcessError

# Constants
DOMAIN_NAME = "yourwebsite.com"  # Replace with your domain name
EMAIL = "admin@yourwebsite.com"  # Replace with your email address
CERTBOT_COMMAND = "certbot"  # Path to Certbot or the command if installed globally

def install_ssl_certificate(domain, email):
    """
    Install SSL certificate using Certbot for the given domain.
    :param domain: The domain name to install the SSL certificate on.
    :param email: The email address for SSL certificate registration.
    """
    print(f"Starting SSL certificate installation for {domain}...")

    try:
        # Run Certbot command to obtain and install SSL certificates
        result = run(
            [CERTBOT_COMMAND, "--nginx", "-d", domain, "--email", email, "--agree-tos", "--non-interactive"],
            check=True,
            capture_output=True,
            text=True
        )
        
        # Output success message
        print("SSL certificate installation successful.")
        print("Certbot output:\n", result.stdout)
    
    except FileNotFoundError:
        print("Error: Certbot is not installed on the system. Please install Certbot and try again.")
    except CalledProcessError as e:
        print("Error: SSL certificate installation failed.")
        print("Certbot error output:\n", e.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ensure environment variables are set or print warnings
    if not DOMAIN_NAME or not EMAIL:
        print("Error: Please configure DOMAIN_NAME and EMAIL constants before running the script.")
    else:
        # Start SSL installation process
        install_ssl_certificate(DOMAIN_NAME, EMAIL)
```

> **Note**: Before running this script, ensure that Certbot is installed on your server and your domain is properly configured to point to your server. Also, replace `DOMAIN_NAME` and `EMAIL` with the appropriate values for your website.
