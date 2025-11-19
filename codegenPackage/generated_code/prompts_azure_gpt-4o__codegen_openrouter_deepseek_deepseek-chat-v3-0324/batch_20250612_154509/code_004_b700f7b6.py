"""
Generated Code Metadata:
========================
Original URL: https://braveser.com
Prompt: Develop a Python program that simulates the Brave browser's cookie-blocking mechanism to prevent tracking during web browsing, based on the features described on Braveser.com.
Generated: DETERMINISTIC_b700f7b651fbb38d
Batch ID: 20250612_154509
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
import re
from typing import Dict, List, Optional, Set
from urllib.parse import urlparse

class CookieBlockingSimulator:
    """
    Simulates Brave browser's cookie-blocking mechanism to prevent tracking.
    Handles first-party and third-party cookies based on domain matching.
    """
    
    def __init__(self):
        # Domains that are allowed to set cookies (first-party)
        self.allowed_domains: Set[str] = set()
        
        # Cookies that have been blocked
        self.blocked_cookies: Dict[str, List[str]] = {}
        
        # Regular expression patterns for known trackers
        self.tracker_patterns = [
            r"\.doubleclick\.net$",
            r"\.google-analytics\.com$",
            r"\.facebook\.com$",
            r"\.twitter\.com$",
            r"\.scorecardresearch\.com$",
            r"\.hotjar\.com$",
            r"\.adsrvr\.org$",
            r"\.adnxs\.com$"
        ]
        
        # Compiled regex patterns for better performance
        self.compiled_tracker_patterns = [re.compile(pattern) for pattern in self.tracker_patterns]
    
    def is_tracker_domain(self, domain: str) -> bool:
        """
        Check if a domain matches known tracker patterns.
        
        Args:
            domain: The domain to check
            
        Returns:
            bool: True if domain matches tracker patterns, False otherwise
        """
        if not domain:
            return False
            
        for pattern in self.compiled_tracker_patterns:
            if pattern.search(domain):
                return True
        return False
    
    def get_base_domain(self, url: str) -> Optional[str]:
        """
        Extract the base domain from a URL.
        
        Args:
            url: The URL to parse
            
        Returns:
            str: The base domain or None if invalid URL
        """
        try:
            parsed = urlparse(url)
            if not parsed.netloc:
                return None
                
            # Simple domain extraction - in production would use more sophisticated parsing
            parts = parsed.netloc.split('.')
            if len(parts) >= 2:
                return '.'.join(parts[-2:])
            return parsed.netloc
        except Exception:
            return None
    
    def should_block_cookie(self, cookie_domain: str, site_domain: str) -> bool:
        """
        Determine if a cookie should be blocked based on Brave's rules.
        
        Args:
            cookie_domain: The domain attempting to set the cookie
            site_domain: The domain of the current website
            
        Returns:
            bool: True if cookie should be blocked, False otherwise
        """
        if not cookie_domain or not site_domain:
            return True
            
        # First-party cookies are allowed
        if cookie_domain == site_domain:
            return False
            
        # Check if cookie domain is a subdomain of site domain
        if cookie_domain.endswith(f".{site_domain}"):
            return False
            
        # Block known trackers
        if self.is_tracker_domain(cookie_domain):
            return True
            
        # Default to blocking third-party cookies
        return True
    
    def process_cookie(self, cookie_domain: str, site_url: str, cookie_name: str) -> bool:
        """
        Process a cookie request and determine if it should be blocked.
        
        Args:
            cookie_domain: The domain attempting to set the cookie
            site_url: The URL of the current website
            cookie_name: The name of the cookie
            
        Returns:
            bool: True if cookie was allowed, False if blocked
        """
        site_domain = self.get_base_domain(site_url)
        if not site_domain:
            return False
            
        if site_domain not in self.allowed_domains:
            self.allowed_domains.add(site_domain)
            
        if self.should_block_cookie(cookie_domain, site_domain):
            if site_domain not in self.blocked_cookies:
                self.blocked_cookies[site_domain] = []
            self.blocked_cookies[site_domain].append(f"{cookie_domain}:{cookie_name}")
            return False
            
        return True
    
    def get_blocked_cookies_report(self) -> Dict[str, List[str]]:
        """
        Get a report of all blocked cookies organized by site domain.
        
        Returns:
            Dict[str, List[str]]: Mapping of site domains to list of blocked cookies
        """
        return self.blocked_cookies.copy()

# Example usage
if __name__ == "__main__":
    simulator = CookieBlockingSimulator()
    
    # Simulate visiting a website
    current_site = "https://example.com"
    
    # Test cookies
    test_cookies = [
        ("example.com", current_site, "session_id"),  # First-party - allowed
        ("sub.example.com", current_site, "prefs"),   # Subdomain - allowed
        ("google-analytics.com", current_site, "ga_id"),  # Tracker - blocked
        ("facebook.com", current_site, "fb_tracker"),  # Tracker - blocked
        ("anothersite.com", current_site, "ad_id")    # Third-party - blocked
    ]
    
    for cookie_domain, site_url, cookie_name in test_cookies:
        allowed = simulator.process_cookie(cookie_domain, site_url, cookie_name)
        status = "ALLOWED" if allowed else "BLOCKED"
        print(f"Cookie {cookie_name} from {cookie_domain} on {site_url}: {status}")
    
    # Print blocked cookies report
    print("\nBlocked Cookies Report:")
    for site, cookies in simulator.get_blocked_cookies_report().items():
        print(f"\nSite: {site}")
        for cookie in cookies:
            print(f"  - {cookie}")
```
