"""
Generated Code Metadata:
========================
Original URL: https://familiaprevilife.com
Prompt: Write code to create a blog section for a health and wellness website, where articles like "¿Qué es el sistema inmune?" and "¿Qué tipo de alimentos debemos evitar consumir en exceso?" can be categorized and displayed.
Generated: DETERMINISTIC_a72df26c8b61764e
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the Article model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Article {self.title}>'

# Route to display all articles
@app.route('/')
def index():
    try:
        articles = Article.query.all()  # Fetch all articles from the database
        return render_template('index.html', articles=articles)  # Render the index template
    except Exception as e:
        flash('Error fetching articles: ' + str(e))  # Flash error message
        return redirect(url_for('index'))

# Route to create a new article
@app.route('/new', methods=['GET', 'POST'])
def new_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        
        # Validate input
        if not title or not content or not category:
            flash('All fields are required!')
            return redirect(url_for('new_article'))

        # Create a new article instance
        new_article = Article(title=title, content=content, category=category)
        try:
            db.session.add(new_article)  # Add the article to the session
            db.session.commit()  # Commit the session to save the article
            flash('Article created successfully!')
            return redirect(url_for('index'))  # Redirect to the index page
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error creating article: ' + str(e))  # Flash error message
            return redirect(url_for('new_article'))

    return render_template('new_article.html')  # Render the new article form

# Route to display articles by category
@app.route('/category/<string:category>')
def category_articles(category):
    try:
        articles = Article.query.filter_by(category=category).all()  # Fetch articles by category
        return render_template('category.html', articles=articles, category=category)  # Render category template
    except Exception as e:
        flash('Error fetching articles by category: ' + str(e))  # Flash error message
        return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Blog de Salud y Bienestar</title>
</head>
<body>
    <h1>Artículos de Salud y Bienestar</h1>
    <a href="{{ url_for('new_article') }}">Crear nuevo artículo</a>
    <ul>
        {% for article in articles %}
            <li>
                <h2>{{ article.title }}</h2>
                <p>{{ article.content }}</p>
                <p>Categoría: {{ article.category }}</p>
                <p>Publicado el: {{ article.date_posted.strftime('%Y-%m-%d') }}</p>
                <a href="{{ url_for('category_articles', category=article.category) }}">Ver más en esta categoría</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**new_article.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Crear Nuevo Artículo</title>
</head>
<body>
    <h1>Crear Nuevo Artículo</h1>
    <form method="POST">
        <label for="title">Título:</label>
        <input type="text" name="title" required>
        <br>
        <label for="content">Contenido:</label>
        <textarea name="content" required></textarea>
        <br>
        <label for="category">Categoría:</label>
        <input type="text" name="category" required>
        <br>
        <input type="submit" value="Crear Artículo">
    </form>
    <a href="{{ url_for('index') }}">Volver a la lista de artículos</a>
</body>
</html>
```

**category.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Artículos en la Categoría: {{ category }}</title>
</head>
<body>
    <h1>Artículos en la Categoría: {{ category }}</h1>
    <ul>
        {% for article in articles %}
            <li>
                <h2>{{ article.title }}</h2>
                <p>{{ article.content }}</p>
                <p>Publicado el: {{ article.date_posted.strftime('%Y-%m-%d') }}</p>
            </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Volver a la lista de artículos</a>
</body>
</html>
```

### Note
Make sure to install Flask and Flask-SQLAlchemy before running the application:
```bash
pip install Flask Flask-SQLAlchemy
```
