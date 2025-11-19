"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobothebear.pages.dev
Prompt: Develop a web application that displays the roadmap for Bobo the Bear, highlighting milestones like CoinGecko listings and community partnerships.
Generated: DETERMINISTIC_1bb5ea102955b9d2
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for the web application
from flask import Flask, render_template, jsonify

# Initialize Flask application
app = Flask(__name__)

# Define the roadmap milestones for Bobo the Bear
roadmap = [
    {
        "phase": "Phase 1 - Launch",
        "milestones": [
            "Token deployment on the blockchain",
            "Initial website creation",
            "Social media presence established"
        ]
    },
    {
        "phase": "Phase 2 - Growth",
        "milestones": [
            "Community partnerships initiated",
            "Marketing campaigns launched",
            "First CoinGecko listing achieved"
        ]
    },
    {
        "phase": "Phase 3 - Expansion",
        "milestones": [
            "New features added to the platform",
            "Further listings on major exchanges",
            "Global community outreach programs"
        ]
    }
]

# Error handler for 404: Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Page not found"}), 404

# Error handler for 500: Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Define the route for the homepage
@app.route("/")
def home():
    # Render roadmap information on the homepage
    return render_template("index.html", roadmap=roadmap)

# Define route for API access to roadmap data
@app.route("/api/roadmap", methods=["GET"])
def get_roadmap():
    # Return roadmap data as JSON
    return jsonify({"roadmap": roadmap})

# Start the Flask application
if __name__ == "__main__":
    # Run the app in debug mode for development
    app.run(debug=True)
```

Create the `templates/index.html` file for the homepage:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bobo the Bear Roadmap</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 10px 20px;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        .phase {
            margin-bottom: 20px;
        }
        .milestones {
            padding-left: 20px;
        }
        .milestones li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Bobo the Bear Roadmap</h1>
    </header>
    <div class="container">
        {% for phase in roadmap %}
        <div class="phase">
            <h2>{{ phase.phase }}</h2>
            <ul class="milestones">
                {% for milestone in phase.milestones %}
                <li>{{ milestone }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

This code provides a clean and production-ready implementation of the requested web application.
