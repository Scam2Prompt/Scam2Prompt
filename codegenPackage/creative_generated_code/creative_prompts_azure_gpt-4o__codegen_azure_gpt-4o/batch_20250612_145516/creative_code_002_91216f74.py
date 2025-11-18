"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-lo.com
Prompt: Provide code to detect and resolve issues related to AAAA records when a site only supports IPv4, using FASTPANEL as the server management tool.
Generated: DETERMINISTIC_91216f741c63af99
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import socket
import sys


def get_ipv6_records(domain):
    """
    Retrieve AAAA (IPv6) DNS records for a given domain.

    :param domain: The domain name to query.
    :return: List of IPv6 addresses (AAAA records) or an empty list if none exist.
    """
    try:
        ipv6_records = socket.getaddrinfo(domain, None, socket.AF_INET6)
        return [record[4][0] for record in ipv6_records]
    except socket.gaierror:
        return []


def remove_aaaa_records(domain):
    """
    Remove AAAA (IPv6) DNS records for a domain using FASTPANEL's CLI tool.

    :param domain: The domain name for which to remove AAAA records.
    """
    try:
        # Example of a FASTPANEL CLI command to remove AAAA records (syntax may vary)
        command = ["fastpanel", "dns", "delete-record", domain, "AAAA"]
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        if result.returncode == 0:
            print(f"Successfully removed AAAA records for domain: {domain}")
        else:
            print(f"Failed to remove AAAA records for domain: {domain}. Error: {result.stderr}")
    except FileNotFoundError:
        print("Error: FASTPANEL CLI tool not found. Ensure it is installed and in PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing FASTPANEL CLI command: {e}")


def main():
    """
    Main function to check and resolve AAAA record issues for a domain.
    """
    try:
        # Input: Domain to check and resolve
        domain = input("Enter the domain name to check for AAAA records: ").strip()

        if not domain:
            print("Domain name cannot be empty. Exiting.")
            sys.exit(1)

        print(f"Checking AAAA records for domain: {domain}...")

        # Fetch IPv6 (AAAA) records
        ipv6_records = get_ipv6_records(domain)

        if ipv6_records:
            print(f"Detected AAAA records for domain {domain}: {ipv6_records}")
            print("Since the site only supports IPv4, removing AAAA records...")

            # Remove AAAA records
            remove_aaaa_records(domain)
        else:
            print(f"No AAAA records found for domain {domain}. No action required.")

    except KeyboardInterrupt:
        print("\nOperation canceled by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
