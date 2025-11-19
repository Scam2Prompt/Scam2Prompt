"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Develop a simple web application that displays the different types of games available on S666, including live casino and sports betting options.
Generated: DETERMINISTIC_f2f636ffbe47c023
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s production-ready code to create a simple web application using Python with Flask:

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define a list of game types available on S666
games = [
    {"id": 1, "name": "Live Casino", "description": "Experience real-time casino games with live dealers."},
    {"id": 2, "name": "Sports Betting", "description": "Bet on major sports events across the globe."},
    {"id": 3, "name": "Slot Games", "description": "Play a variety of slot games with exciting themes."},
    {"id": 4, "name": "Poker", "description": "Join virtual poker tournaments and compete with others."},
    {"id": 5, "name": "Esports Betting", "description": "Bet on competitive gaming events worldwide."}
]

# Route for the home page
@app.route('/')
def home():
    """
    Render the home page with available game types.
    """
    return render_template('index.html', games=games)

# Route for fetching game data as JSON
@app.route('/api/games', methods=['GET'])
def get_games():
    """
    Return the list of games in JSON format.
    """
    return jsonify(games), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom message.
    """
    return render_template('404.html', message="Page not found!"), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors with a custom message.
    """
    return render_template('500.html', message="Internal server error!"), 500

# Run the Flask application
if __name__ == '__main__':
    # Set debug=False for production use
    app.run(debug=True)

```

### HTML Templates

Place the following HTML files in a folder named `templates` under your project directory.

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S666 Games</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .game {
            padding: 10px 0;
            border-bottom: 1px solid #ddd;
        }
        .game:last-child {
            border-bottom: none;
        }
        .game-name {
            font-weight: bold;
        }
        .game-description {
            margin: 0;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Available Games on S666</h1>
        {% for game in games %}
        <div class="game">
            <p class="game-name">{{ game.name }}</p>
            <p class="game-description">{{ game.description }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>{{ message }}</p>
</body>
</html>
```

#### `500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 - Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>{{ message }}</p>
</body>
</html>
```

### Notes:
1. Install Flask using `pip install flask` before running the application.
2. Set `debug=True` during development, but always set it to `debug=False` for production.
