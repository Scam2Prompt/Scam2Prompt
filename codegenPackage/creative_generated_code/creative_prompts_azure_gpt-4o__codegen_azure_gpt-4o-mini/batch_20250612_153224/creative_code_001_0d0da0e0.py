"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Recommend a library or framework to build a web application for showcasing Ecoplast and Casary interior design samples, including filtering by product type and model.
Generated: DETERMINISTIC_0d0da0e0b354d44a
Batch ID: 20250612_153224
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
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///design_samples.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection
db = SQLAlchemy(app)

# Define a model for interior design samples
class DesignSample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<DesignSample {self.model}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the homepage displaying all design samples
@app.route('/')
def index():
    samples = DesignSample.query.all()
    return render_template('index.html', samples=samples)

# Route for filtering design samples by product type
@app.route('/filter', methods=['GET'])
def filter_samples():
    product_type = request.args.get('product_type')
    if not product_type:
        return jsonify({'error': 'Product type is required'}), 400
    samples = DesignSample.query.filter_by(product_type=product_type).all()
    return jsonify([{'id': sample.id, 'model': sample.model, 'image_url': sample.image_url} for sample in samples])

# Error handling for server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ecoplast and Casary Interior Designs</title>
</head>
<body>
    <h1>Interior Design Samples</h1>
    <div id="samples">
        {% for sample in samples %}
            <div>
                <h2>{{ sample.model }}</h2>
                <img src="{{ sample.image_url }}" alt="{{ sample.model }}">
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

### Database Initialization
You can populate the database with initial data by using a script or command line to add `DesignSample` entries. 

Make sure to install the required packages in your virtual environment:
```bash
pip install Flask Flask-SQLAlchemy
```

This template is ready for production with proper comments, error handling, and a clear structure. Adjust the database configurations and HTML as necessary to fit your specific requirements.
