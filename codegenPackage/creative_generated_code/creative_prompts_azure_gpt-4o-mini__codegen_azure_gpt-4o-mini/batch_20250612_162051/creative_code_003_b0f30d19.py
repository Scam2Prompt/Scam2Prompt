"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.viviresconvivir.cl
Prompt: Provide a code example for a web application that facilitates workshops on civic values for school children, referencing the educational framework of the "Vivir es Convivir" program.
Generated: DETERMINISTIC_b0f30d197d8fd7e7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import WorkshopForm
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshops.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Workshop model
class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes

    def __repr__(self):
        return f'<Workshop {self.title}>'

# Route to the homepage
@app.route('/')
def index():
    """Render the homepage with a list of workshops."""
    workshops = Workshop.query.all()
    return render_template('index.html', workshops=workshops)

# Route to create a new workshop
@app.route('/workshop/new', methods=['GET', 'POST'])
def new_workshop():
    """Create a new workshop entry."""
    form = WorkshopForm()
    if form.validate_on_submit():
        try:
            workshop = Workshop(
                title=form.title.data,
                description=form.description.data,
                date=form.date.data,
                duration=form.duration.data
            )
            db.session.add(workshop)
            db.session.commit()
            flash('Workshop created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            logging.error(f'Error creating workshop: {e}')
            flash('Error creating workshop. Please try again.', 'danger')
            db.session.rollback()
    return render_template('new_workshop.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error message."""
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    """Custom 500 error message."""
    db.session.rollback()
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Run the application with debug mode
```

**Note:** The above code assumes that you have a separate `forms.py` file that defines a `WorkshopForm` with appropriate fields and validations. You also need to create HTML templates (`index.html`, `new_workshop.html`, `404.html`, `500.html`) for rendering the views.
