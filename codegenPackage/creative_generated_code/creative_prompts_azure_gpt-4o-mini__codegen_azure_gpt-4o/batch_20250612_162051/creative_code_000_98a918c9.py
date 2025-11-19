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
# app.py

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Sample data for hot tub models
hot_tub_data = [
    {
        "id": 1,
        "model": "RelaxPro 2000",
        "price": 4999.99,
        "capacity": "4 People",
        "jets": 20,
        "dimensions": "78x78x34 inches",
        "features": ["LED Lighting", "Bluetooth Audio", "Energy Efficient"]
    },
    {
        "id": 2,
        "model": "HydroLux 5000",
        "price": 7499.99,
        "capacity": "6 People",
        "jets": 40,
        "dimensions": "84x84x36 inches",
        "features": ["Wifi Control", "Waterfall Feature", "Heated Loungers"]
    },
    {
        "id": 3,
        "model": "AquaJoy 3000",
        "price": 5999.99,
        "capacity": "5 People",
        "jets": 30,
        "dimensions": "80x80x34 inches",
        "features": ["Salt Water System", "LED Lighting", "Energy Saving Mode"]
    }
]

@app.route('/')
def home():
    """
    Renders the homepage where users can view and compare hot tub models.
    """
    return render_template('index.html', hot_tub_data=hot_tub_data)


@app.route('/compare', methods=['POST'])
def compare_models():
    """
    Endpoint to compare selected hot tub models based on user input.
    """
    try:
        # Retrieve selected model IDs from the request data
        selected_ids = request.json.get('selected_ids')
        if not selected_ids or not isinstance(selected_ids, list):
            return jsonify({"error": "Invalid input. Please provide a list of IDs."}), 400

        # Filter the hot tub data to include only selected models
        selected_models = [model for model in hot_tub_data if model['id'] in selected_ids]

        # Validate if selected models exist
        if not selected_models:
            return jsonify({"error": "No matching models found for the provided IDs."}), 404

        return jsonify(selected_models), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hot Tub Comparison</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .hot-tub {
            border: 1px solid #ddd;
            padding: 1em;
            margin-bottom: 1em;
        }
        .hot-tub h3 {
            margin: 0;
        }
    </style>
</head>
<body>
    <h1>Compare Hot Tub Models</h1>
    <form id="compare-form">
        <!-- Render hot tub models dynamically -->
        {% for tub in hot_tub_data %}
        <div class="hot-tub">
            <h3>{{ tub.model }}</h3>
            <p>Price: ${{ tub.price }}</p>
            <p>Capacity: {{ tub.capacity }}</p>
            <p>Jets: {{ tub.jets }}</p>
            <p>Dimensions: {{ tub.dimensions }}</p>
            <p>Features: {{ ", ".join(tub.features) }}</p>
            <input type="checkbox" name="compare" value="{{ tub.id }}"> Compare
        </div>
        {% endfor %}
        <button type="button" id="compare-button">Compare</button>
    </form>
    <div id="results"></div>

    <script>
        document.getElementById('compare-button').addEventListener('click', async () => {
            const selectedIds = Array.from(document.querySelectorAll('input[name="compare"]:checked'))
                .map(checkbox => parseInt(checkbox.value));

            if (selectedIds.length === 0) {
                alert('Please select at least one model to compare.');
                return;
            }

            try {
                const response = await fetch('/compare', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ selected_ids: selectedIds })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    alert(`Error: ${errorData.error}`);
                    return;
                }

                const data = await response.json();
                const resultsDiv = document.getElementById('results');
                resultsDiv.innerHTML = '<h2>Comparison Results:</h2>';
                data.forEach(tub => {
                    const tubDiv = document.createElement('div');
                    tubDiv.classList.add('hot-tub');
                    tubDiv.innerHTML = `
                        <h3>${tub.model}</h3>
                        <p>Price: $${tub.price}</p>
                        <p>Capacity: ${tub.capacity}</p>
                        <p>Jets: ${tub.jets}</p>
                        <p>Dimensions: ${tub.dimensions}</p>
                        <p>Features: ${tub.features.join(', ')}</p>
                    `;
                    resultsDiv.appendChild(tubDiv);
                });
            } catch (error) {
                alert('An unexpected error occurred while fetching comparison data.');
            }
        });
    </script>
</body>
</html>
```
