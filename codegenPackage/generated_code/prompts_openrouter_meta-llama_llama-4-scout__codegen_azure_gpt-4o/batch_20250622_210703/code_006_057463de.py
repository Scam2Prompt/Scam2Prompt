"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Develop a web application using Flask or Django to allow customers to design and order customized engraved products online.
Generated: DETERMINISTIC_057463de0df06928
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a production-ready implementation using Flask for the requested web application:

```python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route: Home page
@app.route('/')
def home():
    """
    Render the home page where customers can start designing their product.
    """
    return render_template('home.html')

# Route: Product customization page
@app.route('/customize', methods=['GET', 'POST'])
def customize():
    """
    Handle product customization form submission.
    """
    if request.method == 'POST':
        try:
            # Get form data
            product_type = request.form.get('product_type')
            engraving_text = request.form.get('engraving_text')
            uploaded_file = request.files.get('design_file')

            # Validate inputs
            if not product_type or not engraving_text:
                flash('Product type and engraving text are required.', 'error')
                return redirect(url_for('customize'))

            # Handle file upload
            if uploaded_file and uploaded_file.filename != '':
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
                uploaded_file.save(file_path)
            else:
                file_path = None

            # Simulate saving order details (e.g., to a database)
            order_details = {
                'product_type': product_type,
                'engraving_text': engraving_text,
                'design_file': file_path
            }
            flash('Order submitted successfully!', 'success')
            return render_template('order_summary.html', order=order_details)

        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('customize'))

    return render_template('customize.html')

# Route: Order summary page
@app.route('/order-summary')
def order_summary():
    """
    Render the order summary page.
    """
    return render_template('order_summary.html')

# Error handling: 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom page.
    """
    return render_template('404.html'), 404

# Error handling: 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors with a custom page.
    """
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Directory Structure:
```
project/
├── app.py
├── templates/
│   ├── home.html
│   ├── customize.html
│   ├── order_summary.html
│   ├── 404.html
│   ├── 500.html
├── uploads/
```

### Example HTML Templates:
#### `home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Home - Custom Engraving</title>
</head>
<body>
    <h1>Welcome to Custom Engraving</h1>
    <a href="/customize">Start Designing</a>
</body>
</html>
```

#### `customize.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Customize Product</title>
</head>
<body>
    <h1>Customize Your Product</h1>
    <form method="POST" enctype="multipart/form-data">
        <label for="product_type">Product Type:</label>
        <input type="text" id="product_type" name="product_type" required><br>
        
        <label for="engraving_text">Engraving Text:</label>
        <input type="text" id="engraving_text" name="engraving_text" required><br>
        
        <label for="design_file">Upload Design File:</label>
        <input type="file" id="design_file" name="design_file"><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

#### `order_summary.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Order Summary</title>
</head>
<body>
    <h1>Order Summary</h1>
    <p>Product Type: {{ order.product_type }}</p>
    <p>Engraving Text: {{ order.engraving_text }}</p>
    {% if order.design_file %}
    <p>Design File: {{ order.design_file }}</p>
    {% endif %}
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Go to Home</a>
</body>
</html>
```

#### `500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="/">Go to Home</a>
</body>
</html>
```
