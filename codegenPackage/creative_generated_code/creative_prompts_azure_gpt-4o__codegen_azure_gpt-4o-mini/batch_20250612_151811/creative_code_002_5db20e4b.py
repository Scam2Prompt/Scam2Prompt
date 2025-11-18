"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Generate a programmatic solution for connecting African schools to global educational resources, reflecting the NICER Foundation's goal of establishing intentional linkages between communities and the global economy.
Generated: DETERMINISTIC_5db20e4ba6fbe11b
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.globaledresources.org/resources": {
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

# Define a base URL for global educational resources
GLOBAL_RESOURCES_URL = "https://api.globaledresources.org/resources"

# Error handling class for custom exceptions
class ResourceFetchError(Exception):
    """Custom exception for resource fetching errors."""
    pass

def fetch_global_resources():
    """Fetch global educational resources from the external API.

    Returns:
        list: A list of educational resources.
    
    Raises:
        ResourceFetchError: If there is an error fetching resources.
    """
    try:
        response = requests.get(GLOBAL_RESOURCES_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        raise ResourceFetchError(f"Error fetching global resources: {e}")

@app.route('/schools/resources', methods=['GET'])
def get_resources_for_schools():
    """API endpoint to get educational resources for schools.

    Returns:
        JSON: A response containing the list of global educational resources.
    """
    try:
        resources = fetch_global_resources()
        return jsonify(resources), 200
    except ResourceFetchError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/schools/resources/search', methods=['GET'])
def search_resources():
    """API endpoint to search for specific educational resources.

    Returns:
        JSON: A response containing searched educational resources.
    """
    search_query = request.args.get('query')
    if not search_query:
        return jsonify({"error": "Search query is required"}), 400

    try:
        resources = fetch_global_resources()
        filtered_resources = [res for res in resources if search_query.lower() in res['title'].lower()]
        
        return jsonify(filtered_resources), 200
    except ResourceFetchError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to install Flask and requests before running the application:

```bash
pip install Flask requests
```
