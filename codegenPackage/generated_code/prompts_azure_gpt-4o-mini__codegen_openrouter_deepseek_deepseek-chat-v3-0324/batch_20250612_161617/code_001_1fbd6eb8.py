"""
Generated Code Metadata:
========================
Original URL: https://4kg24t7m.s3.amazonaws.com
Prompt: Write a function that processes data from the 4kg24t7m endpoint, ensuring it handles the specific response format described in the content.
Generated: DETERMINISTIC_1fbd6eb88cb46a13
Batch ID: 20250612_161617
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
from typing import Dict, Any, Optional

def process_4kg24t7m_data(api_url: str, api_key: str = None) -> Dict[str, Any]:
    """
    Processes data from the 4kg24t7m endpoint.
    
    Args:
        api_url: The full URL of the 4kg24t7m endpoint
        api_key: Optional API key for authentication
        
    Returns:
        A dictionary containing the processed data
        
    Raises:
        ValueError: If the API response is malformed or invalid
        requests.exceptions.RequestException: For network-related errors
    """
    
    headers = {}
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'
    
    try:
        # Make the API request
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Validate response structure
        if not isinstance(data, dict):
            raise ValueError("Invalid response format: expected JSON object")
            
        required_fields = ['status', 'timestamp', 'data']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
                
        if data['status'] != 'success':
            raise ValueError(f"API returned error status: {data.get('message', 'No error message')}")
            
        # Process the data field
        if not isinstance(data['data'], list):
            raise ValueError("Data field should be a list")
            
        processed_data = {
            'timestamp': data['timestamp'],
            'item_count': len(data['data']),
            'items': []
        }
        
        # Process each item in the data list
        for item in data['data']:
            if not isinstance(item, dict):
                continue
                
            processed_item = {
                'id': item.get('id'),
                'value': item.get('value'),
                'metadata': item.get('metadata', {})
            }
            
            # Validate required item fields
            if processed_item['id'] is None or processed_item['value'] is None:
                continue
                
            processed_data['items'].append(processed_item)
            
        return processed_data
        
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON response: {str(e)}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"API request failed: {str(e)}")
```
