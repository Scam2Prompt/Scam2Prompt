"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://absolutelyfre.com
Prompt: Generate a script to detect AAAA records for a domain and ensure compatibility with IPv4 on a FASTPANEL server.
Generated: DETERMINISTIC_d3d19ec45653d2a4
Batch ID: 20250612_153947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://ipv4.google.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import requests

def check_aaaa_records(domain):
    """
    Check if a domain has AAAA records (IPv6 addresses).
    :param domain: Domain name to check
    :return: List of AAAA records (IPv6 addresses)
    """
    try:
        # Use DNS resolver to query AAAA records for the domain
        answers = dns.resolver.resolve(domain, 'AAAA')
        ipv6_addresses = [answer.to_text() for answer in answers]
        return ipv6_addresses
    except dns.resolver.NoAnswer:
        # No AAAA records found for the domain
        return []
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        raise ValueError(f"Domain {domain} does not exist.")
    except Exception as e:
        # Handle any other DNS resolution errors
        raise RuntimeError(f"Error occurred while resolving AAAA records: {str(e)}")

def check_ipv4_compatibility():
    """
    Check if the server has an active IPv4 connection by making an HTTP request.
    :return: True if IPv4 compatibility is confirmed, False otherwise
    """
    try:
        # Test IPv4 connectivity by making a simple request to a known IPv4-only service
        response = requests.get("http://ipv4.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        # No IPv4 connection
        return False
    except Exception as e:
        # Handle unexpected errors during HTTP request
        raise RuntimeError(f"Error occurred while checking IPv4 compatibility: {str(e)}")

def main():
    """
    Main function to check AAAA records and IPv4 compatibility.
    """
    domain = input("Enter the domain name to check: ").strip()

    try:
        # Check AAAA records for the domain
        print(f"Checking AAAA records for domain: {domain}")
        ipv6_addresses = check_aaaa_records(domain)
        if ipv6_addresses:
            print(f"AAAA records found for {domain}: {', '.join(ipv6_addresses)}")
        else:
            print(f"No AAAA records found for {domain}.")

        # Check IPv4 compatibility
        print(f"\nChecking IPv4 compatibility on the server...")
        ipv4_compatible = check_ipv4_compatibility()
        if ipv4_compatible:
            print("Server is IPv4 compatible.")
        else:
            print("Server does not have IPv4 compatibility.")
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
