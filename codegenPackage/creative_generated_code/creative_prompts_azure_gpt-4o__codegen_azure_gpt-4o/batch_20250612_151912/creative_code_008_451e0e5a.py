"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stormtoken.site
Prompt: Write code to query DNS servers and verify if a domain is correctly pointed to hosting servers, including error handling for misconfigurations.
Generated: DETERMINISTIC_451e0e5ab74a4488
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def verify_dns(domain, expected_ips):
    """
    Verifies if a domain is correctly pointed to expected hosting server IPs.

    Args:
        domain (str): The domain name to query DNS records for.
        expected_ips (list): List of expected IPs to verify against.

    Returns:
        dict: A dictionary containing the query result and status.
    """
    result = {
        "domain": domain,
        "expected_ips": expected_ips,
        "resolved_ips": [],
        "status": "Unknown",
        "error": None
    }

    try:
        # Query the A record for the domain using the DNS resolver
        answers = dns.resolver.resolve(domain, 'A')
        resolved_ips = [str(answer) for answer in answers]
        result["resolved_ips"] = resolved_ips

        # Check if the resolved IPs match the expected IPs
        if set(resolved_ips) == set(expected_ips):
            result["status"] = "Correctly Configured"
        else:
            result["status"] = "Misconfigured"

    except dns.resolver.NoAnswer:
        # Handle cases where no answer is returned for the query
        result["status"] = "Error"
        result["error"] = f"No A record found for domain: {domain}"

    except dns.resolver.NXDOMAIN:
        # Handle cases where the domain does not exist
        result["status"] = "Error"
        result["error"] = f"Domain does not exist: {domain}"

    except dns.resolver.Timeout:
        # Handle cases where the DNS query times out
        result["status"] = "Error"
        result["error"] = "DNS query timed out"

    except dns.exception.DNSException as e:
        # Catch any other DNS-related exceptions
        result["status"] = "Error"
        result["error"] = f"An unexpected DNS error occurred: {str(e)}"

    return result

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    expected_host_ips = ["93.184.216.34"]  # Replace with the expected IPs of your hosting servers

    dns_check_result = verify_dns(domain_to_check, expected_host_ips)
    print("DNS Verification Result:")
    print(dns_check_result)
```
