"""
Generated Code Metadata:
========================
Original URL: https://thebalichili.com
Prompt: Design a web application for a digital marketing agency, including features for social media management, client tracking, and campaign analytics.
Generated: DETERMINISTIC_7f676ceaccd8a2dd
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a web application for a digital marketing agency using Python's Flask framework. It includes features for social media management, client tracking, and campaign analytics. Note that this is a simplified version to fit within the constraints of this format.

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agency.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Models
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    analytics = db.Column(db.JSON, nullable=True)  # Store campaign analytics as JSON

class SocialMediaPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default="Scheduled")  # Status: Scheduled, Posted, Failed

# Routes
@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/clients', methods=['GET', 'POST'])
def manage_clients():
    """Manage clients: GET to list, POST to create."""
    if request.method == 'GET':
        clients = Client.query.all()
        return jsonify([{'id': c.id, 'name': c.name, 'email': c.email, 'phone': c.phone} for c in clients])
    elif request.method == 'POST':
        data = request.json
        try:
            new_client = Client(name=data['name'], email=data['email'], phone=data.get('phone'))
            db.session.add(new_client)
            db.session.commit()
            return jsonify({'message': 'Client added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

@app.route('/campaigns', methods=['GET', 'POST'])
def manage_campaigns():
    """Manage campaigns: GET to list, POST to create."""
    if request.method == 'GET':
        campaigns = Campaign.query.all()
        return jsonify([{
            'id': c.id, 'name': c.name, 'client_id': c.client_id,
            'start_date': c.start_date, 'end_date': c.end_date,
            'budget': c.budget, 'analytics': c.analytics
        } for c in campaigns])
    elif request.method == 'POST':
        data = request.json
        try:
            new_campaign = Campaign(
                name=data['name'],
                client_id=data['client_id'],
                start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
                end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
                budget=data['budget'],
                analytics=data.get('analytics', {})
            )
            db.session.add(new_campaign)
            db.session.commit()
            return jsonify({'message': 'Campaign added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

@app.route('/social-media-posts', methods=['GET', 'POST'])
def manage_social_media_posts():
    """Manage social media posts: GET to list, POST to create."""
    if request.method == 'GET':
        posts = SocialMediaPost.query.all()
        return jsonify([{
            'id': p.id, 'platform': p.platform, 'content': p.content,
            'scheduled_date': p.scheduled_date, 'status': p.status
        } for p in posts])
    elif request.method == 'POST':
        data = request.json
        try:
            new_post = SocialMediaPost(
                platform=data['platform'],
                content=data['content'],
                scheduled_date=datetime.strptime(data['scheduled_date'], '%Y-%m-%d %H:%M:%S'),
                status=data.get('status', 'Scheduled')
            )
            db.session.add(new_post)
            db.session.commit()
            return jsonify({'message': 'Social media post scheduled successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Run the app
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Notes:
- This code assumes you have Flask and SQLAlchemy installed (`pip install flask flask-sqlalchemy`).
- The database is SQLite for simplicity; you can replace it with a production-grade database like PostgreSQL or MySQL.
- Templates (e.g., `index.html`) are not included in this snippet but can be added in a `templates` folder.
- For production, use a WSGI server like Gunicorn and configure environment variables for sensitive data.
