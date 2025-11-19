"""
Generated Code Metadata:
========================
Original URL: https://teamadver.com
Prompt: Write a code snippet for a custom website that integrates SEO-friendly features and e-commerce capabilities, inspired by Team Adver's web development services.
Generated: DETERMINISTIC_cd94a0f93944d46d
Batch ID: 20250612_160526
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
from flask_seo import SEO
import os
from werkzeug.utils import secure_filename
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Initialize SEO
seo = SEO(app)
seo.update_site_name("Team Adver E-Commerce")
seo.update_title("Premium Products - Team Adver")
seo.update_description("Shop high-quality products with SEO-optimized e-commerce solutions by Team Adver")
seo.update_keywords(["ecommerce", "shop", "products", "Team Adver", "SEO"])

# Initialize database
db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create database tables
with app.app_context():
    db.create_all()

# Helper function for file upload
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# Routes
@app.route('/')
def home():
    products = Product.query.order_by(Product.created_at.desc()).limit(4).all()
    return render_template('index.html', products=products)

@app.route('/products')
def products():
    category = request.args.get('category', 'all')
    if category == 'all':
        products = Product.query.order_by(Product.created_at.desc()).all()
    else:
        products = Product.query.filter_by(category=category).order_by(Product.created_at.desc()).all()
    return render_template('products.html', products=products, category=category)

@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', product=product)

@app.route('/add-to-cart/<int:id>')
def add_to_cart(id):
    # Cart functionality would be implemented here
    flash('Product added to cart!', 'success')
    return redirect(url_for('product_detail', id=id))

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/admin/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        category = request.form['category']
        
        # Handle file upload
        if 'image' not in request.files:
            flash('No image uploaded', 'danger')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            product = Product(
                name=name,
                description=description,
                price=price,
                image=filename,
                category=category
            )
            
            db.session.add(product)
            db.session.commit()
            flash('Product added successfully!', 'success')
            return redirect(url_for('home'))
    
    return render_template('admin/add_product.html')

# Sitemap route for SEO
@app.route('/sitemap.xml')
def sitemap():
    products = Product.query.all()
    pages = [
        {'url': url_for('home', _external=True), 'lastmod': datetime.utcnow().strftime('%Y-%m-%d')},
        {'url': url_for('products', _external=True), 'lastmod': datetime.utcnow().strftime('%Y-%m-%d')},
        {'url': url_for('checkout', _external=True), 'lastmod': datetime.utcnow().strftime('%Y-%m-%d')}
    ]
    
    for product in products:
        pages.append({
            'url': url_for('product_detail', id=product.id, _external=True),
            'lastmod': product.updated_at.strftime('%Y-%m-%d')
        })
    
    sitemap_xml = render_template('sitemap.xml', pages=pages)
    response = app.make_response(sitemap_xml)
    response.headers['Content-Type'] = 'application/xml'
    return response

# Robots.txt for SEO
@app.route('/robots.txt')
def robots():
    return """User-agent: *
Allow: /
Sitemap: {0}
""".format(url_for('sitemap', _external=True))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```
