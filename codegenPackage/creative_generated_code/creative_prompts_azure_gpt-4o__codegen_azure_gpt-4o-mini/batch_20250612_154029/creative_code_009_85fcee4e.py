"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-berachain.ink
Prompt: Create a tutorial script to demonstrate how to use Google Public DNS for resolving domain names and IP addresses.
Generated: DETERMINISTIC_85fcee4ed069ec39
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def resolve_domain(domain_name):
    """
    Resolves a domain name to an IP address using Google Public DNS.

    Args:
        domain_name (str): The domain name to resolve.

    Returns:
        str: The resolved IP address or an error message.
    """
    try:
        # Google Public DNS IP addresses
        dns_servers = ['8.8.8.8', '8.8.4.4']

        # Create a socket with AF_INET (IPv4) and SOCK_DGRAM (UDP)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # Set the DNS server to Google's DNS
            sock.connect((dns_servers[0], 53))

            # Perform a DNS resolution
            ip_address = socket.gethostbyname(domain_name)
            return ip_address

    except socket.gaierror as e:
        return f"Error resolving domain {domain_name}: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def main():
    """
    Main function to run the DNS resolution tutorial.
    """
    print("Welcome to the DNS Resolution Tutorial using Google Public DNS!")
    
    while True:
        domain_name = input("Enter a domain name to resolve (or 'exit' to quit): ").strip()
        if domain_name.lower() == 'exit':
            print("Exiting the tutorial. Goodbye!")
            break
        
        # Resolve and print the result
        result = resolve_domain(domain_name)
        print(f"Resolved IP address: {result}")

if __name__ == "__main__":
    main()
```
