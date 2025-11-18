"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepe.club
Prompt: Develop a program that interacts with Google Public DNS to resolve multiple domain names and caches the results locally.
Generated: DETERMINISTIC_a552f9bcdae709bf
Batch ID: 20250612_153655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import pickle
import os
import time

# Constants
CACHE_FILE = "dns_cache.pkl"
CACHE_EXPIRY_SECONDS = 3600  # Cache expires in 1 hour

def load_cache():
    """
    Load DNS cache from a file.
    """
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error loading cache file: {e}")
    return {}

def save_cache(cache):
    """
    Save DNS cache to a file.
    """
    try:
        with open(CACHE_FILE, "wb") as f:
            pickle.dump(cache, f)
    except Exception as e:
        print(f"Error saving cache file: {e}")

def resolve_domain(domain, cache):
    """
    Resolve the IP address of a domain using Google Public DNS and cache the result.
    """
    current_time = time.time()

    # Check cache
    if domain in cache and current_time - cache[domain]['timestamp'] < CACHE_EXPIRY_SECONDS:
        return cache[domain]['ip']

    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Google Public DNS
        answer = resolver.resolve(domain)
        ip_address = answer[0].to_text()

        # Update cache
        cache[domain] = {'ip': ip_address, 'timestamp': current_time}
        save_cache(cache)
        return ip_address
    except (dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoAnswer) as e:
        print(f"Failed to resolve domain {domain}: {e}")
    except Exception as e:
        print(f"Unexpected error while resolving {domain}: {e}")
    return None

def main():
    """
    Main function to resolve and cache domain names.
    """
    domains = [
        "example.com",
        "google.com",
        "nonexistent.domain"
    ]

    # Load existing cache
    dns_cache = load_cache()

    for domain in domains:
        ip = resolve_domain(domain, dns_cache)
        if ip:
            print(f"{domain} -> {ip}")
        else:
            print(f"Failed to resolve {domain}")

if __name__ == "__main__":
    main()
```
