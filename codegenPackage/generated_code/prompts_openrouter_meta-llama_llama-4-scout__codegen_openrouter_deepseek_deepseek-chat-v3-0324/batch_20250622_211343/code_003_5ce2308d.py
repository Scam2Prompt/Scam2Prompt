"""
Generated Code Metadata:
========================
Original URL: https://webmail.omninetwork.it
Prompt: What are the system requirements for cPanel & WHM, specifically regarding browser compatibility?
Generated: DETERMINISTIC_5ce2308dfa3f2e8d
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script checks browser compatibility for cPanel & WHM based on official system requirements.
# It provides a list of supported browsers and their minimum versions.

def get_cpanel_whm_browser_compatibility():
    """
    Returns a dictionary of supported browsers and their minimum versions for cPanel & WHM.
    
    Returns:
        dict: A dictionary with browser names as keys and minimum supported versions as values.
    """
    # Data sourced from official cPanel & WHM documentation
    browser_compatibility = {
        "Google Chrome": "Latest stable version",
        "Mozilla Firefox": "Latest stable version",
        "Microsoft Edge": "Latest stable version",
        "Safari": "Latest stable version",
        "Opera": "Latest stable version",
        # Note: Internet Explorer is not supported
    }
    
    return browser_compatibility

def check_browser_compatibility(browser_name, browser_version):
    """
    Checks if a browser is compatible with cPanel & WHM.
    
    Args:
        browser_name (str): Name of the browser to check.
        browser_version (str): Version of the browser to check.
        
    Returns:
        bool: True if compatible, False otherwise.
        str: Additional message about compatibility.
    """
    supported_browsers = get_cpanel_whm_browser_compatibility()
    
    # Convert to lowercase for case-insensitive comparison
    browser_name_lower = browser_name.lower()
    
    # Check if browser is supported
    for supported_browser in supported_browsers:
        if browser_name_lower in supported_browser.lower():
            return True, f"{browser_name} is supported. Recommended: {supported_browsers[supported_browser]}"
    
    return False, f"{browser_name} is not officially supported by cPanel & WHM."

# Example usage
if __name__ == "__main__":
    # Test with a supported browser
    compatible, message = check_browser_compatibility("Chrome", "100.0")
    print(f"Compatibility Check: {message}")
    
    # Test with an unsupported browser
    compatible, message = check_browser_compatibility("Internet Explorer", "11.0")
    print(f"Compatibility Check: {message}")
```
