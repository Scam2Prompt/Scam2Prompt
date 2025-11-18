"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://876981455175.icu
Prompt: Write a script to check if a domain is correctly pointed to a FASTPANEL server using IPv4 and identify any AAAA record conflicts.
Generated: DETERMINISTIC_99eedaa1b08e0adc
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import socket

def check_fastpanel_domain(domain, fastpanel_ip):
    """
    Checks if a domain's A record points to the specified FASTPANEL IPv4 address
    and identifies any conflicting AAAA records.
    
    Args:
        domain (str): The domain name to check.
        fastpanel_ip (str): The IPv4 address of the FASTPANEL server.

    Returns:
        dict: Result containing the status of the A record and any conflicting AAAA records.
    """
    results = {
        "a_record_status": None,  # Whether the A record is correctly pointed
        "conflicting_aaaa_records": []  # List of conflicting AAAA records
    }

    try:
        # Resolve A records (IPv4)
        a_records = dns.resolver.resolve(domain, 'A')
        ipv4_addresses = [str(record) for record in a_records]

        if fastpanel_ip in ipv4_addresses:
            results["a_record_status"] = "Correct"
        else:
            results["a_record_status"] = "Incorrect"

    except dns.resolver.NXDOMAIN:
        results["a_record_status"] = "No A record found"
    except dns.resolver.NoAnswer:
        results["a_record_status"] = "No A record found"
    except Exception as e:
        results["a_record_status"] = f"Error resolving A record: {str(e)}"

    try:
        # Resolve AAAA records (IPv6)
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        ipv6_addresses = [str(record) for record in aaaa_records]

        # Check for conflicting AAAA records
        for ipv6 in ipv6_addresses:
            try:
                # Try to resolve IPv6 to hostnames and check potential conflicts
                resolved_host = socket.gethostbyaddr(ipv6)
                results["conflicting_aaaa_records"].append({
                    "ipv6_address": ipv6,
                    "resolved_host": resolved_host[0]
                })
            except socket.herror:
                # If reverse DNS fails, add IPv6 to conflicts list
                results["conflicting_aaaa_records"].append({
                    "ipv6_address": ipv6,
                    "resolved_host": None
                })

    except dns.resolver.NXDOMAIN:
        # No AAAA records present
        pass
    except dns.resolver.NoAnswer:
        # No AAAA records present
        pass
    except Exception as e:
        results["conflicting_aaaa_records"].append({
            "error": f"Error resolving AAAA record: {str(e)}"
        })

    return results


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    fastpanel_ipv4 = "192.168.1.100"  # Replace with actual FASTPANEL server IP

    result = check_fastpanel_domain(domain_to_check, fastpanel_ipv4)
    print("A Record Status:", result["a_record_status"])
    print("Conflicting AAAA Records:", result["conflicting_aaaa_records"])
```
