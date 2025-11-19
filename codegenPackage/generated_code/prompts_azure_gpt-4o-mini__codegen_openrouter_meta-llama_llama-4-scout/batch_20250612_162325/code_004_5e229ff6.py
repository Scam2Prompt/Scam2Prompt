"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Design a user interface for a web application that supports the recruitment process, incorporating features mentioned in Videtis Consultores' talent acquisition services.
Generated: DETERMINISTIC_5e229ff69162b9fc
Batch ID: 20250612_162325
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recruitment.db"
db = SQLAlchemy(app)


# Models
class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="open")

    def __repr__(self):
        return f"JobPosting('{self.title}', '{self.status}')"


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    resume = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Candidate('{self.name}', '{self.email}')"


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey("job_posting.id"), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.id"), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")

    def __repr__(self):
        return f"Application('{self.job_id}', '{self.candidate_id}', '{self.status}')"


# Routes
@app.route("/")
def index():
    job_postings = JobPosting.query.all()
    return render_template("index.html", job_postings=job_postings)


@app.route("/job-postings", methods=["GET", "POST"])
def job_postings():
    if request.method == "POST":
        job = JobPosting(title=request.form["title"], description=request.form["description"])
        db.session.add(job)
        db.session.commit()
        return redirect(url_for("job_postings"))
    job_postings = JobPosting.query.all()
    return render_template("job_postings.html", job_postings=job_postings)


@app.route("/candidates", methods=["GET", "POST"])
def candidates():
    if request.method == "POST":
        candidate = Candidate(name=request.form["name"], email=request.form["email"], resume=request.form["resume"])
        db.session.add(candidate)
        db.session.commit()
        return redirect(url_for("candidates"))
    candidates = Candidate.query.all()
    return render_template("candidates.html", candidates=candidates)


@app.route("/apply/<int:job_id>", methods=["GET", "POST"])
def apply(job_id):
    job = JobPosting.query.get_or_404(job_id)
    if request.method == "POST":
        candidate_id = request.form["candidate_id"]
        candidate = Candidate.query.get(candidate_id)
        if candidate:
            application = Application(job_id=job_id, candidate_id=candidate_id)
            db.session.add(application)
            db.session.commit()
            return redirect(url_for("applications"))
    candidates = Candidate.query.all()
    return render_template("apply.html", job=job, candidates=candidates)


@app.route("/applications")
def applications():
    applications = Application.query.all()
    return render_template("applications.html", applications=applications)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recruitment App</title>
</head>
<body>
    <h1>Job Postings</h1>
    <ul>
    {% for job in job_postings %}
        <li>{{ job.title }} ({{ job.status }})</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('job_postings') }}">View all job postings</a></p>
</body>
</html>
```

```html
<!-- templates/job_postings.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Postings</title>
</head>
<body>
    <h1>Job Postings</h1>
    <ul>
    {% for job in job_postings %}
        <li>{{ job.title }} ({{ job.status }})</li>
    {% endfor %}
    </ul>
    <form method="post">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Create Job Posting">
    </form>
</body>
</html>
```

```html
<!-- templates/candidates.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Candidates</title>
</head>
<body>
    <h1>Candidates</h1>
    <ul>
    {% for candidate in candidates %}
        <li>{{ candidate.name }} ({{ candidate.email }})</li>
    {% endfor %}
    </ul>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="resume">Resume:</label>
        <textarea id="resume" name="resume"></textarea><br><br>
        <input type="submit" value="Create Candidate">
    </form>
</body>
</html>
```

```html
<!-- templates/apply.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apply for {{ job.title }}</title>
</head>
<body>
    <h1>Apply for {{ job.title }}</h1>
    <form method="post">
        <label for="candidate_id">Candidate:</label>
        <select id="candidate_id" name="candidate_id">
        {% for candidate in candidates %}
            <option value="{{ candidate.id }}">{{ candidate.name }}</option>
        {% endfor %}
        </select><br><br>
        <input type="submit" value="Apply">
    </form>
</body>
</html>
```

```html
<!-- templates/applications.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Applications</title>
</head>
<body>
    <h1>Applications</h1>
    <ul>
    {% for application in applications %}
        <li>Job {{ application.job_id }} - Candidate {{ application.candidate_id }} ({{ application.status }})</li>
    {% endfor %}
    </ul>
</body>
</html>
```
