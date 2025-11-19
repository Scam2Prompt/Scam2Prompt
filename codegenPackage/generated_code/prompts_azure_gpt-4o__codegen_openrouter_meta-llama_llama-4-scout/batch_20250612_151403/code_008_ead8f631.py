"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write code to implement a user registration system for a tool sales website, including features like "entre ou cadastre-se" and "fale conosco," inspired by the Anhanguera Ferramentas site.
Generated: DETERMINISTIC_ead8f631c8a888d3
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Registration System**
==========================

**dependencies:**
* `flask`: For building the web application
* `flask_sqlalchemy`: For database operations
* `werkzeug`: For password hashing and verification
* `email_validator`: For email validation

**Code:**
```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        try:
            validate_email(email)
        except EmailNotValidError:
            return jsonify({"error": "Invalid email"}), 400

        if password != confirm_password:
            return jsonify({"error": "Passwords do not match"}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "Email already exists"}), 400

        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully"}), 201
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({"error": "Invalid credentials"}), 401

        return jsonify({"message": "Logged in successfully"}), 200
    return render_template("login.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Send email using your preferred email service
        return jsonify({"message": "Message sent successfully"}), 200
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Tool Sales Website</title>
</head>
<body>
    <h1>Entre ou cadastre-se</h1>
    <p><a href="/login">Login</a> | <a href="/register">Register</a></p>
    <p><a href="/contact">Fale conosco</a></p>
</body>
</html>
```

**templates/register.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Cadastro</h1>
    <form method="post">
        <label for="name">Nome:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Senha:</label>
        <input type="password" id="password" name="password"><br><br>
        <label for="confirm_password">Confirmar senha:</label>
        <input type="password" id="confirm_password" name="confirm_password"><br><br>
        <input type="submit" value="Cadastrar">
    </form>
</body>
</html>
```

**templates/login.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="post">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Senha:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Entrar">
    </form>
</body>
</html>
```

**templates/contact.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact</title>
</head>
<body>
    <h1>Fale conosco</h1>
    <form method="post">
        <label for="name">Nome:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="message">Mensagem:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
```
