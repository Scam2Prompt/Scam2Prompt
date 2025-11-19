"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safesteth.com
Prompt: Generate a code snippet for a web application that integrates an API to search for nearby doctors and clinics, similar to the functionality on SafeSteth.com.
Generated: DETERMINISTIC_d63b7ffddebe1a8d
Batch ID: 20250612_155417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/healthcare/search": {
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
# Flask application to integrate an API for searching nearby doctors and clinics
# Ensure you have Flask installed: pip install flask
# For API integration, you will need an API key for a service that provides location-specific healthcare data

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual API key and endpoint
API_KEY = "your_api_key_here"
API_ENDPOINT = "https://api.example.com/healthcare/search"

@app.route('/search', methods=['GET'])
def search_nearby():
    """
    Endpoint to search for nearby doctors and clinics.
    Expects 'location' and 'radius' as query parameters.
    """
    try:
        # Get query parameters from the request
        location = request.args.get('location')
        radius = request.args.get('radius', '10')  # Default radius is 10 km
        
        if not location:
            return jsonify({"error": "Location parameter is required"}), 400

        # Define the payload for the API request
        payload = {
            "location": location,
            "radius": radius,
            "apikey": API_KEY
        }

        # Make the API request
        response = requests.get(API_ENDPOINT, params=payload)

        # Check for HTTP errors
        response.raise_for_status()

        # Parse the response JSON
        data = response.json()

        # Return the data to the client
        return jsonify({
            "success": True,
            "data": data
        })

    except requests.exceptions.RequestException as e:
        # Handle API request errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Catch-all for other errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    # Ensure this is not used in production; use a proper WSGI server like Gunicorn
    app.run(debug=True)
```

### Notes:
- Replace `API_KEY` and `API_ENDPOINT` with actual values provided by the healthcare API you are integrating.
- The code assumes the API provider supports the `location` and `radius` parameters for filtering results. Adjust as needed based on the API specification.
- Install the required dependency using `pip install requests` if you haven't already.
- Ensure proper API key security measures (e.g., environment variables) when deploying to production.
