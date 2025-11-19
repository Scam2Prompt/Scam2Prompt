"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naimatabbasind.com
Prompt: Illustrate how to use the Naimat Abbas Industries API to retrieve information about their martial arts gear and display it on a web page.
Generated: DETERMINISTIC_fae6bd6f1a279959
Batch ID: 20250612_164058
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.naimatabbasindustries.com/v1": {
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
# Import necessary modules
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Configuration for the API
API_BASE_URL = "https://api.naimatabbasindustries.com/v1"
API_ENDPOINT = "/martial-arts-gear"
API_KEY = "your_api_key_here"  # Replace with your actual API key

def fetch_martial_arts_gear():
    """
    Fetch martial arts gear data from the Naimat Abbas Industries API.
    
    Returns:
        list: A list of martial arts gear items if successful, otherwise None.
    """
    try:
        # Construct the headers for authentication
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        # Make the GET request to the API
        response = requests.get(API_BASE_URL + API_ENDPOINT, headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            return response.json()  # Return the JSON response
        else:
            # Log an error message if the API call fails
            print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Handle exceptions that may occur during the API call
        print(f"Exception occurred while fetching data: {e}")
        return None


@app.route('/')
def index():
    """
    Home route that displays a list of martial arts gear on the webpage.
    
    Returns:
        str: Rendered HTML of the web page.
    """
    # Fetch data from the API
    gear_data = fetch_martial_arts_gear()

    if gear_data is None:
        # Render an error message if data could not be fetched
        return render_template("error.html", message="Failed to retrieve martial arts gear data.")

    # Render the HTML template and pass the gear data
    return render_template("index.html", gear_items=gear_data)


# Error-handling route for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom message.
    """
    return render_template("error.html", message="Page not found."), 404


# Error-handling route for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors with a custom message.
    """
    return render_template("error.html", message="Internal server error."), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

```

**HTML Templates**:

`templates/index.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Martial Arts Gear</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .gear-item {
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .gear-item h3 {
            margin: 0 0 5px;
        }
        .gear-item p {
            margin: 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Martial Arts Gear</h1>
        {% for item in gear_items %}
        <div class="gear-item">
            <h3>{{ item['name'] }}</h3>
            <p>Price: ${{ item['price'] }}</p>
            <p>Description: {{ item['description'] }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

`templates/error.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .error-message {
            text-align: center;
            padding: 20px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="error-message">
        <h1>Error</h1>
        <p>{{ message }}</p>
    </div>
</body>
</html>
```

Replace `your_api_key_here` with your actual API key in the Python code.
