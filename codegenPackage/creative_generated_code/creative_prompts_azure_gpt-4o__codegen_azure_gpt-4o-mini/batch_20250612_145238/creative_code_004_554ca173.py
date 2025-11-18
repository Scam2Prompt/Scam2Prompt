"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Create a REST API endpoint that allows users to query the pricing details for Playland Kenya’s services, including child packages, virtual reality, and PlayStation 5 sessions.
Generated: DETERMINISTIC_554ca173074e6e90
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample data for Playland Kenya's services
pricing_details = {
    'child_packages': {
        'basic': {
            'price': 500,
            'description': 'Basic package for children aged 3-7 years.'
        },
        'premium': {
            'price': 800,
            'description': 'Premium package with additional activities for children aged 3-7 years.'
        }
    },
    'virtual_reality': {
        'session': {
            'price': 1500,
            'description': 'One hour virtual reality session.'
        }
    },
    'playstation_5': {
        'session': {
            'price': 1200,
            'description': 'One hour PlayStation 5 gaming session.'
        }
    }
}

class Pricing(Resource):
    """Endpoint to retrieve pricing details for Playland Kenya's services."""

    def get(self):
        """Handle GET requests to retrieve pricing details."""
        try:
            service_type = request.args.get('service_type')
            if service_type not in pricing_details:
                return {'error': 'Invalid service type. Please choose from child_packages, virtual_reality, or playstation_5.'}, 400
            
            return jsonify(pricing_details[service_type])
        
        except Exception as e:
            # Log the error (placeholder for actual logging)
            print(f"An error occurred: {str(e)}")
            return {'error': 'An unexpected error occurred. Please try again later.'}, 500

# Register the API endpoint
api.add_resource(Pricing, '/api/pricing')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
