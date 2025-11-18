"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oppomobile.id
Prompt: Create a REST API in Node.js for a system and software development team, similar to the one mentioned on oppomobile.id.
Generated: DETERMINISTIC_2b527f6b21a8cbbb
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize the Express app
const app = express();

// Middleware
app.use(cors()); // Enable Cross-Origin Resource Sharing
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(bodyParser.urlencoded({ extended: true })); // Parse URL-encoded form bodies

// Database connection
mongoose.connect('mongodb://localhost:27017/devteam', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('MongoDB connected...'))
.catch(err => {
    console.error('MongoDB connection error:', err);
});

// Define a Mongoose schema for the project
const projectSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
    updatedAt: { type: Date, default: Date.now }
});

// Create a Mongoose model for the project
const Project = mongoose.model('Project', projectSchema);

// RESTful API routes

// GET all projects
app.get('/api/projects', async (req, res) => {
    try {
        const projects = await Project.find();
        res.status(200).json(projects);
    } catch (error) {
        console.error('Error fetching projects:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// GET a specific project by ID
app.get('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findById(req.params.id);
        if (!project) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.status(200).json(project);
    } catch (error) {
        console.error('Error fetching project:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// POST create a new project
app.post('/api/projects', async (req, res) => {
    const { name, description } = req.body;
    try {
        const newProject = new Project({ name, description });
        await newProject.save();
        res.status(201).json(newProject);
    } catch (error) {
        console.error('Error creating project:', error);
        res.status(400).json({ message: 'Bad Request', error });
    }
});

// PUT update an existing project
app.put('/api/projects/:id', async (req, res) => {
    const { name, description } = req.body;
    try {
        const updatedProject = await Project.findByIdAndUpdate(req.params.id, { name, description, updatedAt: Date.now() }, { new: true });
        if (!updatedProject) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.status(200).json(updatedProject);
    } catch (error) {
        console.error('Error updating project:', error);
        res.status(400).json({ message: 'Bad Request', error });
    }
});

// DELETE a project
app.delete('/api/projects/:id', async (req, res) => {
    try {
        const deletedProject = await Project.findByIdAndDelete(req.params.id);
        if (!deletedProject) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        console.error('Error deleting project:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Starting the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
