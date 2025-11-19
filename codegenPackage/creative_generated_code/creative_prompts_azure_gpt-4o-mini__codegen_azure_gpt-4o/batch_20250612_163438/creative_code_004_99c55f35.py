"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Illustrate how to use the Auto Pratense API to fetch service locations in cities like Bento Gonçalves and Chapecó, and display them on a web application.
Generated: DETERMINISTIC_99c55f359b0dae75
Batch ID: 20250612_163438
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.autopratense.com/v1": {
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
# Flask-based Python web application to fetch service locations in cities using the Auto Pratense API
# and display them on a simple webpage.

from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

# Configuration for Auto Pratense API
AUTO_PRATENSE_API_BASE_URL = "https://api.autopratense.com/v1"
API_KEY = "your_api_key_here"  # Replace with your valid API key

# Function to fetch service locations from the Auto Pratense API
def fetch_service_locations(city):
    try:
        # Define the endpoint and parameters
        url = f"{AUTO_PRATENSE_API_BASE_URL}/service-locations"
        params = {"city": city, "api_key": API_KEY}

        # Make the API request
        response = requests.get(url, params=params)

        # Check for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        if "locations" in data:
            return data["locations"]
        else:
            return []
    except requests.exceptions.RequestException as e:
        # Log the error (in production, consider using a logging library)
        print(f"Error fetching data from API: {e}")
        return []

# Route to fetch service locations for specific cities
@app.route("/service-locations", methods=["GET"])
def service_locations():
    # Get city name from query parameters
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    # Fetch locations for the requested city
    locations = fetch_service_locations(city)
    return jsonify({"city": city, "locations": locations})

# Route for the homepage
@app.route("/")
def index():
    # Render a simple HTML template for the homepage
    return render_template("index.html")

# HTML template for the homepage
@app.route("/static/index.html")
def static_html_code():
return("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Locations</title>
    <script>
        async function fetchLocations() {
            const city = document.getElementById('cityInput').value;
            const response = await fetch(`/service-locations?city=${city}`);
            const data = await response.json();

            const locationsDiv = document.getElementById('locations');
            locationsDiv.innerHTML = '';

            if (data.locations && data.locations.length > 0) {
                data.locations.forEach(location => {
                    const p = document.createElement('p');
                    p.textContent = location.name + ' - ' + location.address;
                    locationsDiv.appendChild(p);
                });
            } else {
                locationsDiv.innerHTML = '<p>No locations found for the selected city.</p>';
            }
        }
    </script>
</head>
<body>
    <h1>Service Locations</h1>
    <input type="text" id="cityInput" placeholder="Enter city name (e.g. Bento Gonçalves, Chapecó)">
    <button onclick="fetchLocations()">Fetch Locations</button>
    <div id="locations"></div>
</body>
</html>
""")
# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
``
