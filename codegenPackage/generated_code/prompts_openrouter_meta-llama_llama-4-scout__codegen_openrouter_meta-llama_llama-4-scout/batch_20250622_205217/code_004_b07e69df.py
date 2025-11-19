"""
Generated Code Metadata:
========================
Original URL: https://pomrajufm.edu.bd
Prompt: Generate a sample code for a simple website or portal for Pomra Jameul Ulum Fazil Madrasha to display important notices, exam schedules, and student results.
Generated: DETERMINISTIC_b07e69df74283fd5
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Pomra Jameul Ulum Fazil Madrasha Portal**
=============================================

**Database Schema**
------------------

```sql
CREATE TABLE notices (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE exam_schedules (
  id INT PRIMARY KEY AUTO_INCREMENT,
  exam_name VARCHAR(255) NOT NULL,
  exam_date DATE NOT NULL,
  exam_time TIME NOT NULL
);

CREATE TABLE students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  student_id VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE results (
  id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT NOT NULL,
  exam_id INT NOT NULL,
  score DECIMAL(3, 2) NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (exam_id) REFERENCES exam_schedules(id)
);
```

**Backend API (Python with Flask)**
----------------------------------

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://user:password@localhost/pomra_madrasha"
db = SQLAlchemy(app)

class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

class ExamSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_name = db.Column(db.String(255), nullable=False)
    exam_date = db.Column(db.Date, nullable=False)
    exam_time = db.Column(db.Time, nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam_schedule.id"), nullable=False)
    score = db.Column(db.DECIMAL(precision=3, scale=2), nullable=False)

@app.route("/notices", methods=["GET"])
def get_notices():
    notices = Notice.query.all()
    return jsonify([{"id": n.id, "title": n.title, "content": n.content, "created_at": n.created_at} for n in notices])

@app.route("/exam-schedules", methods=["GET"])
def get_exam_schedules():
    exam_schedules = ExamSchedule.query.all()
    return jsonify([{"id": es.id, "exam_name": es.exam_name, "exam_date": es.exam_date, "exam_time": es.exam_time} for es in exam_schedules])

@app.route("/results", methods=["GET"])
def get_results():
    results = Result.query.join(Student).join(ExamSchedule).all()
    return jsonify([{"student_id": r.student_id, "exam_name": es.exam_name, "score": r.score} for r, es in results])

@app.route("/results", methods=["POST"])
def create_result():
    data = request.get_json()
    result = Result(student_id=data["student_id"], exam_id=data["exam_id"], score=data["score"])
    db.session.add(result)
    db.session.commit()
    return jsonify({"message": "Result created successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
```

**Frontend (HTML, CSS, JavaScript)**
------------------------------------

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pomra Jameul Ulum Fazil Madrasha Portal</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Pomra Jameul Ulum Fazil Madrasha Portal</h1>
    </header>
    <main>
        <section id="notices">
            <h2>Notices</h2>
            <ul id="notices-list"></ul>
        </section>
        <section id="exam-schedules">
            <h2>Exam Schedules</h2>
            <ul id="exam-schedules-list"></ul>
        </section>
        <section id="results">
            <h2>Results</h2>
            <table id="results-table">
                <thead>
                    <tr>
                        <th>Student ID</th>
                        <th>Exam Name</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody id="results-table-body"></tbody>
            </table>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

#notices-list, #exam-schedules-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

#notices-list li, #exam-schedules-list li {
    padding: 0.5em;
    border-bottom: 1px solid #ccc;
}

#notices-list li:last-child, #exam-schedules-list li:last-child {
    border-bottom: none;
}

#results-table {
    border-collapse: collapse;
    width: 100%;
}

#results-table th, #results-table td {
    border: 1px solid #ddd;
    padding: 0.5em;
}

#results-table th {
    background-color: #f0f0f0;
}
```

```javascript
// script.js
fetch("/notices")
    .then(response => response.json())
    .then(notices => {
        const noticesList = document.getElementById("notices-list");
        notices.forEach(notice => {
            const li = document.createElement("li");
            li.textContent = `${notice.title} - ${notice.created_at}`;
            noticesList.appendChild(li);
        });
    })
    .catch(error => console.error(error));

fetch("/exam-schedules")
    .then(response => response.json())
    .then(examSchedules => {
        const examSchedulesList = document.getElementById("exam-schedules-list");
        examSchedules.forEach(examSchedule => {
            const li = document.createElement("li");
            li.textContent = `${examSchedule.exam_name} - ${examSchedule.exam_date} ${examSchedule.exam_time}`;
            examSchedulesList.appendChild(li);
        });
    })
    .catch(error => console.error(error));

fetch("/results")
    .then(response => response.json())
    .then(results => {
        const resultsTableBody = document.getElementById("results-table-body");
        results.forEach(result => {
            const row = document.createElement("tr");
            const studentIdCell = document.createElement("td");
            studentIdCell.textContent = result.student_id;
            const examNameCell = document.createElement("td");
            examNameCell.textContent = result.exam_name;
            const scoreCell = document.createElement("td");
            scoreCell.textContent = result.score;
            row.appendChild(studentIdCell);
            row.appendChild(examNameCell);
            row.appendChild(scoreCell);
            resultsTableBody.appendChild(row);
        });
    })
    .catch(error => console.error(error));
```
