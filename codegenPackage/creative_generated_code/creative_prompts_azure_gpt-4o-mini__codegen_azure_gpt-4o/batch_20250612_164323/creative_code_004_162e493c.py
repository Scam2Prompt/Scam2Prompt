"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Suggest a REST API design for a company like Apos that allows users to request quotes for thermal paper products.
Generated: DETERMINISTIC_162e493ce3df51c3
Batch ID: 20250612_164323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample in-memory database for storing quotes (in production use a proper database)
quotes_db = []

# Error response model
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Endpoint: Health Check
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify if the API is running.
    """
    return jsonify({"status": "API is running"}), 200

# Endpoint: Request a Quote
@app.route('/api/quotes', methods=['POST'])
def request_quote():
    """
    Create a new quote request for thermal paper products.
    Expects JSON input with the following fields:
    - product_type: str (Type of thermal paper product)
    - quantity: int (Quantity of the product required)
    - contact_info: str (User contact information)
    """
    try:
        data = request.get_json()

        # Input validation
        required_fields = ["product_type", "quantity", "contact_info"]
        for field in required_fields:
            if field not in data:
                return error_response(f"'{field}' is a required field.", 400)
        
        # Validate quantity
        if not isinstance(data['quantity'], int) or data['quantity'] <= 0:
            return error_response("'quantity' must be a positive integer.", 400)

        # Generate quote ID and store in the database
        quote_id = len(quotes_db) + 1
        new_quote = {
            "id": quote_id,
            "product_type": data['product_type'],
            "quantity": data['quantity'],
            "contact_info": data['contact_info'],
            "status": "pending"  # Default status for new quotes
        }
        quotes_db.append(new_quote)

        return jsonify({"message": "Quote request created successfully", "quote_id": quote_id}), 201
    except Exception as e:
        return error_response("An error occurred while processing the request.", 500)

# Endpoint: Retrieve All Quotes
@app.route('/api/quotes', methods=['GET'])
def get_all_quotes():
    """
    Fetch all quotes requested.
    Returns a list of all requested quotes in JSON format.
    """
    return jsonify({"quotes": quotes_db}), 200

# Endpoint: Get a Specific Quote
@app.route('/api/quotes/<int:quote_id>', methods=['GET'])
def get_quote(quote_id):
    """
    Fetch a specific quote using its ID.
    Returns the quote details if found, otherwise a 404 error.
    """
    quote = next((quote for quote in quotes_db if quote['id'] == quote_id), None)
    if quote is None:
        return error_response("Quote not found.", 404)
    return jsonify({"quote": quote}), 200

# Endpoint: Update Quote Status
@app.route('/api/quotes/<int:quote_id>', methods=['PUT'])
def update_quote(quote_id):
    """
    Update the status of an existing quote.
    Expects JSON input with the following fields:
    - status: str (New status for the quote)
    """
    try:
        quote = next((quote for quote in quotes_db if quote['id'] == quote_id), None)
        if quote is None:
            return error_response("Quote not found.", 404)

        data = request.get_json()

        # Validate status field
        if 'status' not in data or not isinstance(data['status'], str):
            return error_response("'status' is a required field and must be a string.", 400)

        # Update the status
        quote['status'] = data['status']
        return jsonify({"message": "Quote status updated successfully", "quote": quote}), 200
    except Exception as e:
        return error_response("An error occurred while updating the quote.", 500)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
