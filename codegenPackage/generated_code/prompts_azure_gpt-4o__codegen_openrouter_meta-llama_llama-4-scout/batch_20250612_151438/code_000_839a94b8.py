"""
Generated Code Metadata:
========================
Original URL: https://oppomobile.id
Prompt: Write code to set up a basic system architecture for a software development project, including database integration and API endpoints, suitable for a newly created site like the one at oppomobile.id.
Generated: DETERMINISTIC_839a94b8a04c4adf
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**System Architecture for Software Development Project**
===========================================================

**Database Schema**
------------------

```sql
-- schema.sql

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  project_id INTEGER NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(50) NOT NULL DEFAULT 'open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (project_id) REFERENCES projects(id)
);
```

**Backend API (Node.js and Express)**
--------------------------------------

```javascript
// server.js

const express = require('express');
const app = express();
const { Pool } = require('pg');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Database connection
const db = new Pool({
  user: 'your_username',
  host: 'your_host',
  database: 'your_database',
  password: 'your_password',
  port: 5432,
});

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// API Endpoints

// User Registration
app.post('/api/register', async (req, res) => {
  try {
    const { name, email, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const result = await db.query(
      'INSERT INTO users (name, email, password) VALUES ($1, $2, $3) RETURNING *',
      [name, email, hashedPassword]
    );
    res.json(result.rows[0]);
  } catch (error) {
    res.status(500).json({ message: 'Error registering user' });
  }
});

// User Login
app.post('/api/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const result = await db.query('SELECT * FROM users WHERE email = $1', [email]);
    if (!result.rows[0]) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
    const isValidPassword = await bcrypt.compare(password, result.rows[0].password);
    if (!isValidPassword) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
    const token = jwt.sign({ userId: result.rows[0].id }, 'your_secret_key', {
      expiresIn: '1h',
    });
    res.json({ token });
  } catch (error) {
    res.status(500).json({ message: 'Error logging in' });
  }
});

// Create Project
app.post('/api/projects', authenticateToken, async (req, res) => {
  try {
    const { title, description } = req.body;
    const result = await db.query(
      'INSERT INTO projects (title, description) VALUES ($1, $2) RETURNING *',
      [title, description]
    );
    res.json(result.rows[0]);
  } catch (error) {
    res.status(500).json({ message: 'Error creating project' });
  }
});

// Create Task
app.post('/api/tasks', authenticateToken, async (req, res) => {
  try {
    const { projectId, title, description } = req.body;
    const result = await db.query(
      'INSERT INTO tasks (project_id, title, description) VALUES ($1, $2, $3) RETURNING *',
      [projectId, title, description]
    );
    res.json(result.rows[0]);
  } catch (error) {
    res.status(500).json({ message: 'Error creating task' });
  }
});

// Authenticate Token Middleware
function authenticateToken(req, res, next) {
  const token = req.header('x-access-token');
  if (!token) return res.status(403).json({ message: 'No token provided' });
  jwt.verify(token, 'your_secret_key', (err, decoded) => {
    if (err) return res.status(401).json({ message: 'Invalid token' });
    req.userId = decoded.userId;
    next();
  });
}

const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**Frontend (React)**
--------------------

```javascript
// App.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [projects, setProjects] = useState([]);
  const [tasks, setTasks] = useState([]);
  const [token, setToken] = useState('');

  useEffect(() => {
    axios.get('/api/projects')
      .then(response => {
        setProjects(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleCreateProject = async (event) => {
    event.preventDefault();
    const { title, description } = event.target.elements;
    try {
      const response = await axios.post('/api/projects', {
        title: title.value,
        description: description.value,
      }, {
        headers: {
          'x-access-token': token,
        },
      });
      setProjects([...projects, response.data]);
    } catch (error) {
      console.error(error);
    }
  };

  const handleCreateTask = async (event) => {
    event.preventDefault();
    const { projectId, title, description } = event.target.elements;
    try {
      const response = await axios.post('/api/tasks', {
        projectId: projectId.value,
        title: title.value,
        description: description.value,
      }, {
        headers: {
          'x-access-token': token,
        },
      });
      setTasks([...tasks, response.data]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Projects</h1>
      <ul>
        {projects.map((project) => (
          <li key={project.id}>{project.title}</li>
        ))}
      </ul>
      <form onSubmit={handleCreateProject}>
        <input type="text" name="title" placeholder="Title" />
        <input type="text" name="description" placeholder="Description" />
        <button type="submit">Create Project</button>
      </form>
      <h1>Tasks</h1>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>{task.title}</li>
        ))}
      </ul>
      <form onSubmit={handleCreateTask}>
        <input type="text" name="projectId" placeholder="Project ID" />
        <input type="text" name="title" placeholder="Title" />
        <input type="text" name="description" placeholder="Description" />
        <button type="submit">Create Task</button>
      </form>
    </div>
  );
}

export default App;
```
