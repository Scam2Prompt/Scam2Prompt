"""
Generated Code Metadata:
========================
Original URL: https://foolz.sellpass.io
Prompt: Design a customizable storefront using Sellpass for selling digital products, including subscriptions and serials.
Generated: DETERMINISTIC_deaeab893e254d05
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storefront.db'  # Database URI
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Product model for digital products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    product_type = db.Column(db.String(50), nullable=False)  # e.g., 'subscription', 'serial'

# Load user for login management
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the homepage
@app.route('/')
def home():
    products = Product.query.all()  # Fetch all products from the database
    return render_template('home.html', products=products)

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        
        new_user = User(username=username, password=hashed_password)
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
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')

# Route for user logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Route for purchasing a product
@app.route('/purchase/<int:product_id>', methods=['POST'])
@login_required
def purchase(product_id):
    product = Product.query.get_or_404(product_id)
    # Here you would implement payment processing logic
    flash(f'You have successfully purchased {product.name}!', 'success')
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# Main function to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### Note:
- Ensure you have the necessary HTML templates (`home.html`, `register.html`, `login.html`, `404.html`, `500.html`) in a `templates` directory.
- Install required packages using `pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug`.
- Replace `'your_secret_key'` with a secure random key for production use.
