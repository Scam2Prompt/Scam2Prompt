"""
Generated Code Metadata:
========================
Original URL: https://ghost-name.pages.dev
Prompt: Create a simple script to fetch and display Cloudflare Ray ID and visitor IP information for a given website.
Generated: DETERMINISTIC_10316f0ee804f090
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import argparse
from typing import Optional, Dict, Any

def fetch_website_info(url: str) -> Optional[Dict[str, Any]]:
    """
    Fetch website information including Cloudflare Ray ID and visitor IP.
    
    Args:
        url: Website URL to fetch information from
        
    Returns:
        Dictionary containing response headers and IP information if successful,
        None if request fails
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        headers = response.headers
        ip_info = {
            'ip': response.raw._connection.sock.getpeername()[0],
            'port': response.raw._connection.sock.getpeername()[1]
        }
        
        return {
            'headers': headers,
            'ip_info': ip_info
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website info: {e}")
        return None

def display_info(info: Dict[str, Any]) -> None:
    """
    Display the fetched website information.
    
    Args:
        info: Dictionary containing website information
    """
    if not info:
        print("No information to display")
        return
    
    headers = info['headers']
    ip_info = info['ip_info']
    
    print("\nWebsite Information:")
    print(f"IP Address: {ip_info['ip']}")
    print(f"Port: {ip_info['port']}")
    
    print("\nResponse Headers:")
    for key, value in headers.items():
        if key.lower().startswith('cf-'):
            print(f"{key}: {value}")
    
    ray_id = headers.get('CF-RAY')
    if ray_id:
        print(f"\nCloudflare Ray ID: {ray_id}")
    else:
        print("\nNo Cloudflare Ray ID found in response headers")

def main():
    parser = argparse.ArgumentParser(description='Fetch Cloudflare Ray ID and visitor IP information for a website')
    parser.add_argument('url', help='Website URL to analyze')
    args = parser.parse_args()
    
    website_info = fetch_website_info(args.url)
    display_info(website_info)

if __name__ == '__main__':
    main()
```
