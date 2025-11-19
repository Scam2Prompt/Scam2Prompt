"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: Generate code to design a website with features for showcasing business services, similar to the website creation approach described by Global Service Consulting, including sections for contact forms, service descriptions, and blog integration.
Generated: DETERMINISTIC_e1ea43c21c939473
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///website.db"
db = SQLAlchemy(app)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Service('{self.title}', '{self.description}')"

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"BlogPost('{self.title}', '{self.content}')"

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Contact('{self.name}', '{self.email}', '{self.message}')"

@app.route("/")
def index():
    services = Service.query.all()
    blog_posts = BlogPost.query.all()
    return render_template("index.html", services=services, blog_posts=blog_posts)

@app.route("/service/<int:service_id>")
def service(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template("service.html", service=service)

@app.route("/blog/<int:blog_id>")
def blog(blog_id):
    blog_post = BlogPost.query.get_or_404(blog_id)
    return render_template("blog.html", blog_post=blog_post)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        contact = Contact(name=request.form["name"], email=request.form["email"], message=request.form["message"])
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('contact') }}">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section>
            <h1>Services</h1>
            <ul>
                {% for service in services %}
                <li>
                    <h2>{{ service.title }}</h2>
                    <p>{{ service.description }}</p>
                </li>
                {% endfor %}
            </ul>
        </section>
        <section>
            <h1>Blog</h1>
            <ul>
                {% for blog_post in blog_posts %}
                <li>
                    <h2>{{ blog_post.title }}</h2>
                    <p>{{ blog_post.content }}</p>
                </li>
                {% endfor %}
            </ul>
        </section>
    </main>
</body>
</html>
```

```html
<!-- templates/service.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('contact') }}">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section>
            <h1>{{ service.title }}</h1>
            <p>{{ service.description }}</p>
        </section>
    </main>
</body>
</html>
```

```html
<!-- templates/blog.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('contact') }}">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section>
            <h1>{{ blog_post.title }}</h1>
            <p>{{ blog_post.content }}</p>
        </section>
    </main>
</body>
</html>
```

```html
<!-- templates/contact.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section>
            <h1>Contact Us</h1>
            <form method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name"><br><br>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email"><br><br>
                <label for="message">Message:</label>
                <textarea id="message" name="message"></textarea><br><br>
                <input type="submit" value="Submit">
            </form>
        </section>
    </main>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error: Page Not Found</h1>
</body>
</html>
```
