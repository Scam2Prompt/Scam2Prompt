"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babywif-io.pages.dev
Prompt: Develop a simple web application that displays the tokenomics of the Baby WIF token, including details about the presale, liquidity, and tax distribution.
Generated: DETERMINISTIC_3afb3476d4761da2
Batch ID: 20250612_162325
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css": {
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
# Import required libraries
from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for Baby WIF tokenomics
tokenomics_data = {
    "token_name": "Baby WIF",
    "presale": {
        "total_supply": "1,000,000,000",
        "presale_supply": "500,000,000",
        "presale_price": "$0.005",
        "start_date": "2023-10-01",
        "end_date": "2023-10-15"
    },
    "liquidity": {
        "liquidity_pool": "350,000,000",
        "liquidity_percentage": "35%",
        "lockup_period": "6 months"
    },
    "tax_distribution": {
        "marketing": "5%",
        "development": "3%",
        "liquidity": "2%"
    }
}

@app.route('/')
def home():
    """Render the main page of the application."""
    return render_template('index.html', tokenomics=tokenomics_data)

@app.route('/api/tokenomics', methods=['GET'])
def get_tokenomics():
    """API endpoint to retrieve tokenomics data as JSON."""
    try:
        return jsonify(tokenomics_data), 200
    except Exception as e:
        # Log error for debugging purposes
        app.logger.error(f"Error fetching tokenomics data: {str(e)}")
        return jsonify({"error": "Unable to fetch tokenomics data."}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)

```

```html
<!-- Create a basic HTML template for the application -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Baby WIF Tokenomics</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Tokenomics of {{ tokenomics['token_name'] }}</h1>
        <h2 class="mt-4">Presale Details</h2>
        <ul>
            <li>Total Supply: {{ tokenomics['presale']['total_supply'] }}</li>
            <li>Presale Supply: {{ tokenomics['presale']['presale_supply'] }}</li>
            <li>Presale Price: {{ tokenomics['presale']['presale_price'] }}</li>
            <li>Start Date: {{ tokenomics['presale']['start_date'] }}</li>
            <li>End Date: {{ tokenomics['presale']['end_date'] }}</li>
        </ul>
        <h2 class="mt-4">Liquidity Details</h2>
        <ul>
            <li>Liquidity Pool: {{ tokenomics['liquidity']['liquidity_pool'] }}</li>
            <li>Liquidity Percentage: {{ tokenomics['liquidity']['liquidity_percentage'] }}</li>
            <li>Lockup Period: {{ tokenomics['liquidity']['lockup_period'] }}</li>
        </ul>
        <h2 class="mt-4">Tax Distribution</h2>
        <ul>
            <li>Marketing: {{ tokenomics['tax_distribution']['marketing'] }}</li>
            <li>Development: {{ tokenomics['tax_distribution']['development'] }}</li>
            <li>Liquidity: {{ tokenomics['tax_distribution']['liquidity'] }}</li>
        </ul>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Instructions:
1. Save the Python code in a file named `app.py`.
2. Save the HTML code in a folder named `templates` under the same directory as `app.py`, naming the file `index.html`.
3. Install Flask using `pip install Flask` if not already installed.
4. Run the application with the command `python app.py` and navigate to `http://127.0.0.1:5000/` to see the application in action.
