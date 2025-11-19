"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: What are some modern technologies that a full-stack web developer should be familiar with, and how can they be applied to a personal project like EMFresh2o Digital Resume?
Generated: DETERMINISTIC_4a0c0cf000e3ab54
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates modern technologies that a full-stack web developer can use to build a personal project like EMFresh2o Digital Resume.
The stack includes:
1. Flask (Backend Framework)
2. React (Frontend Framework)
3. SQLite (Database)
4. REST API (Communication between frontend and backend)
5. Docker (Containerization)
6. Tailwind CSS (Modern styling framework)
"""

# Backend: Flask Application
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database setup
DATABASE = 'resume.db'

def init_db():
    """Initialize the SQLite database."""
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resume (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                skills TEXT NOT NULL,
                experience TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

@app.route('/api/resume', methods=['POST'])
def add_resume():
    """API endpoint to add a new resume."""
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        skills = data.get('skills')
        experience = data.get('experience')

        if not all([name, email, skills, experience]):
            return jsonify({'error': 'All fields are required'}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO resume (name, email, skills, experience)
            VALUES (?, ?, ?, ?)
        ''', (name, email, skills, experience))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Resume added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/resume', methods=['GET'])
def get_resumes():
    """API endpoint to fetch all resumes."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM resume')
        resumes = cursor.fetchall()
        conn.close()

        resume_list = [
            {'id': row[0], 'name': row[1], 'email': row[2], 'skills': row[3], 'experience': row[4]}
            for row in resumes
        ]
        return jsonify(resume_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

# Frontend: React Application (React code is typically in a separate file, e.g., App.js)
/*
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [resumes, setResumes] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    skills: '',
    experience: ''
  });

  useEffect(() => {
    // Fetch resumes from the backend
    axios.get('/api/resume')
      .then(response => setResumes(response.data))
      .catch(error => console.error('Error fetching resumes:', error));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Submit new resume to the backend
    axios.post('/api/resume', formData)
      .then(response => {
        alert('Resume added successfully!');
        setResumes([...resumes, response.data]);
        setFormData({ name: '', email: '', skills: '', experience: '' });
      })
      .catch(error => console.error('Error adding resume:', error));
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">EMFresh2o Digital Resume</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <input
          type="text"
          placeholder="Name"
          value={formData.name}
          onChange={(e) => setFormData({ ...formData, name: e.target.value })}
          className="border p-2 mb-2 w-full"
        />
        <input
          type="email"
          placeholder="Email"
          value={formData.email}
          onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          className="border p-2 mb-2 w-full"
        />
        <textarea
          placeholder="Skills"
          value={formData.skills}
          onChange={(e) => setFormData({ ...formData, skills: e.target.value })}
          className="border p-2 mb-2 w-full"
        />
        <textarea
          placeholder="Experience"
          value={formData.experience}
          onChange={(e) => setFormData({ ...formData, experience: e.target.value })}
          className="border p-2 mb-2 w-full"
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">Add Resume</button>
      </form>
      <h2 className="text-xl font-bold mb-2">Resumes</h2>
      <ul>
        {resumes.map(resume => (
          <li key={resume.id} className="border p-2 mb-2">
            <p><strong>Name:</strong> {resume.name}</p>
            <p><strong>Email:</strong> {resume.email}</p>
            <p><strong>Skills:</strong> {resume.skills}</p>
            <p><strong>Experience:</strong> {resume.experience}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
*/

// Dockerfile for containerization
"""
# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install flask

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
"""
```
