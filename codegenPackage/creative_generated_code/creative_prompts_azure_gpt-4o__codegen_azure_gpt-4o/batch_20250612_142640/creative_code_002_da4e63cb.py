"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoag.com
Prompt: Generate code to create a web-based tool that allows users to "Build Your Rhino" by customizing agricultural equipment specifications, similar to the feature on RhinoAg's site.
Generated: DETERMINISTIC_da4e63cb3f1eb7f8
Batch ID: 20250612_142640
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

# Sample data for customization options (In production, this may come from a database)
equipment_options = {
    "category": ["Disc Harrows", "Box Blades", "Rotary Cutters"],
    "size": ["Small", "Medium", "Large"],
    "color": ["Red", "Blue", "Green"],
    "attachments": ["Hydraulics", "Weight Kits", "LED Lights"]
}

# Route to serve the homepage
@app.route('/')
def index():
    # Render template for the customization tool homepage
    return render_template('index.html', options=equipment_options)

# Route to handle customization submission
@app.route('/submit', methods=['POST'])
def submit_customization():
    try:
        # Get submitted data from the request form
        selected_category = request.form.get("category")
        selected_size = request.form.get("size")
        selected_color = request.form.get("color")
        selected_attachments = request.form.getlist("attachments")

        # Validate the inputs
        if not selected_category or not selected_size or not selected_color:
            return jsonify({"error": "Category, size, and color are required fields."}), 400

        # Construct the response object
        customization = {
            "category": selected_category,
            "size": selected_size,
            "color": selected_color,
            "attachments": selected_attachments
        }

        # Return a success response with the customization details
        return jsonify({"message": "Customization successfully submitted!", "data": customization}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Template: `templates/index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Build Your Rhino</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <h1>Build Your Rhino</h1>
    <form id="customization-form" method="POST" action="/submit">
        <div class="form-group">
            <label for="category">Category:</label>
            <select id="category" name="category" required>
                {% for category in options.category %}
                    <option value="{{ category }}">{{ category }}</option>
                {% endfor %}
            </select>
        </div>
        <div class="form-group">
            <label for="size">Size:</label>
            <select id="size" name="size" required>
                {% for size in options.size %}
                    <option value="{{ size }}">{{ size }}</option>
                {% endfor %}
            </select>
        </div>
        <div class="form-group">
            <label for="color">Color:</label>
            <select id="color" name="color" required>
                {% for color in options.color %}
                    <option value="{{ color }}">{{ color }}</option>
                {% endfor %}
            </select>
        </div>
        <div class="form-group">
            <label for="attachments">Attachments:</label>
            {% for attachment in options.attachments %}
                <div>
                    <input type="checkbox" id="attachment-{{ attachment }}" name="attachments" value="{{ attachment }}">
                    <label for="attachment-{{ attachment }}">{{ attachment }}</label>
                </div>
            {% endfor %}
        </div>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
