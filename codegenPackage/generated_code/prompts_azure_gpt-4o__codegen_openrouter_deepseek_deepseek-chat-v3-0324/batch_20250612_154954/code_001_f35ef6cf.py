"""
Generated Code Metadata:
========================
Original URL: https://pegasus-staging.vercel.app
Prompt: Generate a script to display a custom message for users in restricted regions, similar to the "Usual Interface Restricted region" message on the Pegasus website.
Generated: DETERMINISTIC_f35ef6cf3eed3a6a
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Script to display a custom message for users in restricted regions.
"""

import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import ipaddress
import geoip2.database
from typing import Optional, Dict, Any

# Configuration
CONFIG = {
    "host": "0.0.0.0",
    "port": 8080,
    "geoip_db_path": "GeoLite2-Country.mmdb",
    "restricted_countries": ["CU", "IR", "KP", "SY", "RU"],
    "message": {
        "title": "Restricted Region",
        "content": "Our service is not available in your region due to legal restrictions.",
        "status_code": 403
    }
}

class RestrictedRegionHandler(BaseHTTPRequestHandler):
    """HTTP request handler that checks for restricted regions."""
    
    def _get_client_ip(self) -> Optional[str]:
        """Extract client IP from request headers."""
        if 'X-Forwarded-For' in self.headers:
            return self.headers['X-Forwarded-For'].split(',')[0].strip()
        return self.client_address[0]
    
    def _get_country_code(self, ip_address: str) -> Optional[str]:
        """Get country code from IP address using GeoIP database."""
        try:
            with geoip2.database.Reader(CONFIG["geoip_db_path"]) as reader:
                response = reader.country(ip_address)
                return response.country.iso_code
        except (geoip2.errors.AddressNotFoundError, ValueError):
            return None
        except Exception as e:
            print(f"Error looking up country: {e}", file=sys.stderr)
            return None
    
    def _is_restricted_region(self, country_code: Optional[str]) -> bool:
        """Check if country is in restricted list."""
        if country_code is None:
            return False
        return country_code.upper() in CONFIG["restricted_countries"]
    
    def _send_restricted_message(self):
        """Send restricted region response."""
        self.send_response(CONFIG["message"]["status_code"])
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        
        response = {
            "error": {
                "code": CONFIG["message"]["status_code"],
                "message": CONFIG["message"]["content"],
                "title": CONFIG["message"]["title"]
            }
        }
        self.wfile.write(json.dumps(response).encode("utf-8"))
    
    def do_GET(self):
        """Handle GET requests."""
        client_ip = self._get_client_ip()
        
        try:
            # Validate IP address
            ipaddress.ip_address(client_ip)
        except ValueError:
            self.send_error(400, "Invalid IP address")
            return
        
        country_code = self._get_country_code(client_ip)
        
        if self._is_restricted_region(country_code):
            self._send_restricted_message()
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Welcome to our service!")

def run_server():
    """Run the HTTP server."""
    server_address = (CONFIG["host"], CONFIG["port"])
    httpd = HTTPServer(server_address, RestrictedRegionHandler)
    print(f"Server running on {CONFIG['host']}:{CONFIG['port']}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
```
