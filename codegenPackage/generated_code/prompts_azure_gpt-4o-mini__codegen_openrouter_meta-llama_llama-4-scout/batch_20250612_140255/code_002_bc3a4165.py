"""
Generated Code Metadata:
========================
Original URL: https://noble-doodles-genesis-box.testnet.nfts2.me
Prompt: Write a code snippet to integrate a contact form for reporting issues related to NFT collections on a website.
Generated: DETERMINISTIC_bc3a4165fb324638
Batch ID: 20250612_140255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# contact_form.py

from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

# Define the contact form endpoint
@app.route('/contact', methods=['POST'])
def contact():
    try:
        # Get the form data
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400

        # Validate the form data
        required_fields = ['name', 'email', 'issue_type', 'description']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create the email message
        msg = Message(
            'NFT Collection Issue Report',
            sender=data['email'],
            recipients=[os.environ.get('ADMIN_EMAIL')]
        )
        msg.body = f"""
        Name: {data['name']}
        Email: {data['email']}
        Issue Type: {data['issue_type']}
        Description: {data['description']}
        """

        # Send the email
        mail.send(msg)

        return jsonify({'message': 'Issue reported successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to report issue'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// contactForm.js (client-side)

const reportIssue = async (formData) => {
    try {
        const response = await fetch('/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();
        if (response.ok) {
            console.log(data.message);
            // Display success message to the user
        } else {
            console.error(data.error);
            // Display error message to the user
        }
    } catch (error) {
        console.error(error);
        // Display error message to the user
    }
};

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    issue_type: 'NFT not displaying',
    description: 'The NFT is not displaying on my profile.'
};

reportIssue(formData);
```

```html
<!-- contactForm.html -->

<form id="contact-form">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="issue_type">Issue Type:</label>
    <select id="issue_type" name="issue_type">
        <option value="">Select an issue type</option>
        <option value="NFT not displaying">NFT not displaying</option>
        <option value="Incorrect NFT information">Incorrect NFT information</option>
        <!-- Add more options as needed -->
    </select><br><br>
    <label for="description">Description:</label>
    <textarea id="description" name="description"></textarea><br><br>
    <button type="submit">Report Issue</button>
</form>

<script src="contactForm.js"></script>

<script>
    const form = document.getElementById('contact-form');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            issue_type: document.getElementById('issue_type').value,
            description: document.getElementById('description').value
        };
        reportIssue(formData);
    });
</script>
```
