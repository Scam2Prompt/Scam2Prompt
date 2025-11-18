"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Generate code to create a web form for submitting edible printing product orders, including fields for product type, quantity, and custom design upload.
Generated: DETERMINISTIC_760ced1fb8c49301
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

# Initialize Flask app
app = Flask(__name__)

# Secret key for session management (replace with a secure key in production)
app.secret_key = 'supersecretkey'

# Directory for uploading custom design files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions for uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the order form
@app.route('/', methods=['GET', 'POST'])
def order_form():
    if request.method == 'POST':
        # Get form data
        product_type = request.form.get('product_type')
        quantity = request.form.get('quantity')
        file = request.files.get('custom_design')

        # Validate form fields
        if not product_type or not quantity:
            flash('Product type and quantity are required.', 'error')
            return redirect(url_for('order_form'))
        
        try:
            quantity = int(quantity)
            if quantity <= 0:
                flash('Quantity must be a positive number.', 'error')
                return redirect(url_for('order_form'))
        except ValueError:
            flash('Quantity must be an integer.', 'error')
            return redirect(url_for('order_form'))

        # Validate uploaded file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Order submitted successfully!', 'success')
        else:
            flash('Invalid file format. Please upload a valid image file.', 'error')
            return redirect(url_for('order_form'))
        
        # In production, you could process the order here (e.g., save to database)

        return redirect(url_for('order_form'))

    # Render the order form (GET request)
    return render_template('order_form.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- Save this file as templates/order_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edible Printing Product Order</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
        }
        .flash-message {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Edible Printing Product Order</h1>
    <!-- Display flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <p class="flash-message">{{ message }}</p>
            {% endfor %}
        {% endif %}
    {% endwith %}
    <form method="POST" enctype="multipart/form-data">
        <label for="product_type">Product Type:</label>
        <select id="product_type" name="product_type" required>
            <option value="Cake">Cake</option>
            <option value="Cookies">Cookies</option>
            <option value="Cupcakes">Cupcakes</option>
        </select>
        <label for="quantity">Quantity:</label>
        <input type="number" id="quantity" name="quantity" min="1" required>
        <label for="custom_design">Custom Design (Image Upload):</label>
        <input type="file" id="custom_design" name="custom_design" accept="image/*" required>
        <button type="submit">Submit Order</button>
    </form>
</body>
</html>
```
