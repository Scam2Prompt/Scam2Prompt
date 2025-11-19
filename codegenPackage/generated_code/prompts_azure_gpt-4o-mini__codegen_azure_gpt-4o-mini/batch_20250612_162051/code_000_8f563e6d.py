"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: Generate a code snippet for a web application that allows users to search for properties to rent or buy in Neiva, Colombia, similar to the services offered by Inmobiliaria Félix Trujillo Falla.
Generated: DETERMINISTIC_8f563e6de2efe6ef
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/properties": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import requests

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the property API (mocked for this example)
PROPERTY_API_URL = "https://api.example.com/properties"  # Replace with actual API endpoint

@app.route('/')
def index():
    """Render the main search page."""
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_properties():
    """Search for properties based on user input."""
    try:
        # Get search parameters from the request
        property_type = request.args.get('type', default='rent', type=str)
        location = request.args.get('location', default='Neiva, Colombia', type=str)
        min_price = request.args.get('min_price', default=0, type=int)
        max_price = request.args.get('max_price', default=1000000, type=int)

        # Validate input parameters
        if min_price < 0 or max_price < 0 or min_price > max_price:
            return jsonify({"error": "Invalid price range."}), 400

        # Prepare the API request
        params = {
            'type': property_type,
            'location': location,
            'min_price': min_price,
            'max_price': max_price
        }

        # Make a request to the property API
        response = requests.get(PROPERTY_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses

        # Return the JSON response from the API
        return jsonify(response.json()), 200

    except requests.exceptions.RequestException as e:
        # Handle request errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Property Search</title>
</head>
<body>
    <h1>Search for Properties in Neiva, Colombia</h1>
    <form id="searchForm">
        <label for="type">Property Type:</label>
        <select id="type" name="type">
            <option value="rent">Rent</option>
            <option value="buy">Buy</option>
        </select>
        <br>
        <label for="location">Location:</label>
        <input type="text" id="location" name="location" value="Neiva, Colombia" required>
        <br>
        <label for="min_price">Min Price:</label>
        <input type="number" id="min_price" name="min_price" value="0" min="0">
        <br>
        <label for="max_price">Max Price:</label>
        <input type="number" id="max_price" name="max_price" value="1000000" min="0">
        <br>
        <button type="submit">Search</button>
    </form>
    <div id="results"></div>

    <script>
        document.getElementById('searchForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission

            // Gather form data
            const formData = new FormData(this);
            const params = new URLSearchParams(formData).toString();

            // Fetch properties from the server
            fetch(`/search?${params}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    // Display results
                    const resultsDiv = document.getElementById('results');
                    resultsDiv.innerHTML = JSON.stringify(data, null, 2);
                })
                .catch(error => {
                    // Handle errors
                    const resultsDiv = document.getElementById('results');
                    resultsDiv.innerHTML = `Error: ${error.message}`;
                });
        });
    </script>
</body>
</html>
```
