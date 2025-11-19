"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Develop a web application to track the progress of CSR initiatives, such as AIDA's SBI Clinic on Wheels and Swabalambam Silai School, with real-time updates and reports.
Generated: DETERMINISTIC_15215e2cb93c1d27
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**CSR Initiatives Tracker**
==========================

**Backend (Python, Flask, SQLAlchemy)**
--------------------------------------

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///csr_initiatives.db"
db = SQLAlchemy(app)


class Initiative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    progress = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"Initiative('{self.name}', '{self.description}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "progress": self.progress,
        }


class Update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    initiative_id = db.Column(db.Integer, db.ForeignKey("initiative.id"), nullable=False)
    initiative = db.relationship("Initiative", backref=db.backref("updates", lazy=True))
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    progress = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Update('{self.initiative.name}', '{self.description}')"

    def to_dict(self):
        return {
            "id": self.id,
            "initiative_id": self.initiative_id,
            "update_date": self.update_date.isoformat(),
            "description": self.description,
            "progress": self.progress,
        }


@app.route("/initiatives", methods=["GET"])
def get_initiatives():
    initiatives = Initiative.query.all()
    return jsonify([i.to_dict() for i in initiatives])


@app.route("/initiatives", methods=["POST"])
def create_initiative():
    try:
        data = request.get_json()
        initiative = Initiative(name=data["name"], description=data["description"])
        db.session.add(initiative)
        db.session.commit()
        return jsonify(initiative.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@app.route("/initiatives/<int:initiative_id>/updates", methods=["GET"])
def get_updates(initiative_id):
    updates = Update.query.filter_by(initiative_id=initiative_id).all()
    return jsonify([u.to_dict() for u in updates])


@app.route("/initiatives/<int:initiative_id>/updates", methods=["POST"])
def create_update(initiative_id):
    try:
        initiative = Initiative.query.get(initiative_id)
        if not initiative:
            return jsonify({"error": "Initiative not found"}), 404
        data = request.get_json()
        update = Update(
            initiative_id=initiative_id,
            description=data["description"],
            progress=data["progress"],
        )
        db.session.add(update)
        initiative.progress = data["progress"]
        db.session.commit()
        return jsonify(update.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
```

**Frontend (JavaScript, HTML, CSS)**
-----------------------------------

```javascript
// script.js

const initiativesContainer = document.getElementById("initiatives");
const updatesContainer = document.getElementById("updates");

fetch("/initiatives")
  .then(response => response.json())
  .then(initiatives => {
    initiatives.forEach(initiative => {
      const initiativeHTML = `
        <div>
          <h2>${initiative.name}</h2>
          <p>${initiative.description}</p>
          <p>Progress: ${initiative.progress}%</p>
          <button class="view-updates" data-initiative-id="${initiative.id}">View Updates</button>
        </div>
      `;
      initiativesContainer.insertAdjacentHTML("beforeend", initiativeHTML);
    });

    const viewUpdateButtons = document.querySelectorAll(".view-updates");
    viewUpdateButtons.forEach(button => {
      button.addEventListener("click", () => {
        const initiativeId = button.dataset.initiativeId;
        fetch(`/initiatives/${initiativeId}/updates`)
          .then(response => response.json())
          .then(updates => {
            updatesContainer.innerHTML = "";
            updates.forEach(update => {
              const updateHTML = `
                <div>
                  <p>${update.description}</p>
                  <p>Progress: ${update.progress}%</p>
                  <p>Update Date: ${update.update_date}</p>
                </div>
              `;
              updatesContainer.insertAdjacentHTML("beforeend", updateHTML);
            });
          });
      });
    });
  });

document.getElementById("create-initiative-form").addEventListener("submit", event => {
  event.preventDefault();
  const name = document.getElementById("name").value;
  const description = document.getElementById("description").value;
  fetch("/initiatives", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, description }),
  })
    .then(response => response.json())
    .then(initiative => {
      console.log(initiative);
    });
});

document.getElementById("create-update-form").addEventListener("submit", event => {
  event.preventDefault();
  const initiativeId = document.getElementById("initiative-id").value;
  const description = document.getElementById("update-description").value;
  const progress = document.getElementById("update-progress").value;
  fetch(`/initiatives/${initiativeId}/updates`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ description, progress }),
  })
    .then(response => response.json())
    .then(update => {
      console.log(update);
    });
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSR Initiatives Tracker</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>CSR Initiatives Tracker</h1>
  <section id="initiatives"></section>
  <section id="updates"></section>

  <form id="create-initiative-form">
    <label for="name">Name:</label>
    <input type="text" id="name" required>
    <label for="description">Description:</label>
    <textarea id="description" required></textarea>
    <button type="submit">Create Initiative</button>
  </form>

  <form id="create-update-form">
    <label for="initiative-id">Initiative ID:</label>
    <input type="number" id="initiative-id" required>
    <label for="update-description">Description:</label>
    <textarea id="update-description" required></textarea>
    <label for="update-progress">Progress:</label>
    <input type="number" id="update-progress" required>
    <button type="submit">Create Update</button>
  </form>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
  font-family: Arial, sans-serif;
}

#initiatives {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

#updates {
  margin-top: 20px;
}

button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
```
