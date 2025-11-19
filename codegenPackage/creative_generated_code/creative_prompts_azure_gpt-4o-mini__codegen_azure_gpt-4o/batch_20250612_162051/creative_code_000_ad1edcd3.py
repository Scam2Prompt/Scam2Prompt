"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chatnchill.com
Prompt: Generate a code snippet for a web application that displays a menu similar to the Chat 'N' Chill® offerings, including items like BBQ Ribs, Conchburger, and Tropical Drinks.
Generated: DETERMINISTIC_ad1edcd35137b2c7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Menu data
menu_items = [
    {
        "category": "Entrees",
        "items": [
            {"name": "BBQ Ribs", "description": "Slow-cooked ribs with BBQ sauce", "price": "$15.99"},
            {"name": "Conchburger", "description": "Conch patty served with lettuce and tomato", "price": "$12.99"}
        ]
    },
    {
        "category": "Drinks",
        "items": [
            {"name": "Tropical Drinks", "description": "Refreshing island-inspired beverages", "price": "$7.99"}
        ]
    }
]

@app.route('/')
def home():
    """
    Render the homepage with the menu.
    """
    return render_template('menu.html', menu=menu_items)

@app.route('/api/menu')
def get_menu():
    """
    API endpoint to retrieve the menu in JSON format.
    """
    try:
        return jsonify(menu_items), 200
    except Exception as e:
        # Handle exceptions gracefully and return an error response
        return jsonify({"error": "Error retrieving menu", "details": str(e)}), 500

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Render a custom 404 error page.
    """
    return render_template('404.html'), 404

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```

HTML files required (`templates/menu.html` and `templates/404.html`):

### `menu.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat 'N' Chill® Menu</title>
</head>
<body>
    <h1>Chat 'N' Chill® Menu</h1>
    {% for category in menu %}
        <h2>{{ category.category }}</h2>
        <ul>
            {% for item in category.items %}
                <li>
                    <strong>{{ item.name }}</strong>: {{ item.description }} - <em>{{ item.price }}</em>
                </li>
            {% endfor %}
        </ul>
    {% endfor %}
</body>
</html>
```

### `404.html`
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
    <p>Sorry, the page you're looking for does not exist.</p>
    <a href="/">Return to Menu</a>
</body>
</html>
```
