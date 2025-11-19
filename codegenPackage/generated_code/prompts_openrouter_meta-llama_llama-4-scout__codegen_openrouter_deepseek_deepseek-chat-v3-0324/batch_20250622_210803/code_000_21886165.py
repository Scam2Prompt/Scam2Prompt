"""
Generated Code Metadata:
========================
Original URL: https://web3walletsolutions.pages.dev
Prompt: What are common error responses for restricted access on a web server, and how do they relate to LiteSpeed Web Server configurations?
Generated: DETERMINISTIC_218861651490335f
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from http import HTTPStatus
from typing import Dict

# Common HTTP error responses for restricted access
RESTRICTED_ACCESS_ERRORS: Dict[int, str] = {
    HTTPStatus.FORBIDDEN.value: "403 Forbidden - The server understood the request but refuses to authorize it.",
    HTTPStatus.UNAUTHORIZED.value: "401 Unauthorized - Authentication is required and has failed or not been provided.",
    HTTPStatus.NOT_FOUND.value: "404 Not Found - The requested resource could not be found.",
    HTTPStatus.METHOD_NOT_ALLOWED.value: "405 Method Not Allowed - The method specified in the request is not allowed.",
    HTTPStatus.TOO_MANY_REQUESTS.value: "429 Too Many Requests - The user has sent too many requests in a given time.",
}

# LiteSpeed specific configuration mappings
LITESPEED_CONFIG_MAPPINGS: Dict[str, Dict[str, str]] = {
    "403": {
        "config_key": "accessDeniedDir",
        "description": "Controls access to directories when forbidden",
    },
    "401": {
        "config_key": "realm",
        "description": "Defines the authentication realm for basic auth",
    },
    "404": {
        "config_key": "errorPage",
        "description": "Custom error page for not found resources",
    },
    "405": {
        "config_key": "allowedMethods",
        "description": "Specifies allowed HTTP methods",
    },
    "429": {
        "config_key": "throttle",
        "description": "Controls request throttling settings",
    },
}

def get_error_configuration(error_code: int) -> Dict[str, str]:
    """
    Retrieves LiteSpeed configuration details for a given HTTP error code.
    
    Args:
        error_code: HTTP status code to look up
        
    Returns:
        Dictionary containing configuration details
        
    Raises:
        ValueError: If the error code is not found in the mappings
    """
    error_str = str(error_code)
    if error_str not in LITESPEED_CONFIG_MAPPINGS:
        raise ValueError(f"No LiteSpeed configuration found for error code {error_code}")
    
    return LITESPEED_CONFIG_MAPPINGS[error_str]

def get_error_description(error_code: int) -> str:
    """
    Retrieves standard description for a given HTTP error code.
    
    Args:
        error_code: HTTP status code to look up
        
    Returns:
        String description of the error
        
    Raises:
        ValueError: If the error code is not found in the standard responses
    """
    if error_code not in RESTRICTED_ACCESS_ERRORS:
        raise ValueError(f"No standard description found for error code {error_code}")
    
    return RESTRICTED_ACCESS_ERRORS[error_code]
```
