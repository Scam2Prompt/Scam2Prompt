"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Develop a simple web application that allows users to compare rubber flooring options for waterplay areas and sports fields, inspired by the services provided by Rubber Flooring Indonesia.
Generated: DETERMINISTIC_f870764d49b35646
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
# A simple web application to compare rubber flooring options for waterplay areas and sports fields.
# Built using Flask, a lightweight Python web framework.

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for rubber flooring options
rubber_flooring_options = [
    {
        "id": 1,
        "name": "Waterplay Flooring A",
        "type": "Waterplay",
        "material": "EPDM Rubber",
        "durability": "High",
        "price_per_sq_meter": 25,
        "features": ["Slip-resistant", "UV-resistant", "Easy maintenance"]
    },
    {
        "id": 2,
        "name": "Sports Flooring B",
        "type": "Sports",
        "material": "SBR Rubber",
        "durability": "Medium",
        "price_per_sq_meter": 20,
        "features": ["Shock absorption", "Durable", "Customizable colors"]
    },
    {
        "id": 3,
        "name": "Waterplay Flooring C",
        "type": "Waterplay",
        "material": "Recycled Rubber",
        "durability": "Medium",
        "price_per_sq_meter": 18,
        "features": ["Eco-friendly", "Slip-resistant", "Affordable"]
    },
    {
        "id": 4,
        "name": "Sports Flooring D",
        "type": "Sports",
        "material": "PU Rubber",
        "durability": "High",
        "price_per_sq_meter": 30,
        "features": ["High performance", "Weather-resistant", "Long lifespan"]
    }
]

@app.route('/')
def home():
    """
    Render the homepage with options to compare flooring types.
    """
    return render_template('index.html', options=rubber_flooring_options)

@app.route('/compare', methods=['POST'])
def compare():
    """
    Handle comparison requests and return filtered flooring options.
    """
    try:
        # Get user input from the form
        flooring_type = request.form.get('type')
        max_price = request.form.get('max_price', type=float)

        # Filter options based on user input
        filtered_options = [
            option for option in rubber_flooring_options
            if (flooring_type == 'All' or option['type'] == flooring_type) and
               (max_price is None or option['price_per_sq_meter'] <= max_price)
        ]

        # Return filtered options to the user
        return render_template('compare.html', options=filtered_options)
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)

# templates/index.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rubber Flooring Comparison</title>
</head>
<body>
    <h1>Compare Rubber Flooring Options</h1>
    <form action="/compare" method="post">
        <label for="type">Flooring Type:</label>
        <select name="type" id="type">
            <option value="All">All</option>
            <option value="Waterplay">Waterplay</option>
            <option value="Sports">Sports</option>
        </select>
        <br>
        <label for="max_price">Maximum Price per Square Meter:</label>
        <input type="number" name="max_price" id="max_price" step="0.01">
        <br>
        <button type="submit">Compare</button>
    </form>
</body>
</html>
"""

# templates/compare.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparison Results</title>
</head>
<body>
    <h1>Comparison Results</h1>
    {% if options %}
        <ul>
            {% for option in options %}
                <li>
                    <strong>{{ option.name }}</strong> ({{ option.type }})<br>
                    Material: {{ option.material }}<br>
                    Durability: {{ option.durability }}<br>
                    Price per Square Meter: ${{ option.price_per_sq_meter }}<br>
                    Features: {{ option.features | join(', ') }}
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No flooring options match your criteria.</p>
    {% endif %}
    <a href="/">Back to Home</a>
</body>
</html>
"""
```
