"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Generate code to create a web form for requesting a free quote for fence, deck, or pergola installation, including fields for dimensions, material preferences, and project type, as described on "The Fence Guys" website.
Generated: DETERMINISTIC_9a9140750a9942f5
Batch ID: 20250612_153246
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

# Route for serving the web form
@app.route('/')
def home():
    return render_template('quote_form.html')

# Route for handling form submission
@app.route('/submit_quote', methods=['POST'])
def submit_quote():
    try:
        # Extract form data
        project_type = request.form.get('project_type')
        dimensions = request.form.get('dimensions')
        material_preference = request.form.get('material_preference')
        customer_name = request.form.get('customer_name')
        customer_email = request.form.get('customer_email')
        customer_phone = request.form.get('customer_phone')

        # Validate required fields
        if not (project_type and dimensions and material_preference and customer_name and customer_email):
            return jsonify({"error": "All fields are required"}), 400

        # Simulate saving to database or processing the request
        # (This would be replaced with actual database logic in production)
        quote_request = {
            "project_type": project_type,
            "dimensions": dimensions,
            "material_preference": material_preference,
            "customer_name": customer_name,
            "customer_email": customer_email,
            "customer_phone": customer_phone,
        }

        # Return success response
        return jsonify({"message": "Quote request submitted successfully", "data": quote_request}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- quote_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request a Free Quote</title>
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
            margin-bottom: 8px;
        }
        input, select, textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            background-color: #28a745;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <h1>Request a Free Quote</h1>
    <form action="/submit_quote" method="POST">
        <label for="project_type">Project Type:</label>
        <select id="project_type" name="project_type" required>
            <option value="">Select a project type...</option>
            <option value="fence">Fence</option>
            <option value="deck">Deck</option>
            <option value="pergola">Pergola</option>
        </select>

        <label for="dimensions">Dimensions (e.g., 20x30):</label>
        <input type="text" id="dimensions" name="dimensions" placeholder="Enter dimensions" required>

        <label for="material_preference">Material Preferences:</label>
        <textarea id="material_preference" name="material_preference" placeholder="Enter preferred materials" required></textarea>

        <label for="customer_name">Your Name:</label>
        <input type="text" id="customer_name" name="customer_name" placeholder="Enter your name" required>

        <label for="customer_email">Your Email:</label>
        <input type="email" id="customer_email" name="customer_email" placeholder="Enter your email" required>

        <label for="customer_phone">Your Phone Number:</label>
        <input type="text" id="customer_phone" name="customer_phone" placeholder="Enter your phone number">

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
