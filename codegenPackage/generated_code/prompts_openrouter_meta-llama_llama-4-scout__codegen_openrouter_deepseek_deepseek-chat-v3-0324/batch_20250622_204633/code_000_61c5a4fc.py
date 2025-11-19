"""
Generated Code Metadata:
========================
Original URL: https://dogem.life
Prompt: What are common reasons for a website displaying a "not properly configured or disabled" message, and how can I troubleshoot such an issue?
Generated: DETERMINISTIC_61c5a4fce9cba6f6
Batch ID: 20250622_204633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from urllib.parse import urlparse

def check_website_configuration(url):
    """
    Checks common configuration issues that might cause a website to display
    a 'not properly configured or disabled' message.
    
    Args:
        url (str): The URL of the website to check
        
    Returns:
        dict: Dictionary containing check results and suggestions
    """
    results = {
        'url': url,
        'is_reachable': False,
        'status_code': None,
        'server_header': None,
        'content_type': None,
        'content_length': None,
        'issues': [],
        'suggestions': []
    }
    
    try:
        # Validate URL format
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("Invalid URL format")
            
        # Make HEAD request first to check basic availability
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            results['status_code'] = response.status_code
            results['is_reachable'] = True
        except requests.exceptions.RequestException as e:
            results['issues'].append(f"Connection failed: {str(e)}")
            results['suggestions'].append("Check network connectivity and DNS resolution")
            return results
            
        # Check for common error status codes
        if response.status_code >= 400:
            results['issues'].append(f"HTTP error: {response.status_code}")
            
            if response.status_code == 403:
                results['suggestions'].append("Check server permissions and .htaccess files")
            elif response.status_code == 404:
                results['suggestions'].append("Check if requested resource exists")
            elif response.status_code == 500:
                results['suggestions'].append("Check server error logs for details")
            elif response.status_code == 503:
                results['suggestions'].append("Check if service is temporarily unavailable")
                
        # Get server headers
        results['server_header'] = response.headers.get('Server', 'Not specified')
        results['content_type'] = response.headers.get('Content-Type', 'Not specified')
        results['content_length'] = response.headers.get('Content-Length', 'Not specified')
        
        # Check for maintenance mode
        if 'maintenance' in response.headers.get('X-Mode', '').lower():
            results['issues'].append("Website might be in maintenance mode")
            results['suggestions'].append("Check with site administrator")
            
        # Check for common misconfigurations
        if 'Server' not in response.headers:
            results['issues'].append("Server header not exposed (security best practice)")
            
        if 'Content-Type' not in response.headers:
            results['issues'].append("Content-Type header missing")
            results['suggestions'].append("Configure proper Content-Type headers")
            
        # If we got this far without issues but still seeing the message, suggest content check
        if not results['issues']:
            results['suggestions'].append("Check website content files and configuration")
            
    except Exception as e:
        results['issues'].append(f"General error during check: {str(e)}")
        
    return results

def troubleshoot_website(url):
    """
    Main troubleshooting function that runs checks and prints results.
    
    Args:
        url (str): The URL of the website to troubleshoot
    """
    print(f"\nTroubleshooting website: {url}")
    print("=" * 50)
    
    results = check_website_configuration(url)
    
    if not results['is_reachable']:
        print("❌ Website is not reachable")
        for issue in results['issues']:
            print(f" - {issue}")
        for suggestion in results['suggestions']:
            print(f"🔧 Suggestion: {suggestion}")
        return
    
    print(f"✅ Website is reachable (HTTP {results['status_code']})")
    print(f"Server: {results['server_header']}")
    print(f"Content-Type: {results['content_type']}")
    
    if results['issues']:
        print("\n⚠️ Potential issues found:")
        for issue in results['issues']:
            print(f" - {issue}")
            
    if results['suggestions']:
        print("\n🔧 Suggested actions:")
        for suggestion in results['suggestions']:
            print(f" - {suggestion}")
    else:
        print("\nNo obvious configuration issues detected. Check website content and application configuration.")

# Example usage
if __name__ == "__main__":
    website_url = input("Enter website URL to check (include http/https): ")
    troubleshoot_website(website_url)
```
