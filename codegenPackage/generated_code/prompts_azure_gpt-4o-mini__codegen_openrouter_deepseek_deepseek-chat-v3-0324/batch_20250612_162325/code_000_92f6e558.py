"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a code snippet for a web application that allows users to create their own cosmetic brand using the full-service project model described by Fabricare Cosméticos.
Generated: DETERMINISTIC_92f6e558e446265f
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
import uuid

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cosmetic_brands.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize database
db = SQLAlchemy(app)

# Create Brand model
class Brand(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    logo = db.Column(db.String(100))
    owner_name = db.Column(db.String(100), nullable=False)
    owner_email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Brand {self.name}>'

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/brands', methods=['GET', 'POST'])
def handle_brands():
    """Handle brand creation and listing."""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name')
            description = request.form.get('description')
            owner_name = request.form.get('owner_name')
            owner_email = request.form.get('owner_email')
            
            # Validate required fields
            if not all([name, description, owner_name, owner_email]):
                return jsonify({'error': 'Missing required fields'}), 400

            # Handle file upload
            logo = None
            if 'logo' in request.files:
                file = request.files['logo']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    unique_filename = f"{uuid.uuid4()}_{filename}"
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
                    logo = unique_filename

            # Create new brand
            new_brand = Brand(
                name=name,
                description=description,
                logo=logo,
                owner_name=owner_name,
                owner_email=owner_email
            )
            
            db.session.add(new_brand)
            db.session.commit()
            
            return jsonify({
                'message': 'Brand created successfully',
                'brand_id': new_brand.id
            }), 201
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    elif request.method == 'GET':
        try:
            brands = Brand.query.all()
            return jsonify([{
                'id': brand.id,
                'name': brand.name,
                'description': brand.description,
                'logo': brand.logo,
                'owner_name': brand.owner_name,
                'created_at': brand.created_at.isoformat()
            } for brand in brands]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/brands/<brand_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_brand(brand_id):
    """Handle individual brand operations."""
    brand = Brand.query.get_or_404(brand_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': brand.id,
            'name': brand.name,
            'description': brand.description,
            'logo': brand.logo,
            'owner_name': brand.owner_name,
            'owner_email': brand.owner_email,
            'created_at': brand.created_at.isoformat(),
            'updated_at': brand.updated_at.isoformat()
        }), 200
    
    elif request.method == 'PUT':
        try:
            data = request.form
            if 'name' in data:
                brand.name = data['name']
            if 'description' in data:
                brand.description = data['description']
            if 'owner_name' in data:
                brand.owner_name = data['owner_name']
            if 'owner_email' in data:
                brand.owner_email = data['owner_email']
            
            # Handle logo update
            if 'logo' in request.files:
                file = request.files['logo']
                if file and allowed_file(file.filename):
                    # Remove old logo if exists
                    if brand.logo:
                        old_logo_path = os.path.join(app.config['UPLOAD_FOLDER'], brand.logo)
                        if os.path.exists(old_logo_path):
                            os.remove(old_logo_path)
                    
                    # Save new logo
                    filename = secure_filename(file.filename)
                    unique_filename = f"{uuid.uuid4()}_{filename}"
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
                    brand.logo = unique_filename
            
            db.session.commit()
            return jsonify({'message': 'Brand updated successfully'}), 200
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    elif request.method == 'DELETE':
        try:
            # Remove logo file if exists
            if brand.logo:
                logo_path = os.path.join(app.config['UPLOAD_FOLDER'], brand.logo)
                if os.path.exists(logo_path):
                    os.remove(logo_path)
            
            db.session.delete(brand)
            db.session.commit()
            return jsonify({'message': 'Brand deleted successfully'}), 200
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(debug=True)
```
