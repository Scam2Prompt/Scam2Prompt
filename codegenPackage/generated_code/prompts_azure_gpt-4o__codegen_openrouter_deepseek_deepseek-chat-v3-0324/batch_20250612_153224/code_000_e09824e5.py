"""
Generated Code Metadata:
========================
Original URL: https://corelabs.pe
Prompt: Write Python code to integrate two systems using APIs, ensuring interoperability and automation, as described in CoreLabs' approach to system integration.
Generated: DETERMINISTIC_e09824e50332bd16
Batch ID: 20250612_153224
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
import logging
from typing import Dict, Any, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class APIIntegrator:
    """
    A class to handle API integration between two systems.
    Implements CoreLabs' approach to system integration with:
    - Robust error handling
    - Retry mechanism
    - Data validation
    - Logging
    """

    def __init__(self, base_url_system1: str, base_url_system2: str, 
                 api_key_system1: str, api_key_system2: str,
                 timeout: int = 30):
        """
        Initialize the API integrator with system configurations.
        
        Args:
            base_url_system1: Base URL for System 1 API
            base_url_system2: Base URL for System 2 API
            api_key_system1: API key for System 1
            api_key_system2: API key for System 2
            timeout: Request timeout in seconds (default: 30)
        """
        self.base_url_system1 = base_url_system1
        self.base_url_system2 = base_url_system2
        self.api_key_system1 = api_key_system1
        self.api_key_system2 = api_key_system2
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def _make_request(self, url: str, method: str = 'GET', 
                     data: Optional[Dict[str, Any]] = None, 
                     headers: Optional[Dict[str, str]] = None,
                     system: str = 'system1',
                     max_retries: int = 3) -> Dict[str, Any]:
        """
        Internal method to make API requests with retry logic.
        
        Args:
            url: Endpoint URL
            method: HTTP method (GET, POST, PUT, etc.)
            data: Request payload
            headers: Additional headers
            system: Which system to call ('system1' or 'system2')
            max_retries: Maximum number of retries
            
        Returns:
            Response JSON as dictionary
            
        Raises:
            ValueError: If invalid system is specified
            requests.exceptions.RequestException: If request fails after retries
        """
        if system not in ['system1', 'system2']:
            raise ValueError("System must be either 'system1' or 'system2'")

        base_url = self.base_url_system1 if system == 'system1' else self.base_url_system2
        api_key = self.api_key_system1 if system == 'system1' else self.api_key_system2
        
        full_url = f"{base_url}{url}"
        headers = headers or {}
        headers['Authorization'] = f"Bearer {api_key}"
        
        for attempt in range(max_retries):
            try:
                logger.info(f"Making {method} request to {full_url} (attempt {attempt + 1})")
                response = self.session.request(
                    method,
                    full_url,
                    json=data,
                    headers=headers,
                    timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                logger.warning(f"Request failed: {str(e)}")
                if attempt == max_retries - 1:
                    logger.error(f"Max retries reached for {full_url}")
                    raise
                continue

    def sync_data(self, source_endpoint: str, target_endpoint: str, 
                 data_mapping: Dict[str, str]) -> Dict[str, Any]:
        """
        Synchronize data from System 1 to System 2 using specified mapping
