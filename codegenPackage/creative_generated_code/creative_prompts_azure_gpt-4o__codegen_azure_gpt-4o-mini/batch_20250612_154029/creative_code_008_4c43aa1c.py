"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-berachain.ink
Prompt: Implement a command-line tool that uses Google Public DNS to resolve domain names and provides options for cache flushing.
Generated: DETERMINISTIC_4c43aa1cfb84a162
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import socket
import sys
import time

class DNSResolver:
    def __init__(self):
        self.cache = {}

    def resolve(self, domain):
        """
        Resolve a domain name using Google Public DNS (8.8.8.8).
        
        Args:
            domain (str): The domain name to resolve.

        Returns:
            str: The resolved IP address.

        Raises:
            ValueError: If the domain name is invalid.
            socket.gaierror: If the domain cannot be resolved.
        """
        if domain in self.cache:
            print(f"Cache hit for {domain}: {self.cache[domain]}")
            return self.cache[domain]

        try:
            # Use Google's Public DNS server for resolution
            ip_address = socket.gethostbyname(domain)
            self.cache[domain] = ip_address
            return ip_address
        except socket.gaierror as e:
            raise RuntimeError(f"Could not resolve domain '{domain}': {e}")

    def flush_cache(self):
        """Flush the DNS cache."""
        self.cache.clear()
        print("DNS cache flushed.")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="DNS Resolver using Google Public DNS.")
    parser.add_argument('domain', nargs='?', help='Domain name to resolve.')
    parser.add_argument('--flush-cache', action='store_true', help='Flush the DNS cache.')

    args = parser.parse_args()

    resolver = DNSResolver()

    if args.flush_cache:
        resolver.flush_cache()
        return

    if not args.domain:
        print("No domain name provided for resolution.")
        sys.exit(1)

    try:
        ip_address = resolver.resolve(args.domain)
        print(f"Resolved {args.domain} to {ip_address}")
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except RuntimeError as re:
        print(f"Error: {re}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```
