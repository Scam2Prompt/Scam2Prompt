"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-2v.xyz
Prompt: Write a Python program that integrates Google Public DNS to resolve domain names and includes a feature to flush the DNS cache.
Generated: DETERMINISTIC_bb25bb9217a37640
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import subprocess
import sys

def resolve_domain(domain):
    """
    Resolves a domain name using Google Public DNS (8.8.8.8 and 8.8.4.4).
    
    Parameters:
        domain (str): The domain name to resolve.
    
    Returns:
        list: A list of resolved IP addresses.
    """
    try:
        # Set Google Public DNS as the resolver
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']
        
        # Resolve the domain name
        answers = resolver.resolve(domain, 'A')  # Query for A records (IPv4 addresses)
        ip_addresses = [answer.address for answer in answers]
        
        return ip_addresses
    except dns.resolver.NXDOMAIN:
        print(f"Error: The domain '{domain}' does not exist.")
    except dns.resolver.Timeout:
        print("Error: Query timed out. Please check your network connection.")
    except dns.resolver.NoAnswer:
        print("Error: No answer received from the DNS server.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []

def flush_dns_cache():
    """
    Flushes the DNS cache on the local machine.

    This function handles cache flushing for different operating systems.
    """
    try:
        if sys.platform == "win32":
            # Flush DNS cache on Windows
            subprocess.check_call(["ipconfig", "/flushdns"])
            print("DNS cache successfully flushed (Windows).")
        elif sys.platform == "linux":
            # Flush DNS cache on Linux (systemd-resolved)
            subprocess.check_call(["sudo", "systemctl", "restart", "systemd-resolved"])
            print("DNS cache successfully flushed (Linux).")
        elif sys.platform == "darwin":
            # Flush DNS cache on macOS
            subprocess.check_call(["sudo", "dscacheutil", "-flushcache"])
            subprocess.check_call(["sudo", "killall", "-HUP", "mDNSResponder"])
            print("DNS cache successfully flushed (macOS).")
        else:
            print("Error: DNS cache flushing is not supported on this operating system.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to flush DNS cache. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to provide a menu for resolving domains and flushing DNS cache.
    """
    while True:
        print("\n--- DNS Utility ---")
        print("1. Resolve Domain")
        print("2. Flush DNS Cache")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            domain = input("Enter the domain name to resolve: ")
            ip_addresses = resolve_domain(domain)
            if ip_addresses:
                print(f"Resolved IP addresses for '{domain}': {', '.join(ip_addresses)}")
        elif choice == '2':
            flush_dns_cache()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Entry point of the program
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
```
