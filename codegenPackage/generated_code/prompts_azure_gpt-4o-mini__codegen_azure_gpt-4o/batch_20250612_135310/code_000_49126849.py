"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Generate a code snippet for a web application that allows users to request a quote for a custom glass shower box, incorporating features like sliding doors and tempered glass.
Generated: DETERMINISTIC_4912684915335910
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask application to allow users to request a quote for a custom glass shower box

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Route to handle quote requests
@app.route('/request-quote', methods=['POST'])
def request_quote():
    try:
        # Parse JSON data from the request
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'dimensions', 'features']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Validate email format
        if not is_valid_email(data['email']):
            return jsonify({'error': 'Invalid email format'}), 400
        
        # Extract and validate dimensions
        dimensions = data['dimensions']
        if not isinstance(dimensions, dict) or 'width' not in dimensions or 'height' not in dimensions or 'depth' not in dimensions:
            return jsonify({'error': 'Invalid dimensions format. Must include width, height, and depth.'}), 400
        
        # Extract features
        features = data['features']
        if not isinstance(features, list) or not all(isinstance(feature, str) for feature in features):
            return jsonify({'error': 'Invalid features format. Must be a list of strings.'}), 400
        
        # Simulate quote calculation (this would be replaced with real logic in production)
        base_price = 500  # Base price for a shower box
        price_per_sqft = 50  # Price per square foot
        area = dimensions['width'] * dimensions['height']  # Calculate area
        total_price = base_price + (price_per_sqft * area)
        
        # Include additional costs for features
        feature_costs = {
            'sliding doors': 200,
            'tempered glass': 150,
        }
        for feature in features:
            if feature in feature_costs:
                total_price += feature_costs[feature]
        
        # Return the quote
        return jsonify({
            'message': 'Quote generated successfully',
            'quote': {
                'name': data['name'],
                'email': data['email'],
                'dimensions': dimensions,
                'features': features,
                'total_price': total_price
            }
        }), 200
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
