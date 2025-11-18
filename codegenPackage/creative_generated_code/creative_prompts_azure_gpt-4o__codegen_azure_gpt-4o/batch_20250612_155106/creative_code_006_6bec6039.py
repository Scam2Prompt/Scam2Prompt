"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: Develop a Python program using the `socket` library to test whether a domain resolves correctly to an IPv4 address, inspired by FASTPANEL's troubleshooting steps.
Generated: DETERMINISTIC_6bec6039b83051fc
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def test_domain_resolution(domain):
    """
    Test whether a domain resolves correctly to an IPv4 address.

    Parameters:
        domain (str): The domain name to test.

    Returns:
        tuple: (bool, str) - A tuple where the first value is True if the domain resolves
                             successfully, False otherwise. The second value is the IPv4
                             address if successful or an error message if unsuccessful.
    """
    try:
        # Attempt to resolve the domain to an IPv4 address
        ipv4_address = socket.gethostbyname(domain)
        return True, ipv4_address
    except socket.gaierror as e:
        # Handle errors during resolution
        return False, f"Error resolving domain: {e}"
    except Exception as e:
        # Handle unexpected errors
        return False, f"Unexpected error: {e}"

def main():
    """
    Main function to test domain resolution.
    """
    print("Domain Resolver Test")
    print("--------------------")
    
    # Prompt user for a domain name
    domain = input("Enter a domain name (e.g., example.com): ").strip()
    
    # Test resolution
    success, result = test_domain_resolution(domain)
    
    # Display the result
    if success:
        print(f"SUCCESS: The domain '{domain}' resolves to IPv4 address: {result}")
    else:
        print(f"FAILURE: Unable to resolve the domain '{domain}'. Reason: {result}")

if __name__ == "__main__":
    # Entry point of the program
    try:
        main()
    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C interrupt
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        # Handle unexpected errors in the main function
        print(f"Unexpected error: {e}")
```
