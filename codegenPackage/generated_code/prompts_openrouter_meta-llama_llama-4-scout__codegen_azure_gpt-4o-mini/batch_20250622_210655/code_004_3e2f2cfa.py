"""
Generated Code Metadata:
========================
Original URL: https://wordpress.armelin.media
Prompt: Create a RESTful API using Node.js and Express.js to manage architectural project data, similar to how Études Architectural Solutions might manage their projects, and integrate it with a WordPress site.
Generated: DETERMINISTIC_3e2f2cfa9b960d90
Batch ID: 20250622_210655
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
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/architectural_projects'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for architectural projects
const projectSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    client: { type: String, required: true },
    status: { type: String, enum: ['pending', 'in-progress', 'completed'], default: 'pending' },
    createdAt: { type: Date, default: Date.now }
});

// Create a Mongoose model based on the schema
const Project = mongoose.model('Project', projectSchema);

// RESTful API routes

// Get all projects
app.get('/api/projects', async (req, res) => {
    try {
        const projects = await Project.find();
        res.status(200).json(projects);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching projects', error });
    }
});

// Get a single project by ID
app.get('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findById(req.params.id);
        if (!project) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.status(200).json(project);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching project', error });
    }
});

// Create a new project
app.post('/api/projects', async (req, res) => {
    const { title, description, client, status } = req.body;
    const newProject = new Project({ title, description, client, status });

    try {
        const savedProject = await newProject.save();
        res.status(201).json(savedProject);
    } catch (error) {
        res.status(400).json({ message: 'Error creating project', error });
    }
});

// Update an existing project
app.put('/api/projects/:id', async (req, res) => {
    try {
        const updatedProject = await Project.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedProject) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.status(200).json(updatedProject);
    } catch (error) {
        res.status(400).json({ message: 'Error updating project', error });
    }
});

// Delete a project
app.delete('/api/projects/:id', async (req, res) => {
    try {
        const deletedProject = await Project.findByIdAndDelete(req.params.id);
        if (!deletedProject) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        res.status(500).json({ message: 'Error deleting project', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Instructions for Integration with WordPress
To integrate this API with a WordPress site, you can use the WordPress REST API to make HTTP requests to this Node.js API. You can create custom WordPress plugins or use existing ones to fetch and display project data from this API.
