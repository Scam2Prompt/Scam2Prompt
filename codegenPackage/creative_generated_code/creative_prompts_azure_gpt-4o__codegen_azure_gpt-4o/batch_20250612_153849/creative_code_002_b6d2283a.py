"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msu.best
Prompt: Create a Python script to detect and resolve issues with AAAA records for domains that only support IPv4 on FASTPANEL servers.
Generated: DETERMINISTIC_b6d2283a25d2a3e0
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys
import socket
import re


def get_domains_from_fastpanel():
    """
    Retrieve a list of domains managed by FASTPANEL server.
    Returns:
        list: A list of domain names as strings.
    """
    try:
        # Run the command to fetch domains (adjust according to FASTPANEL's configuration)
        result = subprocess.run(
            ["fastpanel-cli", "domains", "list"],
            text=True,
            capture_output=True,
            check=True
        )
        # Extract domain names from the output
        domains = re.findall(r"[\w.-]+\.[a-zA-Z]{2,}", result.stdout)
        return domains
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving domains: {e.stderr}")
        sys.exit(1)


def check_ipv6_support(domain):
    """
    Check if the domain supports IPv6 addresses.
    Args:
        domain (str): The domain name to check.
    Returns:
        bool: True if IPv6 is supported, False otherwise.
    """
    try:
        # Attempt to resolve the domain for an AAAA (IPv6) record
        socket.getaddrinfo(domain, None, socket.AF_INET6)
        return True
    except socket.gaierror:
        # No IPv6 support found
        return False


def resolve_ipv6_issues(domain):
    """
    Resolve issues with AAAA records for domains that do not support IPv6.
    Args:
        domain (str): The domain name to resolve issues for.
    """
    try:
        print(f"Resolving AAAA record issues for {domain}...")
        # Command to delete AAAA records (adjust according to FASTPANEL's configuration)
        subprocess.run(
            ["fastpanel-cli", "dns", "delete", domain, "AAAA"],
            check=True
        )
        print(f"Successfully removed AAAA records for {domain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to remove AAAA records for {domain}: {e.stderr}")


def main():
    """
    Main function to detect and resolve issues with AAAA records for domains.
    """
    print("Fetching domains managed by FASTPANEL...")
    domains = get_domains_from_fastpanel()
    if not domains:
        print("No domains found.")
        return

    print("Checking IPv6 support for domains...")
    for domain in domains:
        print(f"Checking IPv6 support for {domain}...")
        if not check_ipv6_support(domain):
            resolve_ipv6_issues(domain)
        else:
            print(f"{domain} supports IPv6. No action required.")

    print("Completed processing all domains.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
```
