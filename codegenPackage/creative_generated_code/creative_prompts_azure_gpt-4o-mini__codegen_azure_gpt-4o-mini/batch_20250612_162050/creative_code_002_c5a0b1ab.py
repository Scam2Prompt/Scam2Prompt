"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heartofjesuscollege.com
Prompt: Write a Python script that simulates an "Aula Invertida" learning environment, allowing students to access simplified educational materials online.
Generated: DETERMINISTIC_c5a0b1abfc54cf38
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secret key for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///materials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define the Material model
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Material {self.title}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the home page with a list of educational materials."""
    materials = Material.query.all()
    return render_template('index.html', materials=materials)

@app.route('/material/<int:material_id>')
def material_detail(material_id):
    """Display detailed information about a specific educational material."""
    material = Material.query.get_or_404(material_id)
    return render_template('material_detail.html', material=material)

@app.route('/add', methods=['GET', 'POST'])
def add_material():
    """Allow users to add new educational materials."""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and content are required!', 'danger')
            return redirect(url_for('add_material'))

        new_material = Material(title=title, content=content)
        db.session.add(new_material)
        db.session.commit()
        flash('Material added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_material.html')

@app.route('/delete/<int:material_id>', methods=['POST'])
def delete_material(material_id):
    """Delete a specific educational material."""
    material = Material.query.get_or_404(material_id)
    db.session.delete(material)
    db.session.commit()
    flash('Material deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
```

### Additional Files Required
You will also need to create the following HTML templates for the application to work properly:

1. `templates/index.html`
2. `templates/material_detail.html`
3. `templates/add_material.html`

These HTML files should include appropriate forms and displays for your application, but their content is not provided here as per your request. Make sure that you have Flask and Flask-SQLAlchemy installed in your environment to run this code.

```bash
pip install Flask Flask-SQLAlchemy
```
