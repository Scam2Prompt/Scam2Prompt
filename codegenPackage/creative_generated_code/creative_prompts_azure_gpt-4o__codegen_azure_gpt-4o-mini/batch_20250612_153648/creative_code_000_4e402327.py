"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamass.de
Prompt: Write code to prototype a web publishing platform that incorporates SEO optimization and e-commerce functionality, as described in the services offered by metamass.de.
Generated: DETERMINISTIC_4e40232703ed2ce7
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define models for the web publishing platform
class Article(db.Model):
    """Model for storing articles."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'

class Product(db.Model):
    """Model for storing e-commerce products."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Error handling for NotFound and BadRequest
@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error=str(e)), 400

# Route to create a new article
@app.route('/articles', methods=['POST'])
def create_article():
    """Create a new article."""
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    slug = data.get('slug')

    if not title or not content or not slug:
        raise BadRequest("Title, content, and slug are required.")

    new_article = Article(title=title, content=content, slug=slug)
    db.session.add(new_article)
    db.session.commit()
    return jsonify({'message': 'Article created', 'id': new_article.id}), 201

# Route to get all articles
@app.route('/articles', methods=['GET'])
def get_articles():
    """Retrieve all articles."""
    articles = Article.query.all()
    return jsonify([{ 'id': article.id, 'title': article.title, 'slug': article.slug } for article in articles])

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product."""
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    if not name or not description or price is None:
        raise BadRequest("Name, description, and price are required.")

    new_product = Product(name=name, description=description, price=price)
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created', 'id': new_product.id}), 201

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products."""
    products = Product.query.all()
    return jsonify([{ 'id': product.id, 'name': product.name, 'price': product.price } for product in products])

# Route to render a homepage
@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

# Function to run the database migration
def create_database():
    """Create the database and tables."""
    db.create_all()

if __name__ == '__main__':
    create_database()  # Ensure the database is created before starting the app
    app.run(debug=True)  # Run the app in debug mode
```

**Note:** This code uses Flask as a web framework and SQLAlchemy as an ORM for database management. You will need to install Flask and Flask-SQLAlchemy to run this code successfully. Additionally, create an `index.html` file in a `templates` directory for the homepage rendering.
