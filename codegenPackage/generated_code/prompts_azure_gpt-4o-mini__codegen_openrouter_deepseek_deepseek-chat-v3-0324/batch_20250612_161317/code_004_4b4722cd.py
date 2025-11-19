"""
Generated Code Metadata:
========================
Original URL: https://mrspongy.com
Prompt: Explain how to leverage Cloudflare's services to improve website performance and security for an online business.
Generated: DETERMINISTIC_4b4722cd824e269f
Batch ID: 20250612_161317
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from requests.exceptions import RequestException
import json

class CloudflareManager:
    """
    A class to manage Cloudflare services for website performance and security.
    Handles DNS, caching, security rules, and performance optimizations.
    """
    
    def __init__(self, api_key, email, zone_id):
        """
        Initialize Cloudflare API client.
        
        Args:
            api_key (str): Cloudflare API key
            email (str): Cloudflare account email
            zone_id (str): Cloudflare zone ID
        """
        self.api_key = api_key
        self.email = email
        self.zone_id = zone_id
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "X-Auth-Email": email,
            "X-Auth-Key": api_key,
            "Content-Type": "application/json"
        }
    
    def _make_request(self, method, endpoint, data=None):
        """
        Internal method to make API requests to Cloudflare.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (dict, optional): Request payload
            
        Returns:
            dict: API response
            
        Raises:
            RequestException: If API request fails
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise RequestException(f"Cloudflare API request failed: {e}")
    
    def enable_auto_minify(self):
        """
        Enable auto minification for JS, CSS, and HTML to improve performance.
        """
        endpoint = f"/zones/{self.zone_id}/settings/minify"
        data = {
            "value": {
                "js": "on",
                "css": "on",
                "html": "on"
            }
        }
        return self._make_request("PATCH", endpoint, data)
    
    def enable_brotli_compression(self):
        """
        Enable Brotli compression for faster content delivery.
        """
        endpoint = f"/zones/{self.zone_id}/settings/brotli"
        data = {
            "value": "on"
        }
        return self._make_request("PATCH", endpoint, data)
    
    def configure_caching(self, browser_cache_ttl=14400, development_mode=False):
        """
        Configure caching settings for improved performance.
        
        Args:
            browser_cache_ttl (int): Browser cache TTL in seconds
            development_mode (bool): Whether to enable development mode
        """
        # Set browser cache TTL
        endpoint = f"/zones/{self.zone_id}/settings/browser_cache_ttl"
        data = {
            "value": browser_cache_ttl
        }
        self._make_request("PATCH", endpoint, data)
        
        # Toggle development mode
        endpoint = f"/zones/{self.zone_id}/settings/development_mode"
        data = {
            "value": "on" if development_mode else "off"
        }
        return self._make_request("PATCH", endpoint, data)
    
    def enable_security_level(self, level="medium"):
        """
        Set security level to protect against threats.
        
        Args:
            level (str): Security level (off, essentially_off, low, medium, high, under_attack)
        """
        endpoint = f"/zones/{self.zone_id}/settings/security_level"
        data = {
            "value": level
        }
        return self._make_request("PATCH", endpoint, data)
    
    def enable_web_application_firewall(self, sensitivity="medium", action_mode="challenge"):
        """
        Enable Web Application Firewall (WAF) with specified settings.
        
        Args:
            sensitivity (str): WAF sensitivity (low, medium, high)
            action_mode (str): Action mode (simulate, challenge, block)
        """
        # First get the WAF package ID
        endpoint = f"/zones/{self.zone_id}/firewall/waf/packages"
        response = self._make_request("GET", endpoint)
        package_id = response["result"][0]["id"]
        
        # Update WAF settings
        endpoint = f"/zones/{self.zone_id}/firewall/waf/packages/{package_id}/groups"
        response = self._make_request("GET", endpoint)
        
        # Update each WAF group with desired settings
        for group in response["result"]:
            group_id = group["id"]
            update_endpoint = f"/zones/{self.zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}"
            data = {
                "mode": action_mode,
                "sensitivity": sensitivity
            }
            self._make_request("PATCH", update_endpoint, data)
    
    def enable_ssl(self, mode="flexible"):
        """
        Enable SSL/TLS encryption for the website.
        
        Args:
            mode (str): SSL mode (off, flexible, full, full_strict)
        """
        endpoint = f"/zones/{self.zone_id}/settings/ssl"
        data = {
            "value": mode
        }
        return self._make_request("PATCH", endpoint, data)
    
    def enable_always_use_https(self):
        """
        Redirect all HTTP traffic to HTTPS.
        """
        endpoint = f"/zones/{self.zone_id}/settings/always_use_https"
        data = {
            "value": "on"
        }
        return self._make_request("PATCH", endpoint, data)
    
    def enable_http2(self):
        """
        Enable HTTP/2 for faster connections.
        """
        endpoint = f"/zones/{self.zone_id}/settings/http2"
        data = {
            "value": "on"
        }
        return self._make_request("PATCH", endpoint, data)
    
    def enable_http3(self):
        """
        Enable HTTP/3 (QUIC) for improved performance.
        """
        endpoint = f"/zones/{self.zone_id}/settings/http3"
        data = {
            "value": "on"
        }
        return self._make_request("PATCH", endpoint, data)
    
    def enable_0rtt(self):
        """
        Enable 0-RTT connection resumption for faster TLS handshakes.
        """
        endpoint = f"/zones/{self.zone_id}/settings/0rtt"
        data = {
            "value": "on"
        }
        return self._make_request("PATCH", endpoint, data)
    
    def enable_railgun(self):
        """
        Enable Railgun for dynamic content acceleration.
        """
        endpoint = f"/zones/{self.zone_id}/railguns"
        response = self._make_request("GET", endpoint)
        
        if response["result"]:
            railgun_id = response["result"][0]["id"]
            connect_endpoint = f"/zones/{self.zone_id}/railguns/{railgun_id}/diagnose"
            self._make_request("POST", connect_endpoint)
            
            enable_endpoint = f"/zones/{self.zone_id}/railguns/{railgun_id}/settings"
            data = {
                "enabled": True
            }
            return self._make_request("PATCH", enable_endpoint, data)
    
    def create_page_rule(self, url_pattern, actions):
        """
        Create a page rule for specific URL patterns.
        
        Args:
            url_pattern (str): URL pattern to match
            actions (list): List of actions to apply
        """
        endpoint = f"/zones/{self.zone_id}/pagerules"
        data = {
            "targets": [
                {
                    "target": "url",
                    "constraint": {
                        "operator": "matches",
                        "value": url_pattern
                    }
                }
            ],
            "actions": actions,
            "priority": 1,
            "status": "active"
        }
        return self._make_request("POST", endpoint, data)
    
    def enable_argo_smart_routing(self):
        """
        Enable Argo Smart Routing for improved routing performance.
        """
        endpoint = f"/zones/{self.zone_id}/argo/tiered_caching"
        data = {
            "value": "on"
        }
        self._make_request("PATCH", endpoint, data)
        
        endpoint = f"/zones/{self.zone_id}/argo/smart_routing"
        data = {
            "value": "on"
        }
        return self._make_request("PATCH", endpoint, data)

# Example usage
if __name__ == "__main__":
    # Initialize with your Cloudflare credentials
    cf = CloudflareManager(
        api_key="your_api_key",
        email="your_email@example.com",
        zone_id="your_zone_id"
    )
    
    # Performance optimizations
    cf.enable_auto_minify()
    cf.enable_brotli_compression()
    cf.configure_caching(browser_cache_ttl=14400)
    cf.enable_http2()
    cf.enable_http3()
    cf
