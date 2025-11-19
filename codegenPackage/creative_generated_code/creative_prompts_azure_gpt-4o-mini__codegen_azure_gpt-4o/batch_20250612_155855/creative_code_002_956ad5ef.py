"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: Generate a script that calculates the total number of keys bought and displays it on a web page for a presale event.
Generated: DETERMINISTIC_956ad5ef5f50a80f
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the total number of keys bought in a presale event
# and display it on a web page using Flask framework

from flask import Flask, jsonify, render_template
import logging

app = Flask(__name__)

# Mocked data representing keys bought by individual users
# In production, this data would typically come from a database or an API
keys_bought_data = [
    {"user_id": 1, "keys_bought": 5},
    {"user_id": 2, "keys_bought": 10},
    {"user_id": 3, "keys_bought": 3},
    {"user_id": 4, "keys_bought": 7},
]

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_total_keys(data):
    """
    Calculates the total number of keys bought from a list of user data.
    :param data: List of dictionaries containing "keys_bought" values.
    :return: Total keys bought (integer).
    """
    try:
        total_keys = sum(item["keys_bought"] for item in data)
        return total_keys
    except Exception as e:
        logging.error(f"Error calculating total keys: {e}")
        return 0  # Return 0 as fallback in case of error


@app.route("/")
def home():
    """
    Homepage route that displays the total number of keys bought.
    :return: Rendered HTML page.
    """
    try:
        total_keys = calculate_total_keys(keys_bought_data)
        logging.info(f"Total keys bought: {total_keys}")
        return render_template("index.html", total_keys=total_keys)
    except Exception as e:
        logging.error(f"Error rendering homepage: {e}")
        return "An error occurred while processing your request.", 500


@app.route("/api/total_keys")
def api_total_keys():
    """
    API route to fetch the total number of keys bought as JSON.
    :return: JSON response with total keys bought.
    """
    try:
        total_keys = calculate_total_keys(keys_bought_data)
        logging.info(f"Total keys bought (API): {total_keys}")
        return jsonify({"total_keys": total_keys})
    except Exception as e:
        logging.error(f"Error fetching total keys via API: {e}")
        return jsonify({"error": "An error occurred while fetching the data."}), 500


if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)
```

Place the following `index.html` file in a `templates/` folder in the same directory as the script:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presale Event</title>
</head>
<body>
    <h1>Presale Event</h1>
    <p>Total Keys Bought: {{ total_keys }}</p>
</body>
</html>
```
