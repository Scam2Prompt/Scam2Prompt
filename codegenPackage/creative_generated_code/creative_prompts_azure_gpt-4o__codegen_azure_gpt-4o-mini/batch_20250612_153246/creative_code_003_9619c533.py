"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taniphones.com
Prompt: Write code to implement a product comparison feature for smartphones, inspired by the "Compare products" functionality on TaniPhone.com.
Generated: DETERMINISTIC_9619c533ca02225e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import NotFound

# Initialize the Flask application
app = Flask(__name__)

# Sample data for smartphones
smartphones = [
    {
        "id": 1,
        "name": "Smartphone A",
        "brand": "Brand X",
        "features": {
            "screen_size": "6.1 inches",
            "battery": "4000 mAh",
            "camera": "12 MP",
            "price": 699
        }
    },
    {
        "id": 2,
        "name": "Smartphone B",
        "brand": "Brand Y",
        "features": {
            "screen_size": "6.5 inches",
            "battery": "4500 mAh",
            "camera": "48 MP",
            "price": 799
        }
    },
    {
        "id": 3,
        "name": "Smartphone C",
        "brand": "Brand Z",
        "features": {
            "screen_size": "6.2 inches",
            "battery": "3500 mAh",
            "camera": "16 MP",
            "price": 599
        }
    }
]

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html', smartphones=smartphones)

@app.route('/compare', methods=['POST'])
def compare():
    """Compare selected smartphones based on their IDs.

    Returns:
        JSON response containing the comparison results or an error message.
    """
    try:
        # Retrieve smartphone IDs from the request
        selected_ids = request.json.get('ids', [])

        # Validate the input
        if not selected_ids:
            return jsonify({"error": "No smartphones selected for comparison."}), 400

        # Filter the smartphones based on the selected IDs
        comparison_data = [phone for phone in smartphones if phone['id'] in selected_ids]

        # Check if any smartphones were found
        if not comparison_data:
            raise NotFound("No smartphones found with the provided IDs.")

        return jsonify({"comparison": comparison_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 Not Found errors."""
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smartphone Comparison</title>
</head>
<body>
    <h1>Smartphone Comparison</h1>
    <form id="comparison-form">
        <h2>Select Smartphones to Compare:</h2>
        {% for smartphone in smartphones %}
            <div>
                <input type="checkbox" id="phone{{ smartphone.id }}" value="{{ smartphone.id }}">
                <label for="phone{{ smartphone.id }}">{{ smartphone.name }} ({{ smartphone.brand }})</label>
            </div>
        {% endfor %}
        <button type="submit">Compare</button>
    </form>
    <div id="comparison-result"></div>

    <script>
        document.getElementById('comparison-form').onsubmit = async function (e) {
            e.preventDefault();
            const selected = [...document.querySelectorAll('input[type="checkbox"]:checked')]
                .map(checkbox => parseInt(checkbox.value));

            const response = await fetch('/compare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ ids: selected })
            });

            const result = await response.json();
            const resultDiv = document.getElementById('comparison-result');
            resultDiv.innerHTML = '';

            if (response.ok) {
                resultDiv.innerHTML = '<h2>Comparison Results:</h2>';
                result.comparison.forEach(phone => {
                    resultDiv.innerHTML += `<p>${phone.name} - ${JSON.stringify(phone.features)}</p>`;
                });
            } else {
                resultDiv.innerHTML = `<p>Error: ${result.error}</p>`;
            }
        };
    </script>
</body>
</html>
```
