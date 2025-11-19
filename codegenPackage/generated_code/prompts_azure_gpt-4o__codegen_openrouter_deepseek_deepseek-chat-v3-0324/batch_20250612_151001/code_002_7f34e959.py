"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Generate code using Flask to create a web form for booking dumpster rentals, including fields for dumpster size, delivery date, and customer contact information, with backend validation.
Generated: DETERMINISTIC_7f34e9591bc80cb9
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key in production

# Dumpster sizes available for rental
DUMPSTER_SIZES = [
    ('10', '10 Yard'),
    ('20', '20 Yard'),
    ('30', '30 Yard'),
    ('40', '40 Yard')
]

@app.route('/', methods=['GET', 'POST'])
def booking_form():
    if request.method == 'POST':
        # Get form data
        size = request.form.get('size')
        delivery_date_str = request.form.get('delivery_date')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        
        # Validate form data
        errors = []
        
        # Validate dumpster size
        if not size or size not in [s[0] for s in DUMPSTER_SIZES]:
            errors.append('Please select a valid dumpster size.')
        
        # Validate delivery date
        try:
            delivery_date = datetime.strptime(delivery_date_str, '%Y-%m-%d').date()
            if delivery_date < datetime.now().date():
                errors.append('Delivery date must be in the future.')
        except (ValueError, TypeError):
            errors.append('Please enter a valid delivery date (YYYY-MM-DD).')
        
        # Validate name
        if not name or len(name.strip()) < 2:
            errors.append('Please enter a valid name.')
        
        # Validate email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not email or not re.match(email_regex, email):
            errors.append('Please enter a valid email address.')
        
        # Validate phone (basic validation)
        phone_regex = r'^\+?[0-9\s\-\(\)]{7,}$'
        if not phone or not re.match(phone_regex, phone):
            errors.append('Please enter a valid phone number.')
        
        # Validate address
        if not address or len(address.strip()) < 5:
            errors.append('Please enter a valid address.')
        
        if errors:
            for error in errors:
                flash(error)
            return redirect(url_for('booking_form'))
        
        # If validation passes, process the booking (in a real app, you'd save to database)
        flash('Your dumpster rental has been booked successfully!')
        return redirect(url_for('booking_form'))
    
    return render_template('booking_form.html', dumpster_sizes=DUMPSTER_SIZES)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/booking_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dumpster Rental Booking</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, select { width: 100%; padding: 8px; box-sizing: border-box; }
        button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
        button:hover { background-color: #45a049; }
        .error { color: red; margin-bottom: 10px; }
    </style>
</head>
<body>
    <h1>Dumpster Rental Booking</h1>
    
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <div class="error">
                {% for message in messages %}
                    <p>{{ message }}</p>
                {% endfor %}
            </div>
        {% endif %}
    {% endwith %}
    
    <form method="POST" action="/">
        <div class="form-group">
            <label for="size">Dumpster Size:</label>
            <select id="size" name="size" required>
                <option value="">Select a size</option>
                {% for size, label in dumpster_sizes %}
                    <option value="{{ size }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>
        
        <div class="form-group">
            <label for="delivery_date">Delivery Date:</label>
            <input type="date" id="delivery_date" name="delivery_date" required>
        </div>
        
        <div class="form-group">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>
        </div>
        
        <div class="form-group">
            <label for="address">Delivery Address:</label>
            <input type="text" id="address" name="address" required>
        </div>
        
        <button type="submit">Book Dumpster</button>
    </form>
</body>
</html>
```
