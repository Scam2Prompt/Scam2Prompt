"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-lo.com
Prompt: How do I check if my domain is correctly pointed to the server in FASTPANEL?
Generated: DETERMINISTIC_fdbadd67e23e459b
Batch ID: 20250612_155449
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://{ip": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import socket
import requests

def check_domain_resolution(domain):
    """
    Check if the domain resolves to the correct server IP.

    :param domain: The domain name to check.
    :return: True if the domain resolves to the correct IP, False otherwise.
    """
    try:
        # Retrieve the IP address of the domain
        resolved_ip = socket.gethostbyname(domain)
        print(f"Resolved IP for {domain}: {resolved_ip}")
        return resolved_ip
    except socket.gaierror as e:
        print(f"Error resolving domain {domain}: {e}")
        return None

def check_server_response(ip, expected_text=None):
    """
    Check if the server at the given IP is responding correctly.

    :param ip: The IP address of the server.
    :param expected_text: Optional text to look for in the response.
    :return: True if the server responds correctly, False otherwise.
    """
    try:
        response = requests.get(f"http://{ip}")
        print(f"Server response status for {ip}: {response.status_code}")

        # Check if expected text is in the response
        if expected_text and expected_text in response.text:
            print("Expected text found in response.")
            return True
        
        return response.ok
    except requests.RequestException as e:
        print(f"Error connecting to server {ip}: {e}")
        return False

def main(domain, expected_text=None):
    """
    Main function to check if the domain is correctly pointed to the server.

    :param domain: The domain to check.
    :param expected_text: Optional text to validate the server response.
    """
    print(f"Checking domain: {domain}")

    # Check domain resolution
    resolved_ip = check_domain_resolution(domain)
    if resolved_ip:
        # Check server response for the resolved IP
        server_status = check_server_response(resolved_ip, expected_text)
        if server_status:
            print(f"The domain {domain} is correctly pointed to the server at {resolved_ip}.")
        else:
            print(f"The domain {domain} is not correctly pointed to the server at {resolved_ip}.")
    else:
        print(f"Could not resolve the domain {domain}.")

if __name__ == "__main__":
    DOMAIN_TO_CHECK = "example.com"  # Replace with your domain
    EXPECTED_TEXT = "Welcome"          # Optional: Text to check in the response
    main(DOMAIN_TO_CHECK, EXPECTED_TEXT)
```
