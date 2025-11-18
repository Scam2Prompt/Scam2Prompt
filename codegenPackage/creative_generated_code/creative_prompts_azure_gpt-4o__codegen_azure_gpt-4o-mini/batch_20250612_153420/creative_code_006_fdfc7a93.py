"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Create a CMS-based e-commerce website using Icchatva's web development services, ensuring compatibility with payment gateway APIs.
Generated: DETERMINISTIC_fdfc7a931f291976
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import stripe
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  # Replace with your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')  # Replace with your database URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Configure Stripe
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')  # Replace with your Stripe secret key

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Load user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for home page
@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

# Route for product checkout
@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    try:
        amount = float(request.form['amount']) * 100  # Amount in cents
        customer = stripe.Customer.create(email=current_user.username)
        stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='usd',
            description='E-commerce Purchase'
        )
        flash('Payment successful!', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        flash(f'Payment failed: {str(e)}', 'danger')
        return redirect(url_for('home'))

# User registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        flash('Login failed. Check your credentials.', 'danger')
    return render_template('login.html')

# User logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### HTML Templates (home.html, register.html, login.html)
- Please create corresponding HTML templates in the `templates` directory for rendering the views as indicated in the Python code. 

### Database Initialization
- To initialize the database, run the following commands in your terminal:
```bash
flask db init  # Initialize migrations folder
flask db migrate -m "Initial migration."  # Create migration script
flask db upgrade  # Apply migrations to the database
```

### Environment Variables
- Make sure to set the following environment variables before running the application:
  - `SECRET_KEY`: A secret key for session management.
  - `DATABASE_URL`: The URL of your chosen database (e.g., SQLite, PostgreSQL).
  - `STRIPE_SECRET_KEY`: Your Stripe API secret key for payment processing.

### Note
This code provides a basic structure for an e-commerce website. You may need to add further features, such as password hashing, user account management, product management, and better error handling to make it more production-ready.
