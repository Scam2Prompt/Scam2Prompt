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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/interiorDesignDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Project Schema
const projectSchema = new mongoose.Schema({
  projectId: {
    type: String,
    default: uuidv4,
    unique: true
  },
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  clientName: {
    type: String,
    required: true
  },
  startDate: {
    type: Date,
    default: Date.now
  },
  endDate: {
    type: Date
  },
  status: {
    type: String,
    enum: ['planning', 'in-progress', 'completed'],
    default: 'planning'
  },
  budget: {
    type: Number,
    required: true
  },
  rooms: [{
    name: String,
    size: String,
    style: String
  }],
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Project Model
const Project = mongoose.model('Project', projectSchema);

// API Routes

// Create a new project
app.post('/api/projects', async (req, res) => {
  try {
    const project = new Project(req.body);
    await project.save();
    res.status(201).json(project);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Get all projects
app.get('/api/projects', async (req, res) => {
  try {
    const projects = await Project.find().sort({ createdAt: -1 });
    res.json(projects);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get a single project by ID
app.get('/api/projects/:id', async (req, res) => {
  try {
    const project = await Project.findOne({ projectId: req.params.id });
    if (!project) {
      return res.status(404).json({ error: 'Project not found' });
    }
    res.json(project);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Update a project
app.put('/api/projects/:id', async (req, res) => {
  try {
    const project = await Project.findOneAndUpdate(
      { projectId: req.params.id },
      { ...req.body, updatedAt: Date.now() },
      { new: true }
    );
    if (!project) {
      return res.status(404).json({ error: 'Project not found' });
    }
    res.json(project);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Delete a project
app.delete('/api/projects/:id', async (req, res) => {
  try {
    const project = await Project.findOneAndDelete({ projectId: req.params.id });
    if (!project) {
      return res.status(404).json({ error: 'Project not found' });
    }
    res.json({ message: 'Project deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
