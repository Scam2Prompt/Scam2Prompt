"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-app-git-sam-racx-1186-ui-dynamic-pool-pa-2a19c8-wowcats.vercel.app
Prompt: Develop code to integrate Meteora Pools with a decentralized finance (DeFi) portfolio tracker, focusing on dynamic pool data.
Generated: DETERMINISTIC_64bc2dc3cdd02291
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.meteora.pools/v1/pools": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Constants
METEORA_API_URL = "https://api.meteora.pools/v1/pools"

def fetch_pool_data():
    """
    Fetches the dynamic pool data from Meteora Pools API.
    
    Returns:
        dict: A dictionary containing pool data if successful, 
              or an error message if the request fails.
    """
    try:
        response = requests.get(METEORA_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Returns pool data as a dictionary
    except requests.exceptions.HTTPError as http_err:
        return {'error': f'HTTP error occurred: {http_err}'}
    except Exception as err:
        return {'error': f'An error occurred: {err}'}

@app.route('/api/pools', methods=['GET'])
def get_pools():
    """
    API endpoint to get the latest pool data.
    
    Returns:
        JSON response with pool data or an error message.
    """
    pool_data = fetch_pool_data()
    return jsonify(pool_data)

@app.route('/api/pools/<string:pool_id>', methods=['GET'])
def get_pool_by_id(pool_id):
    """
    API endpoint to get details of a specific pool by its ID.
    
    Args:
        pool_id (str): The unique identifier for the pool.
        
    Returns:
        JSON response with pool details or an error message.
    """
    pool_data = fetch_pool_data()
    
    if 'error' in pool_data:
        return jsonify(pool_data), 500
    
    pool_detail = next((pool for pool in pool_data['pools'] if pool['id'] == pool_id), None)

    if pool_detail:
        return jsonify(pool_detail)
    else:
        return jsonify({'error': 'Pool not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Make sure to install the required dependencies using:
```bash
pip install Flask requests
```

This code provides a basic Flask application that fetches dynamic pool data from the Meteora Pools API and serves it through a JSON API. It includes error handling for both HTTP requests and possible data issues.
