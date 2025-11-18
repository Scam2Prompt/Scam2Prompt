"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ispot.cc
Prompt: Recommend libraries or APIs for monitoring DNS changes and detecting propagation issues for a domain.
Generated: DETERMINISTIC_5dae2f2242972285
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s an example implementation in Python using the `dnspython` library for DNS monitoring, along with best practices and clear documentation:

```python
"""
dns_monitor.py

A script to monitor DNS changes and detect propagation issues for a domain.
It uses the dnspython library for querying DNS records.

Requirements:
    - dnspython library (install via pip: `pip install dnspython`)

Author: [Your Name]
"""

import dns.resolver
import dns.exception
import time

# Configurations
DOMAIN = "example.com"  # Replace with the domain to monitor
RECORD_TYPE = "A"       # DNS record type to monitor (e.g., "A", "MX", "NS")
MONITOR_INTERVAL = 60   # Time interval (in seconds) between checks
MAX_RETRIES = 3         # Maximum retries for DNS queries

# Previous DNS record values cache
dns_cache = {}


def fetch_dns_records(domain: str, record_type: str):
    """
    Fetch DNS records for the given domain and record type.
    
    Args:
        domain (str): The domain name to query.
        record_type (str): The type of DNS record to query (e.g., "A", "MX", "NS").

    Returns:
        list: A list of records fetched from DNS.

    Raises:
        dns.exception.DNSException: If there is an error during the DNS query.
    """
    try:
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(domain, record_type)
        return [answer.to_text() for answer in answers]
    except dns.exception.DNSException as e:
        raise e


def monitor_dns_changes(domain: str, record_type: str):
    """
    Monitor DNS changes for the given domain and record type.
    Compares the current DNS records with previously fetched records.

    Args:
        domain (str): The domain name to monitor.
        record_type (str): The type of DNS record to monitor.

    Returns:
        None
    """
    global dns_cache

    try:
        # Fetch current DNS records
        current_records = fetch_dns_records(domain, record_type)
    except dns.exception.DNSException as e:
        print(f"[ERROR] Failed to fetch DNS records: {e}")
        return

    # Compare with cached records
    if domain not in dns_cache or dns_cache[domain] != current_records:
        print(f"[INFO] DNS records changed for {domain} ({record_type}):")
        print(f"Previous records: {dns_cache.get(domain, 'None')}")
        print(f"Current records: {current_records}")
        dns_cache[domain] = current_records  # Update the cache
    else:
        print(f"[INFO] No changes detected for {domain} ({record_type}).")


def main():
    """
    Main function to start DNS monitoring.
    Runs the monitoring loop indefinitely at the configured interval.

    Args:
        None

    Returns:
        None
    """
    print(f"Starting DNS monitoring for {DOMAIN} ({RECORD_TYPE})...")
    while True:
        try:
            monitor_dns_changes(DOMAIN, RECORD_TYPE)
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")
        
        # Wait for the configured interval before checking again
        time.sleep(MONITOR_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] DNS monitoring stopped by user.")
```

### Installation Instructions
1. Install the required library:
   ```bash
   pip install dnspython
   ```
2. Run the script:
   ```bash
   python dns_monitor.py
   ```

Ensure to replace the values of `DOMAIN` and `RECORD_TYPE` with your desired domain and record type. This script can be extended further for more advanced monitoring needs.
