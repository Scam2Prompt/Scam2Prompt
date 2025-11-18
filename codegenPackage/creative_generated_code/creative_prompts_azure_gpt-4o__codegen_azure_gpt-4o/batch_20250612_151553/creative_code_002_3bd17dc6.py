"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alshehhi.net
Prompt: Generate code to create a client-facing application for requesting web design services, including form submission and backend processing, inspired by the "طلب خدمة" (Request Service) feature on Alshehhi.Net.
Generated: DETERMINISTIC_3bd17dc625f62a94
Batch ID: 20250612_151553
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

### Server-side (Python with Flask)

```python
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Validation function for user input
def validate_form_data(name, email, phone, description):
    """Validate the form input."""
    if not name or len(name) < 3:
        return "Name must be at least 3 characters long."
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return "Invalid email address."
    if not phone.isdigit() or len(phone) < 8:
        return "Phone number must be at least 8 digits and numeric."
    if not description or len(description) < 10:
        return "Description must be at least 10 characters long."
    return None

@app.route('/')
def home():
    """Render the homepage with the web design request form."""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_request():
    """Handle form submission."""
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        description = request.form.get('description')

        # Validate form data
        validation_error = validate_form_data(name, email, phone, description)
        if validation_error:
            return jsonify({'success': False, 'message': validation_error}), 400

        # Simulate backend processing (e.g., saving to a database)
        # Replace this with actual database logic as needed.
        print(f"Received new request:\nName: {name}\nEmail: {email}\nPhone: {phone}\nDescription: {description}")

        return jsonify({'success': True, 'message': 'Request submitted successfully!'}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'success': False, 'message': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

---

### Frontend (HTML with Bootstrap)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Design Request Form</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Request Web Design Services</h1>
        <form id="serviceForm">
            <div class="mb-3">
                <label for="name" class="form-label">Full Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email Address</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="mb-3">
                <label for="phone" class="form-label">Phone Number</label>
                <input type="text" class="form-control" id="phone" name="phone" required>
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Project Description</label>
                <textarea class="form-control" id="description" name="description" rows="5" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit Request</button>
        </form>
        <div class="mt-3" id="responseMessage"></div>
    </div>

    <script>
        document.getElementById('serviceForm').addEventListener('submit', async (event) => {
            event.preventDefault();

            const formData = new FormData(event.target);
            const responseMessage = document.getElementById('responseMessage');

            try {
                const response = await fetch('/submit', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();

                if (response.ok) {
                    responseMessage.innerHTML = `<p class="alert alert-success">${data.message}</p>`;
                } else {
                    responseMessage.innerHTML = `<p class="alert alert-danger">${data.message}</p>`;
                }
            } catch (error) {
                responseMessage.innerHTML = `<p class="alert alert-danger">An error occurred: ${error.message}</p>`;
            }
        });
    </script>
</body>
</html>
```
