"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hdadpanaderos.es
Prompt: Write a code snippet to create a digital notice board for a religious brotherhood, similar to the "TABLÓN DIGITAL DE NOTICIAS" feature on the Hermandad de los Panaderos website.
Generated: DETERMINISTIC_9bc5232bf4f8d5b8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong key

# Initialize the database
db = SQLAlchemy(app)

# Model for the notice board
class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Notice {self.title}>"

# Create the database and the database table
with app.app_context():
    db.create_all()

# Route for the home page to display notices
@app.route('/')
def index():
    try:
        notices = Notice.query.order_by(Notice.created_at.desc()).all()  # Get all notices
        return render_template('index.html', notices=notices)  # Render the template with notices
    except Exception as e:
        flash(f"An error occurred while retrieving notices: {str(e)}", "danger")
        return render_template('index.html', notices=[])

# Route to create a new notice
@app.route('/add', methods=['GET', 'POST'])
def add_notice():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        try:
            # Create a new notice and add it to the database
            new_notice = Notice(title=title, content=content)
            db.session.add(new_notice)
            db.session.commit()
            flash("Notice added successfully!", "success")
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred while adding the notice: {str(e)}", "danger")
    return render_template('add_notice.html')

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

**HTML Templates Required:**

1. `index.html` - to display the list of notices.
2. `add_notice.html` - to display the form for adding a new notice.
3. `404.html` - for handling 404 errors.

**Notes:**
- Make sure to install Flask and Flask-SQLAlchemy with `pip install Flask Flask-SQLAlchemy`.
- Update the `SECRET_KEY` to a strong, unique value for session management.
- This code assumes the presence of the required HTML templates for rendering.
