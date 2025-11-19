"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.betterbooking.pk
Prompt: Write a code example for a web application that allows users to view and compare international tour packages from Better Booking.
Generated: DETERMINISTIC_5e72853fef5d4676
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
# A Python web application using Flask to allow users to view and compare international tour packages from Better Booking.

from flask import Flask, jsonify, request, render_template
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data for tour packages (in a real-world app, this would come from a database)
TOUR_PACKAGES = [
    {
        "id": 1,
        "destination": "Paris, France",
        "price": 1200,
        "duration_days": 5,
        "description": "Romantic getaway in the city of lights. Includes hotel accommodations and tours."
    },
    {
        "id": 2,
        "destination": "Tokyo, Japan",
        "price": 2000,
        "duration_days": 7,
        "description": "Experience the vibrant culture of Tokyo. Includes flights, hotel, and guided tours."
    },
    {
        "id": 3,
        "destination": "Rome, Italy",
        "price": 1500,
        "duration_days": 6,
        "description": "Explore ancient Roman landmarks. Includes guided tours and accommodations."
    }
]

@app.route('/')
def home():
    """
    Home route that displays the main page.
    """
    return render_template('index.html')


@app.route('/api/tour-packages', methods=['GET'])
def get_tour_packages():
    """
    API endpoint to retrieve all tour packages.
    Returns a JSON response with the list of tour packages.
    """
    try:
        logging.info("Fetching all tour packages")
        return jsonify({"success": True, "data": TOUR_PACKAGES}), 200
    except Exception as e:
        logging.error(f"Error retrieving tour packages: {str(e)}")
        return jsonify({"success": False, "error": "An error occurred while retrieving tour packages"}), 500


@app.route('/api/tour-packages/<int:package_id>', methods=['GET'])
def get_tour_package(package_id):
    """
    API endpoint to retrieve a single tour package by its ID.
    Returns a JSON response with the package details, or an error if not found.
    """
    try:
        package = next((p for p in TOUR_PACKAGES if p['id'] == package_id), None)
        if not package:
            logging.warning(f"Tour package with ID {package_id} not found")
            return jsonify({"success": False, "error": "Tour package not found"}), 404
        logging.info(f"Fetching tour package with ID {package_id}")
        return jsonify({"success": True, "data": package}), 200
    except Exception as e:
        logging.error(f"Error retrieving tour package: {str(e)}")
        return jsonify({"success": False, "error": "An error occurred while retrieving the tour package"}), 500


@app.route('/compare', methods=['POST'])
def compare_tour_packages():
    """
    Endpoint to compare tour packages based on IDs provided by the user.
    Accepts a JSON payload with the IDs of the packages to compare.
    """
    try:
        data = request.json
        package_ids = data.get("package_ids", [])
        if not package_ids or len(package_ids) < 2:
            logging.warning("Insufficient package IDs for comparison")
            return jsonify({"success": False, "error": "At least two package IDs are required for comparison"}), 400

        packages_to_compare = [p for p in TOUR_PACKAGES if p['id'] in package_ids]
        if len(packages_to_compare) < 2:
            logging.warning("Invalid package IDs provided for comparison")
            return jsonify({"success": False, "error": "Invalid package IDs provided"}), 404

        logging.info(f"Comparing packages: {package_ids}")
        return jsonify({"success": True, "data": packages_to_compare}), 200
    except Exception as e:
        logging.error(f"Error comparing tour packages: {str(e)}")
        return jsonify({"success": False, "error": "An error occurred while comparing tour packages"}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Better Booking Tour Packages</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            text-align: center;
        }
        .container {
            margin: 0 auto;
            max-width: 600px;
        }
        .package {
            border: 1px solid #ccc;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .package h2 {
            margin: 0;
        }
        .package p {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>Better Booking Tour Packages</h1>
    <div class="container">
        <div class="package">
            <h2>Destination: Paris, France</h2>
            <p>Price: $1200</p>
            <p>Duration: 5 days</p>
            <p>Description: Romantic getaway in the city of lights. Includes hotel accommodations and tours.</p>
        </div>
        <div class="package">
            <h2>Destination: Tokyo, Japan</h2>
            <p>Price: $2000</p>
            <p>Duration: 7 days</p>
            <p>Description: Experience the vibrant culture of Tokyo. Includes flights, hotel, and guided tours.</p>
        </div>
        <div class="package">
            <h2>Destination: Rome, Italy</h2>
            <p>Price: $1500</p>
            <p>Duration: 6 days</p>
            <p>Description: Explore ancient Roman landmarks. Includes guided tours and accommodations.</p>
        </div>
    </div>
</body>
</html>
```
