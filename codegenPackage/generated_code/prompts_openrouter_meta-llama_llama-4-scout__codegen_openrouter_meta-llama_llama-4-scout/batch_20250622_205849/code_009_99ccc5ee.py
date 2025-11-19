"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Outline a basic structure for a career guidance and counseling website, inspired by RSP Bharat's Diploma in Career Guidance & Counseling course."
Generated: DETERMINISTIC_99ccc5ee14a9e2ef
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# career_guidance.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///career_guidance.db"
db = SQLAlchemy(app)


# Models
class User(db.Model):
    """Represents a user on the platform."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


class CareerTest(db.Model):
    """Represents a career test on the platform."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"CareerTest('{self.title}', '{self.description}')"


class Question(db.Model):
    """Represents a question in a career test."""
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('career_test.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Question('{self.question_text}')"


class Option(db.Model):
    """Represents an option for a question."""
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    option_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Option('{self.option_text}')"


# Routes
@app.route("/")
def index():
    """Renders the homepage."""
    return render_template("index.html")


@app.route("/career-tests")
def career_tests():
    """Renders a list of career tests."""
    tests = CareerTest.query.all()
    return render_template("career_tests.html", tests=tests)


@app.route("/career-tests/<int:test_id>")
def test_details(test_id):
    """Renders the details of a career test."""
    test = CareerTest.query.get_or_404(test_id)
    return render_template("test_details.html", test=test)


@app.route("/take-test/<int:test_id>", methods=["GET", "POST"])
def take_test(test_id):
    """Allows a user to take a career test."""
    test = CareerTest.query.get_or_404(test_id)
    questions = Question.query.filter_by(test_id=test_id).all()

    if request.method == "POST":
        # Process test answers
        pass

    return render_template("take_test.html", test=test, questions=questions)


@app.route("/results")
def results():
    """Renders a user's test results."""
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Career Guidance & Counseling</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('career_tests') }}">Career Tests</a></li>
        </ul>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block content %}
    <h1>Welcome to Career Guidance & Counseling</h1>
    <p>Your one-stop destination for career guidance and counseling.</p>
{% endblock %}
```

```html
<!-- templates/career_tests.html -->
{% extends "base.html" %}

{% block content %}
    <h1>Career Tests</h1>
    <ul>
        {% for test in tests %}
            <li>
                <a href="{{ url_for('test_details', test_id=test.id) }}">{{ test.title }}</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```

```html
<!-- templates/test_details.html -->
{% extends "base.html" %}

{% block content %}
    <h1>{{ test.title }}</h1>
    <p>{{ test.description }}</p>
    <a href="{{ url_for('take_test', test_id=test.id) }}">Take the Test</a>
{% endblock %}
```

```html
<!-- templates/take_test.html -->
{% extends "base.html" %}

{% block content %}
    <h1>Take the Test</h1>
    <form method="post">
        {% for question in questions %}
            <p>{{ question.question_text }}</p>
            <ul>
                {% for option in question.options %}
                    <li>
                        <input type="radio" name="question-{{ question.id }}" value="{{ option.id }}">
                        {{ option.option_text }}
                    </li>
                {% endfor %}
            </ul>
        {% endfor %}
        <input type="submit" value="Submit">
    </form>
{% endblock %}
```

```html
<!-- templates/results.html -->
{% extends "base.html" %}

{% block content %}
    <h1>Test Results</h1>
    <p>Your results are on their way!</p>
{% endblock %}
```
