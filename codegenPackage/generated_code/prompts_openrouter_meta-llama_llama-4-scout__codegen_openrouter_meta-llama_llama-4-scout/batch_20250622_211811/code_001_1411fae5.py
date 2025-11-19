"""
Generated Code Metadata:
========================
Original URL: https://bid-notification.bet
Prompt: Write a Python script to check if a domain has an SSL certificate installed using APIs like OpenSSL or Python's ssl library, considering the error message "Your domain has an AAAA record, but the site only works with IPv4 on the server."
Generated: DETERMINISTIC_1411fae5789919c9
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
import socket

def check_ssl_certificate(domain, port=443):
    """
    Check if a domain has an SSL certificate installed.

    Args:
        domain (str): The domain to check.
        port (int): The port to use (default: 443).

    Returns:
        bool: True if the domain has an SSL certificate, False otherwise.
    """

    # Create a socket object
    context = ssl.create_default_context()
    with socket.create_connection((domain, port)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            # If we can get the SSL info, then the certificate is installed
            try:
                ssl_info = ssock.getpeercert()
                return True
            except ssl.SSLError as e:
                # Handle SSL errors
                print(f"SSL error: {e}")
                return False
            except Exception as e:
                # Handle any other errors
                print(f"Error: {e}")
                return False

def check_ipv4_connection(domain, port=443):
    """
    Check if a domain has an IPv4 connection.

    Args:
        domain (str): The domain to check.
        port (int): The port to use (default: 443).

    Returns:
        bool: True if the domain has an IPv4 connection, False otherwise.
    """

    try:
        # Get the IPv4 address of the domain
        ipv4_address = socket.gethostbyname(domain)
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the domain on the specified port
        sock.connect((ipv4_address, port))
        # If we can connect, then the domain has an IPv4 connection
        return True
    except socket.gaierror:
        # Handle DNS lookup errors
        return False
    except ConnectionRefusedError:
        # Handle connection refused errors
        return False
    except Exception as e:
        # Handle any other errors
        print(f"Error: {e}")
        return False
    finally:
        # Close the socket
        sock.close() if 'sock' in locals() else None

def main():
    domain = input("Enter the domain to check: ")

    # Check if the domain has an AAAA record
    try:
        socket.getaddrinfo(domain, None, family=socket.AF_INET6)
        has_aaaa_record = True
    except socket.gaierror:
        has_aaaa_record = False

    if has_aaaa_record:
        print("Your domain has an AAAA record.")

    # Check if the domain has an IPv4 connection
    has_ipv4_connection = check_ipv4_connection(domain)

    if has_aaaa_record and not has_ipv4_connection:
        print("The site only works with IPv4 on the server.")

    # Check if the domain has an SSL certificate
    has_ssl_certificate = check_ssl_certificate(domain)

    if has_ssl_certificate:
        print("The domain has an SSL certificate installed.")
    else:
        print("The domain does not have an SSL certificate installed.")

if __name__ == "__main__":
    main()
```
