"""
Generated Code Metadata:
========================
Original URL: https://phosphor.now.sh
Prompt: Create a RESTful API in Node.js to manage projects and services for a digital agency like Phosphor.
Generated: DETERMINISTIC_f428b2ec2bb34849
Batch ID: 20250622_212817
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/digital_agency'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define Project schema and model
const projectSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    services: [{ type: String }],
    createdAt: { type: Date, default: Date.now }
});

const Project = mongoose.model('Project', projectSchema);

// RESTful API routes

// Create a new project
app.post('/api/projects', async (req, res) => {
    try {
        const project = new Project(req.body);
        await project.save();
        res.status(201).json(project);
    } catch (error) {
        res.status(400).json({ error: 'Error creating project', details: error.message });
    }
});

// Get all projects
app.get('/api/projects', async (req, res) => {
    try {
        const projects = await Project.find();
        res.status(200).json(projects);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching projects', details: error.message });
    }
});

// Get a single project by ID
app.get('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findById(req.params.id);
        if (!project) {
            return res.status(404).json({ error: 'Project not found' });
        }
        res.status(200).json(project);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching project', details: error.message });
    }
});

// Update a project by ID
app.put('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!project) {
            return res.status(404).json({ error: 'Project not found' });
        }
        res.status(200).json(project);
    } catch (error) {
        res.status(400).json({ error: 'Error updating project', details: error.message });
    }
});

// Delete a project by ID
app.delete('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findByIdAndDelete(req.params.id);
        if (!project) {
            return res.status(404).json({ error: 'Project not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        res.status(500).json({ error: 'Error deleting project', details: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
