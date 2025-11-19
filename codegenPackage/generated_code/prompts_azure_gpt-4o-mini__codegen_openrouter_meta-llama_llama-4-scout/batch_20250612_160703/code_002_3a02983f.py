"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: Can you provide a code example for a web application that tracks and showcases revitalization projects in small municipalities, inspired by the initiatives from the Starke Orte Netzwerk?
Generated: DETERMINISTIC_3a02983f09de934a
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Revitalization Project Tracker**
=====================================

**Database Schema**
------------------

```sql
CREATE TABLE municipalities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  location VARCHAR(255) NOT NULL
);

CREATE TABLE projects (
  id SERIAL PRIMARY KEY,
  municipality_id INTEGER NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  status VARCHAR(50) NOT NULL CHECK (status IN ('planned', 'in_progress', 'completed')),
  FOREIGN KEY (municipality_id) REFERENCES municipalities(id)
);

CREATE TABLE project_images (
  id SERIAL PRIMARY KEY,
  project_id INTEGER NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  FOREIGN KEY (project_id) REFERENCES projects(id)
);
```

**Backend API (Node.js, Express)**
------------------------------------

```javascript
// server.js
const express = require('express');
const { Pool } = require('pg');
const app = express();
const port = 3000;

// Database connection
const pool = new Pool({
  user: 'your_username',
  host: 'your_host',
  database: 'your_database',
  password: 'your_password',
  port: 5432,
});

// Middleware
app.use(express.json());

// Get all municipalities
app.get('/municipalities', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM municipalities');
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching municipalities' });
  }
});

// Get all projects for a municipality
app.get('/municipalities/:id/projects', async (req, res) => {
  try {
    const municipalityId = req.params.id;
    const result = await pool.query(`SELECT * FROM projects WHERE municipality_id = $1`, [municipalityId]);
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching projects' });
  }
});

// Create a new project
app.post('/municipalities/:id/projects', async (req, res) => {
  try {
    const municipalityId = req.params.id;
    const { name, description, start_date, end_date, status } = req.body;
    const result = await pool.query(`
      INSERT INTO projects (municipality_id, name, description, start_date, end_date, status)
      VALUES ($1, $2, $3, $4, $5, $6)
      RETURNING *
    `, [municipalityId, name, description, start_date, end_date, status]);
    res.json(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error creating project' });
  }
});

// Update a project
app.put('/projects/:id', async (req, res) => {
  try {
    const projectId = req.params.id;
    const { name, description, start_date, end_date, status } = req.body;
    const result = await pool.query(`
      UPDATE projects
      SET name = $1, description = $2, start_date = $3, end_date = $4, status = $5
      WHERE id = $6
      RETURNING *
    `, [name, description, start_date, end_date, status, projectId]);
    res.json(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error updating project' });
  }
});

// Delete a project
app.delete('/projects/:id', async (req, res) => {
  try {
    const projectId = req.params.id;
    await pool.query(`DELETE FROM projects WHERE id = $1`, [projectId]);
    res.json({ message: 'Project deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error deleting project' });
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**Frontend (React)**
---------------------

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [municipalities, setMunicipalities] = useState([]);
  const [projects, setProjects] = useState({});
  const [selectedMunicipality, setSelectedMunicipality] = useState(null);

  useEffect(() => {
    axios.get('/municipalities')
      .then(response => {
        setMunicipalities(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleMunicipalitySelect = (municipality) => {
    setSelectedMunicipality(municipality);
    axios.get(`/municipalities/${municipality.id}/projects`)
      .then(response => {
        setProjects({ ...projects, [municipality.id]: response.data });
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Revitalization Project Tracker</h1>
      <ul>
        {municipalities.map(municipality => (
          <li key={municipality.id}>
            <button onClick={() => handleMunicipalitySelect(municipality)}>
              {municipality.name}
            </button>
          </li>
        ))}
      </ul>
      {selectedMunicipality && (
        <div>
          <h2>Projects in {selectedMunicipality.name}</h2>
          <ul>
            {projects[selectedMunicipality.id] && projects[selectedMunicipality.id].map(project => (
              <li key={project.id}>
                <h3>{project.name}</h3>
                <p>{project.description}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
```

**package.json**
-----------------

```json
{
  "name": "revitalization-project-tracker",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js",
    "start:frontend": "npm start --prefix frontend"
  },
  "dependencies": {
    "express": "^4.17.1",
    "pg": "^8.7.3",
    "react": "^17.0.2",
    "axios": "^0.21.1"
  }
}
```

**frontend/package.json**
---------------------------

```json
{
  "name": "revitalization-project-tracker-frontend",
  "version": "1.0.0",
  "scripts": {
    "start": "react-scripts start"
  },
  "dependencies": {
    "@testing-library/jest-dom": "^5.14.1",
    "@testing-library/react": "^11.2.5",
    "@testing-library/user-event": "^13.5.0",
    "react-scripts": "4.0.3",
    "web-vitals": "^1.1.2"
  }
}
```
