"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erismizar.com
Prompt: Generate a code snippet for an e-commerce website that displays eco-friendly sneakers like the M101 model from Eris Mizar, including options for color and size selection.
Generated: DETERMINISTIC_eb1b312e02426271
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Sample data for sneakers (would typically come from a database)
sneakers = {
    "M101": {
        "name": "Eco-Friendly Sneakers - M101",
        "brand": "Eris Mizar",
        "colors": ["Green", "Blue", "Black"],
        "sizes": ["6", "7", "8", "9", "10", "11"],
        "price": 89.99,
        "description": "Sustainable sneakers crafted for comfort and performance."
    }
}

# Route to display sneaker details
@app.route("/")
def home():
    """
    Renders the main page displaying sneakers.
    """
    return render_template("index.html", sneaker=sneakers["M101"])

# Route to handle color and size selection
@app.route("/select", methods=["POST"])
def select():
    """
    Handles color and size selection from the user.
    Processes the POST request and returns a confirmation response.
    """
    try:
        # Extract color and size from request
        color = request.form.get("color")
        size = request.form.get("size")

        # Validate inputs
        if color not in sneakers["M101"]["colors"]:
            return jsonify({"error": "Invalid color selected."}), 400
        if size not in sneakers["M101"]["sizes"]:
            return jsonify({"error": "Invalid size selected."}), 400

        # Return success response
        return jsonify({
            "message": "Selection successful!",
            "selected_color": color,
            "selected_size": size,
            "price": sneakers["M101"]["price"]
        })

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/index.html` (HTML Template)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ sneaker.name }}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>{{ sneaker.name }}</h1>
        <p><strong>Brand:</strong> {{ sneaker.brand }}</p>
        <p><strong>Description:</strong> {{ sneaker.description }}</p>
        <p><strong>Price:</strong> ${{ sneaker.price }}</p>

        <form id="selection-form" method="POST" action="/select">
            <label for="color">Choose a color:</label><br>
            <select id="color" name="color">
                {% for color in sneaker.colors %}
                <option value="{{ color }}">{{ color }}</option>
                {% endfor %}
            </select><br>

            <label for="size">Choose a size:</label><br>
            <select id="size" name="size">
                {% for size in sneaker.sizes %}
                <option value="{{ size }}">{{ size }}</option>
                {% endfor %}
            </select><br><br>

            <button type="submit">Confirm Selection</button>
        </form>
    </div>

    <script>
        // Example: Handle form submission via JavaScript (to avoid full page reload)
        const form = document.getElementById('selection-form');
        form.addEventListener('submit', async (event) => {
            event.preventDefault();

            const formData = new FormData(form);
            const response = await fetch('/select', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            if (response.ok) {
                alert(`Success: ${result.message}\nColor: ${result.selected_color}\nSize: ${result.selected_size}\nPrice: $${result.price}`);
            } else {
                alert(`Error: ${result.error}`);
            }
        });
    </script>
</body>
</html>
```

### `styles.css` (CSS Styles)
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

h1 {
    color: #2a9d8f;
}

button {
    background-color: #2a9d8f;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #21867a;
}

select {
    padding: 5px;
    margin: 5px 0;
    width: 100%;
}
```
