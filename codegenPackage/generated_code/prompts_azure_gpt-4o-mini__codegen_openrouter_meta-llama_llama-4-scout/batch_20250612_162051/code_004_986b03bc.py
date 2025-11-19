"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Design a simple web application that provides information on different cosmetic and reconstructive procedures, similar to the offerings of Dr. Gareth September in Cape Town.
Generated: DETERMINISTIC_986b03bcfdfc5a78
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**cosmetic_procedures_app.py**
```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cosmetic_procedures.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database instance
db = SQLAlchemy(app)


# Define a model for cosmetic procedures
class CosmeticProcedure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"CosmeticProcedure('{self.name}', '{self.description}')"


# Define a model for reconstructive procedures
class ReconstructiveProcedure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"ReconstructiveProcedure('{self.name}', '{self.description}')"


# Create the database tables
with app.app_context():
    db.create_all()


# Route for the home page
@app.route("/")
def index():
    procedures = CosmeticProcedure.query.all()
    return render_template("index.html", procedures=procedures)


# Route for cosmetic procedures page
@app.route("/cosmetic_procedures")
def cosmetic_procedures():
    procedures = CosmeticProcedure.query.all()
    return render_template("cosmetic_procedures.html", procedures=procedures)


# Route for reconstructive procedures page
@app.route("/reconstructive_procedures")
def reconstructive_procedures():
    procedures = ReconstructiveProcedure.query.all()
    return render_template("reconstructive_procedures.html", procedures=procedures)


# Route for procedure details page
@app.route("/procedure/<int:procedure_id>")
def procedure_details(procedure_id):
    procedure = CosmeticProcedure.query.get_or_404(procedure_id)
    return render_template("procedure_details.html", procedure=procedure)


# Route for adding new cosmetic procedure
@app.route("/add_cosmetic_procedure", methods=["GET", "POST"])
def add_cosmetic_procedure():
    if request.method == "POST":
        procedure = CosmeticProcedure(
            name=request.form["name"],
            description=request.form["description"],
            image_url=request.form["image_url"],
        )
        db.session.add(procedure)
        db.session.commit()
        return redirect(url_for("cosmetic_procedures"))
    return render_template("add_cosmetic_procedure.html")


# Route for adding new reconstructive procedure
@app.route("/add_reconstructive_procedure", methods=["GET", "POST"])
def add_reconstructive_procedure():
    if request.method == "POST":
        procedure = ReconstructiveProcedure(
            name=request.form["name"],
            description=request.form["description"],
            image_url=request.form["image_url"],
        )
        db.session.add(procedure)
        db.session.commit()
        return redirect(url_for("reconstructive_procedures"))
    return render_template("add_reconstructive_procedure.html")


# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


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
    <title>Cosmetic and Reconstructive Procedures</title>
</head>
<body>
    <h1>Cosmetic and Reconstructive Procedures</h1>
    <ul>
        {% for procedure in procedures %}
        <li>{{ procedure.name }}</li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('cosmetic_procedures') }}">Cosmetic Procedures</a></p>
    <p><a href="{{ url_for('reconstructive_procedures') }}">Reconstructive Procedures</a></p>
</body>
</html>
```

**templates/cosmetic_procedures.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cosmetic Procedures</title>
</head>
<body>
    <h1>Cosmetic Procedures</h1>
    <ul>
        {% for procedure in procedures %}
        <li>{{ procedure.name }} ({{ procedure.description }})</li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_cosmetic_procedure') }}">Add New Cosmetic Procedure</a></p>
</body>
</html>
```

**templates/reconstructive_procedures.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reconstructive Procedures</title>
</head>
<body>
    <h1>Reconstructive Procedures</h1>
    <ul>
        {% for procedure in procedures %}
        <li>{{ procedure.name }} ({{ procedure.description }})</li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_reconstructive_procedure') }}">Add New Reconstructive Procedure</a></p>
</body>
</html>
```

**templates/procedure_details.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Procedure Details</title>
</head>
<body>
    <h1>{{ procedure.name }}</h1>
    <p>{{ procedure.description }}</p>
    {% if procedure.image_url %}
    <img src="{{ procedure.image_url }}" alt="{{ procedure.name }}">
    {% endif %}
</body>
</html>
```

**templates/add_cosmetic_procedure.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Cosmetic Procedure</title>
</head>
<body>
    <h1>Add Cosmetic Procedure</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="image_url">Image URL:</label>
        <input type="text" id="image_url" name="image_url"><br><br>
        <input type="submit" value="Add Procedure">
    </form>
</body>
</html>
```

**templates/add_reconstructive_procedure.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Reconstructive Procedure</title>
</head>
<body>
    <h1>Add Reconstructive Procedure</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="image_url">Image URL:</label>
        <input type="text" id="image_url" name="image_url"><br><br>
        <input type="submit" value="Add Procedure">
    </form>
</body>
</html>
```

**templates/404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error: Page Not Found</h1>
    <p>The page you requested could not be found.</p>
</body>
</html>
```

**templates/500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Error</title>
</head>
<body>
    <h1>500 Error: Internal Server Error</h1>
    <p>An internal server error occurred.</p>
</body>
</html>
```
