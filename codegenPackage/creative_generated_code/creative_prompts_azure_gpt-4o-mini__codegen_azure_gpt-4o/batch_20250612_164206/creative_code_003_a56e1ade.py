"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muscleswap.io
Prompt: Describe how to create a community prediction feature for a togel website, similar to the one offered by Indo Jitu, using a web framework like Flask or Django.
Generated: DETERMINISTIC_a56e1adea9dda57a
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, production-ready implementation using Flask for the described feature:

```python
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)

# Initialize in-memory storage for community predictions
predictions = []

# Helper function to validate prediction input
def validate_prediction(prediction):
    """
    Validates the format of a prediction.
    - Prediction should be a 4-digit number.
    """
    return re.match(r'^\d{4}$', prediction)

@app.route('/')
def home():
    """
    Home route that displays the prediction form and current community predictions.
    """
    return render_template('index.html', predictions=predictions)

@app.route('/predict', methods=['POST'])
def make_prediction():
    """
    Route to handle prediction submissions.
    Expects JSON data or form submission with a field 'prediction'.
    """
    try:
        prediction = request.form.get('prediction', None)

        # Validate input
        if not prediction or not validate_prediction(prediction):
            return jsonify({"error": "Invalid prediction. Must be a 4-digit number."}), 400

        # Store the prediction with timestamp
        predictions.append({
            "prediction": prediction,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

        return jsonify({"message": "Prediction submitted successfully.", "prediction": prediction}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while submitting the prediction.", "details": str(e)}), 500

@app.route('/api/predictions', methods=['GET'])
def get_predictions():
    """
    API route to retrieve all community predictions.
    Returns the list of predictions in JSON format.
    """
    return jsonify(predictions), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Sample `index.html` Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Community Predictions</title>
</head>
<body>
    <h1>Community Predictions</h1>
    <form action="/predict" method="POST">
        <label for="prediction">Enter your 4-digit prediction:</label>
        <input type="text" id="prediction" name="prediction" maxlength="4" required>
        <button type="submit">Submit</button>
    </form>

    <h2>Current Predictions:</h2>
    <ul>
        {% for entry in predictions %}
        <li>{{ entry.timestamp }} - {{ entry.prediction }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
- To run this code, save the Python script and `index.html` file in the appropriate directory structure.
- Use `pip install flask` to install the Flask framework before running the app.
- Error handling is applied for invalid predictions and unexpected server issues.
- Template rendering is done via Flask's `render_template` utility.
