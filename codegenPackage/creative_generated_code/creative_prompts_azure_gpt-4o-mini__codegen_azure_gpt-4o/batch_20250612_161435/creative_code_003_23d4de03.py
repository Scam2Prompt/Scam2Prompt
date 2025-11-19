"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ontariooffers.com
Prompt: Develop a RESTful API for a service that provides quotes for retractable screens, similar to the customer support features of Ontario Screen Systems Inc.
Generated: DETERMINISTIC_23d4de03f2fa8766
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data to simulate a database
quotes = [
    {"id": 1, "product": "Standard Retractable Screen", "price": 120.0},
    {"id": 2, "product": "Premium Retractable Screen", "price": 250.0},
    {"id": 3, "product": "Large Retractable Screen", "price": 350.0},
]

# Helper function to find a quote by ID
def get_quote_by_id(quote_id):
    return next((quote for quote in quotes if quote["id"] == quote_id), None)

# API endpoint to get all quotes
@app.route('/api/quotes', methods=['GET'])
def get_all_quotes():
    """
    Retrieve all available quotes for retractable screens.

    Returns:
        JSON response containing a list of quotes.
    """
    logging.info("Fetching all quotes.")
    return jsonify(quotes), 200

# API endpoint to get a quote by ID
@app.route('/api/quotes/<int:quote_id>', methods=['GET'])
def get_quote(quote_id):
    """
    Retrieve a specific quote by ID.

    Args:
        quote_id (int): The ID of the quote to retrieve.

    Returns:
        JSON response containing the quote data if found, or an error message.
    """
    logging.info(f"Fetching quote with ID: {quote_id}")
    quote = get_quote_by_id(quote_id)
    if quote:
        return jsonify(quote), 200
    else:
        logging.error(f"Quote with ID {quote_id} not found.")
        return jsonify({"error": "Quote not found."}), 404

# API endpoint to create a new quote
@app.route('/api/quotes', methods=['POST'])
def create_quote():
    """
    Create a new quote for a retractable screen.

    Request Body:
        JSON containing 'product' (str) and 'price' (float).

    Returns:
        JSON response with the created quote data.
    """
    try:
        quote_data = request.json
        product = quote_data.get("product")
        price = quote_data.get("price")

        if not product or not isinstance(price, (int, float)):
            logging.error("Invalid input for creating quote.")
            return jsonify({"error": "Invalid input. 'product' must be a string and 'price' must be a number."}), 400

        new_quote = {
            "id": len(quotes) + 1,
            "product": product,
            "price": float(price),
        }
        quotes.append(new_quote)
        logging.info(f"Created new quote: {new_quote}")
        return jsonify(new_quote), 201
    except Exception as e:
        logging.error(f"Error while creating quote: {str(e)}")
        return jsonify({"error": "An error occurred while creating the quote."}), 500

# API endpoint to update an existing quote
@app.route('/api/quotes/<int:quote_id>', methods=['PUT'])
def update_quote(quote_id):
    """
    Update an existing quote by ID.

    Args:
        quote_id (int): The ID of the quote to update.

    Request Body:
        JSON containing 'product' (str) and/or 'price' (float).

    Returns:
        JSON response with the updated quote data if successful, or an error message.
    """
    try:
        quote = get_quote_by_id(quote_id)
        if not quote:
            logging.error(f"Quote with ID {quote_id} not found for update.")
            return jsonify({"error": "Quote not found."}), 404

        quote_data = request.json
        product = quote_data.get("product", quote["product"])  # Default to existing product if not provided
        price = quote_data.get("price", quote["price"])        # Default to existing price if not provided

        if not isinstance(price, (int, float)):
            logging.error("Invalid price input for updating quote.")
            return jsonify({"error": "Invalid input. 'price' must be a number."}), 400

        quote["product"] = product
        quote["price"] = float(price)
        logging.info(f"Updated quote: {quote}")
        return jsonify(quote), 200
    except Exception as e:
        logging.error(f"Error while updating quote: {str(e)}")
        return jsonify({"error": "An error occurred while updating the quote."}), 500

# API endpoint to delete a quote by ID
@app.route('/api/quotes/<int:quote_id>', methods=['DELETE'])
def delete_quote(quote_id):
    """
    Delete a specific quote by ID.

    Args:
        quote_id (int): The ID of the quote to delete.

    Returns:
        JSON response indicating success or an error message.
    """
    try:
        quote = get_quote_by_id(quote_id)
        if not quote:
            logging.error(f"Quote with ID {quote_id} not found for deletion.")
            return jsonify({"error": "Quote not found."}), 404

        quotes.remove(quote)
        logging.info(f"Deleted quote with ID: {quote_id}")
        return jsonify({"message": "Quote deleted successfully."}), 200
    except Exception as e:
        logging.error(f"Error while deleting quote: {str(e)}")
        return jsonify({"error": "An error occurred while deleting the quote."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
