"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minipepe.digital
Prompt: Generate code to detect whether an SSL certificate is installed for a domain hosted on FASTPANEL and provide steps to install one if missing.
Generated: DETERMINISTIC_19ece1a52a148dbd
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for detecting whether an SSL certificate is installed for a domain and outlining steps to install one if missing. The script uses the `ssl` and `socket` libraries to check the SSL certificate status of a domain.

```python
import socket
import ssl

def check_ssl_certificate(domain, port=443):
    """
    Checks if an SSL certificate is installed for the given domain.

    Parameters:
        domain (str): The domain to check.
        port (int): The port to check SSL on (default: 443).

    Returns:
        bool: True if SSL certificate is present, False otherwise.
    """
    try:
        # Establish a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the certificate
                certificate = ssock.getpeercert()
                if certificate:
                    print(f"SSL certificate detected for {domain}.")
                    return True
                else:
                    print(f"SSL certificate not found for {domain}.")
                    return False
    except ssl.SSLError as e:
        print(f"SSL error for domain {domain}: {e}")
        return False
    except socket.error as e:
        print(f"Socket error for domain {domain}: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred for domain {domain}: {e}")
        return False

def steps_to_install_ssl():
    """
    Prints steps to install an SSL certificate on a domain hosted on FASTPANEL.
    """
    print("\nSteps to install an SSL certificate on FASTPANEL:")
    print("1. Log in to your FASTPANEL account.")
    print("2. Navigate to the 'Domains' section.")
    print("3. Select your domain from the list.")
    print("4. Go to the 'SSL/TLS' section.")
    print("5. Click the option to issue or install an SSL certificate.")
    print("6. Choose 'Let's Encrypt' for a free SSL certificate or upload your own certificate.")
    print("7. Follow the on-screen instructions to complete the installation.")
    print("8. Verify that the SSL certificate is properly installed by re-running this script.")

if __name__ == "__main__":
    # Example domain to check
    domain_to_check = "example.com"

    print(f"Checking SSL certificate status for {domain_to_check}...")
    is_ssl_installed = check_ssl_certificate(domain_to_check)

    if not is_ssl_installed:
        print(f"\nSSL certificate is missing for {domain_to_check}.")
        steps_to_install_ssl()
```

This code checks if an SSL certificate is installed for a given domain and prints steps to install one on FASTPANEL if it's missing. Ensure to replace `example.com` with the actual domain you want to check when running the script.
