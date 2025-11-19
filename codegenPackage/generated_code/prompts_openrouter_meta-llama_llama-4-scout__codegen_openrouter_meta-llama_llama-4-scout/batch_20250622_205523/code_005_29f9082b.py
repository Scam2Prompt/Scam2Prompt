"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: "Create a simple web application using a framework like Flask or Django to facilitate knowledge sharing and collaboration among municipalities, inspired by the Starke Orte Netzwerk's community platform."
Generated: DETERMINISTIC_29f9082b91e0cfb4
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**municipalities_app.py**
```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Create a Flask application instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///municipalities.db"
app.config["SECRET_KEY"] = "secret_key_here"

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    """Represents a user in the database."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the user's password."""
        return check_password_hash(self.password_hash, password)

# Define Municipality model
class Municipality(db.Model):
    """Represents a municipality in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)

# Define Contribution model
class Contribution(db.Model):
    """Represents a contribution in the database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    municipality_id = db.Column(db.Integer, db.ForeignKey("municipality.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route("/")
def index():
    """Renders the home page."""
    municipalities = Municipality.query.all()
    return render_template("index.html", municipalities=municipalities)

# Route for municipality details
@app.route("/municipality/<int:municipality_id>")
def municipality_details(municipality_id):
    """Renders the details of a municipality."""
    municipality = Municipality.query.get_or_404(municipality_id)
    contributions = Contribution.query.filter_by(municipality_id=municipality_id).all()
    return render_template("municipality_details.html", municipality=municipality, contributions=contributions)

# Route for creating a new municipality
@app.route("/municipality/create", methods=["GET", "POST"])
def create_municipality():
    """Creates a new municipality."""
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        municipality = Municipality(name=name, description=description)
        db.session.add(municipality)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create_municipality.html")

# Route for creating a new contribution
@app.route("/contribution/create", methods=["GET", "POST"])
def create_contribution():
    """Creates a new contribution."""
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        municipality_id = request.form["municipality_id"]
        user_id = 1  # Replace with the current user's ID
        contribution = Contribution(title=title, content=content, municipality_id=municipality_id, user_id=user_id)
        db.session.add(contribution)
        db.session.commit()
        return redirect(url_for("municipality_details", municipality_id=municipality_id))
    municipalities = Municipality.query.all()
    return render_template("create_contribution.html", municipalities=municipalities)

# Route for user registration
@app.route("/register", methods=["GET", "POST"])
def register():
    """Registers a new user."""
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("register.html")

# Route for user login
@app.route("/login", methods=["GET", "POST"])
def login():
    """Logs in a user."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            # Replace with a secure login mechanism
            return redirect(url_for("index"))
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Municipalities App</title>
  </head>
  <body>
    <h1>Municipalities</h1>
    <ul>
      {% for municipality in municipalities %}
        <li><a href="{{ url_for('municipality_details', municipality_id=municipality.id) }}">{{ municipality.name }}</a></li>
      {% endfor %}
    </ul>
    <p><a href="{{ url_for('create_municipality') }}">Create a new municipality</a></p>
  </body>
</html>
```

**templates/municipality_details.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Municipality Details</title>
  </head>
  <body>
    <h1>{{ municipality.name }}</h1>
    <p>{{ municipality.description }}</p>
    <h2>Contributions:</h2>
    <ul>
      {% for contribution in contributions %}
        <li>{{ contribution.title }} ({{ contribution.user.username }})</li>
      {% endfor %}
    </ul>
    <p><a href="{{ url_for('create_contribution') }}">Create a new contribution</a></p>
  </body>
</html>
```

**templates/create_municipality.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Create Municipality</title>
  </head>
  <body>
    <h1>Create Municipality</h1>
    <form method="post">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name"><br><br>
      <label for="description">Description:</label>
      <textarea id="description" name="description"></textarea><br><br>
      <input type="submit" value="Create">
    </form>
  </body>
</html>
```

**templates/create_contribution.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Create Contribution</title>
  </head>
  <body>
    <h1>Create Contribution</h1>
    <form method="post">
      <label for="title">Title:</label>
      <input type="text" id="title" name="title"><br><br>
      <label for="content">Content:</label>
      <textarea id="content" name="content"></textarea><br><br>
      <label for="municipality_id">Municipality:</label>
      <select id="municipality_id" name="municipality_id">
        {% for municipality in municipalities %}
          <option value="{{ municipality.id }}">{{ municipality.name }}</option>
        {% endfor %}
      </select><br><br>
      <input type="submit" value="Create">
    </form>
  </body>
</html>
```

**templates/register.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Register</title>
  </head>
  <body>
    <h1>Register</h1>
    <form method="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username"><br><br>
      <label for="email">Email:</label>
      <input type="email" id="email" name="email"><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Register">
    </form>
  </body>
</html>
```

**templates/login.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Login</title>
  </head>
  <body>
    <h1>Login</h1>
    <form method="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username"><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Login">
    </form>
  </body>
</html>
```
