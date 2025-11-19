"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: Generate a code snippet for a web form that allows users to request a free plumbing quote, including fields for name, phone number, date selection, and zip code.
Generated: DETERMINISTIC_a28ab061bd577f87
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Plumbing Quote</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <form id="quote-form">
        <h2>Request a Free Plumbing Quote</h2>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>

        <label for="date">Preferred Date:</label>
        <input type="date" id="date" name="date" required>

        <label for="zip">Zip Code:</label>
        <input type="text" id="zip" name="zip" pattern="[0-9]{5}" required>

        <button type="submit">Request Quote</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

form {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="tel"], input[type="date"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```

```javascript
// script.js

const form = document.getElementById('quote-form');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const date = document.getElementById('date').value.trim();
    const zip = document.getElementById('zip').value.trim();

    const quoteRequest = {
        name,
        phone,
        date,
        zip
    };

    try {
        // Send data to server for processing
        fetch('/quote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(quoteRequest)
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            alert('Quote request sent successfully!');
            form.reset();
        })
        .catch((error) => {
            console.error(error);
            alert('Error sending quote request. Please try again.');
        });
    } catch (error) {
        console.error(error);
        alert('Error processing quote request. Please try again.');
    }
});
```

```python
# server.py

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/quote', methods=['POST'])
def handle_quote_request():
    try:
        data = request.get_json()
        name = data.get('name')
        phone = data.get('phone')
        date = data.get('date')
        zip_code = data.get('zip')

        # Validate data
        if not all([name, phone, date, zip_code]):
            return jsonify({'error': 'All fields are required'}), 400

        # Process quote request
        quote_request = {
            'name': name,
            'phone': phone,
            'date': date,
            'zip': zip_code
        }

        # Save to database or send to service for processing
        # For demonstration purposes, just log the request
        print(f"Quote request received: {quote_request}")

        return jsonify({'message': 'Quote request sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': 'Error processing quote request'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
