"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Build a web application that showcases furniture collections in a grid layout, with filters for categories (e.g., chairs, poufs, rugs) and features (e.g., "antimacchia," "sanificabile"), based on Nodo Italia's product descriptions.
Generated: DETERMINISTIC_a8a4484a53be49b4
Batch ID: 20250612_153246
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
  "http://127.0.0.1:5000/`.": {
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
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Furniture model
class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    features = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Furniture {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    # Get filter parameters from the request
    category_filter = request.args.get('category')
    feature_filter = request.args.get('feature')

    # Query the database for furniture items
    query = Furniture.query

    # Apply category filter if provided
    if category_filter:
        query = query.filter(Furniture.category == category_filter)

    # Apply feature filter if provided
    if feature_filter:
        query = query.filter(Furniture.features.contains(feature_filter))

    # Fetch the filtered results
    furniture_items = query.all()

    return render_template('index.html', furniture_items=furniture_items)

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Furniture Collection</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Furniture Collection</h1>
        
        <!-- Filter Form -->
        <form class="mb-4" method="get" action="/">
            <div class="form-row">
                <div class="form-group col-md-4">
                    <label for="category">Category</label>
                    <select id="category" name="category" class="form-control">
                        <option value="">All</option>
                        <option value="chairs">Chairs</option>
                        <option value="poufs">Poufs</option>
                        <option value="rugs">Rugs</option>
                    </select>
                </div>
                <div class="form-group col-md-4">
                    <label for="feature">Feature</label>
                    <input type="text" id="feature" name="feature" class="form-control" placeholder="e.g., antimacchia">
                </div>
                <div class="form-group col-md-4">
                    <label>&nbsp;</label>
                    <button type="submit" class="btn btn-primary btn-block">Filter</button>
                </div>
            </div>
        </form>

        <!-- Furniture Grid -->
        <div class="row">
            {% for item in furniture_items %}
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <img src="{{ item.image_url }}" class="card-img-top" alt="{{ item.name }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ item.name }}</h5>
                            <p class="card-text">Category: {{ item.category }}</p>
                            <p class="card-text">Features: {{ item.features }}</p>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

### Instructions to Run the Application
1. Ensure you have Python and Flask installed.
2. Save the Python code in a file named `app.py`.
3. Create a folder named `templates` and save the HTML files inside it.
4. Run the application using the command: `python app.py`.
5. Access the application in your web browser at `http://127.0.0.1:5000/`.
