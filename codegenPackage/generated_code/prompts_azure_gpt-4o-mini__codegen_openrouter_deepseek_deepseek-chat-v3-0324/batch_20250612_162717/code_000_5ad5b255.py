"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Generate a Python script that utilizes the PDC Brush API for managing private label cleaning products in retail.
Generated: DETERMINISTIC_5ad5b25506d77f49
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, List, Optional

class PDCBrushAPI:
    """
    A Python client for interacting with the PDC Brush API for managing private label cleaning products.
    
    Attributes:
        base_url (str): The base URL for the PDC Brush API.
        api_key (str): The API key for authentication.
        headers (dict): Default headers for API requests.
    """
    
    def __init__(self, api_key
