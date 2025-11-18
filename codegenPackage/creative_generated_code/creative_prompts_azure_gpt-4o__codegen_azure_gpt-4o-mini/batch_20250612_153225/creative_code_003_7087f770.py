"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubhasamaya.com
Prompt: Create a web-based tool using Flask or Django that integrates a Nepali date converter and Unicode-to-Preeti/Preeti-to-Unicode text conversion features, inspired by the tools available on Shubhasamaya.com.
Generated: DETERMINISTIC_7087f7709e1116ff
Batch ID: 20250612_153225
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.6.0.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Dummy functions for date conversion and Unicode to Preeti conversion
def nepali_date_converter(date_str):
    # Placeholder for actual Nepali date conversion logic
    # This function should convert a Gregorian date to Nepali date format
    return f"Nepali date for {date_str}"

def unicode_to_pretti(text):
    # Placeholder for actual Unicode to Preeti conversion logic
    # This function should convert Unicode text to Preeti format
    return f"Preeti version of '{text}'"

def pretti_to_unicode(text):
    # Placeholder for actual Preeti to Unicode conversion logic
    # This function should convert Preeti text to Unicode format
    return f"Unicode version of '{text}'"

@app.route('/')
def index():
    """Render the index page for the application."""
    return render_template('index.html')

@app.route('/convert_date', methods=['POST'])
def convert_date():
    """Convert Gregorian date to Nepali date."""
    try:
        date_str = request.form.get('date')
        if not date_str:
            return jsonify({"error": "No date provided"}), 400
        
        nepali_date = nepali_date_converter(date_str)
        return jsonify({"nepali_date": nepali_date}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/unicode_to_preeti', methods=['POST'])
def convert_unicode_to_pretti():
    """Convert Unicode text to Preeti."""
    try:
        text = request.form.get('text')
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        preeti_text = unicode_to_pretti(text)
        return jsonify({"preeti_text": preeti_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/preeti_to_unicode', methods=['POST'])
def convert_pretti_to_unicode():
    """Convert Preeti text to Unicode."""
    try:
        text = request.form.get('text')
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        unicode_text = pretti_to_unicode(text)
        return jsonify({"unicode_text": unicode_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nepali Date & Text Converter</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Nepali Date & Text Converter</h1>
    
    <h2>Date Conversion</h2>
    <input type="date" id="dateInput" required>
    <button onclick="convertDate()">Convert Date</button>
    <p id="dateResult"></p>

    <h2>Unicode to Preeti Conversion</h2>
    <textarea id="unicodeInput" rows="4" cols="50" required></textarea>
    <button onclick="convertUnicodeToPreeti()">Convert to Preeti</button>
    <p id="unicodeResult"></p>

    <h2>Preeti to Unicode Conversion</h2>
    <textarea id="preetiInput" rows="4" cols="50" required></textarea>
    <button onclick="convertPreetiToUnicode()">Convert to Unicode</button>
    <p id="preetiResult"></p>

    <script>
        function convertDate() {
            const date = $('#dateInput').val();
            $.post('/convert_date', { date: date })
                .done(function(data) {
                    $('#dateResult').text(data.nepali_date);
                })
                .fail(function(jqXHR) {
                    $('#dateResult').text(jqXHR.responseJSON.error);
                });
        }

        function convertUnicodeToPreeti() {
            const text = $('#unicodeInput').val();
            $.post('/unicode_to_preeti', { text: text })
                .done(function(data) {
                    $('#unicodeResult').text(data.preeti_text);
                })
                .fail(function(jqXHR) {
                    $('#unicodeResult').text(jqXHR.responseJSON.error);
                });
        }

        function convertPreetiToUnicode() {
            const text = $('#preetiInput').val();
            $.post('/preeti_to_unicode', { text: text })
                .done(function(data) {
                    $('#preetiResult').text(data.unicode_text);
                })
                .fail(function(jqXHR) {
                    $('#preetiResult').text(jqXHR.responseJSON.error);
                });
        }
    </script>
</body>
</html>
```

### Instructions
- Save the Python code in a file named `app.py`.
- Create a folder named `templates` in the same directory as `app.py` and save the HTML code as `index.html` inside that folder.
- Install Flask by running `pip install Flask`.
- Run the application using `python app.py`.
- Access the tool in your web browser at `http://127.0.0.1:5000/`.
