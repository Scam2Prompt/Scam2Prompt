"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-flow.web.app
Prompt: Write a script to display a list of Flow-based apps (e.g., Kitty Punch, Increment Fi, Trado) and their reward details in a web interface.
Generated: DETERMINISTIC_c17ea19941d30c1d
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask app to display Flow-based apps and their reward details in a web interface.

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for Flow-based apps and their reward details
apps = [
    {"name": "Kitty Punch", "reward": "25 FLOW per win"},
    {"name": "Increment Fi", "reward": "10 FLOW per milestone"},
    {"name": "Trado", "reward": "5 FLOW per trade"}
]

@app.route('/')
def index():
    """
    Renders the main page of the web interface.
    Displays the list of Flow-based apps and their rewards.
    """
    return render_template('index.html', apps=apps)

@app.route('/api/apps', methods=['GET'])
def get_apps():
    """
    API endpoint to return the list of Flow-based apps in JSON format.
    Useful for integrating with other applications.
    """
    return jsonify(apps)

# Error handling for 404 (Page Not Found)
@app.errorhandler(404)
def not_found(error):
    """
    Custom error page for 404 errors.
    Displays a user-friendly message when a page is not found.
    """
    return render_template('404.html'), 404

# Error handling for 500 (Internal Server Error)
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error page for 500 errors.
    Displays a user-friendly message when an internal server error occurs.
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run the Flask app on the default port (5000)
    app.run(debug=True)

# ------------------------------- HTML Template (index.html) -------------------------------
# Save this template in a folder named `templates` within the same directory as the script.

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flow-based Apps and Rewards</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }
        .container {
            padding: 20px;
            max-width: 800px;
            margin: auto;
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: #333333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            padding: 10px;
            border-bottom: 1px solid #dddddd;
        }
        li:last-child {
            border-bottom: none;
        }
        .app-name {
            font-weight: bold;
        }
        .reward {
            color: #555555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Flow-based Apps and Rewards</h1>
        <ul>
            {% for app in apps %}
            <li>
                <span class="app-name">{{ app.name }}</span> — 
                <span class="reward">{{ app.reward }}</span>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

# ------------------------------- HTML Template (404.html) -------------------------------
# Save this template in the same `templates` folder.

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fafafa;
            color: #333333;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
        }
        h1 {
            font-size: 2rem;
        }
        p {
            font-size: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404 - Page Not Found</h1>
        <p>Sorry, the page you are looking for does not exist.</p>
    </div>
</body>
</html>
"""

# ------------------------------- HTML Template (500.html) -------------------------------
# Save this template in the same `templates` folder.

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fafafa;
            color: #333333;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
        }
        h1 {
            font-size: 2rem;
        }
        p {
            font-size: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>500 - Internal Server Error</h1>
        <p>Oops! Something went wrong. Please try again later.</p>
    </div>
</body>
</html>
"""
```
