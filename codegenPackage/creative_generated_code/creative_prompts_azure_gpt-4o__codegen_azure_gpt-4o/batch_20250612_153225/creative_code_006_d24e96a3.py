"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubhasamaya.com
Prompt: Generate a REST API design for a service that provides Nepali date conversion and Unicode-to-Preeti text conversion, similar to the utilities on Shubhasamaya.com.
Generated: DETERMINISTIC_d24e96a36267bac6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: REST API service for Nepali date conversion and Unicode-to-Preeti text conversion.

from flask import Flask, request, jsonify
from datetime import datetime
import traceback

app = Flask(__name__)

# Function for converting a Gregorian date to a Nepali date.
def convert_to_nepali_date(gregorian_date):
    """
    Converts a Gregorian date to a Nepali date.
    For simplicity, this is a placeholder. Replace with actual logic.
    """
    # Placeholder logic for Nepali date conversion
    try:
        nepali_date = f"Nepali equivalent of {gregorian_date}"  # Replace with actual library or algorithm
        return nepali_date
    except Exception as e:
        raise ValueError("Failed to convert date: " + str(e))

# Function for converting Unicode text to Preeti text.
def unicode_to_preeti(unicode_text):
    """
    Converts Unicode text to Preeti text.
    For simplicity, this is a placeholder. Replace with actual logic.
    """
    try:
        preeti_text = unicode_text.replace("क", "k")  # Replace with actual mapping logic
        return preeti_text
    except Exception as e:
        raise ValueError("Failed to convert text: " + str(e))

@app.route('/api/nepali-date', methods=['POST'])
def nepali_date_conversion():
    """
    Endpoint for converting Gregorian date to Nepali date.
    Expects JSON input with 'gregorian_date' in 'YYYY-MM-DD' format.
    """
    try:
        data = request.get_json()
        if not data or 'gregorian_date' not in data:
            return jsonify({'error': 'Missing gregorian_date in request body'}), 400
        
        gregorian_date = data['gregorian_date']
        # Validate input date format
        try:
            datetime.strptime(gregorian_date, '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

        nepali_date = convert_to_nepali_date(gregorian_date)
        return jsonify({'nepali_date': nepali_date}), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.route('/api/unicode-to-preeti', methods=['POST'])
def unicode_to_preeti_conversion():
    """
    Endpoint for converting Unicode text to Preeti text.
    Expects JSON input with 'unicode_text'.
    """
    try:
        data = request.get_json()
        if not data or 'unicode_text' not in data:
            return jsonify({'error': 'Missing unicode_text in request body'}), 400
        
        unicode_text = data['unicode_text']
        preeti_text = unicode_to_preeti(unicode_text)
        return jsonify({'preeti_text': preeti_text}), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({'error': 'Internal server error', 'details': traceback.format_exc()}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)  # Set debug=False for production
```
