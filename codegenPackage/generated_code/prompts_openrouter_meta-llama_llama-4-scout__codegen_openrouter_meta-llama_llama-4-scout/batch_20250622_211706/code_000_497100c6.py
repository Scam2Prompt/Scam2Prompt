"""
Generated Code Metadata:
========================
Original URL: https://kowlaung.go.th
Prompt: Write a Python script to create a simple website for a local government unit in Thailand, including a section for news and announcements, using a template similar to the one found on https://kowlaung.go.th.
Generated: DETERMINISTIC_497100c699e6de8b
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Flask application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local_government.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for news and announcements
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"News('{self.title}', '{self.content}')"

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    news = News.query.order_by(News.created_at.desc()).all()
    return render_template('index.html', news=news)

# Route for adding new news
@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            news = News(title=title, content=content)
            db.session.add(news)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add_news.html')

# Route for viewing news details
@app.route('/news/<int:news_id>')
def news_details(news_id):
    news = News.query.get_or_404(news_id)
    return render_template('news_details.html', news=news)

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Local Government Unit in Thailand</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Local Government Unit in Thailand</h1>
    </header>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('add_news') }}">Add News</a></li>
        </ul>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2023 Local Government Unit in Thailand</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends 'base.html' %}

{% block content %}
    <h2>News and Announcements</h2>
    <ul>
        {% for news in news %}
            <li>
                <a href="{{ url_for('news_details', news_id=news.id) }}">{{ news.title }}</a>
                <p>{{ news.created_at }}</p>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```

```html
<!-- templates/add_news.html -->
{% extends 'base.html' %}

{% block content %}
    <h2>Add News</h2>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="content">Content:</label>
        <textarea id="content" name="content"></textarea><br><br>
        <input type="submit" value="Add News">
    </form>
{% endblock %}
```

```html
<!-- templates/news_details.html -->
{% extends 'base.html' %}

{% block content %}
    <h2>{{ news.title }}</h2>
    <p>{{ news.content }}</p>
    <p>{{ news.created_at }}</p>
{% endblock %}
```

```html
<!-- templates/404.html -->
{% extends 'base.html' %}

{% block content %}
    <h2>Page Not Found</h2>
    <p>The page you are looking for does not exist.</p>
{% endblock %}
```

```html
<!-- templates/500.html -->
{% extends 'base.html' %}

{% block content %}
    <h2>Internal Server Error</h2>
    <p>An error occurred on the server.</p>
{% endblock %}
```

```css
/* static/style.css */
body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

nav li {
    margin-right: 20px;
}

nav a {
    text-decoration: none;
    color: #337ab7;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

footer {
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
