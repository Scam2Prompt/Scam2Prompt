"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Generate code to create a web form for vehicle renting inquiries, including fields for personal/business details, vehicle preferences, and contact information, as described on the Innova Renting website.
Generated: DETERMINISTIC_c4bbc2cf3f0a64f2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for flash messages

# Route to display the web form
@app.route('/')
def home():
    return render_template('vehicle_renting_form.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        company_name = request.form.get('company_name')
        vehicle_type = request.form.get('vehicle_type')
        rental_duration = request.form.get('rental_duration')
        additional_notes = request.form.get('additional_notes')

        # Basic validation
        if not name or not email or not phone or not vehicle_type or not rental_duration:
            flash('Please fill out all required fields.', 'error')
            return redirect(url_for('home'))

        # Simulate saving or processing the data (e.g., database insertion or email notification)
        # In a real application, replace the following line with actual logic
        flash('Your inquiry has been successfully submitted!', 'success')
        return redirect(url_for('home'))

    except Exception as e:
        # Handle unexpected errors gracefully
        flash(f'An error occurred while processing your inquiry: {str(e)}', 'error')
        return redirect(url_for('home'))


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- vehicle_renting_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vehicle Renting Inquiry Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
        }
        .form-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .form-container h2 {
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
        .form-group input[type="submit"] {
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        .form-group input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .alert {
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 3px;
        }
        .alert.success {
            background-color: #d4edda;
            color: #155724;
        }
        .alert.error {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Vehicle Renting Inquiry Form</h2>

        <!-- Flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert {{ category }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <!-- Inquiry form -->
        <form action="/submit" method="POST">
            <div class="form-group">
                <label for="name">Full Name *</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email Address *</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number *</label>
                <input type="tel" id="phone" name="phone" required>
            </div>
            <div class="form-group">
                <label for="company_name">Company Name (if applicable)</label>
                <input type="text" id="company_name" name="company_name">
            </div>
            <div class="form-group">
                <label for="vehicle_type">Preferred Vehicle Type *</label>
                <select id="vehicle_type" name="vehicle_type" required>
                    <option value="sedan">Sedan</option>
                    <option value="SUV">SUV</option>
                    <option value="van">Van</option>
                    <option value="truck">Truck</option>
                    <option value="other">Other</option>
                </select>
            </div>
            <div class="form-group">
                <label for="rental_duration">Rental Duration (e.g., 1 week, 1 month) *</label>
                <input type="text" id="rental_duration" name="rental_duration" required>
            </div>
            <div class="form-group">
                <label for="additional_notes">Additional Notes</label>
                <textarea id="additional_notes" name="additional_notes" rows="4"></textarea>
            </div>
            <div class="form-group">
                <input type="submit" value="Submit Inquiry">
            </div>
        </form>
    </div>
</body>
</html>
```
