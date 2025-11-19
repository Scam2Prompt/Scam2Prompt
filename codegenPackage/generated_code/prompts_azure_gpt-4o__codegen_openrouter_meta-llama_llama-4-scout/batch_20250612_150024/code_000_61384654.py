"""
Generated Code Metadata:
========================
Original URL: https://bid-notification.bet
Prompt: Write code to check if a domain is correctly pointed to a server using DNS records, including AAAA and A records, as described in FASTPANEL troubleshooting documentation.
Generated: DETERMINISTIC_61384654064025cd
Batch ID: 20250612_150024
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
        dict: A dictionary containing the DNS records for the domain.
    """

    # Initialize an empty dictionary to store DNS records
    dns_records = {}

    try:
        # Query AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        dns_records['AAAA'] = [record.to_text() for record in aaaa_records]

    except dns.resolver.NoAnswer:
        # No AAAA records found
        dns_records['AAAA'] = None

    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' does not exist.")
        return None

    try:
        # Query A records
        a_records = dns.resolver.resolve(domain, 'A')
        dns_records['A'] = [record.to_text() for record in a_records]

    except dns.resolver.NoAnswer:
        # No A records found
        dns_records['A'] = None

    return dns_records


def check_server_reachability(ip_address):
    """
    Check if a server is reachable.

    Args:
        ip_address (str): The IP address of the server.

    Returns:
        bool: True if the server is reachable, False otherwise.
    """

    import socket

    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET6 if ':' in ip_address else socket.AF_INET)

        # Set a timeout of 2 seconds
        sock.settimeout(2)

        # Try to connect to the server
        sock.connect((ip_address, 80))

        # If we reach this point, the server is reachable
        return True

    except (socket.error, OSError):
        # If an error occurs, the server is not reachable
        return False

    finally:
        # Close the socket
        sock.close()


def main():
    domain = input("Enter the domain to check: ")

    dns_records = check_dns_records(domain)

    if dns_records is not None:
        print(f"DNS Records for {domain}:")
        for record_type, records in dns_records.items():
            if records is not None:
                print(f"{record_type}: {', '.join(records)}")
            else:
                print(f"{record_type}: No records found")

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
        print("\nExiting...")
```

You will need to install the `dnspython` library to run this code. You can do this with pip:

```bash
pip install dnspython
```
