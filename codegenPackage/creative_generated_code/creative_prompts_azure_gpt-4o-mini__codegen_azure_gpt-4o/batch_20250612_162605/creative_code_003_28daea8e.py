"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethegas.in
Prompt: Explain the difference between AAAA and IPv4 records and how they affect website accessibility.
Generated: DETERMINISTIC_28daea8e0e598e3c
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that explains the difference between AAAA (IPv6) and IPv4 records and how they affect website accessibility. It retrieves DNS records for a domain and checks their presence.

```python
import dns.resolver

def get_dns_records(domain):
    """
    Fetches and displays the IPv4 and IPv6 (AAAA) DNS records for the given domain.

    Args:
        domain (str): The domain name to query.

    Returns:
        dict: A dictionary containing IPv4 and IPv6 records.
    """
    dns_records = {"IPv4": [], "IPv6": []}

    try:
        # Query for A (IPv4) records
        a_records = dns.resolver.resolve(domain, 'A')
        dns_records["IPv4"] = [record.to_text() for record in a_records]
    except dns.resolver.NoAnswer:
        print(f"No IPv4 (A) records found for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
        return dns_records
    except Exception as e:
        print(f"An error occurred while fetching IPv4 (A) records: {e}")

    try:
        # Query for AAAA (IPv6) records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        dns_records["IPv6"] = [record.to_text() for record in aaaa_records]
    except dns.resolver.NoAnswer:
        print(f"No IPv6 (AAAA) records found for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
        return dns_records
    except Exception as e:
        print(f"An error occurred while fetching IPv6 (AAAA) records: {e}")

    return dns_records


def main():
    """
    Entry point for the script. Prompts the user for a domain name and fetches its DNS records.
    """
    domain = input("Enter the domain name to check DNS records: ").strip()

    if not domain:
        print("Invalid input. Please enter a valid domain name.")
        return

    print(f"\nFetching DNS records for {domain}...\n")
    records = get_dns_records(domain)

    print("Results:")
    print(f"IPv4 Records: {', '.join(records['IPv4']) if records['IPv4'] else 'None'}")
    print(f"IPv6 Records: {', '.join(records['IPv6']) if records['IPv6'] else 'None'}")

    print("\nImpact on Website Accessibility:")
    if records["IPv4"] and records["IPv6"]:
        print("The website is accessible via both IPv4 and IPv6, ensuring maximum compatibility.")
    elif records["IPv4"]:
        print("The website is accessible only via IPv4. Users with IPv6-only connections may face issues.")
    elif records["IPv6"]:
        print("The website is accessible only via IPv6. Users with IPv4-only connections may face issues.")
    else:
        print("The website has no DNS records for IPv4 or IPv6, making it inaccessible.")


if __name__ == "__main__":
    main()
```

### Key Features of the Code:
- **IPv4 Records**: Queried with DNS `A` records.
- **IPv6 Records**: Queried with DNS `AAAA` records.
- **Error Handling**: Handles domain non-existence (`NXDOMAIN`), no answer (`NoAnswer`), and other exceptions gracefully.
- **Accessibility Explanation**: Provides insights based on the presence of DNS records.

To execute this code, you need to install the `dnspython` library. You can install it using:
```bash
pip install dnspython
```
