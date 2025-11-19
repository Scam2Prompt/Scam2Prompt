"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: How can I check if my domain is correctly pointed to a server, and what API or library can assist with this verification?
Generated: DETERMINISTIC_1c6321da22e01c0c
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
import socket

def check_domain_pointing(domain_name, expected_ip):
    """
    Function to check if a domain is correctly pointed to the expected server IP.

    Parameters:
    - domain_name (str): The domain name to check.
    - expected_ip (str): The expected IP address the domain should point to.

    Returns:
    - dict: A dictionary containing the result of the check and error details if applicable.
    """
    result = {
        "domain": domain_name,
        "expected_ip": expected_ip,
        "actual_ip": None,
        "is_pointed_correctly": False,
        "error": None
    }

    try:
        # Resolve the domain name to get its IP address
        answers = dns.resolver.resolve(domain_name, 'A')  # Query for A records (IPv4)
        actual_ips = [answer.to_text() for answer in answers]
        result["actual_ip"] = actual_ips

        # Check if the expected IP is in the resolved IPs
        if expected_ip in actual_ips:
            result["is_pointed_correctly"] = True
    except dns.resolver.NXDOMAIN:
        result["error"] = "Domain does not exist."
    except dns.resolver.Timeout:
        result["error"] = "DNS resolution timed out."
    except dns.resolver.NoAnswer:
        result["error"] = "No answer received from DNS server."
    except Exception as e:
        result["error"] = f"An unexpected error occurred: {str(e)}"

    return result


def main():
    """
    Main function to demonstrate domain pointing verification.

    Prompts the user for a domain name and expected IP address,
    then checks if the domain is correctly pointed to the server.
    """
    print("Domain Pointing Check")
    domain_name = input("Enter the domain name (e.g., example.com): ").strip()
    expected_ip = input("Enter the expected IP address (e.g., 192.168.1.1): ").strip()

    # Call the function to check domain pointing
    result = check_domain_pointing(domain_name, expected_ip)

    # Display results
    print("\nCheck Results:")
    print(f"Domain: {result['domain']}")
    print(f"Expected IP: {result['expected_ip']}")
    print(f"Actual IP(s): {result['actual_ip']}")
    if result["error"]:
        print(f"Error: {result['error']}")
    else:
        if result["is_pointed_correctly"]:
            print("Status: The domain is correctly pointed to the expected IP.")
        else:
            print("Status: The domain is NOT correctly pointed to the expected IP.")


if __name__ == "__main__":
    # Entry point to the program
    main()
```

### Requirements:
1. Install the `dnspython` library to ensure DNS resolution works:
   ```bash
   pip install dnspython
   ```
2. This script handles common DNS resolution errors and provides clear and actionable output for the user. It is production-ready and adheres to best practices.
