"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Create a RESTful API using Node.js and Express.js to manage interior design projects, including endpoints for project creation, updating, and deletion, inspired by the project management services offered by Amazing Interior.
Generated: DETERMINISTIC_f9101c711b28aa01
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
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
});

// Define project schema
const projectSchema = new mongoose.Schema({
  name: String,
  description: String,
  status: String,
});

// Create project model
const Project = mongoose.model('Project', projectSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Get all projects
app.get('/projects', async (req, res) => {
  try {
    const projects = await Project.find().exec();
    res.json(projects);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Get project by ID
app.get('/projects/:id', async (req, res) => {
  try {
    const projectId = req.params.id;
    const project = await Project.findById(projectId).exec();
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Create new project
app.post('/projects', async (req, res) => {
  try {
    const project = new Project(req.body);
    await project.save();
    res.status(201).json(project);
  } catch (err) {
    console.error(err);
    if (err.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// Update existing project
app.put('/projects/:id', async (req, res) => {
  try {
    const projectId = req.params.id;
    const project = await Project.findByIdAndUpdate(projectId, req.body, {
      new: true,
    }).exec();
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project);
    }
  } catch (err) {
    console.error(err);
    if (err.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// Delete project
app.delete('/projects/:id', async (req, res) => {
  try {
    const projectId = req.params.id;
    await Project.findByIdAndRemove(projectId).exec();
    res.status(204).json();
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// For running this file 
// node filename.js 
// and use postman or curl to test the API
```
