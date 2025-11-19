"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csh-gamesapp.weebly.com
Prompt: What library can I use to build a customizable e-commerce website similar to Piuka's, focusing on accessories and promotions?
Generated: DETERMINISTIC_4c41d3640581e246
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define database model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<Product {self.name}>'

# Route to display all products
@app.route('/')
def index():
    try:
        products = Product.query.all()  # Fetch all products from database
        return render_template('index.html', products=products)
    except Exception as e:
        return handle_error(e)

# Route to add a new product
@app.route('/add', methods=['POST'])
def add_product():
    try:
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        image_url = request.form.get('image_url')
        category = request.form['category']
        
        new_product = Product(name=name, description=description, price=price, image_url=image_url, category=category)
        db.session.add(new_product)
        db.session.commit()
        
        return redirect(url_for('index'))
    except Exception as e:
        return handle_error(e)

# Error handling
@app.errorhandler(HTTPException)
def handle_error(e):
    return render_template('error.html', error=e), e.code

@app.errorhandler(Exception)
def handle_general_error(e):
    return render_template('error.html', error='An unexpected error occurred.'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```

**HTML Templates:**
- `index.html`: Template to display the list of products.
- `error.html`: Template to display error messages. 

**Database Migration:**
- To initialize and migrate the database, run:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

**Note**: Ensure that Flask, Flask-SQLAlchemy, and Flask-Migrate are installed in your Python environment.
