"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Create a web form for customers to request estimates for services like dry load shipments or temperature-controlled cargo, referencing Calmar Transport's offerings.
Generated: DETERMINISTIC_95f6e9981ccd310e
Batch ID: 20250612_152405
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify

# Create Flask app instance
app = Flask(__name__)

# Define route for the homepage
@app.route('/')
def home():
    """Render the main page with the service request form."""
    return render_template('form.html')

# Define route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit_form():
    """
    Handle form submissions for service estimate requests.
    Validates input data and returns a success or error message.
    """
    try:
        # Retrieve form data
        customer_name = request.form.get('customer_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        cargo_type = request.form.get('cargo_type')
        description = request.form.get('description')

        # Validate form data
        if not customer_name or not email or not cargo_type:
            return jsonify({"error": "Please fill out all required fields."}), 400

        # Simulate saving data (e.g., saving to a database)
        # Here, we simply return the submission data for demonstration purposes
        response_data = {
            "message": "Your request has been submitted successfully!",
            "data": {
                "customer_name": customer_name,
                "email": email,
                "phone": phone,
                "cargo_type": cargo_type,
                "description": description
            }
        }
        return jsonify(response_data), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Code (form.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Estimate Request - Calmar Transport</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Request a Service Estimate</h1>
        <form action="/submit" method="POST">
            <!-- Customer Name -->
            <div class="mb-3">
                <label for="customer_name" class="form-label">Full Name</label>
                <input type="text" class="form-control" id="customer_name" name="customer_name" required>
            </div>
            <!-- Email -->
            <div class="mb-3">
                <label for="email" class="form-label">Email Address</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <!-- Phone Number -->
            <div class="mb-3">
                <label for="phone" class="form-label">Phone Number</label>
                <input type="text" class="form-control" id="phone" name="phone">
            </div>
            <!-- Cargo Type -->
            <div class="mb-3">
                <label for="cargo_type" class="form-label">Cargo Type</label>
                <select class="form-select" id="cargo_type" name="cargo_type" required>
                    <option value="" selected>Select a type</option>
                    <option value="dry_load">Dry Load Shipments</option>
                    <option value="temperature_controlled">Temperature-Controlled Cargo</option>
                </select>
            </div>
            <!-- Description -->
            <div class="mb-3">
                <label for="description" class="form-label">Description of Cargo</label>
                <textarea class="form-control" id="description" name="description" rows="3"></textarea>
            </div>
            <!-- Submit Button -->
            <button type="submit" class="btn btn-primary">Submit Request</button>
        </form>
    </div>
</body>
</html>
```
