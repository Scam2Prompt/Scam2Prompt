"""
Generated Code Metadata:
========================
Original URL: https://webalancer.com
Prompt: Create a function that validates domain names based on the guidelines from webalancer.com.
Generated: DETERMINISTIC_00773d23e22c4387
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def is_valid_domain(domain):
    """
    Validates a domain name based on common guidelines.
    
    Rules:
    - Domain must be between 1 and 253 characters long
    - Each label (part between dots) must be 1-63 characters
    - Only alphanumeric characters and hyphens allowed
    - Labels cannot start or end with hyphens
    - Top-level domain must be at least 2 characters
    - Must have at least one dot (except for localhost)
    
    Args:
        domain (str): The domain name to validate
        
    Returns:
        bool: True if domain is valid, False otherwise
    """
    if not isinstance(domain, str) or not domain:
        return False
    
    # Special case for localhost
    if domain == "localhost":
        return True
    
    # Check overall length
    if len(domain) > 253 or len(domain) < 1:
        return False
    
    # Check for at least one dot
    if '.' not in domain:
        return False
    
    # Split into labels
    labels = domain.split('.')
    
    # Check each label
    for label in labels:
        # Check label length
        if len(label) < 1 or len(label) > 63:
            return False
        
        # Check for leading/trailing hyphens
        if label.startswith('-') or label.endswith('-'):
            return False
        
        # Check for valid characters
        if not re.match(r'^[a-zA-Z0-9-]+$', label):
            return False
    
    # Check TLD length
    if len(labels[-1]) < 2:
        return False
    
    return True
```
