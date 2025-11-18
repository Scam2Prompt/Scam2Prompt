"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridger.finance
Prompt: Provide code to automate the detection of AAAA records for a domain and verify if the server supports IPv6, referencing FASTPANEL's troubleshooting guidelines.
Generated: DETERMINISTIC_8a3bce2528761b0c
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def check_ipv6_support(domain):
    """
    Detects AAAA records for a given domain and verifies if the server supports IPv6.

    Parameters:
        domain (str): The domain name to query.

    Returns:
        dict: A dictionary containing whether IPv6 is supported and the list of AAAA records.
    """
    try:
        # Initialize a resolver instance
        resolver = dns.resolver.Resolver()

        # Query AAAA records for the domain
        answers = resolver.resolve(domain, 'AAAA')

        # Extract IPv6 addresses from the results
        ipv6_addresses = [answer.to_text() for answer in answers]

        return {
            "IPv6_Supported": True,  # AAAA records indicate IPv6 support
            "AAAA_Records": ipv6_addresses
        }

    except dns.resolver.NoAnswer:
        # No AAAA records found
        return {
            "IPv6_Supported": False,
            "AAAA_Records": []
        }

    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        return {
            "IPv6_Supported": False,
            "Error": "Domain does not exist"
        }

    except dns.exception.Timeout:
        # DNS query timed out
        return {
            "IPv6_Supported": False,
            "Error": "DNS query timed out"
        }

    except dns.resolver.NoNameservers:
        # No nameservers could be reached
        return {
            "IPv6_Supported": False,
            "Error": "No nameservers are available"
        }

    except Exception as e:
        # Handle any unexpected errors
        return {
            "IPv6_Supported": False,
            "Error": str(e)
        }


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    result = check_ipv6_support(domain_to_check)

    print("IPv6 Support:", result["IPv6_Supported"])
    if "AAAA_Records" in result and result["AAAA_Records"]:
        print("AAAA Records:")
        for record in result["AAAA_Records"]:
            print(f" - {record}")
    elif "Error" in result:
        print("Error:", result["Error"])
```
