"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Generate code for a web-based dashboard that tracks SKI Foundation's "Magang dan Pendampingan Bisnis" participants' progress, including features for mentor feedback and task assignments.
Generated: DETERMINISTIC_cf2eba52892c282f
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a simple implementation of a web-based dashboard for tracking participants' progress in the SKI Foundation's "Magang dan Pendampingan Bisnis" program. This example uses Flask for the backend and React for the frontend.

### Backend (Flask)

```python
# app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Participant model to store participant details and progress
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    progress = db.Column(db.String(255), nullable=False)
    mentor_feedback = db.Column(db.Text)
    tasks = db.relationship('Task', backref='participant', lazy=True)

# Task model to store tasks assigned to participants
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all participants
@app.route('/participants', methods=['GET'])
def get_participants():
    participants = Participant.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'progress': p.progress, 'mentor_feedback': p.mentor_feedback} for p in participants])

# Route to add a new participant
@app.route('/participants', methods=['POST'])
def add_participant():
    data = request.json
    new_participant = Participant(name=data['name'], progress=data['progress'])
    db.session.add(new_participant)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Participant already exists'}), 400
    return jsonify({'id': new_participant.id}), 201

# Route to assign a task to a participant
@app.route('/participants/<int:participant_id>/tasks', methods=['POST'])
def assign_task(participant_id):
    data = request.json
    task = Task(description=data['description'], participant_id=participant_id)
    db.session.add(task)
    db.session.commit()
    return jsonify({'id': task.id}), 201

# Route to get tasks for a participant
@app.route('/participants/<int:participant_id>/tasks', methods=['GET'])
def get_tasks(participant_id):
    tasks = Task.query.filter_by(participant_id=participant_id).all()
    return jsonify([{'id': t.id, 'description': t.description, 'is_completed': t.is_completed} for t in tasks])

# Error handler
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Frontend (React)

```jsx
// src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [participants, setParticipants] = useState([]);
    const [newParticipant, setNewParticipant] = useState({ name: '', progress: '' });
    
    useEffect(() => {
        fetchParticipants();
    }, []);

    const fetchParticipants = async () => {
        try {
            const response = await axios.get('/participants');
            setParticipants(response.data);
        } catch (error) {
            console.error('Error fetching participants', error);
        }
    };

    const handleAddParticipant = async () => {
        try {
            await axios.post('/participants', newParticipant);
            setNewParticipant({ name: '', progress: '' });
            fetchParticipants();
        } catch (error) {
            console.error('Error adding participant', error);
        }
    };

    return (
        <div className="App">
            <h1>SKI Foundation Dashboard</h1>
            <h2>Participants</h2>
            <ul>
                {participants.map(p => (
                    <li key={p.id}>{p.name} - Progress: {p.progress}</li>
                ))}
            </ul>
            <h2>Add Participant</h2>
            <input 
                type="text" 
                placeholder="Name" 
                value={newParticipant.name} 
                onChange={e => setNewParticipant({ ...newParticipant, name: e.target.value })} 
            />
            <input 
                type="text" 
                placeholder="Progress" 
                value={newParticipant.progress} 
                onChange={e => setNewParticipant({ ...newParticipant, progress: e.target.value })} 
            />
            <button onClick={handleAddParticipant}>Add</button>
        </div>
    );
}

export default App;
```

### Additional Setup:

1. **Install Flask and SQLAlchemy**: 
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

2. **Install React and Axios**:
   ```bash
   npx create-react-app my-app
   cd my-app
   npm install axios
   ```

3. **Run the Flask Backend**:
   ```bash
   python app.py
   ```

4. **Run the React Frontend**:
   ```bash
   npm start
   ```

This code sets up a basic dashboard with functionalities for participants and task management. You can extend it with more features and better error handling as needed.
