"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: Generate a code snippet for a web application that allows users to request quotes for custom aluminum window installations, incorporating features like user input for project specifications and contact information.
Generated: DETERMINISTIC_f282c0fc2207b145
Batch ID: 20250612_162510
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

# Define a class to hold project specifications
class ProjectSpecs:
    def __init__(self, width, height, type, quantity):
        self.width = width
        self.height = height
        self.type = type
        self.quantity = quantity

# Define a class to hold user contact information
class ContactInfo:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# In-memory storage for quotes (replace with a database in production)
quotes = []

# Route to request a quote
@app.route('/request-quote', methods=['POST'])
def request_quote():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        project_specs_data = data.get('projectSpecs')
        contact_info_data = data.get('contactInfo')

        if not project_specs_data or not contact_info_data:
            return jsonify({'error': 'Project specifications and contact information are required'}), 400

        project_specs = ProjectSpecs(
            project_specs_data['width'],
            project_specs_data['height'],
            project_specs_data['type'],
            project_specs_data['quantity']
        )

        contact_info = ContactInfo(
            contact_info_data['name'],
            contact_info_data['email'],
            contact_info_data['phone']
        )

        # Calculate the quote (this is a simple example, actual calculation may vary)
        quote = {
            'projectSpecs': {
                'width': project_specs.width,
                'height': project_specs.height,
                'type': project_specs.type,
                'quantity': project_specs.quantity
            },
            'contactInfo': {
                'name': contact_info.name,
                'email': contact_info.email,
                'phone': contact_info.phone
            },
            'quote': {
                'total': project_specs.quantity * 100  # Simple calculation for example purposes
            }
        }

        quotes.append(quote)

        return jsonify(quote), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all quotes
@app.route('/quotes', methods=['GET'])
def get_quotes():
    try:
        return jsonify(quotes), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// client.js

const form = document.getElementById('quote-form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const projectSpecs = {
        width: document.getElementById('width').value,
        height: document.getElementById('height').value,
        type: document.getElementById('type').value,
        quantity: document.getElementById('quantity').value
    };

    const contactInfo = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value
    };

    try {
        const response = await fetch('/request-quote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ projectSpecs, contactInfo })
        });

        if (!response.ok) {
            throw new Error(response.statusText);
        }

        const quote = await response.json();
        console.log(quote);
        // Display the quote to the user
    } catch (error) {
        console.error(error);
        // Display an error message to the user
    }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request a Quote</title>
</head>
<body>
    <h1>Request a Quote</h1>
    <form id="quote-form">
        <h2>Project Specifications</h2>
        <label for="width">Width:</label>
        <input type="text" id="width" name="width"><br><br>
        <label for="height">Height:</label>
        <input type="text" id="height" name="height"><br><br>
        <label for="type">Type:</label>
        <input type="text" id="type" name="type"><br><br>
        <label for="quantity">Quantity:</label>
        <input type="number" id="quantity" name="quantity"><br><br>

        <h2>Contact Information</h2>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone"><br><br>

        <input type="submit" value="Request Quote">
    </form>

    <script src="client.js"></script>
</body>
</html>
```
