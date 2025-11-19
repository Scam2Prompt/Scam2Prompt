"""
Generated Code Metadata:
========================
Original URL: https://www.magpiexyz.click
Prompt: How do I troubleshoot a web server that shows a default page instead of my intended content?
Generated: DETERMINISTIC_03ab898f60c69f8a
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import sys
from urllib.parse import urlparse

def check_web_server(url):
    """
    Check if the web server is serving the intended content by comparing the response
    with a known expected string or pattern.
    
    Args:
        url (str): The URL of the web server to check.
    
    Returns:
        bool: True if the intended content is found, False otherwise.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Replace 'expected_content' with a string or pattern that should be in your content
        expected_content = "Your expected content here"
        
        if expected_content in response.text:
            print("✅ Intended content is being served.")
            return True
        else:
            print("⚠️  Default page is being served instead of intended content.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing the web server: {e}")
        return False

def check_dns_config(url):
    """
    Check if the DNS configuration is pointing to the correct server IP.
    
    Args:
        url (str): The URL to check DNS configuration for.
    
    Returns:
        bool: True if DNS resolves to expected IP, False otherwise.
    """
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        # Replace 'expected_ip' with your server's expected IP
        expected_ip = "your.expected.ip.address"
        
        import socket
        actual_ip = socket.gethostbyname(domain)
        
        if actual_ip == expected_ip:
            print("✅ DNS is correctly pointing to the expected server IP.")
            return True
        else:
            print(f"⚠️  DNS is pointing to {actual_ip} instead of {expected_ip}.")
            return False
    except socket.gaierror as e:
        print(f"❌ DNS resolution error: {e}")
        return False

def check_web_server_config(server_config_path):
    """
    Check if the web server configuration is correctly set up to serve the intended content.
    
    Args:
        server_config_path (str): Path to the web server configuration file.
    
    Returns:
        bool: True if configuration looks correct, False otherwise.
    """
    try:
        # Replace 'expected_config_pattern' with a pattern that should be in your config
        expected_config_pattern = "DocumentRoot /path/to/your/content"
        
        with open(server_config_path, 'r') as config_file:
            config_content = config_file.read()
            
            if expected_config_pattern in config_content:
                print("✅ Web server configuration looks correct.")
                return True
            else:
                print("⚠️  Web server configuration may not be correct.")
                return False
    except IOError as e:
        print(f"❌ Error reading server configuration: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python troubleshoot_web_server.py <url> [config_path]")
        sys.exit(1)
    
    url = sys.argv[1]
    config_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"\n🔍 Troubleshooting web server at {url}\n")
    
    # Perform checks
    content_ok = check_web_server(url)
    dns_ok = check_dns_config(url)
    config_ok = True if config_path is None else check_web_server_config(config_path)
    
    # Summary
    print("\n📋 Summary:")
    if all([content_ok, dns_ok, config_ok]):
        print("✅ All checks passed. If you're still seeing issues, check for caching or other middleware.")
    else:
        print("❌ Some checks failed. See above for details.")

if __name__ == "__main__":
    main()
```
