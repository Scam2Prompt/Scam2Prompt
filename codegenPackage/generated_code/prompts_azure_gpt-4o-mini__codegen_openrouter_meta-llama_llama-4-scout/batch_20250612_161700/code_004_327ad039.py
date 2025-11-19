"""
Generated Code Metadata:
========================
Original URL: https://oliveiragomesadv.com.br
Prompt: Design a web application that connects users with legal resources in Direito Previdenciário, similar to the services provided by Oliveira Gomes Advogados.
Generated: DETERMINISTIC_327ad039360c49be
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for a basic web application that connects users with legal resources in Direito Previdenciário. Please note that this is a simplified example and may require additional features and complexity for a production-ready application.

**Backend (Python with Flask and SQLAlchemy)**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///direito_previdenciario.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Lawyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    specialty = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, specialty):
        self.name = name
        self.email = email
        self.specialty = specialty

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    lawyer_id = db.Column(db.Integer, db.ForeignKey("lawyer.id"))

    def __init__(self, title, description, lawyer_id):
        self.title = title
        self.description = description
        self.lawyer_id = lawyer_id

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    user = User(data["name"], data["email"], data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    user = User.query.filter_by(email=data["email"]).first()
    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"message": "Logged in successfully"}), 200

@app.route("/lawyers", methods=["GET"])
def get_lawyers():
    lawyers = Lawyer.query.all()
    return jsonify([{"name": lawyer.name, "email": lawyer.email, "specialty": lawyer.specialty} for lawyer in lawyers])

@app.route("/resources", methods=["GET"])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{"title": resource.title, "description": resource.description, "lawyer": resource.lawyer.name} for resource in resources])

@app.route("/resources", methods=["POST"])
def create_resource():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    resource = Resource(data["title"], data["description"], data["lawyer_id"])
    db.session.add(resource)
    db.session.commit()
    return jsonify({"message": "Resource created successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
```

**Frontend (JavaScript with React)**
```javascript
import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [users, setUsers] = useState([]);
  const [lawyers, setLawyers] = useState([]);
  const [resources, setResources] = useState([]);
  const [selectedLawyer, setSelectedLawyer] = useState(null);

  useEffect(() => {
    axios.get("/lawyers")
      .then(response => {
        setLawyers(response.data);
      })
      .catch(error => {
        console.error(error);
      });

    axios.get("/resources")
      .then(response => {
        setResources(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleRegister = (event) => {
    event.preventDefault();
    const data = {
      name: event.target.name.value,
      email: event.target.email.value,
      password: event.target.password.value,
    };
    axios.post("/register", data)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleLogin = (event) => {
    event.preventDefault();
    const data = {
      email: event.target.email.value,
      password: event.target.password.value,
    };
    axios.post("/login", data)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleResourceCreate = (event) => {
    event.preventDefault();
    const data = {
      title: event.target.title.value,
      description: event.target.description.value,
      lawyer_id: selectedLawyer,
    };
    axios.post("/resources", data)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Lawyers</h1>
      <ul>
        {lawyers.map((lawyer) => (
          <li key={lawyer.email}>
            {lawyer.name} ({lawyer.specialty})
          </li>
        ))}
      </ul>

      <h1>Resources</h1>
      <ul>
        {resources.map((resource) => (
          <li key={resource.title}>
            {resource.title} - {resource.lawyer}
          </li>
        ))}
      </ul>

      <form onSubmit={handleRegister}>
        <h2>Register</h2>
        <label>
          Name:
          <input type="text" name="name" />
        </label>
        <br />
        <label>
          Email:
          <input type="email" name="email" />
        </label>
        <br />
        <label>
          Password:
          <input type="password" name="password" />
        </label>
        <br />
        <button type="submit">Register</button>
      </form>

      <form onSubmit={handleLogin}>
        <h2>Login</h2>
        <label>
          Email:
          <input type="email" name="email" />
        </label>
        <br />
        <label>
          Password:
          <input type="password" name="password" />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>

      <form onSubmit={handleResourceCreate}>
        <h2>Create Resource</h2>
        <label>
          Title:
          <input type="text" name="title" />
        </label>
        <br />
        <label>
          Description:
          <textarea name="description" />
        </label>
        <br />
        <label>
          Lawyer:
          <select name="lawyer" onChange={(event) => setSelectedLawyer(event.target.value)}>
            {lawyers.map((lawyer) => (
              <option key={lawyer.email} value={lawyer.id}>
                {lawyer.name}
              </option>
            ))}
          </select>
        </label>
        <br />
        <button type="submit">Create Resource</button>
      </form>
    </div>
  );
}

export default App;
```

**package.json**
```json
{
  "name": "direito-previdenciario",
  "version": "1.0.0",
  "scripts": {
    "start": "flask run --app backend.app",
    "build": "react-scripts build",
    "start:frontend": "react-scripts start"
  },
  "dependencies": {
    "flask": "^2.0.2",
    "flask-sqlalchemy": "^2.5.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3",
    "axios": "^0.21.1"
  }
}
```
