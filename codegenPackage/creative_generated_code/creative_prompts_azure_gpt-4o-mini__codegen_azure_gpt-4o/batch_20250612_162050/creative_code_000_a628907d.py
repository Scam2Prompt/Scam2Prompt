"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nellyservis.sk
Prompt: Generate a code snippet for a web application that allows users to request a quote for window installation services, similar to the offerings on NellyServis.
Generated: DETERMINISTIC_a628907d6c5e10f8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for simplicity. Replace with a database in production.
quotes = []

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to request a quote for window installation services.
    Expects JSON input with user's details and window specifications.
    """
    try:
        # Parse and validate input data
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input. JSON body is required."}), 400

        required_fields = ['name', 'email', 'phone', 'window_type', 'dimensions', 'quantity']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Create a quote request object
        quote_request = {
            "id": len(quotes) + 1,  # Simple incremental ID, replace with UUID in production
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "window_type": data['window_type'],
            "dimensions": data['dimensions'],
            "quantity": data['quantity']
        }
        
        # Store the quote request (temporary in-memory storage)
        quotes.append(quote_request)
        
        # Return success response
        return jsonify({
            "message": "Quote request submitted successfully.",
            "quote_id": quote_request["id"]
        }), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/quotes', methods=['GET'])
def get_quotes():
    """
    Endpoint to retrieve all quote requests (for demonstration purposes only).
    In production, implement authentication/authorization to restrict access.
    """
    return jsonify(quotes), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
