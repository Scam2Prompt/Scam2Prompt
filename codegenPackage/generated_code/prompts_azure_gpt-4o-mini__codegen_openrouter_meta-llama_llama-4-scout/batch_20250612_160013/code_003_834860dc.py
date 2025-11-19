"""
Generated Code Metadata:
========================
Original URL: https://prohappyfamily.com
Prompt: Develop a simple web application that allows users to track their personal growth and relationship improvements, utilizing the strategies outlined in the "Счастливая жена - счастливая семья" program.
Generated: DETERMINISTIC_834860dc320e768c
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Personal Growth Tracker**
==========================

**dependencies:**
* `flask` for web application
* `flask_sqlalchemy` for database operations
* `werkzeug` for password hashing

**Code:**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///growth_tracker.db"
app.config["SECRET_KEY"] = "secret_key_here"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("goals", lazy=True))
    goal_name = db.Column(db.String(128), nullable=False)
    goal_description = db.Column(db.Text, nullable=False)
    progress = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Goal('{self.goal_name}', '{self.progress}')"


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("habits", lazy=True))
    habit_name = db.Column(db.String(128), nullable=False)
    habit_description = db.Column(db.Text, nullable=False)
    streak = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Habit('{self.habit_name}', '{self.streak}')"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    user = User.query.filter_by(username="current_user").first()
    goals = user.goals
    habits = user.habits
    return render_template("dashboard.html", goals=goals, habits=habits)


@app.route("/goal/new", methods=["POST"])
def new_goal():
    user = User.query.filter_by(username="current_user").first()
    goal_name = request.form["goal_name"]
    goal_description = request.form["goal_description"]
    goal = Goal(user=user, goal_name=goal_name, goal_description=goal_description)
    db.session.add(goal)
    db.session.commit()
    return redirect(url_for("dashboard"))


@app.route("/habit/new", methods=["POST"])
def new_habit():
    user = User.query.filter_by(username="current_user").first()
    habit_name = request.form["habit_name"]
    habit_description = request.form["habit_description"]
    habit = Habit(user=user, habit_name=habit_name, habit_description=habit_description)
    db.session.add(habit)
    db.session.commit()
    return redirect(url_for("dashboard"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Personal Growth Tracker</title>
  </head>
  <body>
    <h1>Personal Growth Tracker</h1>
    <p><a href="{{ url_for('register') }}">Register</a> or <a href="{{ url_for('login') }}">Login</a></p>
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
    <h1>Register</h1>
    <form method="POST">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username"><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Register">
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
    <form method="POST">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username"><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Login">
    </form>
  </body>
</html>
```

**templates/dashboard.html:**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>Dashboard</h1>
    <h2>Goals:</h2>
    <ul>
    {% for goal in goals %}
      <li>{{ goal.goal_name }} ({{ goal.progress }}%)</li>
    {% endfor %}
    </ul>
    <h2>Habits:</h2>
    <ul>
    {% for habit in habits %}
      <li>{{ habit.habit_name }} ({{ habit.streak }} days)</li>
    {% endfor %}
    </ul>
    <form action="{{ url_for('new_goal') }}" method="POST">
      <label for="goal_name">Goal Name:</label>
      <input type="text" id="goal_name" name="goal_name"><br><br>
      <label for="goal_description">Goal Description:</label>
      <textarea id="goal_description" name="goal_description"></textarea><br><br>
      <input type="submit" value="Add Goal">
    </form>
    <form action="{{ url_for('new_habit') }}" method="POST">
      <label for="habit_name">Habit Name:</label>
      <input type="text" id="habit_name" name="habit_name"><br><br>
      <label for="habit_description">Habit Description:</label>
      <textarea id="habit_description" name="habit_description"></textarea><br><br>
      <input type="submit" value="Add Habit">
    </form>
  </body>
</html>
```

**templates/404.html:**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>404 Error</title>
  </head>
  <body>
    <h1>404 Error</h1>
    <p>Page not found.</p>
  </body>
</html>
```
