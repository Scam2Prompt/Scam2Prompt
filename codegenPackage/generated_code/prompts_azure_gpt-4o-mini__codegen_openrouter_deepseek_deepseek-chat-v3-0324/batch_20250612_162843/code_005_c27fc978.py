"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Describe how to implement a customer feedback system for a travel agency that specializes in luxury safaris, ensuring exceptional service is highlighted.
Generated: DETERMINISTIC_c27fc978d5a5b59f
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python implementation for a customer feedback system using Flask for a luxury safari travel agency:

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from typing import List, Dict, Optional

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
db = SQLAlchemy(app)

# Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    safari_package = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=False)
    highlights = db.Column(db.Text, nullable=False)  # Store exceptional service highlights
    photo_path = db.Column(db.String(255))
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_featured = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Feedback {self.customer_name}>'

# Create database tables
with app.app_context():
    db.create_all()

def allowed_file(filename: str) -> bool:
    """Check if file has an allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """Endpoint to submit new feedback"""
    try:
        # Get form data
        customer_name = request.form.get('customer_name')
        email = request.form.get('email')
        safari_package = request.form.get('safari_package')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        highlights = request.form.get('highlights')  # Exceptional service aspects
        
        # Validate required fields
        if not all([customer_name, email, safari_package, rating, comments, highlights]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Handle file upload if exists
        photo_path = None
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                photo_path = filepath
        
        # Create feedback entry
        feedback = Feedback(
            customer_name=customer_name,
            email=email,
            safari_package=safari_package,
            rating=int(rating),
            comments=comments,
            highlights=highlights,
            photo_path=photo_path
        )
        
        db.session.add(feedback)
        db.session.commit()
        
        return jsonify({'message': 'Feedback submitted successfully!', 'id': feedback.id}), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Endpoint to retrieve feedback with filtering options"""
    try:
        package_filter = request.args.get('package')
        min_rating = request.args.get('min_rating')
        featured_only = request.args.get('featured') == 'true'
        
        query = Feedback.query
        
        if package_filter:
            query = query.filter(Feedback.safari_package == package_filter)
        if min_rating:
            query = query.filter(Feedback.rating >= int(min_rating))
        if featured_only:
            query = query.filter(Feedback.is_featured == True)
            
        feedback_list = query.order_by(Feedback.submission_date.desc()).all()
        
        feedback_data = []
        for fb in feedback_list:
            feedback_data.append({
                'id': fb.id,
                'customer_name': fb.customer_name,
                'safari_package': fb.safari_package,
                'rating': fb.rating,
                'comments': fb.comments,
                'highlights': fb.highlights,
                'photo_path': fb.photo_path,
                'submission_date': fb.submission_date.isoformat(),
                'is_featured': fb.is_featured
            })
            
        return jsonify(feedback_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feature-feedback/<int:feedback_id>', methods=['PUT'])
def feature_feedback(feedback_id: int):
    """Endpoint to mark feedback as featured"""
    try:
        feedback = Feedback.query.get_or_404(feedback_id)
        feedback.is_featured = True
        db.session.commit()
        return jsonify({'message': 'Feedback featured successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/feedback-stats', methods=['GET'])
def get_feedback_stats():
    """Endpoint to get statistics about feedback"""
    try:
        # Basic statistics
        total_feedback = Feedback.query.count()
        average_rating = db.session.query(db.func.avg(Feedback.rating)).scalar() or 0
        featured_count = Feedback.query.filter_by(is_featured=True).count()
        
        # Package-wise statistics
        package_stats = db.session.query(
            Feedback.safari_package,
            db.func.count(Feedback.id),
            db.func.avg(Feedback.rating)
        ).group_by(Feedback.safari_package).all()
        
        response = {
            'total_feedback': total_feedback,
            'average_rating': round(float(average_rating), 1),
            'featured_count': featured_count,
            'package_stats': [{
                'package': package,
                'count': count,
                'avg_rating': round(float(avg_rating), 1)
            } for package, count, avg_rating in package_stats]
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# HTML template routes
@app.route('/')
def index():
    """Render feedback submission form"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Render feedback dashboard"""
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Note: This is the backend implementation. You would also need to create HTML templates (`index.html` and `dashboard.html`) in a `templates` folder and set up static files for the frontend. The implementation includes:

1. Feedback submission with photo uploads
2. Exceptional service highlights tracking
3. Feedback retrieval with filtering
4. Featured feedback management
5. Statistics reporting
6. Proper error handling and validation
7. Database models for persistence

To complete the system, you would need to implement the frontend templates and optionally add user authentication if needed.
