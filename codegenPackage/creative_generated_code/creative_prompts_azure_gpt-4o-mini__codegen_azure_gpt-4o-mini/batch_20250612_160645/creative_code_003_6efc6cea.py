"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Provide an example of a backend setup for a corporate website that includes custom design and management features, as outlined on ra-don.com.
Generated: DETERMINISTIC_6efc6cea34b72f7a
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model for the website content
class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Page {self.title}>'

# Route to render the homepage
@app.route('/')
def home():
    """Renders the homepage with a list of pages."""
    pages = Page.query.all()  # Fetch all pages from the database
    return render_template('home.html', pages=pages)

# Route to manage a specific page
@app.route('/page/<int:page_id>')
def page(page_id):
    """Renders a specific page."""
    page = Page.query.get_or_404(page_id)  # Fetch page by ID or return 404
    return render_template('page.html', page=page)

# Route to create a new page (for management)
@app.route('/admin/page/new', methods=['GET', 'POST'])
def new_page():
    """Creates a new page."""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_page = Page(title=title, content=content)
        db.session.add(new_page)
        db.session.commit()
        return jsonify({'message': 'Page created successfully!'}), 201
    return render_template('new_page.html')

# Route to update an existing page (for management)
@app.route('/admin/page/<int:page_id>/edit', methods=['GET', 'POST'])
def edit_page(page_id):
    """Updates an existing page."""
    page = Page.query.get_or_404(page_id)

    if request.method == 'POST':
        page.title = request.form['title']
        page.content = request.form['content']
        db.session.commit()
        return jsonify({'message': 'Page updated successfully!'}), 200
    return render_template('edit_page.html', page=page)

# Route to delete a page (for management)
@app.route('/admin/page/<int:page_id>/delete', methods=['POST'])
def delete_page(page_id):
    """Deletes a page."""
    page = Page.query.get_or_404(page_id)
    db.session.delete(page)
    db.session.commit()
    return jsonify({'message': 'Page deleted successfully!'}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors."""
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    """Handles 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point
if __name__ == '__main__':
    # Run the application in debug mode if not in production
    app.run(debug=os.getenv('FLASK_ENV') != 'production')
``` 

Make sure to create the corresponding HTML templates (`home.html`, `page.html`, `new_page.html`, `edit_page.html`) in a `templates` directory at the root of your project to ensure the app runs properly.
