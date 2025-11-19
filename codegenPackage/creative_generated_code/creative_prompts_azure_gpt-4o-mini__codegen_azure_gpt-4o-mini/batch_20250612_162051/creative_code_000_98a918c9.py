"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hottubs.countryleisuremfg.com
Prompt: Generate a code snippet for a web application that allows users to compare different hot tub models from Country Leisure, including features like pricing and specifications.
Generated: DETERMINISTIC_98a918c94c77c80b
Batch ID: 20250612_162051
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
import json

# Initialize the Flask application
app = Flask(__name__)

# Sample data for hot tub models
hot_tub_data = [
    {
        "model": "Luxury Spa",
        "price": 5999.99,
        "features": {
            "seating_capacity": 6,
            "jets": 40,
            "energy_rating": "A+",
            "dimensions": "84 x 84 x 36 inches"
        }
    },
    {
        "model": "Relaxation Tub",
        "price": 3999.99,
        "features": {
            "seating_capacity": 4,
            "jets": 20,
            "energy_rating": "A",
            "dimensions": "76 x 76 x 34 inches"
        }
    },
    {
        "model": "Family Oasis",
        "price": 7999.99,
        "features": {
            "seating_capacity": 8,
            "jets": 50,
            "energy_rating": "A++",
            "dimensions": "90 x 90 x 38 inches"
        }
    }
]

@app.route('/')
def index():
    """Render the main comparison page."""
    return render_template('index.html', hot_tubs=hot_tub_data)

@app.route('/compare', methods=['POST'])
def compare():
    """Compare selected hot tub models based on user input."""
    try:
        # Get the models to compare from the request
        selected_models = request.json.get('models', [])
        
        # Filter the hot tub data based on selected models
        comparison_data = [model for model in hot_tub_data if model["model"] in selected_models]
        
        if not comparison_data:
            return jsonify({"error": "No valid models selected."}), 400
        
        return jsonify(comparison_data), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hot Tub Comparison</title>
</head>
<body>
    <h1>Compare Hot Tub Models</h1>
    <form id="compareForm">
        <label for="models">Select Models (comma-separated):</label>
        <input type="text" id="models" name="models" required>
        <button type="submit">Compare</button>
    </form>
    <div id="comparisonResult"></div>

    <script>
        document.getElementById('compareForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const models = document.getElementById('models').value.split(',').map(model => model.trim());

            fetch('/compare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ models: models })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    document.getElementById('comparisonResult').innerText = data.error;
                } else {
                    let resultHtml = '<h2>Comparison Result</h2><ul>';
                    data.forEach(hotTub => {
                        resultHtml += `<li>${hotTub.model}: Price - $${hotTub.price}, Features - ${JSON.stringify(hotTub.features)}</li>`;
                    });
                    resultHtml += '</ul>';
                    document.getElementById('comparisonResult').innerHTML = resultHtml;
                }
            })
            .catch(error => {
                document.getElementById('comparisonResult').innerText = 'An error occurred: ' + error.message;
            });
        });
    </script>
</body>
</html>
```
