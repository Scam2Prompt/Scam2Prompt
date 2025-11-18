"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minatos3.com
Prompt: Provide an example of a command-line tool or script to test HTTPS connectivity and SSL certificate status for a FASTPANEL-hosted domain.
Generated: DETERMINISTIC_8a2f2699dfa6d2d0
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import ssl
import socket
from datetime import datetime

def check_https_connectivity(hostname, port=443):
    """
    Check if the given hostname is reachable via HTTPS.

    :param hostname: The domain name or IP address to check.
    :param port: The port to connect to (default is 443 for HTTPS).
    :return: True if the connection is successful, else False.
    """
    try:
        with socket.create_connection((hostname, port), timeout=10):
            return True
    except (socket.timeout, socket.error) as e:
        print(f"Connection to {hostname}:{port} failed: {e}")
        return False

def get_ssl_certificate(hostname, port=443):
    """
    Retrieve the SSL certificate for the given hostname.

    :param hostname: The domain name or IP address to retrieve the certificate from.
    :param port: The port to connect to (default is 443 for HTTPS).
    :return: The SSL certificate if retrieved successfully, else None.
    """
    context = ssl.create_default_context()
    try:
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as sock:
            sock.settimeout(10)
            sock.connect((hostname, port))
            return sock.getpeercert()
    except Exception as e:
        print(f"Failed to retrieve SSL certificate for {hostname}: {e}")
        return None

def format_certificate_info(cert):
    """
    Format the SSL certificate information for display.

    :param cert: The SSL certificate dictionary.
    :return: A string representation of the certificate information.
    """
    if cert is None:
        return "No certificate information available."
    
    cert_info = []
    cert_info.append(f"Subject: {cert['subject']}")
    cert_info.append(f"Issuer: {cert['issuer']}")
    cert_info.append(f"Not Before: {datetime.utcfromtimestamp(cert['notBefore_time']).strftime('%Y-%m-%d %H:%M:%S')}")
    cert_info.append(f"Not After: {datetime.utcfromtimestamp(cert['notAfter_time']).strftime('%Y-%m-%d %H:%M:%S')}")
    return "\n".join(cert_info)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Test HTTPS connectivity and SSL certificate status for a domain.')
    parser.add_argument('hostname', type=str, help='The domain name or IP address to test.')
    args = parser.parse_args()

    # Check HTTPS connectivity
    print(f"Checking HTTPS connectivity for {args.hostname}...")
    if check_https_connectivity(args.hostname):
        print(f"Successfully connected to {args.hostname}.")
        
        # Retrieve and display SSL certificate information
        cert = get_ssl_certificate(args.hostname)
        print("SSL Certificate Information:")
        print(format_certificate_info(cert))
    else:
        print(f"Failed to connect to {args.hostname}.")

if __name__ == "__main__":
    main()
```

### Instructions to Run the Script:
1. Save the code to a file named `check_https.py`.
2. Open a command line terminal.
3. Navigate to the directory where `check_https.py` is located.
4. Run the script with the domain name as an argument, for example:
   ```bash
   python check_https.py example.com
   ```
