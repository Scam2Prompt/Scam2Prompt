"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fli.so
Prompt: How can I implement metadata customization for URLs in a link management system, similar to Fli.so's meta controls?
Generated: DETERMINISTIC_d55d7e972cf85770
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Link(db.Model):
    """Model representing a shortened link with metadata."""
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    custom_slug = db.Column(db.String(100), unique=True)
    meta_title = db.Column(db.String(255))
    meta_description = db.Column(db.String(500))

    def __repr__(self):
        return f'<Link {self.custom_slug}>'

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/link', methods=['POST'])
def create_link():
    """API endpoint to create a new shortened link with metadata."""
    data = request.json
    try:
        new_link = Link(
            original_url=data['original_url'],
            custom_slug=data['custom_slug'],
            meta_title=data.get('meta_title', ''),
            meta_description=data.get('meta_description', '')
        )
        db.session.add(new_link)
        db.session.commit()
        return jsonify({'message': 'Link created successfully!', 'link': new_link.custom_slug}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/link/<slug>', methods=['GET'])
def get_link(slug):
    """API endpoint to retrieve a shortened link and its metadata."""
    link = Link.query.filter_by(custom_slug=slug).first()
    if not link:
        return jsonify({'error': 'Link not found'}), 404
    return jsonify({
        'original_url': link.original_url,
        'custom_slug': link.custom_slug,
        'meta_title': link.meta_title,
        'meta_description': link.meta_description
    })

@app.route('/link/<slug>', methods=['DELETE'])
def delete_link(slug):
    """API endpoint to delete a shortened link."""
    link = Link.query.filter_by(custom_slug=slug).first()
    if not link:
        return jsonify({'error': 'Link not found'}), 404
    try:
        db.session.delete(link)
        db.session.commit()
        return jsonify({'message': 'Link deleted successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False)
```
