"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Implement a content management system (CMS) for a business website, allowing clients to easily update content, images, and other elements, using a platform like WordPress or a custom solution.
Generated: DETERMINISTIC_3d9ff366340b3bdf
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python-based implementation of a custom CMS using the Flask framework. This is a simplified version of a CMS that allows users to manage content and images. It includes basic CRUD operations and follows best practices.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'  # Database configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Folder for image uploads
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # Limit file size to 2MB

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define database model for content
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Content {self.title}>'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Route: Home page displaying all content
@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

# Route: Add new content
@app.route('/add', methods=['GET', 'POST'])
def add_content():
    if request.method == 'POST':
        try:
            title = request.form['title']
            body = request.form['body']
            image = request.files['image']

            # Validate input
            if not title or not body:
                flash('Title and body are required!', 'error')
                return redirect(url_for('add_content'))

            # Handle image upload
            image_filename = None
            if image and image.filename != '':
                image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(image_filename)

            # Save content to database
            new_content = Content(title=title, body=body, image=image_filename)
            db.session.add(new_content)
            db.session.commit()
            flash('Content added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error adding content: {str(e)}', 'error')
            return redirect(url_for('add_content'))

    return render_template('add_content.html')

# Route: Edit existing content
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_content(id):
    content = Content.query.get_or_404(id)
    if request.method == 'POST':
        try:
            content.title = request.form['title']
            content.body = request.form['body']
            image = request.files['image']

            # Handle image upload
            if image and image.filename != '':
                image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(image_filename)
                content.image = image_filename

            db.session.commit()
            flash('Content updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error updating content: {str(e)}', 'error')
            return redirect(url_for('edit_content', id=id))

    return render_template('edit_content.html', content=content)

# Route: Delete content
@app.route('/delete/<int:id>', methods=['POST'])
def delete_content(id):
    try:
        content = Content.query.get_or_404(id)
        if content.image and os.path.exists(content.image):
            os.remove(content.image)  # Delete associated image file
        db.session.delete(content)
        db.session.commit()
        flash('Content deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting content: {str(e)}', 'error')
    return redirect(url_for('index'))

# Route: API endpoint to fetch all content as JSON
@app.route('/api/contents', methods=['GET'])
def api_contents():
    contents = Content.query.all()
    return jsonify([{
        'id': content.id,
        'title': content.title,
        'body': content.body,
        'image': content.image
    } for content in contents])

# Error handling: 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the Flask app
    app.run(debug=True)
```

### Notes:
1. **Templates**: You will need HTML templates (`index.html`, `add_content.html`, `edit_content.html`, `404.html`) for rendering pages. These templates should include forms for adding/editing content and displaying content.
2. **Static Files**: Ensure the `static/uploads` directory exists for image uploads.
3. **Security**: Replace `your_secret_key` with a secure key and consider additional security measures for production (e.g., input validation, HTTPS, etc.).
4. **Database**: This example uses SQLite for simplicity. For production, consider using a more robust database like PostgreSQL or MySQL.
