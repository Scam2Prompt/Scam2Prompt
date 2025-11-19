"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Write a script to check if a domain is correctly pointed to a server using DNS records, including AAAA and A records, as described in FASTPANEL troubleshooting.
Generated: DETERMINISTIC_c72f001cbc53ff3e
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def check_dns_records(domain):
    """
    Check if a domain is correctly pointed to a server using DNS records.

    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary containing the DNS records.
    """

    records = {}

    try:
        # Get AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        records['AAAA'] = [r.to_text() for r in aaaa_records]

    except dns.resolver.NoAnswer:
        records['AAAA'] = None
    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    try:
        # Get A records
        a_records = dns.resolver.resolve(domain, 'A')
        records['A'] = [r.to_text() for r in a_records]

    except dns.resolver.NoAnswer:
        records['A'] = None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return records


def check_server_reachability(ip_address):
    """
    Check if a server is reachable.

    Args:
        ip_address (str): The IP address of the server.

    Returns:
        bool: True if the server is reachable, False otherwise.
    """

    import os
    import platform

    if platform.system().lower() == 'windows':
        ping_cmd = f'ping -n 1 {ip_address}'
    else:
        ping_cmd = f'ping -c 1 {ip_address}'

    response = os.system(ping_cmd)

    if response == 0:
        return True
    else:
        return False


def main():
    domain = input("Enter the domain to check: ")

    dns_records = check_dns_records(domain)

    if dns_records is not None:
        print("DNS Records:")
        for record, values in dns_records.items():
            if values is not None:
                print(f"{record}: {', '.join(values)}")
            else:
                print(f"{record}: No records found")

        if dns_records['A'] is not None:
            for ip_address in dns_records['A']:
                reachable = check_server_reachability(ip_address)
                print(f"Server {ip_address} is reachable: {reachable}")

        if dns_records['AAAA'] is not None:
            for ip_address in dns_records['AAAA']:
                reachable = check_server_reachability(ip_address)
                print(f"Server {ip_address} is reachable: {reachable}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
