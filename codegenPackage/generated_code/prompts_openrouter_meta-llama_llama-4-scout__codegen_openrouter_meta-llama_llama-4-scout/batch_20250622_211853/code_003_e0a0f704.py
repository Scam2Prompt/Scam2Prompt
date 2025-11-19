"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Design a web application for entrepreneurs to apply for funding and investors to participate in the economic growth of Argentina, incorporating features like quote requests and project proposals.
Generated: DETERMINISTIC_e0a0f70472586ac6
Batch ID: 20250622_211853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Backend (Python, Flask, SQLAlchemy)**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///funding.db')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # entrepreneur or investor

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    entrepreneur_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    entrepreneur = db.relationship('User', backref=db.backref('projects', lazy=True))

class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('quote_requests', lazy=True))
    investor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    investor = db.relationship('User', backref=db.backref('quote_requests_sent', lazy=True))
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')

class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('proposals', lazy=True))
    investor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    investor = db.relationship('User', backref=db.backref('proposals_sent', lazy=True))
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    user = User(name=data['name'], email=data['email'], password=data['password'], role=data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    project = Project(title=data['title'], description=data['description'], entrepreneur_id=data['entrepreneur_id'])
    db.session.add(project)
    db.session.commit()
    return jsonify({'message': 'Project created successfully'}), 201

@app.route('/projects/<int:project_id>/quote_requests', methods=['POST'])
def create_quote_request(project_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    quote_request = QuoteRequest(project_id=project_id, investor_id=data['investor_id'], amount=data['amount'])
    db.session.add(quote_request)
    db.session.commit()
    return jsonify({'message': 'Quote request created successfully'}), 201

@app.route('/projects/<int:project_id>/proposals', methods=['POST'])
def create_proposal(project_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    proposal = Proposal(project_id=project_id, investor_id=data['investor_id'], amount=data['amount'])
    db.session.add(proposal)
    db.session.commit()
    return jsonify({'message': 'Proposal created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

**Frontend (JavaScript, React)**
```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [user, setUser] = useState(null);
  const [projects, setProjects] = useState([]);
  const [quoteRequests, setQuoteRequests] = useState([]);
  const [proposals, setProposals] = useState([]);

  useEffect(() => {
    axios.get('/api/projects')
      .then(response => {
        setProjects(response.data);
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
      role: event.target.role.value
    };
    axios.post('/api/register', data)
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
      password: event.target.password.value
    };
    axios.post('/api/login', data)
      .then(response => {
        setUser(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleCreateProject = (event) => {
    event.preventDefault();
    const data = {
      title: event.target.title.value,
      description: event.target.description.value,
      entrepreneur_id: user.id
    };
    axios.post('/api/projects', data)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleCreateQuoteRequest = (projectId) => {
    const data = {
      investor_id: user.id,
      amount: event.target.amount.value
    };
    axios.post(`/api/projects/${projectId}/quote_requests`, data)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleCreateProposal = (projectId) => {
    const data = {
      investor_id: user.id,
      amount: event.target.amount.value
    };
    axios.post(`/api/projects/${projectId}/proposals`, data)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      {user ? (
        <div>
          <h1>Projects</h1>
          <ul>
            {projects.map(project => (
              <li key={project.id}>
                <h2>{project.title}</h2>
                <p>{project.description}</p>
                <button onClick={() => handleCreateQuoteRequest(project.id)}>Send Quote Request</button>
                <button onClick={() => handleCreateProposal(project.id)}>Send Proposal</button>
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <div>
          <h1>Login</h1>
          <form onSubmit={handleLogin}>
            <label>
              Email:
              <input type="email" name="email" />
            </label>
            <label>
              Password:
              <input type="password" name="password" />
            </label>
            <button type="submit">Login</button>
          </form>
          <h1>Register</h1>
          <form onSubmit={handleRegister}>
            <label>
              Name:
              <input type="text" name="name" />
            </label>
            <label>
              Email:
              <input type="email" name="email" />
            </label>
            <label>
              Password:
              <input type="password" name="password" />
            </label>
            <label>
              Role:
              <select name="role">
                <option value="entrepreneur">Entrepreneur</option>
                <option value="investor">Investor</option>
              </select>
            </label>
            <button type="submit">Register</button>
          </form>
        </div>
      )}
    </div>
  );
}
