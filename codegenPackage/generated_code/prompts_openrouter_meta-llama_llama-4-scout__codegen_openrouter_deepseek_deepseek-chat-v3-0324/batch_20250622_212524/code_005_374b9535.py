"""
Generated Code Metadata:
========================
Original URL: https://www.garygeng.net
Prompt: Develop a regular expression pattern to extract relevant information from Clash node subscription links and URLs.
Generated: DETERMINISTIC_374b95359219421d
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Optional, Dict

def extract_clash_node_info(url: str) -> Optional[Dict[str, str]]:
    """
    Extracts relevant information from a Clash node subscription URL.
    
    Args:
        url: The subscription URL to parse.
        
    Returns:
        A dictionary containing extracted information (name, server, port, etc.),
        or None if no match is found.
    """
    # Pattern to match common Clash subscription URL formats
    pattern = re.compile(
        r'(?:clash://|https?://)(?P<server>[^:/]+)(?::(?P<port>\d+))?'  # Server and port
        r'(?:/(?P<name>[^/?]+))?'                                       # Optional name
        r'(?:\?|&)?(?:remarks=(?P<remarks>[^&]+))?'                     # Optional remarks
        r'(?:&?password=(?P<password>[^&]+))?'                          # Optional password
        r'(?:&?type=(?P<type>[^&]+))?'                                  # Optional type
        r'(?:&?encrypt=(?P<encrypt>[^&]+))?'                            # Optional encryption
        r'(?:&?obfs=(?P<obfs>[^&]+))?'                                  # Optional obfuscation
        r'(?:&?protocol=(?P<protocol>[^&]+))?'                          # Optional protocol
        r'(?:&?path=(?P<path>[^&]+))?'                                  # Optional path
        r'(?:&?host=(?P<host>[^&]+))?'                                  # Optional host
        r'(?:&?tls=(?P<tls>[^&]+))?'                                    # Optional TLS
        r'(?:.*)?$', re.IGNORECASE
    )
    
    match = pattern.search(url)
    if not match:
        return None
        
    # Extract groups and filter out None values
    result = {k: v for k, v in match.groupdict().items() if v is not None}
    
    # Clean up URL-encoded values if present
    if 'remarks' in result:
        result['remarks'] = re.sub(r'%20', ' ', result['remarks'])
    if 'name' in result:
        result['name'] = re.sub(r'%20', ' ', result['name'])
    
    return result
```
