"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rubberflooringindonesia.com
Prompt: Develop a simple web application that allows users to compare rubber flooring options for waterplay areas and sports fields, inspired by the services provided by Rubber Flooring Indonesia.
Generated: DETERMINISTIC_f870764d49b35646
Batch ID: 20250612_164110
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.min.css": {
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
# app.py
# A simple web application to compare rubber flooring options for waterplay areas and sports fields.

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample database of rubber flooring options
flooring_options = [
    {
        "id": 1,
        "name": "EcoWaterPlay Rubber",
        "type": "Waterplay Area",
        "durability": "High",
        "price_per_square_meter": 30,
        "features": ["Slip-resistant", "UV-resistant", "Eco-friendly"]
    },
    {
        "id": 2,
        "name": "SportFlex Rubber",
        "type": "Sports Field",
        "durability": "Very High",
        "price_per_square_meter": 45,
        "features": ["Shock-absorbent", "Durable", "Weather-resistant"]
    },
    {
        "id": 3,
        "name": "AquaFlex Rubber",
        "type": "Waterplay Area",
        "durability": "Medium",
        "price_per_square_meter": 25,
        "features": ["Colorful designs", "Slip-resistant"]
    },
    {
        "id": 4,
        "name": "ProSport Rubber",
        "type": "Sports Field",
        "durability": "High",
        "price_per_square_meter": 40,
        "features": ["Anti-fatigue", "Durable"]
    }
]


@app.route('/')
def home():
    """
    Render the home page of the application.
    """
    return render_template('index.html')


@app.route('/compare', methods=['POST'])
def compare_flooring():
    """
    Handle the comparison of rubber flooring options based on user input.
    """
    try:
        # Get user input from the form
        flooring_type = request.form.get('flooring_type')
        max_price = request.form.get('max_price')

        # Validate and convert input
        if not flooring_type:
            return jsonify({'error': 'Flooring type is required'}), 400
        if not max_price:
            return jsonify({'error': 'Maximum price is required'}), 400

        max_price = float(max_price)

        # Filter flooring options based on input
        filtered_options = [
            option for option in flooring_options
            if option['type'].lower() == flooring_type.lower() and option['price_per_square_meter'] <= max_price
        ]

        return jsonify({'results': filtered_options})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide a numeric value for the maximum price.'}), 400
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


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
    <title>Rubber Flooring Comparison</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.min.css">
    <style>
        body {
            margin: 40px;
        }
    </style>
</head>
<body>
    <h1>Compare Rubber Flooring Options</h1>
    <form id="comparison-form">
        <label for="flooring_type">Flooring Type (Waterplay Area / Sports Field):</label>
        <input type="text" id="flooring_type" name="flooring_type" required>

        <label for="max_price">Maximum Price (per square meter):</label>
        <input type="number" id="max_price" name="max_price" required>

        <button type="submit">Compare</button>
    </form>

    <h2>Results</h2>
    <div id="results"></div>

    <script>
        document.getElementById('comparison-form').addEventListener('submit', async (event) => {
            event.preventDefault();

            const flooringType = document.getElementById('flooring_type').value;
            const maxPrice = document.getElementById('max_price').value;

            const response = await fetch('/compare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `flooring_type=${encodeURIComponent(flooringType)}&max_price=${encodeURIComponent(maxPrice)}`,
            });

            const resultDiv = document.getElementById('results');
            resultDiv.innerHTML = ''; // Clear previous results

            if (response.ok) {
                const data = await response.json();
                if (data.results.length > 0) {
                    data.results.forEach(option => {
                        const optionDiv = document.createElement('div');
                        optionDiv.innerHTML = `
                            <h3>${option.name}</h3>
                            <p>Type: ${option.type}</p>
                            <p>Durability: ${option.durability}</p>
                            <p>Price per square meter: $${option.price_per_square_meter}</p>
                            <p>Features: ${option.features.join(', ')}</p>
                        `;
                        resultDiv.appendChild(optionDiv);
                    });
                } else {
                    resultDiv.innerHTML = '<p>No options found matching your criteria.</p>';
                }
            } else {
                const error = await response.json();
                resultDiv.innerHTML = `<p>Error: ${error.error}</p>`;
            }
        });
    </script>
</body>
</html>
```
