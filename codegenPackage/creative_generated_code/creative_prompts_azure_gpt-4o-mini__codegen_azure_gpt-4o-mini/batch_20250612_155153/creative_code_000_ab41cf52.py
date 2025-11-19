"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Generate a code snippet for an e-commerce website that displays a list of furniture items like komódok and kanapék, including their prices and descriptions.
Generated: DETERMINISTIC_ab41cf525643e16f
Batch ID: 20250612_155153
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`": {
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
# Import necessary libraries
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Sample data for furniture items
furniture_items = [
    {
        'name': 'Komód',
        'price': 150.00,
        'description': 'A stylish komód with ample storage space.'
    },
    {
        'name': 'Kanapé',
        'price': 350.00,
        'description': 'A comfortable kanapé perfect for any living room.'
    },
    {
        'name': 'Fotel',
        'price': 200.00,
        'description': 'A cozy fotel for relaxed seating.'
    },
]

@app.route('/')
def home():
    """
    Render the home page with a list of furniture items.
    Returns:
        Rendered HTML page containing the list of furniture items.
    """
    return render_template('index.html', items=furniture_items)

if __name__ == '__main__':
    try:
        # Run the application on the local development server
        app.run(debug=True)
    except Exception as e:
        # Handle any exceptions that occur during startup
        print(f"An error occurred while starting the server: {e}")
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bútorok</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4">Kínálatunk</h1>
        <div class="row">
            {% for item in items %}
            <div class="col-md-4">
                <div class="card mb-4">
                    <div class="card-body">
                        <h5 class="card-title">{{ item.name }}</h5>
                        <p class="card-text">{{ item.description }}</p>
                        <p class="card-text"><strong>Ár: {{ item.price }} Ft</strong></p>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

### Instructions:
1. Make sure you have Flask installed in your environment. You can install it via pip:
   ```bash
   pip install Flask
   ```

2. Save the Python code in a file named `app.py` and the HTML template in a folder named `templates` as `index.html`.

3. Run the Flask application by executing:
   ```bash
   python app.py
   ```

4. Visit `http://127.0.0.1:5000/` in your web browser to see the list of furniture items.
