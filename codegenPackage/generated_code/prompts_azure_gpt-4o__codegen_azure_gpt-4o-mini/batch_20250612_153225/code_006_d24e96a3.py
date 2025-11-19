"""
Generated Code Metadata:
========================
Original URL: https://shubhasamaya.com
Prompt: Generate a REST API design for a service that provides Nepali date conversion and Unicode-to-Preeti text conversion, similar to the utilities on Shubhasamaya.com.
Generated: DETERMINISTIC_d24e96a36267bac6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data for Unicode to Preeti conversion
unicode_to_preeti_map = {
    "नमस्ते": "नमस्ते",
    "संसार": "संसार",
    # Add more mappings as needed
}

def unicode_to_preeti(text):
    """
    Convert Unicode text to Preeti font.
    
    Args:
        text (str): The Unicode text to convert.
    
    Returns:
        str: The converted Preeti text.
    """
    return ''.join(unicode_to_preeti_map.get(char, char) for char in text)

def nepali_date_conversion(date_str):
    """
    Convert a Gregorian date to Nepali date.
    
    Args:
        date_str (str): The date in 'YYYY-MM-DD' format.
    
    Returns:
        str: The converted Nepali date.
    """
    # Placeholder for actual conversion logic
    # This should be replaced with a proper Nepali date conversion algorithm
    return f"Nepali Date for {date_str}"

@app.route('/convert/unicode-to-preeti', methods=['POST'])
def convert_unicode_to_preeti():
    """
    API endpoint to convert Unicode text to Preeti font.
    
    Request Body:
        {
            "text": "Unicode text to convert"
        }
    
    Returns:
        JSON response with converted text.
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "Text is required"}), 400
        
        converted_text = unicode_to_preeti(text)
        return jsonify({"converted_text": converted_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/convert/nepali-date', methods=['POST'])
def convert_nepali_date():
    """
    API endpoint to convert Gregorian date to Nepali date.
    
    Request Body:
        {
            "date": "YYYY-MM-DD"
        }
    
    Returns:
        JSON response with converted Nepali date.
    """
    try:
        data = request.get_json()
        date_str = data.get('date', '')
        
        if not date_str:
            return jsonify({"error": "Date is required"}), 400
        
        # Validate date format
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format, should be YYYY-MM-DD"}), 400
        
        nepali_date = nepali_date_conversion(date_str)
        return jsonify({"nepali_date": nepali_date}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
