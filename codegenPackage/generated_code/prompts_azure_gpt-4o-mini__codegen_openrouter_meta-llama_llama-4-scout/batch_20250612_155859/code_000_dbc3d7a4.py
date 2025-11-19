"""
Generated Code Metadata:
========================
Original URL: https://cohencues.com
Prompt: Generate a code snippet for a web form that allows users to request a custom cue quote, including fields for name, email, subject, and message, similar to the quote request process on Cohen Cues.
Generated: DETERMINISTIC_dbc3d7a4830a8155
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a function to handle form data and send it via email
def send_email(name, email, subject, message):
    # For simplicity, we'll use a placeholder email sending function
    # In a real application, use a library like smtplib or yagmail
    print(f"Email sent from {email} with subject {subject} and message {message}")
    return True

# Define a route for the quote request form
@app.route('/request-quote', methods=['POST'])
def request_quote():
    try:
        # Get form data from the request
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Validate form fields
        required_fields = ['name', 'email', 'subject', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        # Send the email
        if send_email(name, email, subject, message):
            return jsonify({'success': 'Quote request sent successfully'}), 200
        else:
            return jsonify({'error': 'Failed to send quote request'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Cue Quote Request</title>
    <style>
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

        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
        }

        button[type="submit"] {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button[type="submit"]:hover {
            background-color: #3e8e41;
        }
    </style>
</head>
<body>
    <form id="quote-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="subject">Subject:</label>
        <input type="text" id="subject" name="subject" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send Request</button>
    </form>

    <script>
        const form = document.getElementById('quote-form');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(form);
            const jsonData = Object.fromEntries(formData);

            try {
                const response = await fetch('/request-quote', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(jsonData)
                });

                const result = await response.json();

                if (result.success) {
                    alert('Quote request sent successfully!');
                    form.reset();
                } else {
                    alert('Error sending quote request: ' + result.error);
                }
            } catch (error) {
                console.error(error);
                alert('Error sending quote request: ' + error.message);
            }
        });
    </script>
</body>
</html>
```
