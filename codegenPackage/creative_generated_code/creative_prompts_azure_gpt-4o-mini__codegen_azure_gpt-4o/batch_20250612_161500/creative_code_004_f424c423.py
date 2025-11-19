"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://detaljreklam.se
Prompt: Write a code example for a web form that collects customer details for printing services, ensuring it includes fields for items like brochures and roll-ups, as mentioned on Detalj Reklam's site.
Generated: DETERMINISTIC_f424c423a115bff5
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the form page
@app.route('/')
def index():
    return render_template('form.html')  # Render the HTML form

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Collect form data
        customer_name = request.form.get('customer_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        brochures_quantity = request.form.get('brochures_quantity')
        rollups_quantity = request.form.get('rollups_quantity')
        
        # Validate required fields
        if not customer_name or not email or not phone:
            return jsonify({"error": "Missing required customer details."}), 400
        
        # Ensure quantities are numeric and non-negative
        try:
            brochures_quantity = int(brochures_quantity) if brochures_quantity else 0
            rollups_quantity = int(rollups_quantity) if rollups_quantity else 0
            if brochures_quantity < 0 or rollups_quantity < 0:
                return jsonify({"error": "Quantities must be non-negative."}), 400
        except ValueError:
            return jsonify({"error": "Quantities must be valid integers."}), 400

        # Simulate saving to a database (replace with actual DB code in production)
        # For now, we simply return the collected data as a confirmation
        response_data = {
            "customer_name": customer_name,
            "email": email,
            "phone": phone,
            "brochures_quantity": brochures_quantity,
            "rollups_quantity": rollups_quantity
        }
        return jsonify({"message": "Form submitted successfully!", "data": response_data}), 200
    except Exception as e:
        # Generic error handling
        return jsonify({"error": "An error occurred while processing the form.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

```html
<!-- form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Printing Services Form</title>
</head>
<body>
    <h1>Customer Details for Printing Services</h1>
    <form action="/submit" method="POST">
        <!-- Customer name -->
        <label for="customer_name">Customer Name:</label>
        <input type="text" id="customer_name" name="customer_name" required>
        <br><br>
        
        <!-- Email -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        
        <!-- Phone -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>
        <br><br>
        
        <!-- Brochures quantity -->
        <label for="brochures_quantity">Number of Brochures:</label>
        <input type="number" id="brochures_quantity" name="brochures_quantity" min="0">
        <br><br>
        
        <!-- Roll-ups quantity -->
        <label for="rollups_quantity">Number of Roll-ups:</label>
        <input type="number" id="rollups_quantity" name="rollups_quantity" min="0">
        <br><br>
        
        <!-- Submit button -->
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
