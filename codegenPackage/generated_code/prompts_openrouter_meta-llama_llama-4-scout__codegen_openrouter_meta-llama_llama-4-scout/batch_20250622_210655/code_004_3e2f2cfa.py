"""
Generated Code Metadata:
========================
Original URL: https://wordpress.armelin.media
Prompt: Create a RESTful API using Node.js and Express.js to manage architectural project data, similar to how Études Architectural Solutions might manage their projects, and integrate it with a WordPress site.
Generated: DETERMINISTIC_3e2f2cfa9b960d90
Batch ID: 20250622_210655
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-wordpress-site.com/wp-json/wp/v2/posts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const mysql = require('mysql');
const cors = require('cors');
const axios = require('axios');

// Enable CORS
app.use(cors());

// Enable JSON parsing
app.use(express.json());

// Database connection settings
const dbHost = 'your_host';
const dbUser = 'your_user';
const dbPassword = 'your_password';
const dbName = 'your_database';

// Create database connection
const db = mysql.createConnection({
  host: dbHost,
  user: dbUser,
  password: dbPassword,
  database: dbName
});

// Connect to database
db.connect((err) => {
  if (err) {
    console.error('error connecting:', err);
    return;
  }
  console.log('connected as id ' + db.threadId);
});

// API endpoint to get all projects
app.get('/api/projects', (req, res) => {
  db.query('SELECT * FROM projects', (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error fetching projects' });
    } else {
      res.send(results);
    }
  });
});

// API endpoint to get a project by ID
app.get('/api/projects/:id', (req, res) => {
  const id = req.params.id;
  db.query('SELECT * FROM projects WHERE id = ?', [id], (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error fetching project' });
    } else if (results.length === 0) {
      res.status(404).send({ message: 'Project not found' });
    } else {
      res.send(results[0]);
    }
  });
});

// API endpoint to create a new project
app.post('/api/projects', (req, res) => {
  const { name, description, status } = req.body;
  if (!name || !description || !status) {
    res.status(400).send({ message: 'Please provide all required fields' });
  } else {
    db.query('INSERT INTO projects SET ?', { name, description, status }, (err, results) => {
      if (err) {
        console.error('error:', err);
        res.status(500).send({ message: 'Error creating project' });
      } else {
        res.send({ id: results.insertId, name, description, status });
      }
    });
  }
});

// API endpoint to update a project
app.put('/api/projects/:id', (req, res) => {
  const id = req.params.id;
  const { name, description, status } = req.body;
  if (!name || !description || !status) {
    res.status(400).send({ message: 'Please provide all required fields' });
  } else {
    db.query('UPDATE projects SET ? WHERE id = ?', [{ name, description, status }, id], (err, results) => {
      if (err) {
        console.error('error:', err);
        res.status(500).send({ message: 'Error updating project' });
      } else if (results.affectedRows === 0) {
        res.status(404).send({ message: 'Project not found' });
      } else {
        res.send({ id, name, description, status });
      }
    });
  }
});

// API endpoint to delete a project
app.delete('/api/projects/:id', (req, res) => {
  const id = req.params.id;
  db.query('DELETE FROM projects WHERE id = ?', [id], (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error deleting project' });
    } else if (results.affectedRows === 0) {
      res.status(404).send({ message: 'Project not found' });
    } else {
      res.send({ message: 'Project deleted successfully' });
    }
  });
});

// WordPress REST API endpoint to get posts
const wordpressApiUrl = 'https://your-wordpress-site.com/wp-json/wp/v2/posts';

// API endpoint to get projects with related WordPress posts
app.get('/api/projects-with-posts', (req, res) => {
  db.query('SELECT * FROM projects', (err, projects) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error fetching projects' });
    } else {
      const promises = projects.map((project) => {
        return axios.get(wordpressApiUrl)
          .then((response) => {
            const posts = response.data;
            project.posts = posts;
            return project;
          })
          .catch((error) => {
            console.error('error:', error);
            return project;
          });
      });
      Promise.all(promises).then((projectsWithPosts) => {
        res.send(projectsWithPosts);
      });
    }
  });
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
