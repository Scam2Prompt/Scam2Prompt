"""
Generated Code Metadata:
========================
Original URL: https://foolz.sellpass.io
Prompt: Generate code to create a customizable storefront using Sellpass for selling digital products like software, subscriptions, or accounts. Include features such as customer authentication and 1-click checkout.
Generated: DETERMINISTIC_17360f57c92c86eb
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sellpass import Sellpass
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///store.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Sellpass client
sellpass_client = Sellpass(
    api_key=os.environ.get('SELLPASS_API_KEY'),
    store_id=os.environ.get('SELLPASS_STORE_ID')
)

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    purchases = db.relationship('Purchase', backref='user', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sellpass_id = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    is_subscription = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(255))

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    transaction_id = db.Column(db.String(120), nullable=False)
    purchase_date = db.Column(db.DateTime, server_default=db.func.now())

# Helper Functions
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def sync_products():
    try:
        products = sellpass_client.get_products()
        for product_data in products:
            product = Product.query.filter_by(sellpass_id=product_data['id']).first()
            if not product:
                product = Product(
                    sellpass_id=product_data['id'],
                    name=product_data['name'],
                    description=product_data.get('description', ''),
                    price=product_data['price'],
                    is_subscription=product_data.get('is_subscription', False),
                    image_url=product_data.get('image_url', '')
                )
                db.session.add(product)
        db.session.commit()
        return True
    except Exception as e:
        app.logger.error(f"Error syncing products: {str(e)}")
        return False

# Routes
@app.route('/')
def home():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        flash('Logged in successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    purchases = Purchase.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', user=user, purchases=purchases)

@app.route('/checkout/<int:product_id>', methods=['GET', 'POST'])
@login_required
def checkout(product_id):
    product = Product.query.get_or_404(product_id)
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        try:
            # Create Sellpass checkout
            checkout_data = {
                'product_id': product.sellpass_id,
                'customer_email': user.email,
                'customer_name': user.username,
                'redirect_url': url_for('checkout_success', _external=True),
                'webhook_url': url_for('webhook', _external=True)
            }
            
            checkout_response = sellpass_client.create_checkout(checkout_data)
            return redirect(checkout_response['checkout_url'])
        except Exception as e:
            app.logger.error(f"Checkout error: {str(e)}")
            flash('An error occurred during checkout. Please try again.', 'danger')
            return redirect(url_for('product_detail', product_id=product.id))
    
    return render_template('checkout.html', product=product)

@app.route('/checkout/success')
@login_required
def checkout_success():
    flash('Purchase completed successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        event_type = data['event']
        
        if event_type == 'order.completed':
            order = data['data']
            user = User.query.filter_by(email=order['customer']['email']).first()
            product = Product.query.filter_by(sellpass_id=order['product_id']).first()
            
            if user and product:
                purchase = Purchase(
                    user_id=user.id,
                    product_id=product.id,
                    transaction_id=order['id']
                )
                db.session.add(purchase)
                db.session.commit()
                
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        app.logger.error(f"Webhook error: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Admin Routes
@app.route('/admin/sync-products')
@login_required
def admin_sync_products():
    if sync_products():
        flash('Products synced successfully', 'success')
    else:
        flash('Failed to sync products', 'danger')
    return redirect(url_for('home'))

# Initialize Database
@app.before_first_request
def initialize_database():
    db.create_all()
    sync_products()

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', False))
```
