"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jaraesconstruction.com
Prompt: Develop a REST API endpoint that allows users to report storm damage to their roofs, referencing the expertise of JaraEs Construction LLC in identifying such issues.
Generated: DETERMINISTIC_b51ed11e2d9bbdf1
Batch ID: 20250612_161520
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

# Initialize the Flask app
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for reported damages (for demonstration purposes, replace with a database in production)
damage_reports = []


@app.route('/report-damage', methods=['POST'])
def report_damage():
    """
    REST API endpoint to report storm damage to roofs.
    This allows users to submit details about roof damage for assessment by JaraEs Construction LLC.
    """
    try:
        # Parse input JSON data from the request
        data = request.get_json()
        
        # Validate required input fields
        if not data or 'name' not in data or 'address' not in data or 'damage_description' not in data:
            return jsonify({"error": "Missing required fields: 'name', 'address', 'damage_description'"}), 400

        # Extract data
        name = data['name']
        address = data['address']
        damage_description = data['damage_description']
        contact_number = data.get('contact_number')  # Optional field

        # Create a damage report object
        damage_report = {
            "name": name,
            "address": address,
            "damage_description": damage_description,
            "contact_number": contact_number,
        }

        # Store the damage report (in production, this should be saved to a database)
        damage_reports.append(damage_report)
        logging.info(f"New damage report submitted: {damage_report}")

        # Return a success response to the client
        return jsonify({"message": "Damage report submitted successfully!", "report": damage_report}), 201

    except Exception as e:
        # Log the error and return an error response
        logging.error(f"Error processing damage report: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request."}), 500


@app.route('/damage-reports', methods=['GET'])
def get_damage_reports():
    """
    REST API endpoint to retrieve all damage reports.
    This is primarily for administrative purposes.
    """
    try:
        return jsonify({"damage_reports": damage_reports}), 200
    except Exception as e:
        # Log the error and return an error response
        logging.error(f"Error retrieving damage reports: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving damage reports."}), 500


if __name__ == '__main__':
    # Start the Flask development server (replace with production-grade server for deployment)
    app.run(debug=True)
```
