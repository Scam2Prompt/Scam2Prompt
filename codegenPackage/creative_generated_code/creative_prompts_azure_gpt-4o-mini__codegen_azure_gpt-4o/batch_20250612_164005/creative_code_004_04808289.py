"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.pages.dev
Prompt: How do I configure DNS settings for a newly acquired sub-domain to ensure it is secure?
Generated: DETERMINISTIC_048082899c8117d9
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code using the `dnspython` library to securely manage and configure DNS settings for a newly acquired sub-domain. Ensure you have the `dnspython` library installed (`pip install dnspython`) before running this code.

```python
import dns.zone
import dns.query
import dns.update
import dns.tsigkeyring
import dns.rdatatype

# Constants for configuration
PRIMARY_DNS_SERVER = "your.primary.dns.server"  # Replace with your DNS server IP/hostname
SUBDOMAIN = "secure.yourdomain.com"            # Replace with your sub-domain
TTL = 3600                                     # Time-to-live for DNS records
TSIG_KEY_NAME = "your-tsig-key-name"
TSIG_KEY_SECRET = "your-tsig-key-secret"

def configure_dns():
    """
    Configure DNS settings for a newly acquired sub-domain.
    Ensures the sub-domain is secured using TSIG authentication.
    """
    try:
        # Create a TSIG keyring for secure DNS communication
        keyring = dns.tsigkeyring.from_text({TSIG_KEY_NAME: TSIG_KEY_SECRET})

        # Create an update object for the DNS zone
        update = dns.update.Update(SUBDOMAIN, keyring=keyring)

        # Add secure DNS records (example: A record pointing to an IP address)
        update.add('@', TTL, dns.rdatatype.A, '192.168.1.100')  # Replace with desired IP address

        # Add an example MX record (Mail Exchange) for securing email transactions
        update.add('@', TTL, dns.rdatatype.MX, '10 mail.yourdomain.com')

        # Add TXT record for SPF (Sender Policy Framework) configuration
        update.add('@', TTL, dns.rdatatype.TXT, '"v=spf1 include:yourdomain.com -all"')

        # Send the DNS update to the server
        response = dns.query.tcp(update, PRIMARY_DNS_SERVER)

        print("DNS Configuration Completed:")
        print(response)

    except dns.exception.DNSException as error:
        print(f"An error occurred during DNS configuration: {error}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    configure_dns()
```

This code configures DNS settings for the sub-domain securely using TSIG authentication. Replace placeholders (`your.primary.dns.server`, `your-tsig-key-name`, `your-tsig-key-secret`, etc.) with actual values before using it.
