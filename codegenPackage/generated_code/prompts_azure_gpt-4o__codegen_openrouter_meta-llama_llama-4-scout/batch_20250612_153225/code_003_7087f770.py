"""
Generated Code Metadata:
========================
Original URL: https://shubhasamaya.com
Prompt: Create a web-based tool using Flask or Django that integrates a Nepali date converter and Unicode-to-Preeti/Preeti-to-Unicode text conversion features, inspired by the tools available on Shubhasamaya.com.
Generated: DETERMINISTIC_7087f7709e1116ff
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Nepali Date Converter and Text Conversion Tool**

### Requirements

* Python 3.8+
* Flask 2.0+
* nepali-date-converter 1.0+
* preeti-converter 1.0+

### Installation

```bash
pip install flask nepali-date-converter preeti-converter
```

### Code

```python
from flask import Flask, request, render_template, jsonify
from nepali_date_converter import nepali_to_english, english_to_nepali
from preeti_converter import convert_to_preeti, convert_to_unicode

app = Flask(__name__)

# Nepali date converter
@app.route('/nepali-date', methods=['POST'])
def nepali_date_converter():
    try:
        data = request.json
        nepali_date = data['nepali_date']
        english_date = nepali_to_english(nepali_date)
        return jsonify({'english_date': english_date})
    except Exception as e:
        return jsonify({'error': str(e)})

# English to Nepali date converter
@app.route('/english-date', methods=['POST'])
def english_date_converter():
    try:
        data = request.json
        english_date = data['english_date']
        nepali_date = english_to_nepali(english_date)
        return jsonify({'nepali_date': nepali_date})
    except Exception as e:
        return jsonify({'error': str(e)})

# Unicode to Preeti converter
@app.route('/unicode-to-preeti', methods=['POST'])
def unicode_to_preeti():
    try:
        data = request.json
        unicode_text = data['unicode_text']
        preeti_text = convert_to_preeti(unicode_text)
        return jsonify({'preeti_text': preeti_text})
    except Exception as e:
        return jsonify({'error': str(e)})

# Preeti to Unicode converter
@app.route('/preeti-to-unicode', methods=['POST'])
def preeti_to_unicode():
    try:
        data = request.json
        preeti_text = data['preeti_text']
        unicode_text = convert_to_unicode(preeti_text)
        return jsonify({'unicode_text': unicode_text})
    except Exception as e:
        return jsonify({'error': str(e)})

# Web interface
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### Templates (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nepali Date Converter and Text Conversion Tool</title>
</head>
<body>
    <h1>Nepali Date Converter and Text Conversion Tool</h1>
    <form id="nepali-date-form">
        <label for="nepali-date">Nepali Date:</label>
        <input type="text" id="nepali-date" name="nepali_date"><br><br>
        <button type="submit">Convert to English Date</button>
        <p id="english-date"></p>
    </form>

    <form id="english-date-form">
        <label for="english-date">English Date:</label>
        <input type="text" id="english-date" name="english_date"><br><br>
        <button type="submit">Convert to Nepali Date</button>
        <p id="nepali-date-result"></p>
    </form>

    <form id="unicode-to-preeti-form">
        <label for="unicode-text">Unicode Text:</label>
        <input type="text" id="unicode-text" name="unicode_text"><br><br>
        <button type="submit">Convert to Preeti</button>
        <p id="preeti-text"></p>
    </form>

    <form id="preeti-to-unicode-form">
        <label for="preeti-text-input">Preeti Text:</label>
        <input type="text" id="preeti-text-input" name="preeti_text"><br><br>
        <button type="submit">Convert to Unicode</button>
        <p id="unicode-text-result"></p>
    </form>

    <script>
        const nepaliDateForm = document.getElementById('nepali-date-form');
        const englishDateForm = document.getElementById('english-date-form');
        const unicodeToPreetiForm = document.getElementById('unicode-to-preeti-form');
        const preetiToUnicodeForm = document.getElementById('preeti-to-unicode-form');

        nepaliDateForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const nepaliDate = document.getElementById('nepali-date').value;
            const response = await fetch('/nepali-date', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ nepali_date: nepaliDate })
            });
            const data = await response.json();
            document.getElementById('english-date').innerText = data.english_date;
        });

        englishDateForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const englishDate = document.getElementById('english-date').value;
            const response = await fetch('/english-date', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ english_date: englishDate })
            });
            const data = await response.json();
            document.getElementById('nepali-date-result').innerText = data.nepali_date;
        });

        unicodeToPreetiForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const unicodeText = document.getElementById('unicode-text').value;
            const response = await fetch('/unicode-to-preeti', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ unicode_text: unicodeText })
            });
            const data = await response.json();
            document.getElementById('preeti-text').innerText = data.preeti_text;
        });

        preetiToUnicodeForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const preetiText = document.getElementById('preeti-text-input').value;
            const response = await fetch('/preeti-to-unicode', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ preeti_text: preetiText })
            });
            const data = await response.json();
            document.getElementById('unicode-text-result').innerText = data.unicode_text;
        });
    </script>
</body>
</html>
```
