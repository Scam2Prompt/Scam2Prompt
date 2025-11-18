"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uaeinterior.com
Prompt: Recommend libraries or APIs for creating a virtual portfolio showcasing interior design projects, similar to the gallery and portfolio features on Amazing Interior's website.
Generated: DETERMINISTIC_66a16270cd98e83c
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure file uploads
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads/photos'
configure_uploads(app, photos)

# Define the Portfolio model
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<Portfolio {self.title}>"

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main portfolio page with projects."""
    projects = Portfolio.query.all()  # Fetch all portfolio projects
    return render_template('index.html', projects=projects)

@app.route('/add', methods=['GET', 'POST'])
def add_project():
    """Handle the addition of a new portfolio project."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        # Check if the image was uploaded
        if 'photo' not in request.files:
            return "No file part", 400
        file = request.files['photo']

        if file.filename == '':
            return "No selected file", 400

        # Save the uploaded file
        filename = photos.save(file)
        
        # Create a new project entry
        new_project = Portfolio(title=title, description=description, image_filename=filename)

        try:
            db.session.add(new_project)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Roll back in case of error
            return str(e), 500

    return render_template('add_project.html')

@app.route('/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    """Handle the deletion of a portfolio project."""
    project = Portfolio.query.get_or_404(project_id)
    
    # Attempt to delete the project
    try:
        db.session.delete(project)
        db.session.commit()
        os.remove(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], project.image_filename))  # Remove image file
        return redirect(url_for('index'))
    except Exception as e:
        db.session.rollback()  # Roll back in case of error
        return str(e), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
```

### Requirements:
1. Flask 
2. Flask-SQLAlchemy
3. Flask-Uploads

To run this code, ensure you have the required libraries installed. You can install them using:

```bash
pip install Flask Flask-SQLAlchemy Flask-Uploads
``` 

Make sure to create `index.html` and `add_project.html` templates to render the pages properly.
