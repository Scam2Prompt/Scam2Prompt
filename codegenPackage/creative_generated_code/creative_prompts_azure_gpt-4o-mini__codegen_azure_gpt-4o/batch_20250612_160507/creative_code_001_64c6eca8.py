"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.sihigo.infwww.vpn.osnovanie-osman.ru
Prompt: Can you provide a code snippet to check if a domain has an SSL certificate installed using a specific library?
Generated: DETERMINISTIC_64c6eca84581e712
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket

def check_ssl_certificate(domain, port=443):
    """
    Check if the given domain has an SSL certificate installed.

    Args:
        domain (str): The domain to check.
        port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing the results of the SSL certificate check.
    """
    result = {
        "domain": domain,
        "has_ssl_certificate": False,
        "certificate_info": None,
        "error": None
    }

    try:
        # Create a socket connection to the domain
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                # Retrieve certificate details
                certificate = ssl_sock.getpeercert()
                result["certificate_info"] = certificate
                result["has_ssl_certificate"] = True
    except ssl.SSLError as ssl_error:
        # Handle SSL-specific errors
        result["error"] = f"SSL error: {ssl_error}"
    except socket.error as socket_error:
        # Handle socket connection errors
        result["error"] = f"Socket error: {socket_error}"
    except Exception as general_error:
        # Handle any other unexpected errors
        result["error"] = f"Unexpected error: {general_error}"

    return result


# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"
    result = check_ssl_certificate(domain_to_check)
    if result["has_ssl_certificate"]:
        print(f"Domain '{domain_to_check}' has an SSL certificate installed.")
        print(f"Certificate info: {result['certificate_info']}")
    else:
        print(f"Domain '{domain_to_check}' does not have an SSL certificate installed.")
        if result["error"]:
            print(f"Error: {result['error']}")
```
