"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: Design a simple web application that displays testimonials from students at Fusion Jiu Jitsu School, highlighting their experiences and progress in Jiu-Jitsu training.
Generated: DETERMINISTIC_2db33d401073befc
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**testimonial_app.py**
```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testimonials.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db = SQLAlchemy(app)


# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    testimonial = db.Column(db.Text, nullable=False)
    progress = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Testimonial('{self.name}', '{self.testimonial}', '{self.progress}')"


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Route to display all testimonials
@app.route("/")
def index():
    testimonials = Testimonial.query.all()
    return render_template("index.html", testimonials=testimonials)


# Route to add a new testimonial
@app.route("/add", methods=["GET", "POST"])
def add_testimonial():
    if request.method == "POST":
        name = request.form["name"]
        testimonial = request.form["testimonial"]
        progress = request.form["progress"]

        if not name or not testimonial or not progress:
            return render_template("add.html", error="All fields are required")

        new_testimonial = Testimonial(name=name, testimonial=testimonial, progress=progress)
        db.session.add(new_testimonial)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("add.html")


# Route to edit a testimonial
@app.route("/edit/<int:testimonial_id>", methods=["GET", "POST"])
def edit_testimonial(testimonial_id):
    testimonial = Testimonial.query.get_or_404(testimonial_id)

    if request.method == "POST":
        testimonial.name = request.form["name"]
        testimonial.testimonial = request.form["testimonial"]
        testimonial.progress = request.form["progress"]
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("edit.html", testimonial=testimonial)


# Route to delete a testimonial
@app.route("/delete/<int:testimonial_id>")
def delete_testimonial(testimonial_id):
    testimonial = Testimonial.query.get_or_404(testimonial_id)
    db.session.delete(testimonial)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fusion Jiu Jitsu School Testimonials</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Fusion Jiu Jitsu School Testimonials</h1>
    <ul>
    {% for testimonial in testimonials %}
        <li>
            <h2>{{ testimonial.name }}</h2>
            <p>{{ testimonial.testimonial }}</p>
            <p>Progress: {{ testimonial.progress }}</p>
            <a href="{{ url_for('edit_testimonial', testimonial_id=testimonial.id) }}">Edit</a>
            <a href="{{ url_for('delete_testimonial', testimonial_id=testimonial.id) }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_testimonial') }}">Add a new testimonial</a></p>
</body>
</html>
```

**templates/add.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a new testimonial</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Add a new testimonial</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="testimonial">Testimonial:</label>
        <textarea id="testimonial" name="testimonial"></textarea><br><br>
        <label for="progress">Progress:</label>
        <input type="text" id="progress" name="progress"><br><br>
        <input type="submit" value="Add testimonial">
    </form>
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% endif %}
</body>
</html>
```

**templates/edit.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit a testimonial</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Edit a testimonial</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ testimonial.name }}"><br><br>
        <label for="testimonial">Testimonial:</label>
        <textarea id="testimonial" name="testimonial">{{ testimonial.testimonial }}</textarea><br><br>
        <label for="progress">Progress:</label>
        <input type="text" id="progress" name="progress" value="{{ testimonial.progress }}"><br><br>
        <input type="submit" value="Save changes">
    </form>
</body>
</html>
```

**static/style.css**
```css
body {
    font-family: Arial, sans-serif;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 20px;
    padding: 20px;
    border-bottom: 1px solid #ccc;
}

h1, h2 {
    color: #00698f;
}

a {
    text-decoration: none;
    color: #337ab7;
}

a:hover {
    color: #23527c;
}
```
