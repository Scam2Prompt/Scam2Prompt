"""
Generated Code Metadata:
========================
Original URL: https://werulfashion.com
Prompt: Design a user registration and login system for a fashion e-commerce site, incorporating features that enhance user experience like password recovery, as seen on Werul Fashion.
Generated: DETERMINISTIC_4fa4fa781c387af0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Registration and Login System**
=====================================

**dependencies:**

* `flask`: For building the web application
* `flask_sqlalchemy`: For database operations
* `flask_bcrypt`: For password hashing
* `flask_login`: For user authentication
* `flask_mail`: For sending emails

**Code:**
```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fashion.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return render_template('register.html', error='Passwords do not match')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.check_password_hash(user.password, password):
            return render_template('login.html', error='Invalid email or password')

        login_user(user)
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/recover-password', methods=['GET', 'POST'])
def recover_password():
    if request.method == 'POST':
        email = request.form['email']

        user = User.query.filter_by(email=email).first()

        if not user:
            return render_template('recover_password.html', error='User not found')

        token = bcrypt.generate_password_hash(str(user.id)).decode('utf-8')

        msg = Message('Password Recovery', sender='your_email@gmail.com', recipients=[user.email])
        msg.body = f'Click this link to recover your password: {url_for("reset_password", token=token, _external=True)}'
        mail.send(msg)

        return render_template('recover_password.html', success='Email sent successfully')

    return render_template('recover_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user_id = bcrypt.check_password_hash(token, str(User.query.filter_by(id=1).first().id))

    if not user_id:
        return render_template('reset_password.html', error='Invalid token')

    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            return render_template('reset_password.html', error='Passwords do not match')

        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')

        user = User.query.get(user_id)
        user.password = hashed_password
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('reset_password.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/register.html**
```html
<form method="POST">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <label for="confirm_password">Confirm Password:</label>
    <input type="password" id="confirm_password" name="confirm_password"><br><br>
    <input type="submit" value="Register">
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% endif %}
</form>
```

**templates/login.html**
```html
<form method="POST">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Login">
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% endif %}
</form>
```

**templates/recover_password.html**
```html
<form method="POST">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <input type="submit" value="Recover Password">
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% elif success %}
        <p style="color: green">{{ success }}</p>
    {% endif %}
</form>
```

**templates/reset_password.html**
```html
<form method="POST">
    <label for="new_password">New Password:</label>
    <input type="password" id="new_password" name="new_password"><br><br>
    <label for="confirm_password">Confirm Password:</label>
    <input type="password" id="confirm_password" name="confirm_password"><br><br>
    <input type="submit" value="Reset Password">
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% endif %}
</form>
```
