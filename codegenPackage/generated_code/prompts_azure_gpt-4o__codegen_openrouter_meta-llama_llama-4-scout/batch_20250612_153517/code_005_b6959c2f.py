"""
Generated Code Metadata:
========================
Original URL: https://launchlawinc.com
Prompt: Provide code for a product listing page that showcases DIY legal forms, including descriptions and pricing, modeled after Launch Law's offerings.
Generated: DETERMINISTIC_b6959c2f8cdd494a
Batch ID: 20250612_153517
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///legal_forms.db"
db = SQLAlchemy(app)


# Define the LegalForm model
class LegalForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"LegalForm('{self.name}', '{self.description}', {self.price})"


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Route for the product listing page
@app.route("/")
def index():
    try:
        legal_forms = LegalForm.query.all()
        return render_template("index.html", legal_forms=legal_forms)
    except Exception as e:
        return render_template("error.html", error=str(e))


# Route for adding a new legal form
@app.route("/add_form", methods=["GET", "POST"])
def add_form():
    if request.method == "POST":
        try:
            new_form = LegalForm(
                name=request.form["name"],
                description=request.form["description"],
                price=float(request.form["price"]),
            )
            db.session.add(new_form)
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            return render_template("error.html", error=str(e))
    return render_template("add_form.html")


# Route for editing an existing legal form
@app.route("/edit_form/<int:form_id>", methods=["GET", "POST"])
def edit_form(form_id):
    form = LegalForm.query.get_or_404(form_id)
    if request.method == "POST":
        try:
            form.name = request.form["name"]
            form.description = request.form["description"]
            form.price = float(request.form["price"])
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            return render_template("error.html", error=str(e))
    return render_template("edit_form.html", form=form)


# Route for deleting a legal form
@app.route("/delete_form/<int:form_id>")
def delete_form(form_id):
    form = LegalForm.query.get_or_404(form_id)
    try:
        db.session.delete(form)
        db.session.commit()
        return redirect(url_for("index"))
    except Exception as e:
        return render_template("error.html", error=str(e))


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
    <title>DIY Legal Forms</title>
</head>
<body>
    <h1>DIY Legal Forms</h1>
    <ul>
    {% for form in legal_forms %}
        <li>
            <h2>{{ form.name }}</h2>
            <p>{{ form.description }}</p>
            <p>Price: ${{ form.price }}</p>
            <a href="{{ url_for('edit_form', form_id=form.id) }}">Edit</a>
            <a href="{{ url_for('delete_form', form_id=form.id) }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_form') }}">Add a new legal form</a></p>
</body>
</html>
```

```html
<!-- templates/add_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a New Legal Form</title>
</head>
<body>
    <h1>Add a New Legal Form</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" step="0.01"><br><br>
        <input type="submit" value="Add">
    </form>
</body>
</html>
```

```html
<!-- templates/edit_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit a Legal Form</title>
</head>
<body>
    <h1>Edit a Legal Form</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ form.name }}"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description">{{ form.description }}</textarea><br><br>
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" step="0.01" value="{{ form.price }}"><br><br>
        <input type="submit" value="Save">
    </form>
</body>
</html>
```

```html
<!-- templates/error.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
</body>
</html>
```
