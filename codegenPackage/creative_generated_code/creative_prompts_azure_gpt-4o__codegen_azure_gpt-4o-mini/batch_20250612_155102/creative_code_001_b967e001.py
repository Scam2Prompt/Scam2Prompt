"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.biz
Prompt: Generate code to verify the presence of an SSL certificate for a website hosted on FASTPANEL and provide steps to install one if missing.
Generated: DETERMINISTIC_b967e001c805fdde
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
import sys

def check_ssl_certificate(hostname, port=443):
    """
    Check if an SSL certificate is present for the given hostname and port.

    :param hostname: The hostname to check for an SSL certificate.
    :param port: The port to connect to (default is 443 for HTTPS).
    :return: Tuple (bool, str) indicating the presence of SSL certificate and the certificate details or error message.
    """
    try:
        # Create a connection to the hostname and port.
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the SSL certificate
                ssl_info = ssock.getpeercert()
                return True, ssl_info
    except Exception as e:
        # Handle exceptions and return an error message.
        return False, str(e)

def install_ssl_certificate(hostname):
    """
    Provide steps to install an SSL certificate if missing.

    :param hostname: The hostname for which to install the SSL certificate.
    """
    print(f"\nTo install an SSL certificate for {hostname}, follow these steps:")
    print("1. Log in to your FASTPANEL dashboard.")
    print("2. Navigate to the 'Websites' section.")
    print("3. Find your domain and click on 'Manage'.")
    print("4. Go to the 'SSL' settings.")
    print("5. Choose 'Get Free SSL' or upload your own certificate.")
    print("6. Follow the prompts to complete the installation.")
    print("7. Restart your web server to apply the changes.")

def main():
    """
    Main function to check for SSL certificate presence and provide instructions if missing.
    """
    if len(sys.argv) != 2:
        print("Usage: python check_ssl.py <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]
    has_certificate, result = check_ssl_certificate(hostname)

    if has_certificate:
        print(f"SSL certificate is present for {hostname}.")
        print("Certificate details:", result)
    else:
        print(f"No SSL certificate found for {hostname}. Error: {result}")
        install_ssl_certificate(hostname)

if __name__ == "__main__":
    main()
```

To run the code, save it to a file named `check_ssl.py` and execute it from the command line with the hostname as an argument:

```
python check_ssl.py example.com
```
