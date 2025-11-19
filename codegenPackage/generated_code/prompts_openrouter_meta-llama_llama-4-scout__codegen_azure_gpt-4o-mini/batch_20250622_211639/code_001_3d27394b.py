"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Explain the importance of SPF in Microsoft 365 and provide a code snippet to set up a SPF record.
Generated: DETERMINISTIC_3d27394b20264bc9
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import dns.update
import dns.query
import dns.tsigkeyring

# Constants for DNS server and domain
DNS_SERVER = 'your_dns_server_ip'  # Replace with your DNS server IP
DOMAIN = 'yourdomain.com'            # Replace with your domain
SPF_RECORD = 'v=spf1 include:spf.protection.outlook.com -all'

def create_spf_record(domain, spf_record):
    """
    Create or update an SPF record for the specified domain.

    Args:
        domain (str): The domain for which to set the SPF record.
        spf_record (str): The SPF record string to set.

    Raises:
        Exception: If there is an error while updating the DNS record.
    """
    try:
        # Create a DNS update request
        update = dns.update.Update(domain)

        # Set the SPF record
        update.replace('@', 3600, 'TXT', spf_record)

        # Send the update to the DNS server
        response = dns.query.tcp(update, DNS_SERVER)

        # Check for errors in the response
        if response.rcode() != 0:
            raise Exception(f"Failed to update SPF record: {dns.rcode.to_text(response.rcode())}")

        print(f"SPF record for {domain} updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to create/update the SPF record
create_spf_record(DOMAIN, SPF_RECORD)
```

**Note:** Replace `your_dns_server_ip` and `yourdomain.com` with your actual DNS server IP and domain name. Ensure you have the `dnspython` library installed to run this code. You can install it using `pip install dnspython`.
