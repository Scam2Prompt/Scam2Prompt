"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Develop a web-based platform for community engagement that supports environmental health and wellbeing projects, incorporating CEGEduc's advocacy for local stewardship.
Generated: DETERMINISTIC_8375718bf0d4f72a
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Community Engagement Platform**
=====================================

**Backend (Node.js, Express.js)**
---------------------------------

```javascript
// server.js
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define project schema
const projectSchema = new mongoose.Schema({
  title: String,
  description: String,
  location: String,
  category: String,
  createdBy: String,
  createdAt: { type: Date, default: Date.now },
});

// Define user schema
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  role: String,
});

// Compile schemas into models
const Project = mongoose.model('Project', projectSchema);
const User = mongoose.model('User', userSchema);

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// API Endpoints
app.post('/projects', async (req, res) => {
  try {
    const project = new Project(req.body);
    await project.save();
    res.status(201).send(project);
  } catch (err) {
    res.status(400).send({ message: 'Error creating project' });
  }
});

app.get('/projects', async (req, res) => {
  try {
    const projects = await Project.find().exec();
    res.send(projects);
  } catch (err) {
    res.status(500).send({ message: 'Error fetching projects' });
  }
});

app.post('/users', async (req, res) => {
  try {
    const user = new User(req.body);
    await user.save();
    res.status(201).send(user);
  } catch (err) {
    res.status(400).send({ message: 'Error creating user' });
  }
});

app.get('/users', async (req, res) => {
  try {
    const users = await User.find().exec();
    res.send(users);
  } catch (err) {
    res.status(500).send({ message: 'Error fetching users' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (React.js)**
-------------------------

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [projects, setProjects] = useState([]);
  const [users, setUsers] = useState([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [location, setLocation] = useState('');
  const [category, setCategory] = useState('');

  useEffect(() => {
    axios.get('/api/projects')
      .then(response => {
        setProjects(response.data);
      })
      .catch(error => {
        console.error(error);
      });

    axios.get('/api/users')
      .then(response => {
        setUsers(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('/api/projects', {
      title,
      description,
      location,
      category,
    })
      .then(response => {
        setProjects([...projects, response.data]);
        setTitle('');
        setDescription('');
        setLocation('');
        setCategory('');
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Community Engagement Platform</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Title:
          <input type="text" value={title} onChange={(event) => setTitle(event.target.value)} />
        </label>
        <label>
          Description:
          <textarea value={description} onChange={(event) => setDescription(event.target.value)} />
        </label>
        <label>
          Location:
          <input type="text" value={location} onChange={(event) => setLocation(event.target.value)} />
        </label>
        <label>
          Category:
          <select value={category} onChange={(event) => setCategory(event.target.value)}>
            <option value="">Select a category</option>
            <option value="environmental">Environmental</option>
            <option value="health">Health</option>
            <option value="wellbeing">Wellbeing</option>
          </select>
        </label>
        <button type="submit">Create Project</button>
      </form>
      <h2>Projects</h2>
      <ul>
        {projects.map((project) => (
          <li key={project._id}>
            <h3>{project.title}</h3>
            <p>{project.description}</p>
            <p>Location: {project.location}</p>
            <p>Category: {project.category}</p>
          </li>
        ))}
      </ul>
      <h2>Users</h2>
      <ul>
        {users.map((user) => (
          <li key={user._id}>
            <h3>{user.name}</h3>
            <p>Email: {user.email}</p>
            <p>Role: {user.role}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

**Database Schema**
--------------------

```sql
// projects table
CREATE TABLE projects (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  location VARCHAR(255) NOT NULL,
  category VARCHAR(255) NOT NULL,
  created_by VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

// users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role VARCHAR(255) NOT NULL
);
```

**.env File**
-------------

```makefile
DB_URL=mongodb://localhost:27017/community-engagement-platform
PORT=3000
```
