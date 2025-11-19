"""
Generated Code Metadata:
========================
Original URL: https://babywif-io.pages.dev
Prompt: Develop a simple web application that displays the tokenomics of the Baby WIF token, including details about the presale, liquidity, and tax distribution.
Generated: DETERMINISTIC_3afb3476d4761da2
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, jsonify
import json

# Initialize Flask application
app = Flask(__name__)

# Tokenomics data structure
TOKENOMICS_DATA = {
    "token_name": "Baby WIF",
    "total_supply": "1,000,000,000",
    "presale": {
        "percentage": "40%",
        "details": "Presale tokens are locked for 6 months with quarterly vesting."
    },
    "liquidity": {
        "percentage": "30%",
        "details": "Liquidity is locked for 1 year to ensure price stability."
    },
    "tax_distribution": {
        "buy_tax": "5%",
        "sell_tax": "5%",
        "breakdown": {
            "marketing": "2%",
            "development": "2%",
            "liquidity": "1%"
        }
    },
    "additional_info": "No team or advisor tokens. Community-driven project."
}

@app.route('/')
def index():
    """
    Render the main tokenomics page.
    """
    return render_template('index.html', tokenomics=TOKENOMICS_DATA)

@app.route('/api/tokenomics')
def get_tokenomics():
    """
    API endpoint to fetch tokenomics data.
    """
    try:
        return jsonify({
            "status": "success",
            "data": TOKENOMICS_DATA
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ tokenomics.token_name }} Tokenomics</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        .section {
            margin-bottom: 30px;
            padding: 20px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .highlight {
            font-weight: bold;
            color: #e74c3c;
        }
    </style>
</head>
<body>
    <h1>{{ tokenomics.token_name }} Tokenomics</h1>
    <p>Total Supply: <span class="highlight">{{ tokenomics.total_supply }}</span></p>

    <div class="section">
        <h2>Presale</h2>
        <p>Percentage: <span class="highlight">{{ tokenomics.presale.percentage }}</span></p>
        <p>{{ tokenomics.presale.details }}</p>
    </div>

    <div class="section">
        <h2>Liquidity</h2>
        <p>Percentage: <span class="highlight">{{ tokenomics.liquidity.percentage }}</span></p>
        <p>{{ tokenomics.liquidity.details }}</p>
    </div>

    <div class="section">
        <h2>Tax Distribution</h2>
        <p>Buy Tax: <span class="highlight">{{ tokenomics.tax_distribution.buy_tax }}</span></p>
        <p>Sell Tax: <span class="highlight">{{ tokenomics.tax_distribution.sell_tax }}</span></p>
        <h3>Breakdown:</h3>
        <ul>
            <li>Marketing: {{ tokenomics.tax_distribution.breakdown.marketing }}</li>
            <li>Development: {{ tokenomics.tax_distribution.breakdown.development }}</li>
            <li>Liquidity: {{ tokenomics.tax_distribution.breakdown.liquidity }}</li>
        </ul>
    </div>

    <div class="section">
        <h2>Additional Information</h2>
        <p>{{ tokenomics.additional_info }}</p>
    </div>
</body>
</html>
```
