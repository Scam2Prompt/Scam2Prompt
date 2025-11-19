"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextjs-ai-chatbot-drh.pages.dev
Prompt: Generate a code snippet for a web application that allows users to join forums and local chapters for the TRUMP MAGA movement.
Generated: DETERMINISTIC_ceec75cfc43ab414
Batch ID: 20250612_155534
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
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forums.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your actual secret key

# Initialize the database
db = SQLAlchemy(app)

# Define the Forum model
class Forum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Forum {self.name}>'

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template("error.html", error=e), e.code

# Route to display all forums
@app.route('/')
def index():
    forums = Forum.query.all()  # Fetch all forums from the database
    return render_template('index.html', forums=forums)

# Route to create a new forum
@app.route('/create', methods=['GET', 'POST'])
def create_forum():
    if request.method == 'POST':
        forum_name = request.form.get('name')
        forum_description = request.form.get('description')

        if not forum_name:
            flash('Forum name is required!', 'error')
            return redirect(url_for('create_forum'))

        # Create a new Forum object
        new_forum = Forum(name=forum_name, description=forum_description)
        
        # Add and commit the new forum to the database
        try:
            db.session.add(new_forum)
            db.session.commit()
            flash('Forum created successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating forum: {str(e)}', 'error')
        
        return redirect(url_for('index'))

    return render_template('create_forum.html')

# Run the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```

**HTML Files (Assumed to be in a 'templates' folder)**

`index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forums</title>
</head>
<body>
    <h1>Forums</h1>
    <a href="{{ url_for('create_forum') }}">Create a New Forum</a>
    <ul>
        {% for forum in forums %}
            <li>{{ forum.name }} - {{ forum.description }}</li>
        {% endfor %}
    </ul>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

`create_forum.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Forum</title>
</head>
<body>
    <h1>Create a New Forum</h1>
    <form method="POST">
        <label for="name">Forum Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea>
        <button type="submit">Create</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Forums</a>
</body>
</html>
```

`error.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error {{ error.code }}</h1>
    <p>{{ error.description }}</p>
    <a href="{{ url_for('index') }}">Go Back</a>
</body>
</html>
```
