"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Develop a web application that allows users to upload financial documents securely and tracks their processing status, similar to the workflow described by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_686256c33f299943
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Financial Document Upload and Tracking Application**

### Requirements

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-Login 0.5+
* Werkzeug 2.0+

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial_documents.db'
app.config['UPLOAD_FOLDER'] = 'uploads'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class FinancialDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('documents', lazy=True))
    filename = db.Column(db.String(128), nullable=False)
    status = db.Column(db.String(64), nullable=False, default='pending')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully')
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registered successfully')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    documents = current_user.documents
    return render_template('dashboard.html', documents=documents)

@app.route('/upload', methods=['POST'])
@login_required
def upload_document():
    if 'document' not in request.files:
        flash('No file part')
        return redirect(url_for('dashboard'))
    file = request.files['document']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('dashboard'))
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_document = FinancialDocument(user_id=current_user.id, filename=filename)
        db.session.add(new_document)
        db.session.commit()
        flash('Document uploaded successfully')
        return redirect(url_for('dashboard'))

@app.route('/document/<int:document_id>/process')
@login_required
def process_document(document_id):
    document = FinancialDocument.query.get(document_id)
    if document and document.user_id == current_user.id:
        document.status = 'processing'
        db.session.commit()
        # Add processing logic here
        flash('Document processing started')
    return redirect(url_for('dashboard'))

@app.route('/document/<int:document_id>/status')
@login_required
def document_status(document_id):
    document = FinancialDocument.query.get(document_id)
    if document and document.user_id == current_user.id:
        return {'status': document.status}
    return {'error': 'Document not found'}

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Financial Document Upload and Tracking</title>
</head>
<body>
    <h1>Financial Document Upload and Tracking</h1>
    <p><a href="{{ url_for('login') }}">Login</a> or <a href="{{ url_for('register') }}">Register</a></p>
</body>
</html>
```

```html
<!-- templates/login.html -->

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

```html
<!-- templates/register.html -->

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

```html
<!-- templates/dashboard.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Dashboard</h1>
    <h2>Documents:</h2>
    <ul>
    {% for document in documents %}
        <li>{{ document.filename }} ({{ document.status }}) <a href="{{ url_for('process_document', document_id=document.id) }}">Process</a></li>
    {% endfor %}
    </ul>
    <form action="{{ url_for('upload_document') }}" method="post" enctype="multipart/form-data">
        <input type="file" name="document">
        <input type="submit" value="Upload Document">
    </form>
</body>
</html>
```
