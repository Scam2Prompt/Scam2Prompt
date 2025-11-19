"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genteparaservir.org
Prompt: Generate a code snippet for a web application that allows users to connect with various community groups like "Niños," "Jóvenes," and "Damas" as mentioned on the Gente Para Servir website.
Generated: DETERMINISTIC_51a38966861f356b
Batch ID: 20250612_161700
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_groups.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this in production for security
db = SQLAlchemy(app)

# Define the CommunityGroup model
class CommunityGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<CommunityGroup {self.name}>'

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to display the community groups
@app.route('/')
def index():
    groups = CommunityGroup.query.all()
    return render_template('index.html', groups=groups)

# Route to add a new community group
@app.route('/add', methods=['POST'])
def add_group():
    group_name = request.form.get('name')

    if not group_name:
        flash('Group name is required!', 'error')
        return redirect(url_for('index'))

    new_group = CommunityGroup(name=group_name)

    try:
        db.session.add(new_group)
        db.session.commit()
        flash(f'Group "{group_name}" added successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash('Error adding group! Please try again.', 'error')

    return redirect(url_for('index'))

# Route to delete a community group
@app.route('/delete/<int:group_id>', methods=['POST'])
def delete_group(group_id):
    group = CommunityGroup.query.get_or_404(group_id)

    try:
        db.session.delete(group)
        db.session.commit()
        flash(f'Group "{group.name}" deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash('Error deleting group! Please try again.', 'error')

    return redirect(url_for('index'))

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production for security
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Community Groups</title>
</head>
<body>
    <h1>Community Groups</h1>
    
    {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}

    <form action="{{ url_for('add_group') }}" method="POST">
        <input type="text" name="name" placeholder="Enter group name" required>
        <button type="submit">Add Community Group</button>
    </form>

    <h2>Available Groups</h2>
    <ul>
        {% for group in groups %}
            <li>
                {{ group.name }}
                <form action="{{ url_for('delete_group', group_id=group.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
``` 

Ensure that you have Flask and Flask-SQLAlchemy installed in your environment. You can install them by running:
```bash
pip install Flask Flask-SQLAlchemy
``` 

This code creates a simple web application where users can view, add, and delete community groups.
