"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-clink.org
Prompt: Write a script to configure a new host in Nginx Proxy Manager using its API, ensuring proper routing and SSL setup.
Generated: DETERMINISTIC_130a7f6ebb538d86
Batch ID: 20250612_145616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-nginx-proxy-manager-url": {
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
import requests
import json

# Configuration variables
NPM_URL = "http://your-nginx-proxy-manager-url"  # Change to your NPM URL
API_KEY = "your_api_key"  # Change to your API key
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def create_ssl_certificate(domain):
    """Create an SSL certificate for the specified domain."""
    ssl_data = {
        "cert": "",
        "key": "",
        "domain": domain,
        "letsencrypt": True,  # Use Let's Encrypt for SSL
        "dns": False
    }
    response = requests.post(f"{NPM_URL}/api/nginx/ssl", headers=HEADERS, json=ssl_data)
    
    if response.status_code == 201:
        return response.json()['id']  # Return SSL certificate ID
    else:
        raise Exception(f"Failed to create SSL certificate: {response.content.decode()}")

def create_host(domain, ssl_id):
    """Create a new host configuration in Nginx Proxy Manager."""
    host_data = {
        "domain": domain,
        "forward": {
            "host": "your-backend-url",  # Change to your backend URL
            "port": 80,                   # Change to your desired port
            "scheme": "http"             # Change to "https" if needed
        },
        "sslId": ssl_id,
        "blockExploit": True,
        "accessControl": {
            "enabled": False
        }
    }
    
    response = requests.post(f"{NPM_URL}/api/nginx/hosts", headers=HEADERS, json=host_data)
    
    if response.status_code == 201:
        return response.json()  # Return the created host details
    else:
        raise Exception(f"Failed to create host: {response.content.decode()}")

def configure_nginx_proxy_manager(domain):
    """Main function to configure a new host in Nginx Proxy Manager."""
    try:
        ssl_id = create_ssl_certificate(domain)
        host_info = create_host(domain, ssl_id)
        print("Host created successfully:", json.dumps(host_info, indent=2))
        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Example domain to configure
    DOMAIN = "example.com"  # Change to your domain
    configure_nginx_proxy_manager(DOMAIN)
```

**Note:** Before running the script, ensure to replace placeholders such as `your-nginx-proxy-manager-url`, `your_api_key`, `your-backend-url`, and `example.com` with actual values suitable for your environment.
