"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Implement a library function that validates the structure of filenames based on the patterns observed in "5mev69v8" and similar files.
Generated: DETERMINISTIC_16bf3e44d9083443
Batch ID: 20250612_161520
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

def validate_filename(filename: str) -> Tuple[bool, Optional[str]]:
    """
    Validates the structure of a filename based on the pattern observed in "5mev69v8" and similar files.
    
    The expected pattern is:
    - 1 or more alphanumeric characters
    - Followed by 1 or more lowercase letters
    - Followed by 1 or more digits
    - Followed by 1 or more lowercase letters
    - Optional file extension (e.g., .txt, .jpg)
    
    Args:
        filename: The filename to validate
        
    Returns:
        A tuple containing:
        - bool: True if filename matches pattern, False otherwise
        - Optional[str]: Error message if validation fails, None otherwise
    """
    # Remove any leading/trailing whitespace
    filename = filename.strip()
    
    # Check if filename is empty
    if not filename:
        return False, "Filename cannot be empty"
    
    # Split into base name and extension
    parts = filename.rsplit('.', 1)
    base_name = parts[0]
    extension = parts[1] if len(parts) > 1 else None
    
    # Validate base name pattern
    pattern = r'^[a-zA-Z0-9]+[a-z]+\d+[a-z]+$'
    if not re.fullmatch(pattern, base_name):
        return False, f"Base name '{base_name}' does not match required pattern"
    
    # Validate extension if present
    if extension:
        ext_pattern = r'^[a-zA-Z0-9]{1,10}$'
        if not re.fullmatch(ext_pattern, extension):
            return False, f"Extension '{extension}' is invalid"
    
    return True, None
```
