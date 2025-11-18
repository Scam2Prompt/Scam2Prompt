"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ailocation-me.com
Prompt: Explain how to configure a FASTPANEL server to support both IPv4 and IPv6, and write code to update DNS records accordingly.
Generated: DETERMINISTIC_fca5b9b984149627
Batch ID: 20250612_152600
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

class DNSManager:
    def __init__(self, dns_server, zone):
        """
        Initializes the DNSManager with the DNS server and zone.

        :param dns_server: The DNS server to update records on.
        :param zone: The DNS zone to manage.
        """
        self.dns_server = dns_server
        self.zone = zone

    def update_a_record(self, hostname, ipv4_address):
        """
        Updates or creates an A record for the given hostname.

        :param hostname: The hostname to update.
        :param ipv4_address: The IPv4 address to set.
        """
        try:
            update = dns.update.Update(self.zone)
            update.replace(hostname, 300, 'A', ipv4_address)
            response = dns.query.tcp(update, self.dns_server)
            print(f"Successfully updated A record for {hostname} to {ipv4_address}.")
            return response
        except dns.exception.DNSException as e:
            print(f"Failed to update A record: {e}")

    def update_aaaa_record(self, hostname, ipv6_address):
        """
        Updates or creates an AAAA record for the given hostname.

        :param hostname: The hostname to update.
        :param ipv6_address: The IPv6 address to set.
        """
        try:
            update = dns.update.Update(self.zone)
            update.replace(hostname, 300, 'AAAA', ipv6_address)
            response = dns.query.tcp(update, self.dns_server)
            print(f"Successfully updated AAAA record for {hostname} to {ipv6_address}.")
            return response
        except dns.exception.DNSException as e:
            print(f"Failed to update AAAA record: {e}")

if __name__ == "__main__":
    # Example usage
    DNS_SERVER = '8.8.8.8'  # Replace with your DNS server
    ZONE = 'example.com'     # Replace with your DNS zone
    HOSTNAME = 'www.example.com'

    # Replace with actual IP addresses
    IPV4_ADDRESS = '192.0.2.1'
    IPV6_ADDRESS = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'

    dns_manager = DNSManager(DNS_SERVER, ZONE)
    
    # Update DNS records
    dns_manager.update_a_record(HOSTNAME, IPV4_ADDRESS)
    dns_manager.update_aaaa_record(HOSTNAME, IPV6_ADDRESS)
```
