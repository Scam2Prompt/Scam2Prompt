"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubaswap.com
Prompt: Write code to implement a promotional banner system for displaying bonuses and jackpots dynamically on a gaming website, inspired by MESIN128.
Generated: DETERMINISTIC_f5315f362717aaf7
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
import random
import logging

# Initialize Flask application
app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Sample data for bonuses and jackpots
PROMOTIONS = [
    {"type": "bonus", "amount": 100, "message": "Get a $100 bonus on your first deposit!"},
    {"type": "jackpot", "amount": 5000, "message": "Join the jackpot of $5000!"},
    {"type": "bonus", "amount": 50, "message": "Claim a $50 bonus today!"},
    {"type": "jackpot", "amount": 10000, "message": "Mega Jackpot of $10,000 is waiting for you!"}
]

@app.route('/')
def index():
    """Render the main page with the promotional banner."""
    return render_template('index.html')

@app.route('/api/promotions', methods=['GET'])
def get_promotions():
    """API endpoint to fetch a random promotion for the banner."""
    try:
        promotion = random.choice(PROMOTIONS)
        logging.info("Fetched promotion: %s", promotion)
        return jsonify(promotion), 200
    except Exception as e:
        logging.error("Error fetching promotions: %s", e)
        return jsonify({"error": "Unable to fetch promotions."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**HTML (index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Promotional Banner</title>
    <style>
        #promo-banner {
            background-color: #f0f0f0;
            padding: 20px;
            text-align: center;
            border: 1px solid #ccc;
            margin: 20px;
            font-size: 1.5em;
        }
    </style>
</head>
<body>
    <div id="promo-banner">Loading promotion...</div>
    
    <script>
        // Fetch a random promotion and display it
        async function fetchPromotion() {
            try {
                const response = await fetch('/api/promotions');
                if (!response.ok) throw new Error('Network response was not ok');
                const promotion = await response.json();
                document.getElementById('promo-banner').innerText = promotion.message;
            } catch (error) {
                document.getElementById('promo-banner').innerText = "Error fetching promotion.";
                console.error('There was a problem with the fetch operation:', error);
            }
        }

        // Fetch a promotion when the page loads
        window.onload = fetchPromotion;
    </script>
</body>
</html>
```

This code provides a simple promotional banner system using Flask for the backend and basic HTML for the frontend. It includes proper error handling, logging, and serves dynamic promotions. The HTML file needs to be saved as `index.html` in a `templates` directory for the Flask application to serve it correctly.
