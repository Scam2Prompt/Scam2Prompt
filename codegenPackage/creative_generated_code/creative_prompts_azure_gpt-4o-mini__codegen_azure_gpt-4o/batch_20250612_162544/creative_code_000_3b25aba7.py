"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aydinspirate.com
Prompt: Generate a code snippet for a web application that allows users to customize and order motorized blinds from a selection of styles like Sheer Elegance and Honeycell.
Generated: DETERMINISTIC_3b25aba74d765532
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application to customize and order motorized blinds

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for blind styles and customization options
BLIND_STYLES = [
    {"id": 1, "name": "Sheer Elegance", "price_per_unit": 75},
    {"id": 2, "name": "Honeycell", "price_per_unit": 65},
]

COLORS = ["White", "Ivory", "Gray", "Beige"]
MOTOR_TYPES = ["Standard", "Remote-controlled", "Smart (Wi-Fi)"]

@app.route('/')
def home():
    """
    Render the homepage where users can select and customize motorized blinds.
    """
    return render_template('home.html', styles=BLIND_STYLES, colors=COLORS, motors=MOTOR_TYPES)


@app.route('/order', methods=['POST'])
def order():
    """
    Endpoint for processing blind orders.
    """
    try:
        # Extract data from the request
        style_id = int(request.form.get('style_id'))
        color = request.form.get('color')
        motor_type = request.form.get('motor_type')
        width = float(request.form.get('width'))
        height = float(request.form.get('height'))

        # Validate inputs
        if style_id not in [style["id"] for style in BLIND_STYLES]:
            return jsonify({"error": "Invalid blind style selected"}), 400
        if color not in COLORS:
            return jsonify({"error": "Invalid color selected"}), 400
        if motor_type not in MOTOR_TYPES:
            return jsonify({"error": "Invalid motor type selected"}), 400
        if width <= 0 or height <= 0:
            return jsonify({"error": "Width and height must be positive values"}), 400

        # Calculate the price
        selected_style = next(style for style in BLIND_STYLES if style["id"] == style_id)
        area = width * height  # Area of the blind in square feet
        price = area * selected_style["price_per_unit"]

        # Add motor type premium
        if motor_type == "Remote-controlled":
            price += 50
        elif motor_type == "Smart (Wi-Fi)":
            price += 100

        # Success response
        return jsonify({
            "message": "Order placed successfully!",
            "details": {
                "style": selected_style["name"],
                "color": color,
                "motor_type": motor_type,
                "width": width,
                "height": height,
                "price": price
            }
        })
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### `home.html` template example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize Motorized Blinds</title>
</head>
<body>
    <h1>Customize and Order Motorized Blinds</h1>
    <form action="/order" method="POST">
        <label for="style">Select Blind Style:</label>
        <select name="style_id" id="style">
            {% for style in styles %}
            <option value="{{ style.id }}">{{ style.name }} - ${{ style.price_per_unit }}/sqft</option>
            {% endfor %}
        </select>

        <label for="color">Select Color:</label>
        <select name="color" id="color">
            {% for color in colors %}
            <option value="{{ color }}">{{ color }}</option>
            {% endfor %}
        </select>

        <label for="motor">Select Motor Type:</label>
        <select name="motor_type" id="motor">
            {% for motor in motors %}
            <option value="{{ motor }}">{{ motor }}</option>
            {% endfor %}
        </select>

        <label for="width">Width (ft):</label>
        <input type="number" step="0.1" name="width" id="width" required>

        <label for="height">Height (ft):</label>
        <input type="number" step="0.1" name="height" id="height" required>

        <button type="submit">Place Order</button>
    </form>
</body>
</html>
```
