"""
Generated Code Metadata:
========================
Original URL: https://armaghanenajaf.org
Prompt: Illustrate how to use the Armaghan-e-Najaf database to track the progress of educational programs for orphans in a web application.
Generated: DETERMINISTIC_b3e8384af7cef482
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Armaghan-e-Najaf Database Web Application**
=====================================================

**Database Schema**
------------------

```sql
CREATE TABLE Orphan (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    program_id INT,
    FOREIGN KEY (program_id) REFERENCES EducationalProgram(id)
);

CREATE TABLE EducationalProgram (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE ProgramProgress (
    id INT PRIMARY KEY,
    orphan_id INT NOT NULL,
    program_id INT NOT NULL,
    progress_date DATE NOT NULL,
    progress_description TEXT,
    FOREIGN KEY (orphan_id) REFERENCES Orphan(id),
    FOREIGN KEY (program_id) REFERENCES EducationalProgram(id)
);
```

**Backend API (Python with Flask and SQLAlchemy)**
------------------------------------------------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///armaghan_e_najaf.db"
db = SQLAlchemy(app)


class Orphan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey("educational_program.id"))

    def __repr__(self):
        return f"Orphan('{self.name}', '{self.age}')"


class EducationalProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"EducationalProgram('{self.name}', '{self.start_date}', '{self.end_date}')"


class ProgramProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orphan_id = db.Column(db.Integer, db.ForeignKey("orphan.id"), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey("educational_program.id"), nullable=False)
    progress_date = db.Column(db.Date, nullable=False)
    progress_description = db.Column(db.Text)

    def __repr__(self):
        return f"ProgramProgress('{self.progress_date}', '{self.progress_description}')"


@app.route("/orphans", methods=["GET", "POST"])
def orphans():
    if request.method == "GET":
        orphans = Orphan.query.all()
        return jsonify([{"id": o.id, "name": o.name, "age": o.age} for o in orphans])
    elif request.method == "POST":
        data = request.get_json()
        new_orphan = Orphan(name=data["name"], age=data["age"], program_id=data["program_id"])
        db.session.add(new_orphan)
        db.session.commit()
        return jsonify({"id": new_orphan.id, "name": new_orphan.name, "age": new_orphan.age}), 201


@app.route("/programs", methods=["GET", "POST"])
def programs():
    if request.method == "GET":
        programs = EducationalProgram.query.all()
        return jsonify([{"id": p.id, "name": p.name, "start_date": p.start_date, "end_date": p.end_date} for p in programs])
    elif request.method == "POST":
        data = request.get_json()
        new_program = EducationalProgram(name=data["name"], description=data["description"], start_date=datetime.strptime(data["start_date"], "%Y-%m-%d").date(), end_date=datetime.strptime(data["end_date"], "%Y-%m-%d").date())
        db.session.add(new_program)
        db.session.commit()
        return jsonify({"id": new_program.id, "name": new_program.name, "start_date": new_program.start_date, "end_date": new_program.end_date}), 201


@app.route("/progress", methods=["GET", "POST"])
def progress():
    if request.method == "GET":
        progress = ProgramProgress.query.all()
        return jsonify([{"id": p.id, "orphan_id": p.orphan_id, "program_id": p.program_id, "progress_date": p.progress_date, "progress_description": p.progress_description} for p in progress])
    elif request.method == "POST":
        data = request.get_json()
        new_progress = ProgramProgress(orphan_id=data["orphan_id"], program_id=data["program_id"], progress_date=datetime.strptime(data["progress_date"], "%Y-%m-%d").date(), progress_description=data["progress_description"])
        db.session.add(new_progress)
        db.session.commit()
        return jsonify({"id": new_progress.id, "orphan_id": new_progress.orphan_id, "program_id": new_progress.program_id, "progress_date": new_progress.progress_date, "progress_description": new_progress.progress_description}), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Frontend (JavaScript with HTML and CSS)**
-----------------------------------------

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Armaghan-e-Najaf Database</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Armaghan-e-Najaf Database</h1>
    <section id="orphans">
        <h2>Orphans</h2>
        <ul id="orphan-list"></ul>
        <form id="add-orphan-form">
            <input type="text" id="name" placeholder="Name">
            <input type="number" id="age" placeholder="Age">
            <input type="number" id="program-id" placeholder="Program ID">
            <button id="add-orphan-btn">Add Orphan</button>
        </form>
    </section>
    <section id="programs">
        <h2>Programs</h2>
        <ul id="program-list"></ul>
        <form id="add-program-form">
            <input type="text" id="program-name" placeholder="Name">
            <input type="text" id="program-description" placeholder="Description">
            <input type="date" id="start-date" placeholder="Start Date">
            <input type="date" id="end-date" placeholder="End Date">
            <button id="add-program-btn">Add Program</button>
        </form>
    </section>
    <section id="progress">
        <h2>Progress</h2>
        <ul id="progress-list"></ul>
        <form id="add-progress-form">
            <input type="number" id="orphan-id" placeholder="Orphan ID">
            <input type="number" id="program-id-progress" placeholder="Program ID">
            <input type="date" id="progress-date" placeholder="Progress Date">
            <input type="text" id="progress-description" placeholder="Progress Description">
            <button id="add-progress-btn">Add Progress</button>
        </form>
    </section>

    <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js

fetch("/orphans")
    .then(response => response.json())
    .then(data => {
        const orphanList = document.getElementById("orphan-list");
        data.forEach(orphan => {
            const listItem = document.createElement("li");
            listItem.textContent = `${orphan.name} (${orphan.age})`;
            orphanList.appendChild(listItem);
        });
    });

document.getElementById("add-orphan-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const programId = document.getElementById("program-id").value;
    fetch("/orphans", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, age, program_id: programId }),
    })
        .then(response => response.json())
        .then(data => {
            const orphanList = document.getElementById("orphan-list");
            const listItem = document.createElement("li");
            listItem.textContent = `${data.name} (${data.age})`;
            orphanList.appendChild(listItem);
        });
});

fetch("/programs")
    .then(response => response.json())
    .then(data => {
        const programList = document.getElementById("program-list");
        data.forEach(program => {
            const listItem = document.createElement("li");
            listItem.textContent = `${program.name} (${program.start_date} - ${program.end_date})`;
            programList.appendChild(listItem);
        });
    });

document.getElementById("add-program-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("program-name").value;
    const description = document.getElementById("program-description").value;
    const
