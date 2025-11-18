"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nucleicinsights.com
Prompt: Using Python Flask, create a backend for a portfolio website that includes sections for professional skills, work experience, and a blog, inspired by Umama Shahid's design.
Generated: DETERMINISTIC_5341fca9bd3f4bdc
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the models for the database
class Skill(db.Model):
    """Model for storing professional skills."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    proficiency = db.Column(db.String(50), nullable=False)

class Experience(db.Model):
    """Model for storing work experience."""
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

class BlogPost(db.Model):
    """Model for storing blog posts."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.String(50), nullable=False)

# Route to serve the main portfolio page
@app.route('/')
def index():
    """Render the main portfolio page."""
    return render_template('index.html')

# API route to get all skills
@app.route('/api/skills', methods=['GET'])
def get_skills():
    """Fetch all professional skills."""
    try:
        skills = Skill.query.all()
        return jsonify([{'id': skill.id, 'name': skill.name, 'proficiency': skill.proficiency} for skill in skills])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to get all work experiences
@app.route('/api/experience', methods=['GET'])
def get_experience():
    """Fetch all work experiences."""
    try:
        experiences = Experience.query.all()
        return jsonify([{'id': exp.id, 'job_title': exp.job_title, 'company': exp.company,
                         'start_date': exp.start_date, 'end_date': exp.end_date,
                         'description': exp.description} for exp in experiences])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to get all blog posts
@app.route('/api/blog', methods=['GET'])
def get_blog_posts():
    """Fetch all blog posts."""
    try:
        posts = BlogPost.query.all()
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content,
                         'date_posted': post.date_posted} for post in posts])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not Found'}), 404

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 Internal Server Errors."""
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Create the database if it doesn't exist
    if not os.path.exists('portfolio.db'):
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- Create a directory named `templates` and add an `index.html` file to serve as the main page for the portfolio.
- Set up Flask-Migrate to handle database migrations as you modify the models.
- Make sure to install the required packages using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy Flask-Migrate
  ```
