"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hosico-cat.fun
Prompt: What steps should I take if my domain has an AAAA record but only works with IPv4 on the server?
Generated: DETERMINISTIC_119402205ede8ccf
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def check_and_resolve(domain_name):
    """
    Checks if a domain has an AAAA (IPv6) record and tests IPv6 connectivity.
    If the server only supports IPv4, provides recommendations.
    """
    try:
        # Resolve AAAA record for the domain
        logging.info(f"Checking AAAA record for domain: {domain_name}")
        answers = dns.resolver.resolve(domain_name, 'AAAA')
        ipv6_addresses = [answer.to_text() for answer in answers]

        logging.info(f"Found AAAA records (IPv6): {ipv6_addresses}")

        # Test IPv6 connectivity
        logging.info("Testing IPv6 connectivity...")
        for ipv6_address in ipv6_addresses:
            result = subprocess.run(['ping', '-6', '-c', '1', ipv6_address],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                logging.info(f"Successfully pinged IPv6 address: {ipv6_address}")
            else:
                logging.warning(f"Failed to ping IPv6 address: {ipv6_address}")
                logging.warning(f"Server may not support IPv6.")

        logging.info("Completed IPv6 connectivity test.")

    except dns.resolver.NoAnswer:
        logging.warning(f"No AAAA record found for domain: {domain_name}")
    except dns.resolver.NXDOMAIN:
        logging.error(f"Domain name does not exist: {domain_name}")
    except Exception as e:
        logging.error(f"An error occurred while resolving AAAA records: {str(e)}")
        logging.exception(e)
        return

    logging.info("If the server does not support IPv6, consider removing the AAAA record from DNS settings.")


if __name__ == "__main__":
    # Replace 'example.com' with the domain you want to check.
    domain = "example.com"
    check_and_resolve(domain)
```
