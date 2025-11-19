"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: Write a script to generate a quote request form for IDG Fiber products, allowing users to input quantities for items like Glass Fiber Reinforced Concrete (GFRC) and AR Fiber, and calculate the total cost.
Generated: DETERMINISTIC_ee3c5a6aacc3b424
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for production

# Define product prices
PRODUCT_PRICES = {
    'GFRC': 50.0,  # Price per unit for Glass Fiber Reinforced Concrete
    'AR_Fiber': 30.0  # Price per unit for AR Fiber
}

@app.route('/', methods=['GET', 'POST'])
def quote_request():
    """
    Render the quote request form and handle form submissions.
    """
    if request.method == 'POST':
        try:
            # Get quantities from the form
            gfrc_quantity = int(request.form.get('gfrc_quantity', 0))
            ar_fiber_quantity = int(request.form.get('ar_fiber_quantity', 0))

            # Validate quantities
            if gfrc_quantity < 0 or ar_fiber_quantity < 0:
                raise ValueError("Quantities must be non-negative.")

            # Calculate total cost
            total_cost = (gfrc_quantity * PRODUCT_PRICES['GFRC'] +
                          ar_fiber_quantity * PRODUCT_PRICES['AR_Fiber'])

            # Flash a success message with the total cost
            flash(f'Total cost for your quote: ${total_cost:.2f}', 'success')
            return redirect(url_for('quote_request'))

        except ValueError as e:
            # Handle invalid input
            flash(str(e), 'error')

    return render_template('quote_request.html')

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Template (quote_request.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quote Request Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Quote Request Form for IDG Fiber Products</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST">
            <div class="form-group">
                <label for="gfrc_quantity">Quantity of Glass Fiber Reinforced Concrete (GFRC):</label>
                <input type="number" id="gfrc_quantity" name="gfrc_quantity" class="form-control" min="0" required>
            </div>
            <div class="form-group">
                <label for="ar_fiber_quantity">Quantity of AR Fiber:</label>
                <input type="number" id="ar_fiber_quantity" name="ar_fiber_quantity" class="form-control" min="0" required>
            </div>
            <button type="submit" class="btn btn-primary">Calculate Total Cost</button>
        </form>
    </div>
</body>
</html>
```

**Instructions:**
1. Save the Python code in a file named `app.py`.
2. Save the HTML code in a folder named `templates` as `quote_request.html`.
3. Install Flask using `pip install Flask`.
4. Run the application with `python app.py`.
5. Access the form at `http://127.0.0.1:5000/`.
