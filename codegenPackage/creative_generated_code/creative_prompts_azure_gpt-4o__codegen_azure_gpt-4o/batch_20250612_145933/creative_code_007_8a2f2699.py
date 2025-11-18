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
#!/usr/bin/env python3

import socket
import ssl
from datetime import datetime
import argparse
import sys


def check_https_connectivity(domain, port=443):
    """
    Tests HTTPS connectivity and retrieves SSL certificate information.
    :param domain: The domain name to test.
    :param port: The port to connect to (default: 443).
    :return: None
    """
    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                # Get certificate details
                cert = ssl_sock.getpeercert()

                # Check connectivity
                print(f"[SUCCESS] Successfully connected to {domain}:{port} over HTTPS.")

                # Parse SSL certificate details
                subject = dict(x[0] for x in cert['subject'])
                issuer = dict(x[0] for x in cert['issuer'])
                not_before = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
                not_after = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")

                # Output certificate details
                print("\n[SSL CERTIFICATE DETAILS]")
                print(f"  Subject: {subject.get('commonName', 'N/A')}")
                print(f"  Issued By: {issuer.get('commonName', 'N/A')}")
                print(f"  Valid From: {not_before.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"  Valid Until: {not_after.strftime('%Y-%m-%d %H:%M:%S')}")

                # Check expiration status
                if datetime.now() > not_after:
                    print("[WARNING] The SSL certificate has expired!")
                else:
                    days_remaining = (not_after - datetime.now()).days
                    print(f"[INFO] SSL certificate is valid. Days remaining: {days_remaining}")

    except socket.timeout:
        print(f"[ERROR] Connection to {domain}:{port} timed out.")
    except ssl.SSLError as e:
        print(f"[ERROR] SSL error occurred: {e}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Test HTTPS connectivity and SSL certificate status for a domain."
    )
    parser.add_argument(
        "domain",
        type=str,
        help="The domain name to test (e.g., example.com)."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=443,
        help="The port to test (default: 443)."
    )
    args = parser.parse_args()

    # Run the connectivity check
    check_https_connectivity(args.domain, args.port)


if __name__ == "__main__":
    # Ensure the script runs correctly from the command line
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Script interrupted by user.")
        sys.exit(0)
```
