"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Write a script that generates a product page for a collectible comic book edition, including features like "20 random copies containing a signature" and a "limited stock" badge, inspired by the Top G #3.1 Parallel Protocols edition.
Generated: DETERMINISTIC_4f94f7277c25e987
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Product information
PRODUCT_NAME = "Top G #3.1 Parallel Protocols"
TOTAL_COPIES = 500
SIGNED_COPIES = 20
LIMITED_STOCK_THRESHOLD = 50

# Generate random signed copies (IDs)
signed_copy_ids = random.sample(range(1, TOTAL_COPIES + 1), SIGNED_COPIES)

@app.route("/")
def product_page():
    """
    Serve the product page for the collectible comic book edition.
    """
    # Determine if the stock is limited
    stock_remaining = TOTAL_COPIES - len(signed_copy_ids)
    is_limited_stock = stock_remaining <= LIMITED_STOCK_THRESHOLD

    return render_template(
        "product_page.html",
        product_name=PRODUCT_NAME,
        total_copies=TOTAL_COPIES,
        signed_copy_ids=signed_copy_ids,
        stock_remaining=stock_remaining,
        is_limited_stock=is_limited_stock
    )

@app.route("/api/get_signed_copies")
def get_signed_copies():
    """
    API endpoint to retrieve signed copy IDs.
    """
    return jsonify({"signed_copy_ids": signed_copy_ids})

# Error handling example for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Page not found"), 404

# Run the Flask server
if __name__ == "__main__":
    # Run the server on localhost with debug mode off for production readiness
    app.run(host="0.0.0.0", port=5000, debug=False)
```

---

### `templates/product_page.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product_name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .badge {
            display: inline-block;
            padding: 5px 10px;
            color: white;
            background-color: red;
            border-radius: 5px;
        }
        .stock-info {
            margin-top: 10px;
        }
        .signature {
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>{{ product_name }}</h1>

    <p>Total Copies: {{ total_copies }}</p>
    <p>Signed Copies: <span class="signature">{{ signed_copy_ids | length }}</span></p>
    {% if is_limited_stock %}
        <div class="badge">Limited Stock!</div>
    {% endif %}
    <div class="stock-info">
        <p>Stock Remaining: {{ stock_remaining }}</p>
    </div>
</body>
</html>
```
