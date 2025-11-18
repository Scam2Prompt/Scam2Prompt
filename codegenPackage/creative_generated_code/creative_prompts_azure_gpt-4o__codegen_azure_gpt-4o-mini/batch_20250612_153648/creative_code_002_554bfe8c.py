"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakingreward.org
Prompt: Provide an example of how to implement SDNS recursive cloud services for DNS resolution, referencing CNNIC's SDNS technology.
Generated: DETERMINISTIC_554bfe8c1a511bcb
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.query
import dns.resolver
import dns.message
import dns.exception
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class SDNSClient:
    def __init__(self, sdns_address: str):
        """
        Initializes the SDNSClient with the specified SDNS server address.
        
        :param sdns_address: The address of the SDNS server (e.g., "dns://example.com")
        """
        self.sdns_address = sdns_address

    def resolve(self, domain: str) -> str:
        """
        Resolves a domain using the SDNS server.

        :param domain: The domain name to resolve.
        :return: The resolved IP address.
        :raises Exception: Raises an exception if resolution fails.
        """
        try:
            # Create a DNS query message
            query = dns.message.make_query(domain, dns.rdatatype.A)
            response = dns.query.tcp(query, self.sdns_address)
            
            # Check if response is valid
            if response.rcode() != dns.rcode.NOERROR:
                raise Exception(f"Failed to resolve {domain}: {response.rcode()}")

            # Extract IP address from the answer section
            for answer in response.answer:
                if answer.rdtype == dns.rdatatype.A:
                    return answer[0].address

            raise Exception(f"No A record found for {domain}")
        
        except dns.exception.Timeout:
            logging.error("Query to SDNS server timed out.")
            raise
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            raise

if __name__ == "__main__":
    # Example usage of the SDNSClient class
    sdns_address = "dns://1.1.1.1"  # Replace with a valid SDNS address
    domain = "example.com"  # The domain to resolve
    sdns_client = SDNSClient(sdns_address)

    try:
        ip_address = sdns_client.resolve(domain)
        logging.info(f"Resolved {domain} to {ip_address}")
    except Exception as e:
        logging.error(f"DNS resolution failed: {str(e)}")
```

Make sure to replace `"dns://1.1.1.1"` with the appropriate SDNS address from CNNIC's services.
