"""
Generated Code Metadata:
========================
Original URL: https://galanetwork.net
Prompt: Develop code to integrate SDNS递归云 services into a network monitoring tool, ensuring compatibility with IPv4 and IPv6 protocols as discussed on the 中国互联网络信息中心 website.
Generated: DETERMINISTIC_357bf59686bd45c5
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import requests
import ipaddress
from typing import Optional, Union, Dict, Any

class SDNSRecursiveCloudIntegration:
    """
    Integrates SDNS recursive cloud services into a network monitoring tool.
    Supports both IPv4 and IPv6 protocols.
    """
    
    def __init__(self, api_endpoint: str, api_key: str, timeout: int = 10):
        """
        Initialize the SDNS recursive cloud integration.
        
        Args:
            api_endpoint: Base URL for the SDNS API
            api_key: Authentication key for the API
            timeout: Request timeout in seconds (default: 10)
        """
        self.api_endpoint = api_endpoint.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def _validate_ip(self, ip_address: str) -> bool:
        """
        Validate if the given string is a valid IPv4 or IPv6 address.
        
        Args:
            ip_address: IP address to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            ipaddress.ip_address(ip_address)
            return True
        except ValueError:
            return False
    
    def _make_request(self, method: str, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make an API request to the SDNS service.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            path: API endpoint path
            data: Optional payload for the request
            
        Returns:
            Dict: JSON response from the API
            
        Raises:
            requests.exceptions.RequestException: If the request fails
            ValueError: If the response is not valid JSON or contains errors
        """
        url = f"{self.api_endpoint}/{path.lstrip('/')}"
        try:
            response = requests.request(
                method,
                url,
                json=data,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response: {e}")
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API request failed: {e}")
    
    def query_dns_records(self, domain: str, record_type: str = 'A') -> Dict[str, Any]:
        """
        Query DNS records for a domain using SDNS recursive cloud.
        
        Args:
            domain: Domain name to query
            record_type: DNS record type (A, AAAA, MX, etc.)
            
        Returns:
            Dict: DNS records information
            
        Raises:
            ValueError: If domain is invalid or record type is unsupported
        """
        if not domain or not isinstance(domain, str):
            raise ValueError("Domain must be a non-empty string")
        
        valid_types = {'A', 'AAAA', 'MX', 'CNAME', 'TXT', 'NS'}
        if record_type.upper() not in valid_types:
            raise ValueError(f"Unsupported record type: {record_type}")
        
        return self._make_request('GET', f'/dns/query?domain={domain}&type={record_type}')
    
    def check_ip_reputation(self, ip_address: str) -> Dict[str, Any]:
        """
        Check the reputation of an IP address using SDNS services.
        
        Args:
            ip_address: IPv4 or IPv6 address to check
            
        Returns:
            Dict: Reputation information
            
        Raises:
            ValueError: If IP address is invalid
        """
        if not self._validate_ip(ip_address):
            raise ValueError(f"Invalid IP address: {ip_address}")
        
        return self._make_request('GET', f'/reputation/check?ip={ip_address}')
    
    def get_network_statistics(self, protocol: str = 'both') -> Dict[str, Any]:
        """
        Get network statistics from SDNS recursive cloud.
        
        Args:
            protocol: 'ipv4', 'ipv6', or 'both' (default)
            
        Returns:
            Dict: Network statistics
            
        Raises:
            ValueError: If protocol is invalid
        """
        valid_protocols = {'ipv4', 'ipv6', 'both'}
        if protocol.lower() not in valid_protocols:
            raise ValueError(f"Invalid protocol: {protocol}")
        
        return self._make_request('GET', f'/stats/network?protocol={protocol.lower()}')
    
    def resolve_hostname(self, hostname: str, ip_version: int = 0) -> Dict[str, Any]:
        """
        Resolve a hostname to IP address(es) using SDNS recursive cloud.
        
        Args:
            hostname: Hostname to resolve
            ip_version: 4 for IPv4, 6 for IPv6, 0 for both (default)
            
        Returns:
            Dict: Resolution results
            
        Raises:
            ValueError: If hostname is invalid or IP version is unsupported
        """
        if not hostname or not isinstance(hostname, str):
            raise ValueError("Hostname must be a non-empty string")
        
        if ip_version not in {0, 4, 6}:
            raise ValueError("IP version must be 0 (both), 4 (IPv4), or 6 (IPv6)")
        
        params = {'hostname': hostname}
        if ip_version != 0:
            params['version'] = ip_version
            
        return self._make_request('GET', '/resolve', params)
```
