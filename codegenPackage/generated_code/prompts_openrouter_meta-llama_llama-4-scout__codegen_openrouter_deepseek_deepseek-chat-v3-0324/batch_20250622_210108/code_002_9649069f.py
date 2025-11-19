"""
Generated Code Metadata:
========================
Original URL: https://waltztechsec.com
Prompt: Generate code for a basic geo-location service using IP geolocation or device tracking, inspired by WaltzTech Security's geo-location services.
Generated: DETERMINISTIC_9649069f0a236134
Batch ID: 20250622_210108
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://ip-api.com/json/{ip_address": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.ipify.org?format=json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.ipgeolocation.io/ipgeo?apiKey={self.api_key}&ip={ip_address": {
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
import json
import socket
from functools import lru_cache
from typing import Optional, Dict, Any
from ipaddress import ip_address

class GeoLocationService:
    """
    A basic geo-location service that uses IP geolocation APIs.
    Inspired by WaltzTech Security's geo-location services.
    """
    
    def __init__(self, api_key: str = None, api_provider: str = "ipapi"):
        """
        Initialize the GeoLocationService with API configuration.
        
        Args:
            api_key (str): API key for the geolocation service provider
            api_provider (str): Service provider ('ipapi' or 'ipgeolocation')
        """
        self.api_key = api_key
        self.api_provider = api_provider.lower()
        
        if self.api_provider not in ["ipapi", "ipgeolocation"]:
            raise ValueError("Invalid API provider. Choose 'ipapi' or 'ipgeolocation'")
    
    def _get_public_ip(self) -> str:
        """
        Get the public IP address of the current device.
        
        Returns:
            str: Public IP address
            
        Raises:
            RuntimeError: If unable to determine public IP
        """
        try:
            response = requests.get('https://api.ipify.org?format=json')
            response.raise_for_status()
            return response.json()['ip']
        except Exception as e:
            raise RuntimeError(f"Failed to get public IP: {str(e)}")
    
    def _validate_ip(self, ip: str) -> bool:
        """
        Validate if the given string is a valid IP address.
        
        Args:
            ip (str): IP address to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            ip_address(ip)
            return True
        except ValueError:
            return False
    
    @lru_cache(maxsize=128)
    def get_location(self, ip_address: Optional[str] = None) -> Dict[str, Any]:
        """
        Get geolocation information for an IP address.
        
        Args:
            ip_address (str, optional): IP address to lookup. If None, uses current device's IP.
            
        Returns:
            dict: Dictionary containing geolocation information
            
        Raises:
            ValueError: If IP address is invalid
            RuntimeError: If API request fails
        """
        if ip_address is None:
            ip_address = self._get_public_ip()
        
        if not self._validate_ip(ip_address):
            raise ValueError(f"Invalid IP address: {ip_address}")
        
        try:
            if self.api_provider == "ipapi":
                url = f"http://ip-api.com/json/{ip_address}"
                if self.api_key:
                    url += f"?access_key={self.api_key}"
            else:  # ipgeolocation
                if not self.api_key:
                    raise ValueError("API key is required for ipgeolocation provider")
                url = f"https://api.ipgeolocation.io/ipgeo?apiKey={self.api_key}&ip={ip_address}"
            
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if self.api_provider == "ipapi" and data.get('status') == 'fail':
                raise RuntimeError(data.get('message', 'API request failed'))
            
            return self._standardize_response(data)
        
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request failed: {str(e)}")
    
    def _standardize_response(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Standardize the response format across different providers.
        
        Args:
            data (dict): Raw API response
            
        Returns:
            dict: Standardized geolocation data
        """
        if self.api_provider == "ipapi":
            return {
                'ip': data.get('query', ''),
                'country': data.get('country', ''),
                'country_code': data.get('countryCode', ''),
                'region': data.get('regionName', ''),
                'city': data.get('city', ''),
                'zip': data.get('zip', ''),
                'latitude': data.get('lat', 0),
                'longitude': data.get('lon', 0),
                'timezone': data.get('timezone', ''),
                'isp': data.get('isp', ''),
                'organization': data.get('org', ''),
                'as_number': data.get('as', '')
            }
        else:  # ipgeolocation
            return {
                'ip': data.get('ip', ''),
                'country': data.get('country_name', ''),
                'country_code': data.get('country_code2', ''),
                'region': data.get('state_prov', ''),
                'city': data.get('city', ''),
                'zip': data.get('zipcode', ''),
                'latitude': float(data.get('latitude', 0)),
                'longitude': float(data.get('longitude', 0)),
                'timezone': data.get('time_zone', {}).get('name', ''),
                'isp': data.get('isp', ''),
                'organization': data.get('organization', ''),
                'as_number': data.get('asn', '')
            }
    
    def get_current_location(self) -> Dict[str, Any]:
        """
        Get geolocation information for the current device.
        
        Returns:
            dict: Dictionary containing geolocation information
        """
        return self.get_location()
```
