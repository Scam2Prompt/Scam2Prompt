"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiweb.pro
Prompt: Create a script to detect and fix AAAA record issues for a domain that only supports IPv4 on a FASTPANEL server.
Generated: DETERMINISTIC_539c2118f10ef6b2
Batch ID: 20250612_153755
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
DOMAIN = 'example.com'  # Replace with your domain
DNS_SERVER = '8.8.8.8'  # Google Public DNS, replace with your DNS server if needed

def get_aaaa_records(domain):
    """Retrieve AAAA records for the specified domain."""
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        return [str(record) for record in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        logging.info(f'No AAAA records found for {domain}.')
        return []
    except Exception as e:
        logging.error(f'Error retrieving AAAA records: {e}')
        return []

def delete_aaaa_records(domain):
    """Delete all AAAA records for the specified domain."""
    update = dns.update.Update(domain)
    update.delete(domain, 'AAAA')
    try:
        response = dns.query.tcp(update, DNS_SERVER)
        if response.rcode() == 0:
            logging.info(f'Successfully deleted AAAA records for {domain}.')
        else:
            logging.error(f'Failed to delete AAAA records: {response.rcode()}')
    except dns.exception.DNSException as e:
        logging.error(f'Error during DNS update: {e}')

def add_a_record(domain, ipv4_address):
    """Add an A record for the specified domain with the given IPv4 address."""
    update = dns.update.Update(domain)
    update.add(domain, 300, 'A', ipv4_address)  # TTL set to 300 seconds
    try:
        response = dns.query.tcp(update, DNS_SERVER)
        if response.rcode() == 0:
            logging.info(f'Successfully added A record for {domain} with IP {ipv4_address}.')
        else:
            logging.error(f'Failed to add A record: {response.rcode()}')
    except dns.exception.DNSException as e:
        logging.error(f'Error during DNS update: {e}')

def main():
    """Main function to detect and fix AAAA record issues."""
    logging.info('Starting AAAA record check for domain: %s', DOMAIN)

    # Detect AAAA records
    aaaa_records = get_aaaa_records(DOMAIN)
    
    # If AAAA records are found, delete them
    if aaaa_records:
        delete_aaaa_records(DOMAIN)
    
    # Add an A record (assuming a known IPv4 address)
    ipv4_address = '192.0.2.1'  # Replace with your actual IPv4 address
    add_a_record(DOMAIN, ipv4_address)

if __name__ == "__main__":
    main()
```
