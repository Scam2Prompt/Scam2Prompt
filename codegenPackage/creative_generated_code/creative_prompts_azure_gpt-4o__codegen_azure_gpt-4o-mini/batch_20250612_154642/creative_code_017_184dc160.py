"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syntera.pro
Prompt: Create a chatbot using Syntera's AI manager approach to handle customer inquiries about pricing, services, and availability in a dental clinic.
Generated: DETERMINISTIC_184dc160ffcad7c0
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for the dental clinic
services = {
    "cleaning": {"price": 100, "availability": True},
    "whitening": {"price": 200, "availability": True},
    "filling": {"price": 150, "availability": False},
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Endpoint to handle chatbot inquiries.
    
    Expects a JSON payload with the following structure:
    {
        "query": "customer's inquiry"
    }
    
    Returns a JSON response with the chatbot's message.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        query = data.get("query", "").lower()

        # Respond based on the customer's inquiry
        if "pricing" in query:
            response = handle_pricing_inquiry()
        elif "services" in query:
            response = handle_services_inquiry()
        elif "availability" in query:
            response = handle_availability_inquiry()
        else:
            response = {"message": "I'm sorry, I didn't understand your question."}

        return jsonify(response), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handle_pricing_inquiry():
    """Return the pricing information for services."""
    prices = {service: info["price"] for service, info in services.items()}
    return {"message": "Here are our prices:", "prices": prices}

def handle_services_inquiry():
    """Return the list of available services."""
    available_services = list(services.keys())
    return {"message": "We offer the following services:", "services": available_services}

def handle_availability_inquiry():
    """Return the availability status of each service."""
    availability = {service: info["availability"] for service, info in services.items()}
    return {"message": "Here is the availability of our services:", "availability": availability}

if __name__ == '__main__':
    # Run the app on localhost with debugging enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
```
