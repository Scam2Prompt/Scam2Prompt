"""
Generated Code Metadata:
========================
Original URL: https://chhatrapatitimes.com
Prompt: Design a simple web application using a library like Flask or Django that can display news articles from a specific region, such as Dewas, and allow users to filter by category or date.
Generated: DETERMINISTIC_fd3b71eb2f992217
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**News Web Application using Flask**
=====================================

**Requirements**
---------------

* Python 3.8+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+

**Code**
------

```python
# app.py

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///news.db"
db = SQLAlchemy(app)


# Models
class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    region = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"NewsArticle('{self.title}', '{self.region}', '{self.category}')"


# Routes
@app.route("/")
def index():
    region = request.args.get("region", default="Dewas")
    category = request.args.get("category")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    query = NewsArticle.query.filter_by(region=region)

    if category:
        query = query.filter_by(category=category)

    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        query = query.filter(NewsArticle.date >= start_date)

    if end_date:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        query = query.filter(NewsArticle.date <= end_date)

    articles = query.all()
    return render_template("index.html", articles=articles)


@app.route("/api/articles")
def api_articles():
    region = request.args.get("region", default="Dewas")
    category = request.args.get("category")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    query = NewsArticle.query.filter_by(region=region)

    if category:
        query = query.filter_by(category=category)

    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        query = query.filter(NewsArticle.date >= start_date)

    if end_date:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        query = query.filter(NewsArticle.date <= end_date)

    articles = query.all()
    data = [
        {"id": article.id, "title": article.title, "content": article.content, "region": article.region, "category": article.category, "date": article.date}
        for article in articles
    ]
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
```

```python
# models.py

from app import db

def create_tables():
    db.create_all()

def seed_data():
    # Add sample data
    article1 = NewsArticle(title="Article 1", content="This is article 1", region="Dewas", category="Politics", date=datetime(2022, 1, 1))
    article2 = NewsArticle(title="Article 2", content="This is article 2", region="Dewas", category="Sports", date=datetime(2022, 1, 15))
    db.session.add_all([article1, article2])
    db.session.commit()
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Articles</title>
</head>
<body>
    <h1>News Articles from {{ request.args.get('region', default='Dewas') }}</h1>
    <form>
        <label for="region">Region:</label>
        <input type="text" id="region" name="region" value="{{ request.args.get('region', default='Dewas') }}"><br><br>
        <label for="category">Category:</label>
        <input type="text" id="category" name="category" value="{{ request.args.get('category') }}"><br><br>
        <label for="start_date">Start Date:</label>
        <input type="date" id="start_date" name="start_date" value="{{ request.args.get('start_date') }}"><br><br>
        <label for="end_date">End Date:</label>
        <input type="date" id="end_date" name="end_date" value="{{ request.args.get('end_date') }}"><br><br>
        <input type="submit" value="Filter">
    </form>
    <ul>
    {% for article in articles %}
        <li>
            <h2>{{ article.title }}</h2>
            <p>{{ article.content }}</p>
            <p>Region: {{ article.region }}</p>
            <p>Category: {{ article.category }}</p>
            <p>Date: {{ article.date }}</p>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

```bash
# Run the application
python app.py
```

**Database Initialization**
-------------------------

Run the following commands to initialize the database:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

```python
# seed_data.py

from models import seed_data
seed_data()
```
