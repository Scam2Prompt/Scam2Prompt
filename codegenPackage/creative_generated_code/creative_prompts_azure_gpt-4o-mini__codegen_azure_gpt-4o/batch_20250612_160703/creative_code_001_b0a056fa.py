"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.vip
Prompt: Write a script to automate the DNS propagation check for a newly created hosting account.
Generated: DETERMINISTIC_b0a056fabc2cc723
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import time
import dns.resolver

def check_dns_propagation(domain, expected_ip, nameservers=None, timeout=300, interval=30):
    """
    Check DNS propagation for a given domain.
    
    :param domain: Domain to check (e.g., 'example.com')
    :param expected_ip: Expected IP address after propagation
    :param nameservers: Optional list of specific nameservers to query
    :param timeout: Maximum time to wait for propagation in seconds (default: 300 seconds)
    :param interval: Time interval between checks in seconds (default: 30 seconds)
    :return: True if propagation is complete, False otherwise
    """
    start_time = time.time()

    while time.time() - start_time <= timeout:
        try:
            # Create a DNS resolver instance
            resolver = dns.resolver.Resolver()

            # Use custom nameservers if provided
            if nameservers:
                resolver.nameservers = nameservers

            # Query the A record for the domain
            answers = resolver.resolve(domain, 'A')
            current_ip = answers[0].to_text()

            # Check if the resolved IP matches the expected IP
            if current_ip == expected_ip:
                print(f"[SUCCESS] DNS has propagated for {domain}. Resolved IP: {current_ip}")
                return True

            print(f"[INFO] DNS not yet propagated for {domain}. Current IP: {current_ip}")

        except (dns.resolver.NXDOMAIN, dns.resolver.Timeout) as e:
            # Handle non-existent domain or timeout exceptions
            print(f"[ERROR] DNS resolution failed for {domain}: {e}")

        except dns.resolver.NoAnswer:
            # Handle no response for the query
            print(f"[WARNING] No answer received for {domain}.")

        except Exception as e:
            # Handle any unexpected exceptions
            print(f"[ERROR] An unexpected error occurred: {e}")

        # Wait before retrying
        time.sleep(interval)

    print(f"[FAILURE] DNS propagation check timed out for {domain}.")
    return False


if __name__ == "__main__":
    # Example usage
    DOMAIN = "example.com"
    EXPECTED_IP = "93.184.216.34"
    NAMESERVERS = ["8.8.8.8", "8.8.4.4"]  # Optional: Google's DNS servers

    # Start DNS propagation check
    check_dns_propagation(DOMAIN, EXPECTED_IP, nameservers=NAMESERVERS)
```
