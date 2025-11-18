"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cocula.gob.mx
Prompt: Write code for a web application that allows residents of Cocula to view and filter municipal announcements, such as those listed on the Cocula government website, by category and date.
Generated: DETERMINISTIC_afc72e133be4b434
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: cocula_announcements_app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cocula_announcements.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Announcement model
class Announcement(db.Model):
    __tablename__ = 'announcements'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert Announcement object to dictionary for JSON response."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'category': self.category,
            'date_posted': self.date_posted.strftime('%Y-%m-%d %H:%M:%S')
        }

# Create database tables if not already created
with app.app_context():
    db.create_all()

# Route: Get all announcements or filter by category and date
@app.route('/announcements', methods=['GET'])
def get_announcements():
    try:
        # Get query parameters
        category = request.args.get('category', None)
        start_date = request.args.get('start_date', None)
        end_date = request.args.get('end_date', None)

        # Base query
        query = Announcement.query

        # Filter by category if provided
        if category:
            query = query.filter(Announcement.category == category)

        # Filter by date range if provided
        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                query = query.filter(Announcement.date_posted >= start_date)
            except ValueError:
                return jsonify({'error': 'Invalid start_date format. Use YYYY-MM-DD.'}), 400

        if end_date:
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
                query = query.filter(Announcement.date_posted <= end_date)
            except ValueError:
                return jsonify({'error': 'Invalid end_date format. Use YYYY-MM-DD.'}), 400

        # Execute query and fetch results
        announcements = query.all()
        return jsonify([announcement.to_dict() for announcement in announcements]), 200

    except SQLAlchemyError as e:
        return jsonify({'error': 'Database query failed.', 'details': str(e)}), 500

# Route: Add a new announcement (for administrative use)
@app.route('/announcements', methods=['POST'])
def add_announcement():
    try:
        # Parse request JSON data
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        category = data.get('category')

        # Validate required fields
        if not title or not content or not category:
            return jsonify({'error': 'Missing required fields: title, content, category'}), 400

        # Create and save new announcement
        new_announcement = Announcement(title=title, content=content, category=category)
        db.session.add(new_announcement)
        db.session.commit()

        return jsonify({'message': 'Announcement added successfully.', 'announcement': new_announcement.to_dict()}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database operation failed.', 'details': str(e)}), 500

# Route: Health check for the server
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK', 'message': 'Server is healthy.'}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
