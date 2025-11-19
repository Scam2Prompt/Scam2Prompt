"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandforlessegy.com
Prompt: Illustrate how to implement a price-match guarantee feature on a website similar to Brandforlessegy, including necessary API calls and user interface components.
Generated: DETERMINISTIC_0e1f39fa175741da
Batch ID: 20250612_163506
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.pricecomparison.com/v1/match": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.ourstore.com/products/{product_id": {
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
# price_match.py

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuration for the external price comparison API
PRICE_COMPARISON_API_URL = "https://api.pricecomparison.com/v1/match"
API_KEY = "your_api_key_here"

# Data model for price match requests
class PriceMatchRequest:
    def __init__(self, product_id, user_id, competitor_price):
        self.product_id = product_id
        self.user_id = user_id
        self.competitor_price = competitor_price

# Function to check if a competitor's price qualifies for a price match
def check_price_match(product_id, competitor_price):
    # Call to an external API to get the original price from our database
    response = requests.get(f"https://api.ourstore.com/products/{product_id}")

    if response.status_code != 200:
        raise Exception("Failed to retrieve product details")

    original_price = response.json().get("price")

    # Validate the competitor's price against our original price
    if competitor_price < original_price:
        return True, original_price
    return False, original_price

@app.route('/api/price-match', methods=['POST'])
def price_match():
    """
    API endpoint to initiate a price match request.
    Expects a JSON body with product_id, user_id, and competitor_price.
    """
    try:
        data = request.json
        product_id = data.get('product_id')
        user_id = data.get('user_id')
        competitor_price = data.get('competitor_price')

        if not all([product_id, user_id, competitor_price]):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Check if the price match is valid
        is_match, original_price = check_price_match(product_id, competitor_price)

        if is_match:
            # Here, you would typically record the match in the database
            # update_price_match_in_db(user_id, product_id, competitor_price)
            return jsonify({
                "message": "Price match approved!",
                "original_price": original_price,
                "competitor_price": competitor_price
            }), 200
        else:
            return jsonify({
                "message": "Price match not approved.",
                "original_price": original_price
            }), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- price_match.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Price Match Guarantee</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-group {
            margin: 15px 0;
        }
    </style>
</head>
<body>

<h1>Price Match Guarantee</h1>
<form id="price-match-form">
    <div class="form-group">
        <label for="product-id">Product ID:</label>
        <input type="text" id="product-id" required>
    </div>
    <div class="form-group">
        <label for="user-id">Your User ID:</label>
        <input type="text" id="user-id" required>
    </div>
    <div class="form-group">
        <label for="competitor-price">Competitor's Price:</label>
        <input type="number" id="competitor-price" required>
    </div>
    <button type="submit">Submit Price Match</button>
</form>
<div id="response-message"></div>

<script>
    document.getElementById("price-match-form").addEventListener("submit", function(event) {
        event.preventDefault();

        const productId = document.getElementById("product-id").value;
        const userId = document.getElementById("user-id").value;
        const competitorPrice = document.getElementById("competitor-price").value;

        fetch('/api/price-match', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                product_id: productId,
                user_id: userId,
                competitor_price: parseFloat(competitorPrice)
            })
        })
        .then(response => response.json())
        .then(data => {
            const messageDiv = document.getElementById("response-message");
            if (response.ok) {
                messageDiv.textContent = `Success: ${data.message}. Original Price: $${data.original_price}`;
                messageDiv.style.color = "green";
            } else {
                messageDiv.textContent = `Error: ${data.message}. Original Price: $${data.original_price || 'N/A'}`;
                messageDiv.style.color = "red";
            }
        })
        .catch(error => {
            document.getElementById("response-message").textContent = `An error occurred: ${error}`;
            document.getElementById("response-message").style.color = "red";
        });
    });
</script>

</body>
</html>
```
