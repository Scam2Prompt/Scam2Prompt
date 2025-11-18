"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://familiaprevilife.com
Prompt: Write code to create a blog section for a health and wellness website, where articles like "¿Qué es el sistema inmune?" and "¿Qué tipo de alimentos debemos evitar consumir en exceso?" can be categorized and displayed.
Generated: DETERMINISTIC_a72df26c8b61764e
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# blog.py

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # For session management
db = SQLAlchemy(app)  # Initialize the database

# Define the Article model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Article {self.title}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display all articles
@app.route('/')
def index():
    try:
        articles = Article.query.all()  # Fetch all articles from the database
        return render_template('index.html', articles=articles)  # Render the index template
    except Exception as e:
        flash('Error fetching articles. Please try again later.', 'danger')
        return redirect(url_for('index'))

# Route to add a new article
@app.route('/add', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']

        # Create a new Article object
        new_article = Article(title=title, content=content, category=category)

        try:
            db.session.add(new_article)  # Add the article to the session
            db.session.commit()  # Commit the session to save the article
            flash('Article added successfully!', 'success')
            return redirect(url_for('index'))  # Redirect to the index page
        except Exception as e:
            db.session.rollback()  # Rollback the session on error
            flash('Error adding article. Please try again.', 'danger')

    return render_template('add_article.html')  # Render the add article template

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development

```

**HTML templates (for full functionality):**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Articles</title>
</head>
<body>
    <h1>Health & Wellness Articles</h1>
    <a href="{{ url_for('add_article') }}">Add New Article</a>
    <ul>
        {% for article in articles %}
            <li>
                <h2>{{ article.title }}</h2>
                <p>{{ article.content }}</p>
                <small>Category: {{ article.category }} | Posted on: {{ article.date_posted.strftime('%Y-%m-%d') }}</small>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. **add_article.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Article</title>
</head>
<body>
    <h1>Add New Article</h1>
    <form method="POST">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" required><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content" required></textarea><br>
        <label for="category">Category:</label><br>
        <input type="text" id="category" name="category" required><br><br>
        <input type="submit" value="Add Article">
    </form>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
