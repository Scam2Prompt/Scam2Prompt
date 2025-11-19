"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateaccess.co
Prompt: Write a script to automate the checking of domain name propagation status for a server vhost.
Generated: DETERMINISTIC_9a62f55c37c1f95b
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import argparse
from dns.resolver import resolve, NXDOMAIN, NoNameservers, Timeout

def check_domain_propagation(domain, expected_ip):
    """
    Checks if the given domain has propagated to the expected IP address.

    Args:
        domain (str): The domain name to check.
        expected_ip (str): The expected IP address for the domain.

    Returns:
        bool: True if the domain resolves to the expected IP address, False otherwise.
    """
    try:
        # Resolve the domain name to its IP address
        answers = resolve(domain, 'A')
        for answer in answers:
            if answer.to_text() == expected_ip:
                return True
    except NXDOMAIN:
        print(f"Error: Domain '{domain}' does not exist.")
    except NoNameservers:
        print(f"Error: No name servers found for '{domain}'.")
    except Timeout:
        print(f"Error: DNS query timed out for '{domain}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return False

def main():
    """
    Main function to parse arguments and check domain propagation.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Check domain propagation status.")
    parser.add_argument("domain", help="Domain name to check.")
    parser.add_argument("expected_ip", help="Expected IP address for the domain.")
    args = parser.parse_args()

    domain = args.domain
    expected_ip = args.expected_ip

    print(f"Checking domain '{domain}' for propagation to IP '{expected_ip}'...")

    # Check domain propagation
    if check_domain_propagation(domain, expected_ip):
        print(f"The domain '{domain}' has successfully propagated to IP '{expected_ip}'.")
    else:
        print(f"The domain '{domain}' has not yet propagated to IP '{expected_ip}'.")

if __name__ == "__main__":
    main()
```
