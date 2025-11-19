"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://absolutelyfre.com
Prompt: How do I configure my domain to work with IPv4 on FASTPANEL if it currently has an AAAA record?
Generated: DETERMINISTIC_6874ecc2d3c33039
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import dns.update
import dns.query
import dns.exception

# Configuration
DOMAIN_NAME = 'yourdomain.com'  # Replace with your actual domain
DNS_SERVER = 'your.dns.server.ip'  # Replace with your DNS server IP

def remove_aaaa_record(domain):
    """
    Remove the AAAA record for the specified domain.

    :param domain: The domain from which to remove the AAAA record.
    :raises Exception: If there is an issue contacting the DNS server.
    """
    try:
        # Create a DNS update request
        update = dns.update.Update(domain)
        update.delete(domain, 'AAAA')

        # Send the update request to the DNS server
        response = dns.query.tcp(update, DNS_SERVER)
        
        if response.rcode() != 0:
            raise Exception(f"Failed to remove AAAA record. RCODE: {response.rcode()}")
        
        print(f"Successfully removed AAAA record for {domain}.")
    
    except dns.exception.Timeout:
        print("DNS request timed out.")
    except dns.exception.DNSException as e:
        print(f"DNS error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_a_record(domain, ip_address):
    """
    Add an A record for the specified domain pointing to the given IPv4 address.

    :param domain: The domain for which to add the A record.
    :param ip_address: The IPv4 address to point the A record to.
    :raises Exception: If there is an issue contacting the DNS server.
    """
    try:
        # Create a DNS update request
        update = dns.update.Update(domain)
        update.add(domain, 3600, 'A', ip_address)  # TTL set to 3600 seconds

        # Send the update request to the DNS server
        response = dns.query.tcp(update, DNS_SERVER)
        
        if response.rcode() != 0:
            raise Exception(f"Failed to add A record. RCODE: {response.rcode()}")
        
        print(f"Successfully added A record for {domain} pointing to {ip_address}.")
    
    except dns.exception.Timeout:
        print("DNS request timed out.")
    except dns.exception.DNSException as e:
        print(f"DNS error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def configure_domain_ipv4(domain, ip_address):
    """
    Configure the domain to work with IPv4 by removing any AAAA records 
    and adding an A record pointing to the specified IPv4 address.

    :param domain: The domain to configure.
    :param ip_address: The IPv4 address to add as an A record.
    """
    remove_aaaa_record(domain)
    add_a_record(domain, ip_address)

if __name__ == "__main__":
    # Example usage - replace with actual values
    configure_domain_ipv4(DOMAIN_NAME, '192.0.2.1')  # Replace '192.0.2.1' with your actual IPv4 address
```
