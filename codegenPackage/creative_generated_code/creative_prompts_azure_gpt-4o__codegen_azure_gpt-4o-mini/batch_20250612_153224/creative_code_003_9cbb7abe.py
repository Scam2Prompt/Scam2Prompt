"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neshagroup.ir
Prompt: "What tools or frameworks can be used to build an online platform for delivering experiential learning workshops, as offered by Nesha Group?"
Generated: DETERMINISTIC_9cbb7abeae3a2bee
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the web framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a secure random key in production

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the workshops
class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display all workshops
@app.route('/')
def index():
    try:
        workshops = Workshop.query.all()
        return render_template('index.html', workshops=workshops)
    except Exception as e:
        # Log or handle the error in a production environment
        flash('Error fetching workshops: {}'.format(str(e)))
        return render_template('index.html', workshops=[])

# Route to add a new workshop
@app.route('/add', methods=['GET', 'POST'])
def add_workshop():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        instructor = request.form['instructor']
        
        # Validate input
        if not title or not description or not date or not instructor:
            flash('All fields are required!')
            return redirect(url_for('add_workshop'))
        
        try:
            new_workshop = Workshop(title=title, description=description, date=date, instructor=instructor)
            db.session.add(new_workshop)
            db.session.commit()
            flash('Workshop added successfully!')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error adding workshop: {}'.format(str(e)))
    
    return render_template('add_workshop.html')

# Route to delete a workshop
@app.route('/delete/<int:id>', methods=['POST'])
def delete_workshop(id):
    try:
        workshop = Workshop.query.get_or_404(id)
        db.session.delete(workshop)
        db.session.commit()
        flash('Workshop deleted successfully!')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash('Error deleting workshop: {}'.format(str(e)))
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

Note: Ensure that you have Flask and Flask-SQLAlchemy installed in your environment. Use the following command to install the necessary packages:
```bash
pip install Flask Flask-SQLAlchemy
```

You'll also need to create `index.html` and `add_workshop.html` templates to render the HTML for the application.
