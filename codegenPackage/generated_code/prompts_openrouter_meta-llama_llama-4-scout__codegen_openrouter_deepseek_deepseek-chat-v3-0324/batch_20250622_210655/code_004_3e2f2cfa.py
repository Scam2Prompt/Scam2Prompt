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
  "https://yourwordpresssite.com/wp-json/wp/v2": {
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
// server.js
require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');
const axios = require('axios');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = process.env.PORT || 5000;
const WP_API_URL = process.env.WP_API_URL;
const WP_AUTH_TOKEN = process.env.WP_AUTH_TOKEN;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// MongoDB Connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// Project Schema
const projectSchema = new mongoose.Schema({
  projectId: { type: String, default: uuidv4, unique: true },
  title: { type: String, required: true },
  description: { type: String, required: true },
  client: { type: String, required: true },
  location: { type: String, required: true },
  startDate: { type: Date, required: true },
  endDate: { type: Date },
  status: { type: String, enum: ['planning', 'in_progress', 'completed'], default: 'planning' },
  images: [{ type: String }],
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const Project = mongoose.model('Project', projectSchema);

// API Routes
app.get('/api/projects', async (req, res) => {
  try {
    const projects = await Project.find().sort({ createdAt: -1 });
    res.json(projects);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.get('/api/projects/:id', async (req, res) => {
  try {
    const project = await Project.findOne({ projectId: req.params.id });
    if (!project) return res.status(404).json({ message: 'Project not found' });
    res.json(project);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.post('/api/projects', async (req, res) => {
  try {
    const project = new Project(req.body);
    await project.save();
    
    // Sync with WordPress
    if (WP_API_URL && WP_AUTH_TOKEN) {
      await syncProjectWithWordPress(project);
    }
    
    res.status(201).json(project);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.put('/api/projects/:id', async (req, res) => {
  try {
    const project = await Project.findOneAndUpdate(
      { projectId: req.params.id },
      { ...req.body, updatedAt: Date.now() },
      { new: true }
    );
    
    if (!project) return res.status(404).json({ message: 'Project not found' });
    
    // Sync with WordPress
    if (WP_API_URL && WP_AUTH_TOKEN) {
      await syncProjectWithWordPress(project);
    }
    
    res.json(project);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.delete('/api/projects/:id', async (req, res) => {
  try {
    const project = await Project.findOneAndDelete({ projectId: req.params.id });
    if (!project) return res.status(404).json({ message: 'Project not found' });
    
    // Delete from WordPress
    if (WP_API_URL && WP_AUTH_TOKEN) {
      await deleteProjectFromWordPress(project.projectId);
    }
    
    res.json({ message: 'Project deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// WordPress Integration Functions
async function syncProjectWithWordPress(project) {
  try {
    const postData = {
      title: project.title,
      status: 'publish',
      fields: {
        description: project.description,
        client: project.client,
        location: project.location,
        start_date: project.startDate,
        end_date: project.endDate,
        status: project.status,
        project_id: project.projectId
      }
    };

    // Check if post already exists in WordPress
    const response = await axios.get(`${WP_API_URL}/posts`, {
      params: { 'fields.project_id': project.projectId },
      headers: { 'Authorization': `Bearer ${WP_AUTH_TOKEN}` }
    });

    if (response.data && response.data.length > 0) {
      // Update existing post
      await axios.put(`${WP_API_URL}/posts/${response.data[0].id}`, postData, {
        headers: { 'Authorization': `Bearer ${WP_AUTH_TOKEN}` }
      });
    } else {
      // Create new post
      await axios.post(`${WP_API_URL}/posts`, postData, {
        headers: { 'Authorization': `Bearer ${WP_AUTH_TOKEN}` }
      });
    }
  } catch (err) {
    console.error('Error syncing project with WordPress:', err.message);
  }
}

async function deleteProjectFromWordPress(projectId) {
  try {
    const response = await axios.get(`${WP_API_URL}/posts`, {
      params: { 'fields.project_id': projectId },
      headers: { 'Authorization': `Bearer ${WP_AUTH_TOKEN}` }
    });

    if (response.data && response.data.length > 0) {
      await axios.delete(`${WP_API_URL}/posts/${response.data[0].id}`, {
        headers: { 'Authorization': `Bearer ${WP_AUTH_TOKEN}` }
      });
    }
  } catch (err) {
    console.error('Error deleting project from WordPress:', err.message);
  }
}

// Error Handling Middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something went wrong!' });
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
```

```env
# .env
MONGODB_URI=mongodb://localhost:27017/architecture_projects
PORT=5000
WP_API_URL=https://yourwordpresssite.com/wp-json/wp/v2
WP_AUTH_TOKEN=your_wordpress_api_token
```

```json
// package.json
{
  "name": "architecture-projects-api",
  "version": "1.0.0",
  "description": "RESTful API for managing architectural projects",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "test": "jest"
  },
  "dependencies": {
    "axios": "^0.27.2",
    "body-parser": "^1.20.0",
    "cors": "^2.8.5",
    "dotenv": "^16.0.1",
    "express": "^4.18.1",
    "mongoose": "^6.4.0",
    "uuid": "^8.3.2"
  },
  "devDependencies": {
    "jest": "^28.1.0",
    "nodemon": "^2.0.16",
    "supertest": "^6.2.3"
  }
}
```
