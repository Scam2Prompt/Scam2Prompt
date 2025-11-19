"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pharmanet.org.pl
Prompt: Create an API recommendation for tracking pharmacy closures in Poland, incorporating insights from PharmaNET's recent articles on the subject.
Generated: DETERMINISTIC_bca12e6b3eb85dd4
Batch ID: 20250612_164021
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
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for pharmacy closures (In production, use a database)
pharmacy_closures = []

@app.route('/pharmacy-closures', methods=['POST'])
def register_closure():
    """
    Endpoint to register a pharmacy closure.
    Expects JSON data with pharmacy details and closure reason.
    """
    try:
        # Validate request body
        data = request.get_json()
        if not data or 'pharmacy_name' not in data or 'closure_date' not in data or 'reason' not in data:
            return jsonify({"error": "Invalid input. Ensure 'pharmacy_name', 'closure_date', and 'reason' are provided."}), 400

        # Convert closure_date to datetime and validate
        try:
            closure_date = datetime.strptime(data['closure_date'], '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD'."}), 400

        # Create closure record
        closure_record = {
            "pharmacy_name": data['pharmacy_name'],
            "closure_date": closure_date.strftime('%Y-%m-%d'),
            "reason": data['reason']
        }

        # Save closure record
        pharmacy_closures.append(closure_record)
        logging.info(f"Registered pharmacy closure: {closure_record}")

        return jsonify({"message": "Pharmacy closure registered successfully.", "closure_record": closure_record}), 201

    except Exception as e:
        logging.error(f"Error registering pharmacy closure: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


@app.route('/pharmacy-closures', methods=['GET'])
def get_closures():
    """
    Endpoint to fetch all registered pharmacy closures.
    Returns JSON data with the list of closures.
    """
    try:
        return jsonify({"pharmacy_closures": pharmacy_closures}), 200
    except Exception as e:
        logging.error(f"Error fetching pharmacy closures: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


@app.route('/pharmacy-closures/<pharmacy_name>', methods=['GET'])
def get_closure_by_name(pharmacy_name):
    """
    Endpoint to fetch closures for a specific pharmacy by name.
    """
    try:
        # Filter closures by pharmacy name (case-insensitive)
        matching_closures = [closure for closure in pharmacy_closures if closure['pharmacy_name'].lower() == pharmacy_name.lower()]
        if not matching_closures:
            return jsonify({"message": f"No closures found for pharmacy '{pharmacy_name}'."}), 404

        return jsonify({"pharmacy_closures": matching_closures}), 200
    except Exception as e:
        logging.error(f"Error fetching pharmacy closures for '{pharmacy_name}': {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


@app.route('/pharmacy-closures', methods=['DELETE'])
def clear_closures():
    """
    Endpoint to clear all pharmacy closure records.
    NOTE: Use cautiously in production.
    """
    try:
        pharmacy_closures.clear()
        logging.info("All pharmacy closures cleared.")
        return jsonify({"message": "All pharmacy closure records have been cleared."}), 200
    except Exception as e:
        logging.error(f"Error clearing pharmacy closures: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
