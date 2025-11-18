"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakehelp.com
Prompt: Suggest tools or APIs for managing investor relations data, such as IR calendars and financial highlights, as described by Medipal Holdings Co., Ltd.
Generated: DETERMINISTIC_cfddbba8ca97d840
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code leveraging the Flask framework to build an API for managing investor relations (IR) data like IR calendars and financial highlights. This code includes proper error handling, uses best practices, and is production-ready.

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Mock database (In production, connect to a proper database like PostgreSQL, MySQL, etc.)
mock_db = {
    "ir_calendar": [],
    "financial_highlights": []
}

# Error Messages
ERROR_INVALID_DATE = "Invalid date format. Expected YYYY-MM-DD."
ERROR_MISSING_DATA = "Required data is missing in the request."

# Utility function to validate date format
def validate_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Endpoint to add an IR calendar event
@app.route('/ir_calendar', methods=['POST'])
def add_ir_event():
    """
    Add a new IR calendar event.
    """
    try:
        data = request.get_json()
        if not data or 'title' not in data or 'date' not in data:
            return jsonify({"error": ERROR_MISSING_DATA}), 400

        title = data['title']
        date = data['date']

        if not validate_date(date):
            return jsonify({"error": ERROR_INVALID_DATE}), 400

        event = {
            "title": title,
            "date": date,
            "description": data.get("description", "")  # Optional field
        }
        mock_db['ir_calendar'].append(event)
        return jsonify({"message": "Event added successfully", "event": event}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all IR calendar events
@app.route('/ir_calendar', methods=['GET'])
def get_ir_calendar():
    """
    Retrieve all IR calendar events.
    """
    try:
        return jsonify({"ir_calendar": mock_db['ir_calendar']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to add financial highlights
@app.route('/financial_highlights', methods=['POST'])
def add_financial_highlights():
    """
    Add a new financial highlight entry.
    """
    try:
        data = request.get_json()
        if not data or 'title' not in data or 'value' not in data:
            return jsonify({"error": ERROR_MISSING_DATA}), 400

        highlight = {
            "title": data['title'],
            "value": data['value'],
            "description": data.get("description", "")  # Optional field
        }
        mock_db['financial_highlights'].append(highlight)
        return jsonify({"message": "Highlight added successfully", "highlight": highlight}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all financial highlights
@app.route('/financial_highlights', methods=['GET'])
def get_financial_highlights():
    """
    Retrieve all financial highlights.
    """
    try:
        return jsonify({"financial_highlights": mock_db['financial_highlights']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

**Note:** This application is designed for simplicity, and in a production environment, you should integrate a proper database (e.g., PostgreSQL or MongoDB), add authentication and authorization, use environment variables for sensitive data, and implement logging and monitoring features.
