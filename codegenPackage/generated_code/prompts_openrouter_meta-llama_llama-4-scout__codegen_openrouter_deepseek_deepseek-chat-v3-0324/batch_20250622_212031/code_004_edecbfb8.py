"""
Generated Code Metadata:
========================
Original URL: https://meteora-app-git-sam-racx-1186-ui-dynamic-pool-pa-2a19c8-wowcats.vercel.app
Prompt: Develop a function to calculate the 24-hour yield for a given Meteora pool, using the provided TVL and volume data.
Generated: DETERMINISTIC_edecbfb8c3c89717
Batch ID: 20250622_212031
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.meteora.ag": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, Optional

def calculate_24h_yield(
    pool_address: str,
    tvl_data: Dict[str, float],
    volume_data: Dict[str, float],
    api_key: Optional[str] = None
) -> float:
    """
    Calculate the 24-hour yield for a given Meteora pool.
    
    Args:
        pool_address: The address of the Meteora pool.
        tvl_data: Dictionary containing TVL (Total Value Locked) data.
                 Expected keys: 'current_tvl', 'previous_tvl'.
        volume_data: Dictionary containing volume data.
                   Expected keys: '24h_volume'.
        api_key: Optional API key for fetching data if not provided.
    
    Returns:
        The calculated 24-hour yield as a percentage.
    
    Raises:
        ValueError: If required data is missing or invalid.
        requests.exceptions.RequestException: If API request fails.
    """
    # Validate input data
    if not pool_address:
        raise ValueError("Pool address cannot be empty")
    
    required_tvl_keys = {'current_tvl', 'previous_tvl'}
    if not required_tvl_keys.issubset(tvl_data.keys()):
        raise ValueError(f"TVL data must contain {required_tvl_keys}")
    
    if '24h_volume' not in volume_data:
        raise ValueError("Volume data must contain '24h_volume'")
    
    current_tvl = tvl_data['current_tvl']
    previous_tvl = tvl_data['previous_tvl']
    daily_volume = volume_data['24h_volume']
    
    if current_tvl <= 0 or previous_tvl <= 0:
        raise ValueError("TVL values must be positive")
    
    if daily_volume < 0:
        raise ValueError("Volume cannot be negative")
    
    # Calculate yield
    try:
        # Calculate TVL change
        tvl_change = current_tvl - previous_tvl
        
        # Calculate yield percentage
        if previous_tvl > 0:
            yield_percentage = ((tvl_change + daily_volume) / previous_tvl) * 100
        else:
            yield_percentage = 0.0
        
        return yield_percentage
    except Exception as e:
        raise ValueError(f"Error calculating yield: {str(e)}")

def fetch_pool_data(pool_address: str, api_key: str) -> Dict:
    """
    Fetch TVL and volume data for a Meteora pool from the API.
    
    Args:
        pool_address: The address of the Meteora pool.
        api_key: API key for authentication.
    
    Returns:
        Dictionary containing 'tvl_data' and 'volume_data'.
    
    Raises:
        requests.exceptions.RequestException: If API request fails.
    """
    headers = {'Authorization': f'Bearer {api_key}'} if api_key else {}
    base_url = "https://api.meteora.ag"
    
    try:
        # Fetch TVL data
        tvl_response = requests.get(
            f"{base_url}/pools/{pool_address}/tvl",
            headers=headers
        )
        tvl_response.raise_for_status()
        tvl_data = tvl_response.json()
        
        # Fetch volume data
        volume_response = requests.get(
            f"{base_url}/pools/{pool_address}/volume",
            headers=headers
        )
        volume_response.raise_for_status()
        volume_data = volume_response.json()
        
        return {
            'tvl_data': {
                'current_tvl': tvl_data.get('current'),
                'previous_tvl': tvl_data.get('previous')
            },
            'volume_data': {
                '24h_volume': volume_data.get('volume_24h', 0)
            }
        }
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(
            f"Failed to fetch pool data: {str(e)}"
        )
```
