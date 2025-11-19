"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Design a web application feature that allows users to explore different wine flavors and aromas, akin to the experiences at FestiVin Caraquet.
Generated: DETERMINISTIC_d113a922caa65ee2
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
# Flask-based web application to explore wine flavors and aromas

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load wine data from a JSON file (simulating a database)
def load_wine_data():
    try:
        with open("wine_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "Wine data file not found."}
    except json.JSONDecodeError:
        return {"error": "Error decoding wine data file."}

# Route: Home page
@app.route("/")
def home():
    """
    Render the home page where users can explore wine flavors and aromas.
    """
    return render_template("index.html")

# Route: Get wine data
@app.route("/api/wines", methods=["GET"])
def get_wines():
    """
    API endpoint to fetch wine data.
    """
    wine_data = load_wine_data()
    if "error" in wine_data:
        return jsonify({"error": wine_data["error"]}), 500
    return jsonify(wine_data)

# Route: Search wine by flavor or aroma
@app.route("/api/search", methods=["GET"])
def search_wines():
    """
    API endpoint to search wines by flavor or aroma.
    """
    query = request.args.get("query", "").lower()
    wine_data = load_wine_data()
    if "error" in wine_data:
        return jsonify({"error": wine_data["error"]}), 500

    # Filter wines based on the query
    filtered_wines = [
        wine for wine in wine_data["wines"]
        if query in wine["flavors"].lower() or query in wine["aromas"].lower()
    ]
    return jsonify(filtered_wines)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully.
    """
    return render_template("404.html"), 404

# Run the application
if __name__ == "__main__":
    app.run(debug=True)

# templates/index.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Explore Wine Flavors and Aromas</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to FestiVin Caraquet Wine Explorer</h1>
    <input type="text" id="search" placeholder="Search by flavor or aroma">
    <button onclick="searchWines()">Search</button>
    <div id="results"></div>

    <script>
        async function searchWines() {
            const query = document.getElementById('search').value;
            const response = await fetch(`/api/search?query=${query}`);
            const wines = await response.json();
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';

            if (wines.length === 0) {
                resultsDiv.innerHTML = '<p>No wines found matching your search.</p>';
            } else {
                wines.forEach(wine => {
                    const wineDiv = document.createElement('div');
                    wineDiv.innerHTML = `<h3>${wine.name}</h3><p>Flavors: ${wine.flavors}</p><p>Aromas: ${wine.aromas}</p>`;
                    resultsDiv.appendChild(wineDiv);
                });
            }
        }
    </script>
</body>
</html>
"""

# templates/404.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Go back to the home page</a>
</body>
</html>
"""

# wine_data.json
"""
{
    "wines": [
        {
            "name": "Chardonnay",
            "flavors": "Citrus, Apple, Pear",
            "aromas": "Vanilla, Butter, Oak"
        },
        {
            "name": "Merlot",
            "flavors": "Plum, Cherry, Chocolate",
            "aromas": "Spice, Tobacco, Cedar"
        },
        {
            "name": "Cabernet Sauvignon",
            "flavors": "Blackberry, Black Currant, Mint",
            "aromas": "Leather, Pepper, Vanilla"
        }
    ]
}
"""

# static/styles.css
"""
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background-color: #f8f8f8;
}

h1 {
    color: #333;
}

input, button {
    margin: 10px 0;
    padding: 10px;
    font-size: 16px;
}

#results div {
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ccc;
    background-color: #fff;
}
"""
```
