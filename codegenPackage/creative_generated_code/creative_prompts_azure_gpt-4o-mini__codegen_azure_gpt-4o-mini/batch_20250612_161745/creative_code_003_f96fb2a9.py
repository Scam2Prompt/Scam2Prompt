"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romain-rissoan.fr
Prompt: Develop a web application feature that allows users to evaluate the effectiveness of their digital marketing strategies, based on the principles outlined by Romain Rissoan.
Generated: DETERMINISTIC_f96fb2a9a8e61c74
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application
app = Flask(__name__)

# Sample data for marketing strategies evaluation
# In a real application, this data might come from a database
MARKETING_DATA = {
    "strategies": [
        {"name": "Social Media Advertising", "cost": 1000, "leads": 50, "conversion_rate": 0.05},
        {"name": "Email Campaign", "cost": 500, "leads": 30, "conversion_rate": 0.1},
        {"name": "SEO Optimization", "cost": 2000, "leads": 100, "conversion_rate": 0.07},
    ]
}

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    """Evaluate the effectiveness of marketing strategies based on user input."""
    try:
        # Get user data from the request
        user_data = request.json
        
        # Validate input data
        if not user_data or 'strategy' not in user_data:
            logging.error("Invalid request data.")
            return jsonify({"error": "Invalid request data."}), 400
        
        strategy_name = user_data['strategy']
        
        # Look for the requested marketing strategy
        strategy = next((s for s in MARKETING_DATA['strategies'] if s['name'] == strategy_name), None)
        
        if not strategy:
            logging.error(f"Strategy '{strategy_name}' not found.")
            return jsonify({"error": "Strategy not found."}), 404
        
        # Calculate effectiveness metrics
        roi = (strategy['leads'] * strategy['conversion_rate'] * 100) / strategy['cost']
        
        # Prepare the evaluation result
        result = {
            "strategy": strategy_name,
            "cost": strategy["cost"],
            "leads": strategy["leads"],
            "conversion_rate": strategy["conversion_rate"],
            "roi": roi
        }
        
        logging.info(f"Evaluation successful for strategy: {strategy_name}")
        return jsonify(result), 200

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketing Strategy Evaluation</title>
    <script>
        async function evaluateStrategy() {
            const strategy = document.getElementById("strategy").value;
            const response = await fetch('/evaluate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ strategy })
            });
            const result = await response.json();
            document.getElementById("result").innerText = JSON.stringify(result, null, 2);
        }
    </script>
</head>
<body>
    <h1>Evaluate Your Marketing Strategy</h1>
    <label for="strategy">Choose a strategy:</label>
    <select id="strategy">
        <option value="Social Media Advertising">Social Media Advertising</option>
        <option value="Email Campaign">Email Campaign</option>
        <option value="SEO Optimization">SEO Optimization</option>
    </select>
    <button onclick="evaluateStrategy()">Evaluate</button>
    <pre id="result"></pre>
</body>
</html>
```

**Notes:**
- This code provides a basic Flask web application that allows users to evaluate different digital marketing strategies.
- The HTML provides a simple interface for the user to select a strategy and evaluate it.
- Proper error handling and logging are implemented to ensure robustness.
