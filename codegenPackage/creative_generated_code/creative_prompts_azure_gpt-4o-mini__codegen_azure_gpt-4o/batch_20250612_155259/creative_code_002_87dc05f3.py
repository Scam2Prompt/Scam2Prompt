"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Write a code snippet to create a registration form for the short courses offered at SMA Rizvi Textile Institute, including fields for name, course selection, and contact information.
Generated: DETERMINISTIC_87dc05f359d819bb
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages securely

# A list of courses offered at SMA Rizvi Textile Institute (example courses)
COURSES = [
    'Textile Designing',
    'Fashion Merchandising',
    'Garment Manufacturing',
    'Quality Control in Textiles',
    'Fabric Analysis'
]

# Route to display the registration form
@app.route('/')
def registration_form():
    return render_template('registration.html', courses=COURSES)

# Route to handle form submissions
@app.route('/register', methods=['POST'])
def register():
    try:
        # Get form data
        name = request.form.get('name')
        contact = request.form.get('contact')
        course = request.form.get('course')

        # Validate form inputs
        if not name or not contact or not course:
            flash('All fields are required!', 'error')
            return redirect(url_for('registration_form'))

        if course not in COURSES:
            flash('Invalid course selection!', 'error')
            return redirect(url_for('registration_form'))

        # Normally, save the data to a database here
        # For demonstration, we'll just flash a success message
        flash(f'Registration successful for {name} in the course "{course}"!', 'success')
        return redirect(url_for('registration_form'))
    except Exception as e:
        # Log the error and show a generic error message
        flash('An error occurred during registration. Please try again later.', 'error')
        print(f"Error: {e}")
        return redirect(url_for('registration_form'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- registration.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Registration</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { max-width: 400px; margin: auto; }
        label { display: block; margin-top: 10px; }
        input, select { width: 100%; padding: 8px; margin-top: 5px; }
        button { margin-top: 10px; padding: 10px; width: 100%; background-color: #007BFF; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .message { margin-top: 10px; padding: 10px; border-radius: 5px; }
        .success { background-color: #d4edda; color: #155724; }
        .error { background-color: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>Course Registration Form</h1>
    <!-- Display flash messages -->
    {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="message {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    <form action="/register" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="contact">Contact Information:</label>
        <input type="text" id="contact" name="contact" required>

        <label for="course">Select Course:</label>
        <select id="course" name="course" required>
            <option value="" disabled selected>Select a course</option>
            {% for course in courses %}
                <option value="{{ course }}">{{ course }}</option>
            {% endfor %}
        </select>

        <button type="submit">Register</button>
    </form>
</body>
</html>
```
