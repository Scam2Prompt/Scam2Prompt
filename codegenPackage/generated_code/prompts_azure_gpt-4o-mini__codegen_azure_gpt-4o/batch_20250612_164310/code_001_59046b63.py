"""
Generated Code Metadata:
========================
Original URL: https://www.gpt-chat.info
Prompt: Write a code snippet for a contact form that handles errors, inspired by the "Lỗi: Không tìm thấy biểu mẫu liên hệ" message on the GPT-Chat page.
Generated: DETERMINISTIC_59046b636abc2043
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to render the contact form
@app.route('/')
def contact_form():
    return render_template('contact_form.html')  # Ensure you have a contact_form.html template

# Route to handle form submission
@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    try:
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form data
        errors = []
        if not name or len(name.strip()) == 0:
            errors.append("Name is required.")
        if not email or len(email.strip()) == 0:
            errors.append("Email is required.")
        elif '@' not in email:  # Basic email validation
            errors.append("Invalid email format.")
        if not message or len(message.strip()) == 0:
            errors.append("Message is required.")

        # If there are validation errors, return them
        if errors:
            return jsonify({"success": False, "errors": errors}), 400

        # Process the form data (e.g., save to database, send email, etc.)
        # For demonstration, we'll just return a success message
        return jsonify({"success": True, "message": "Contact form submitted successfully!"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"success": False, "error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### `contact_form.html` (Example Template)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="/submit_contact_form" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
