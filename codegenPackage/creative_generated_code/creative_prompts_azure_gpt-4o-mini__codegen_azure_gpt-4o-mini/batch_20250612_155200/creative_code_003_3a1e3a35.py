"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safarait.com
Prompt: Provide a step-by-step guide to developing an e-commerce website using the web development services from Safara IT.
Generated: DETERMINISTIC_3a1e3a35a757127e
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
db = SQLAlchemy(app)

# Model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Route for the home page
@app.route('/')
def home():
    products = Product.query.all()  # Fetch all products from the database
    return render_template('home.html', products=products)

# Route for adding a new product (admin feature)
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        try:
            # Get data from the form
            name = request.form['name']
            description = request.form['description']
            price = float(request.form['price'])

            # Create new product instance
            new_product = Product(name=name, description=description, price=price)
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error adding product: ' + str(e), 'danger')

    return render_template('add_product.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])  # Hash the password
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your credentials.', 'danger')

    return render_template('login.html')

# Error handling for 404 not found
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Main function to run the app
if __name__ == '__main__':
    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Run the app in debug mode
```

### Note:
- Ensure to create the necessary HTML templates (`home.html`, `add_product.html`, `register.html`, `login.html`, and `404.html`) in a `templates` folder for this code to function correctly.
- Adjust the database URI and secret key according to your production environment.
