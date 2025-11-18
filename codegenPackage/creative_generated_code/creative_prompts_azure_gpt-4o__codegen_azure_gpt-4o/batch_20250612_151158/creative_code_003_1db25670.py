"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridger.finance
Prompt: Create a diagnostic tool to verify server configurations for domains managed by FASTPANEL, including domain pointing and SSL certificate installation.
Generated: DETERMINISTIC_1db2567050cde842
Batch ID: 20250612_151158
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{domain}/fastpanel": {
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
import ssl
import requests
import argparse

def check_domain_pointing(domain):
    """
    Check if the domain is properly pointing by resolving its IP address.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        str: IP address of the domain if successful, else error message.
    """
    try:
        ip = socket.gethostbyname(domain)
        return f"Domain '{domain}' is pointing to IP: {ip}"
    except socket.gaierror as e:
        return f"Domain '{domain}' is not properly pointed: {str(e)}"


def check_ssl(domain):
    """
    Check if an SSL certificate is installed and valid for the domain.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        str: Message indicating the result of the SSL check.
    """
    try:
        # Connect to the domain using SSL
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                ssl_info = ssock.getpeercert()
        
        # Extract common name from the certificate to verify it matches the domain
        if not ssl_info:
            return f"No SSL certificate found for '{domain}'"
        
        common_name = ssl_info.get('subject', [])
        common_name = [x[1] for x in common_name if x[0] == 'commonName']
        
        if domain in common_name:
            return f"SSL certificate is valid for domain '{domain}'"
        else:
            return f"SSL certificate does not match domain '{domain}'"
    except Exception as e:
        return f"Failed to verify SSL certificate for '{domain}': {str(e)}"


def check_fastpanel(domain):
    """
    Verify FASTPANEL installation and accessibility for the domain.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        str: Message indicating the result of the FASTPANEL check.
    """
    try:
        url = f"https://{domain}/fastpanel"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return f"FASTPANEL is installed and accessible for '{domain}'"
        elif response.status_code == 404:
            return f"FASTPANEL is not installed for '{domain}'"
        else:
            return f"FASTPANEL check for '{domain}' returned status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Failed to verify FASTPANEL for '{domain}': {str(e)}"


def main():
    """
    Main function to run the diagnostic tool for verifying server configurations.
    """
    parser = argparse.ArgumentParser(description="Diagnostic Tool for Server Configurations")
    parser.add_argument("domain", type=str, help="Domain name to verify")
    args = parser.parse_args()

    domain = args.domain

    print("\n--- Running Diagnostics ---")
    print(check_domain_pointing(domain))  # Check domain pointing
    print(check_ssl(domain))             # Check SSL installation
    print(check_fastpanel(domain))       # Check FASTPANEL installation and accessibility
    print("\n--- Diagnostics Completed ---")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
