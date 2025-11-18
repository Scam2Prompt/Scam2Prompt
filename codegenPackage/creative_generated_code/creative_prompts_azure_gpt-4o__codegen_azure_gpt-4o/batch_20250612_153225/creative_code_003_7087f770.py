"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubhasamaya.com
Prompt: Create a web-based tool using Flask or Django that integrates a Nepali date converter and Unicode-to-Preeti/Preeti-to-Unicode text conversion features, inspired by the tools available on Shubhasamaya.com.
Generated: DETERMINISTIC_7087f7709e1116ff
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Flask-based implementation for your request:

```python
from flask import Flask, request, jsonify, render_template
import datetime

app = Flask(__name__)

# Nepali date converter mock functions
def ad_to_bs(ad_date):
    """
    Converts AD date to BS (Nepali Bikram Sambat).
    This is a placeholder function. Implement actual conversion logic here.
    """
    return "2080-01-15"  # Mock response for demonstration

def bs_to_ad(bs_date):
    """
    Converts BS (Nepali Bikram Sambat) date to AD.
    This is a placeholder function. Implement actual conversion logic here.
    """
    return "2023-04-28"  # Mock response for demonstration

# Unicode to Preeti conversion mock function
def unicode_to_preeti(text):
    """
    Converts Unicode text to Preeti font.
    Replace with actual conversion logic.
    """
    return text.replace("अ", "c").replace("आ", "cf")  # Mock response for demonstration

# Preeti to Unicode conversion mock function
def preeti_to_unicode(text):
    """
    Converts Preeti font text to Unicode.
    Replace with actual conversion logic.
    """
    return text.replace("c", "अ").replace("cf", "आ")  # Mock response for demonstration

@app.route('/')
def home():
    """
    Renders the homepage with an input form.
    """
    return render_template('index.html')

@app.route('/convert-date', methods=['POST'])
def convert_date():
    """
    Converts AD to BS or BS to AD based on user input.
    """
    try:
        date_type = request.form.get('date_type')
        date = request.form.get('date')
        if not date or not date_type:
            return jsonify({'error': 'Date and type are required'}), 400

        if date_type == 'ad_to_bs':
            converted_date = ad_to_bs(date)
        elif date_type == 'bs_to_ad':
            converted_date = bs_to_ad(date)
        else:
            return jsonify({'error': 'Invalid date type'}), 400

        return jsonify({'converted_date': converted_date})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/convert-text', methods=['POST'])
def convert_text():
    """
    Converts text between Unicode and Preeti font based on user input.
    """
    try:
        conversion_type = request.form.get('conversion_type')
        text = request.form.get('text')
        if not text or not conversion_type:
            return jsonify({'error': 'Text and conversion type are required'}), 400

        if conversion_type == 'unicode_to_preeti':
            converted_text = unicode_to_preeti(text)
        elif conversion_type == 'preeti_to_unicode':
            converted_text = preeti_to_unicode(text)
        else:
            return jsonify({'error': 'Invalid conversion type'}), 400

        return jsonify({'converted_text': converted_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# HTML template (index.html)
@app.route('/generate-template')
def generate_template():
    """
    Generates and serves the HTML template file for testing purposes.
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nepali Date and Text Converter</title>
    </head>
    <body>
        <h1>Nepali Date and Text Converter</h1>
        <form method="POST" action="/convert-date">
            <h2>Date Conversion</h2>
            <label for="date_type">Conversion Type:</label>
            <select name="date_type" required>
                <option value="ad_to_bs">AD to BS</option>
                <option value="bs_to_ad">BS to AD</option>
            </select>
            <label for="date">Date:</label>
            <input type="text" name="date" placeholder="Enter date" required />
            <button type="submit">Convert Date</button>
        </form>

        <form method="POST" action="/convert-text">
            <h2>Text Conversion</h2>
            <label for="conversion_type">Conversion Type:</label>
            <select name="conversion_type" required>
                <option value="unicode_to_preeti">Unicode to Preeti</option>
                <option value="preeti_to_unicode">Preeti to Unicode</option>
            </select>
            <label for="text">Text:</label>
            <input type="text" name="text" placeholder="Enter text" required />
            <button type="submit">Convert Text</button>
        </form>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
- Replace the placeholder `ad_to_bs`, `bs_to_ad`, `unicode_to_preeti`, and `preeti_to_unicode` functions with actual conversion logic as needed.
- The `/generate-template` route dynamically serves a basic HTML template for testing purposes.
- Save the HTML content from `/generate-template` to a file named `templates/index.html` for proper rendering.
