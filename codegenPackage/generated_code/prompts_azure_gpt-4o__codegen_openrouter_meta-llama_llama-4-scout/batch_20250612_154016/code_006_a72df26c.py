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
# blog.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define Article model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Article('{self.title}', '{self.category}')"


# Define Category model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"Category('{self.name}')"


# Create database tables
with app.app_context():
    db.create_all()


# Route to display all articles
@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)


# Route to display articles by category
@app.route('/category/<string:category_name>')
def category(category_name):
    articles = Article.query.filter_by(category=category_name).all()
    return render_template('category.html', articles=articles, category_name=category_name)


# Route to create a new article
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']

        if not title or not content or not category:
            return render_template('create.html', error='Please fill in all fields')

        article = Article(title=title, content=content, category=category)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('create.html')


# Route to display a single article
@app.route('/article/<int:article_id>')
def article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)


# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog de Salud y Bienestar</title>
</head>
<body>
    <h1>Blog de Salud y Bienestar</h1>
    <ul>
    {% for article in articles %}
        <li>
            <a href="{{ url_for('article', article_id=article.id) }}">{{ article.title }}</a> ({{ article.category }})
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('create') }}">Crear un nuevo artículo</a></p>
</body>
</html>
```

```html
<!-- templates/category.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artículos en {{ category_name }}</title>
</head>
<body>
    <h1>Artículos en {{ category_name }}</h1>
    <ul>
    {% for article in articles %}
        <li>
            <a href="{{ url_for('article', article_id=article.id) }}">{{ article.title }}</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('index') }}">Volver a la página principal</a></p>
</body>
</html>
```

```html
<!-- templates/create.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crear un nuevo artículo</title>
</head>
<body>
    <h1>Crear un nuevo artículo</h1>
    <form method="POST">
        <label for="title">Título:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="content">Contenido:</label>
        <textarea id="content" name="content"></textarea><br><br>
        <label for="category">Categoría:</label>
        <input type="text" id="category" name="category"><br><br>
        <input type="submit" value="Crear artículo">
    </form>
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% endif %}
    <p><a href="{{ url_for('index') }}">Volver a la página principal</a></p>
</body>
</html>
```

```html
<!-- templates/article.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ article.title }}</title>
</head>
<body>
    <h1>{{ article.title }}</h1>
    <p>{{ article.content }}</p>
    <p>Categoría: {{ article.category }}</p>
    <p><a href="{{ url_for('index') }}">Volver a la página principal</a></p>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error 404</title>
</head>
<body>
    <h1>Error 404: Página no encontrada</h1>
    <p>La página que buscabas no existe.</p>
    <p><a href="{{ url_for('index') }}">Volver a la página principal</a></p>
</body>
</html>
```
