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
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from typing import Optional

app = Flask(__name__)
CORS(app)

# Error handling for invalid date format
class InvalidDateFormatError(Exception):
    pass

# Route for Nepali date conversion
@app.route('/convert/nepali-date', methods=['GET'])
def convert_nepali_date():
    """
    Convert a Gregorian date to Nepali date format.
    
    Expected query parameters:
    - date: Date in 'YYYY-MM-DD' format
    
    Returns:
    - JSON object with Nepali date or error message.
    """
    date_str: Optional[str] = request.args.get('date')
    
    if not date_str:
        return jsonify({"error": "Date parameter is required."}), 400

    try:
        # Parse the input date
        gregorian_date = datetime.strptime(date_str, '%Y-%m-%d')
        nepali_date = convert_to_nepali_date(gregorian_date)  # Implement this function
        return jsonify({"nepali_date": nepali_date}), 200
    except ValueError:
        raise InvalidDateFormatError(f"Invalid date format: {date_str}")

@app.errorhandler(InvalidDateFormatError)
def handle_invalid_date_format(error):
    return jsonify({"error": str(error)}), 400

# Route for Unicode-to-Preeti text conversion
@app.route('/convert/unicode-to-preeti', methods=['POST'])
def convert_unicode_to_preeti():
    """
    Convert Unicode text to Preeti font.
    
    Expected JSON body:
    - text: Unicode text to be converted
    
    Returns:
    - JSON object with converted Preeti text or error message.
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({"error": "Text parameter is required."}), 400

    unicode_text = data['text']

    try:
        preeti_text = convert_unicode_to_preeti_font(unicode_text)  # Implement this function
        return jsonify({"preeti_text": preeti_text}), 200
    except Exception as e:
        return jsonify({"error": f"Conversion failed: {str(e)}"}), 500

# Helper function placeholders
def convert_to_nepali_date(gregorian_date):
    """
    Placeholder function for converting Gregorian date to Nepali date.
    Implement the necessary logic here.
    """
    # TODO: Implement date conversion logic
    return "Nepali Date Placeholder"

def convert_unicode_to_preeti_font(unicode_text):
    """
    Placeholder function for converting Unicode text to Preeti font.
    Implement the necessary logic here.
    """
    # TODO: Implement conversion logic
    return "Preeti Font Placeholder"

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```
