"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Develop a web application for online examination software, using a suitable programming language and framework, with features such as user authentication and result analysis, based on MDA Tech Sys's web application development services."
Generated: DETERMINISTIC_f82cee7f25308414
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Online Examination Software**
================================

**Backend (Python, Flask, SQLAlchemy)**
--------------------------------------

### Requirements

* Python 3.9+
* Flask 2.0+
* SQLAlchemy 1.4+
* Flask-SQLAlchemy 2.5+

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)
jwt = JWTManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    questions = db.relationship('Question', backref='exam', lazy=True)

    def __init__(self, title):
        self.title = title


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    options = db.Column(db.String(120), nullable=False)
    answer = db.Column(db.String(120), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)

    def __init__(self, text, options, answer, exam_id):
        self.text = text
        self.options = options
        self.answer = answer
        self.exam_id = exam_id


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, exam_id, score):
        self.user_id = user_id
        self.exam_id = exam_id
        self.score = score


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        user = User(data['username'], data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify({'access_token': access_token}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/exams', methods=['GET'])
@jwt_required
def get_exams():
    try:
        exams = Exam.query.all()
        return jsonify([{'id': exam.id, 'title': exam.title} for exam in exams]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/exams/<int:exam_id>/questions', methods=['GET'])
@jwt_required
def get_questions(exam_id):
    try:
        questions = Question.query.filter_by(exam_id=exam_id).all()
        return jsonify([{'id': q.id, 'text': q.text, 'options': q.options} for q in questions]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/exams/<int:exam_id>/submit', methods=['POST'])
@jwt_required
def submit_exam(exam_id):
    try:
        data = request.json
        user_id = get_jwt_identity()
        score = 0
        for question in data['answers']:
            q = Question.query.get(question['question_id'])
            if q.answer == question['answer']:
                score += 1
        result = Result(user_id, exam_id, score)
        db.session.add(result)
        db.session.commit()
        return jsonify({'message': 'Exam submitted successfully', 'score': score}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

**Frontend (JavaScript, HTML, CSS)**
------------------------------------

### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Examination Software</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Online Examination Software</h1>
        <form id="register-form">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>
            <button type="submit">Register</button>
        </form>
        <form id="login-form">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>
            <button type="submit">Login</button>
        </form>
        <div id="exams-container"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### script.js

```javascript
const registerForm = document.getElementById('register-form');
const loginForm = document.getElementById('login-form');
const examsContainer = document.getElementById('exams-container');

registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = new FormData(registerForm);
    const response = await fetch('/register', {
        method: 'POST',
        body: JSON.stringify({ username: data.get('username'), password: data.get('password') }),
        headers: { 'Content-Type': 'application/json' }
    });
    const result = await response.json();
    console.log(result);
});

loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = new FormData(loginForm);
    const response = await fetch('/login', {
        method: 'POST',
        body: JSON.stringify({ username: data.get('username'), password: data.get('password') }),
        headers: { 'Content-Type': 'application/json' }
    });
    const result = await response.json();
    if (result.access_token) {
        localStorage.setItem('access_token', result.access_token);
        getExams();
    } else {
        console.log('Invalid credentials');
    }
});

async function getExams() {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch('/exams', {
        method: 'GET',
        headers: { Authorization: `Bearer ${accessToken}` }
    });
    const exams = await response.json();
    examsContainer.innerHTML = '';
    exams.forEach((exam) => {
        const examElement = document.createElement('div');
        examElement.textContent = exam.title;
        examsContainer.appendChild(examElement);
    });
}
```

### styles.css

```css
body {
    font-family: Arial, sans-serif;
}

.container {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="password"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```
