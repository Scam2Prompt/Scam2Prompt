"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Create a shareable link generator for a COVID-19 data visualization tool, ensuring the link includes parameters like selected region, scale, and data type as described on the webpage.
Generated: DETERMINISTIC_592aed0e50e0439d
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import urllib.parse
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to generate a shareable link with parameters
def generate_shareable_link(base_url, region, scale, data_type):
    """
    Generates a shareable link for the COVID-19 data visualization tool.
    
    Parameters:
    base_url (str): The base URL of the tool.
    region (str): The selected region (e.g., 'North America', 'Europe').
    scale (str): The scale of visualization (e.g., 'linear', 'logarithmic').
    data_type (str): The type of data to display (e.g., 'cases', 'deaths').
    
    Returns:
    str: A complete URL with encoded parameters.
    """
    try:
        # Parameter dictionary to be encoded in the URL
        params = {
            "region": region,
            "scale": scale,
            "data_type": data_type
        }
        
        # Encode parameters into the query string
        query_string = urllib.parse.urlencode(params)
        
        # Construct the full URL
        shareable_link = f"{base_url}?{query_string}"
        
        return shareable_link
    except Exception as e:
        # Error handling to catch unexpected issues
        raise ValueError(f"Failed to generate a shareable link: {e}")

@app.route('/generate_link', methods=['GET'])
def generate_link():
    """
    Flask route to generate a shareable link based on query parameters.
    
    Query Parameters:
    - base_url: The base URL of the COVID-19 visualization tool.
    - region: The selected region.
    - scale: The visualization scale.
    - data_type: The type of data to display.
    
    Returns:
    JSON response containing the generated link.
    """
    try:
        # Extract query parameters from the request
        base_url = request.args.get('base_url')
        region = request.args.get('region')
        scale = request.args.get('scale')
        data_type = request.args.get('data_type')
        
        # Validate required parameters
        if not base_url or not region or not scale or not data_type:
            return jsonify({"error": "Missing required parameters"}), 400
        
        # Generate the shareable link
        shareable_link = generate_shareable_link(base_url, region, scale, data_type)
        
        # Return the link in JSON format
        return jsonify({"shareable_link": shareable_link}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
