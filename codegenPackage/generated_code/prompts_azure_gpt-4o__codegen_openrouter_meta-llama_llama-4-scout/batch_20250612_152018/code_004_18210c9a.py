"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Generate code to build a subscription form for receiving updates from Darul Raza, ensuring the form validates input fields like email and phone number.
Generated: DETERMINISTIC_18210c9ad54f5bf9
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_form.py

import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a function to validate email addresses
def validate_email(email):
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

# Define a function to validate phone numbers
def validate_phone_number(phone_number):
    """
    Validate a phone number.

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    phone_regex = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(phone_regex, phone_number))

# Define a route for the subscription form
@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        # Get the form data from the request
        data = request.json

        # Check if the required fields are present
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        email = data.get('email')
        phone_number = data.get('phone_number')
        name = data.get('name')

        # Validate the input fields
        if not email or not validate_email(email):
            return jsonify({'error': 'Invalid email address'}), 400

        if not phone_number or not validate_phone_number(phone_number):
            return jsonify({'error': 'Invalid phone number. Please use XXX-XXX-XXXX format.'}), 400

        if not name:
            return jsonify({'error': 'Name is required'}), 400

        # If all fields are valid, process the subscription
        # For demonstration purposes, just return a success message
        return jsonify({'message': 'Subscription successful'}), 201

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
    <title>Darul Raza Subscription Form</title>
    <style>
        form {
            max-width: 500px;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        label {
            display: block;
            margin-bottom: 10px;
        }

        input {
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

        .error {
            color: red;
            font-size: 12px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <form id="subscription-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <div class="error" id="email-error"></div>

        <label for="phone_number">Phone Number:</label>
        <input type="text" id="phone_number" name="phone_number" required pattern="\d{3}-\d{3}-\d{4}">
        <div class="error" id="phone-error"></div>

        <button type="submit">Subscribe</button>
    </form>

    <script>
        const form = document.getElementById('subscription-form');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phoneNumber = document.getElementById('phone_number').value;

            try {
                const response = await fetch('/subscribe', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name, email, phone_number: phoneNumber })
                });

                const data = await response.json();

                if (response.ok) {
                    alert(data.message);
                    form.reset();
                } else {
                    if (data.error.includes('email')) {
                        document.getElementById('email-error').innerText = data.error;
                    } else if (data.error.includes('phone')) {
                        document.getElementById('phone-error').innerText = data.error;
                    } else {
                        alert(data.error);
                    }
                }
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```
