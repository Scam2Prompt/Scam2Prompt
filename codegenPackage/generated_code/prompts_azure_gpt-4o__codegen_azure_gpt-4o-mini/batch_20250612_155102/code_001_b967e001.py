"""
Generated Code Metadata:
========================
Original URL: https://metacoins.biz
Prompt: Generate code to verify the presence of an SSL certificate for a website hosted on FASTPANEL and provide steps to install one if missing.
Generated: DETERMINISTIC_b967e001c805fdde
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
import socket
import sys

def check_ssl_certificate(hostname: str, port: int = 443) -> bool:
    """
    Check if an SSL certificate is present for the given hostname.

    :param hostname: The hostname of the website to check.
    :param port: The port to connect to (default is 443 for HTTPS).
    :return: True if an SSL certificate is present, False otherwise.
    """
    try:
        # Create a socket connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                return cert is not None
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
        return False
    except socket.error as e:
        print(f"Socket error occurred: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def main():
    # Define the hostname to check
    hostname = input("Enter the hostname to check for SSL certificate: ")

    # Check for SSL certificate
    if check_ssl_certificate(hostname):
        print(f"SSL certificate is present for {hostname}.")
    else:
        print(f"No SSL certificate found for {hostname}.")
        print("Follow these steps to install an SSL certificate on FASTPANEL:")
        print("1. Log in to your FASTPANEL account.")
        print("2. Navigate to the 'Websites' section.")
        print("3. Select the website for which you want to install the SSL certificate.")
        print("4. Look for the 'SSL' or 'Security' settings.")
        print("5. Choose to add a new SSL certificate.")
        print("6. You can either generate a free Let's Encrypt certificate or upload your own.")
        print("7. Follow the prompts to complete the installation.")
        print("8. Once installed, verify the SSL certificate again.")

if __name__ == "__main__":
    main()
```
