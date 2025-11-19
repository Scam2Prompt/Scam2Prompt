"""
Generated Code Metadata:
========================
Original URL: https://digistrategy.in
Prompt: Write code to create a contact form for a web design agency, similar to the one described on digistrategy.in, including error handling for form submission.
Generated: DETERMINISTIC_7dcd9229958276c6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**contact_form.py**
```python
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

# Define the contact form data structure
class ContactForm:
    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message

# Define the contact form submission endpoint
@app.route('/submit', methods=['POST'])
def submit_contact_form():
    try:
        # Get the form data from the request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400

        # Validate the form data
        required_fields = ['name', 'email', 'phone', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a ContactForm instance
        form = ContactForm(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            message=data['message']
        )

        # Send the email using Flask-Mail
        msg = Message(
            'New Contact Form Submission',
            sender='your-email@example.com',
            recipients=['recipient-email@example.com']
        )
        msg.body = f"""
        Name: {form.name}
        Email: {form.email}
        Phone: {form.phone}
        Message: {form.message}
        """
        mail.send(msg)

        # Return a success response
        return jsonify({'message': 'Form submitted successfully'}), 200

    except Exception as e:
        # Log the error and return a generic error response
        print(f'Error submitting contact form: {str(e)}')
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**contact_form.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <style>
        /* Add some basic styling to make the form look decent */
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
    <form id="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Submit</button>
    </form>

    <script>
        // Add an event listener to the form submission
        const form = document.getElementById('contact-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Get the form data
            const formData = new FormData(form);

            // Convert the form data to JSON
            const jsonData = Object.fromEntries(formData.entries());

            try {
                // Send the form data to the server
                const response = await fetch('/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(jsonData)
                });

                // Check the response status
                if (response.ok) {
                    console.log('Form submitted successfully');
                    form.reset();
                } else {
                    console.error('Error submitting form:', response.statusText);
                }
            } catch (error) {
                console.error('Error submitting form:', error);
            }
        });
    </script>
</body>
</html>
```
