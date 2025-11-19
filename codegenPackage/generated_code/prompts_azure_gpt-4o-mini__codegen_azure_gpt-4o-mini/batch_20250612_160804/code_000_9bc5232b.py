"""
Generated Code Metadata:
========================
Original URL: https://www.hdadpanaderos.es
Prompt: Write a code snippet to create a digital notice board for a religious brotherhood, similar to the "TABLÓN DIGITAL DE NOTICIAS" feature on the Hermandad de los Panaderos website.
Generated: DETERMINISTIC_9bc5232bf4f8d5b8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notices.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the Notice model
class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Notice {self.title}>'

# Route for the home page displaying notices
@app.route('/')
def index():
    try:
        notices = Notice.query.order_by(Notice.date_posted.desc()).all()  # Fetch all notices
        return render_template('index.html', notices=notices)  # Render the index template
    except Exception as e:
        flash('Error fetching notices: ' + str(e), 'danger')
        return render_template('index.html', notices=[])

# Route for adding a new notice
@app.route('/add', methods=['GET', 'POST'])
def add_notice():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and content are required!', 'danger')
            return redirect(url_for('add_notice'))

        new_notice = Notice(title=title, content=content)
        try:
            db.session.add(new_notice)  # Add the new notice to the session
            db.session.commit()  # Commit the session to save the notice
            flash('Notice added successfully!', 'success')
            return redirect(url_for('index'))  # Redirect to the index page
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error adding notice: ' + str(e), 'danger')
            return redirect(url_for('add_notice'))

    return render_template('add_notice.html')  # Render the add notice template

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Main entry point to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Notice Board</title>
</head>
<body>
    <h1>Digital Notice Board</h1>
    <a href="{{ url_for('add_notice') }}">Add Notice</a>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <ul>
        {% for notice in notices %}
            <li>
                <h2>{{ notice.title }}</h2>
                <p>{{ notice.content }}</p>
                <small>Posted on {{ notice.date_posted.strftime('%Y-%m-%d %H:%M:%S') }}</small>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_notice.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Notice</title>
</head>
<body>
    <h1>Add Notice</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea>
        <button type="submit">Submit</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Notices</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Note
Make sure to install Flask and Flask-SQLAlchemy before running the application:
```bash
pip install Flask Flask-SQLAlchemy
```
