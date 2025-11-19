"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Create a sample API for a brand activation service that tracks customer engagement and product literacy, based on the experiential marketing strategies of Paradigm Group.
Generated: DETERMINISTIC_d7a89ea1b33f3c8d
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory database simulation for customer engagement and product literacy tracking
database = {
    "engagements": [],
    "product_literacy": []
}

# API route to log customer engagement
@app.route('/api/engagements', methods=['POST'])
def log_engagement():
    """
    Logs customer engagement data based on experiential marketing strategies.
    Expected input: JSON object with customer_id, event_type, and timestamp.
    Returns: Confirmation message or error.
    """
    try:
        data = request.json
        # Validate the input
        if not all(key in data for key in ("customer_id", "event_type", "timestamp")):
            return jsonify({"error": "Invalid input. Must include customer_id, event_type, and timestamp."}), 400
        
        # Log engagement data into the database
        database["engagements"].append(data)
        logging.info(f"Engagement logged: {data}")
        return jsonify({"message": "Engagement logged successfully."}), 201

    except Exception as e:
        logging.error(f"Error logging engagement: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

# API route to log product literacy data
@app.route('/api/product-literacy', methods=['POST'])
def log_product_literacy():
    """
    Logs customer product literacy data.
    Expected input: JSON object with customer_id, product_id, literacy_score, and timestamp.
    Returns: Confirmation message or error.
    """
    try:
        data = request.json
        # Validate the input
        if not all(key in data for key in ("customer_id", "product_id", "literacy_score", "timestamp")):
            return jsonify({"error": "Invalid input. Must include customer_id, product_id, literacy_score, and timestamp."}), 400
        
        # Log product literacy data into the database
        database["product_literacy"].append(data)
        logging.info(f"Product literacy logged: {data}")
        return jsonify({"message": "Product literacy logged successfully."}), 201

    except Exception as e:
        logging.error(f"Error logging product literacy: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

# API route to retrieve customer engagement data
@app.route('/api/engagements', methods=['GET'])
def get_engagements():
    """
    Retrieves all customer engagement data.
    Returns: JSON list of engagements.
    """
    return jsonify(database["engagements"]), 200

# API route to retrieve product literacy data
@app.route('/api/product-literacy', methods=['GET'])
def get_product_literacy():
    """
    Retrieves all customer product literacy data.
    Returns: JSON list of product literacy information.
    """
    return jsonify(database["product_literacy"]), 200

# API route to clear engagement data (useful for testing or maintenance)
@app.route('/api/engagements/clear', methods=['DELETE'])
def clear_engagements():
    """
    Clears all customer engagement data (use with caution).
    Returns: Confirmation message.
    """
    database["engagements"] = []
    logging.info("Engagement data cleared.")
    return jsonify({"message": "Engagement data cleared successfully."}), 200

# API route to clear product literacy data (useful for testing or maintenance)
@app.route('/api/product-literacy/clear', methods=['DELETE'])
def clear_product_literacy():
    """
    Clears all customer product literacy data (use with caution).
    Returns: Confirmation message.
    """
    database["product_literacy"] = []
    logging.info("Product literacy data cleared.")
    return jsonify({"message": "Product literacy data cleared successfully."}), 200

# Main entry point to start the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
