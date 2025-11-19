"""
Generated Code Metadata:
========================
Original URL: https://migrate-cheqd.pages.dev
Prompt: Create a function to retrieve the Cloudflare Ray ID and user IP address from a webpage content.
Generated: DETERMINISTIC_d449264fac9064bf
Batch ID: 20250622_210436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Optional, Tuple

def extract_cloudflare_info(html_content: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extracts Cloudflare Ray ID and user IP address from webpage HTML content.
    
    Args:
        html_content: Raw HTML content of the webpage.
        
    Returns:
        Tuple containing (ray_id, ip_address). Both can be None if not found.
    """
    ray_id = None
    ip_address = None
    
    # Extract Ray ID (pattern: e.g., Ray ID: 7e3b4a5b6c7d8e9f)
    ray_id_pattern = r"Ray ID:\s*([0-9a-f]+)"
    ray_match = re.search(ray_id_pattern, html_content, re.IGNORECASE)
    if ray_match:
        ray_id = ray_match.group(1)
    
    # Extract IP address (pattern: e.g., Your IP: 192.168.1.1)
    ip_pattern = r"Your IP.*?([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
    ip_match = re.search(ip_pattern, html_content, re.IGNORECASE)
    if ip_match:
        ip_address = ip_match.group(1)
    
    return (ray_id, ip_address)
```
