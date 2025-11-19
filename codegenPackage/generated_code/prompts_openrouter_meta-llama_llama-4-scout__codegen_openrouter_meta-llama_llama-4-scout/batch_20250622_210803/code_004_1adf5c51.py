"""
Generated Code Metadata:
========================
Original URL: https://rdmerakyat.com
Prompt: Create a RESTful API using Node.js to manage architectural project data, including resources and client information.
Generated: DETERMINISTIC_1adf5c51fbd09bed
Batch ID: 20250622_210803
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
const bodyParser = require('body-parser');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/architectural-projects', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for resources
const resourceSchema = new mongoose.Schema({
    name: String,
    description: String,
    quantity: Number
});

// Define schema for clients
const clientSchema = new mongoose.Schema({
    name: String,
    email: String,
    phone: String
});

// Define schema for projects
const projectSchema = new mongoose.Schema({
    name: String,
    description: String,
    resources: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Resource' }],
    client: { type: mongoose.Schema.Types.ObjectId, ref: 'Client' }
});

// Create models
const Resource = mongoose.model('Resource', resourceSchema);
const Client = mongoose.model('Client', clientSchema);
const Project = mongoose.model('Project', projectSchema);

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Resource API Endpoints

// Get all resources
app.get('/api/resources', async (req, res) => {
    try {
        const resources = await Resource.find().exec();
        res.json(resources);
    } catch (err) {
        res.status(500).json({ message: 'Error fetching resources' });
    }
});

// Get resource by ID
app.get('/api/resources/:id', async (req, res) => {
    try {
        const resource = await Resource.findById(req.params.id).exec();
        if (!resource) {
            res.status(404).json({ message: 'Resource not found' });
        } else {
            res.json(resource);
        }
    } catch (err) {
        res.status(500).json({ message: 'Error fetching resource' });
    }
});

// Create new resource
app.post('/api/resources', async (req, res) => {
    try {
        const resource = new Resource(req.body);
        await resource.save();
        res.json(resource);
    } catch (err) {
        res.status(400).json({ message: 'Error creating resource' });
    }
});

// Update existing resource
app.put('/api/resources/:id', async (req, res) => {
    try {
        const resource = await Resource.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!resource) {
            res.status(404).json({ message: 'Resource not found' });
        } else {
            res.json(resource);
        }
    } catch (err) {
        res.status(400).json({ message: 'Error updating resource' });
    }
});

// Delete resource
app.delete('/api/resources/:id', async (req, res) => {
    try {
        await Resource.findByIdAndRemove(req.params.id);
        res.json({ message: 'Resource deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: 'Error deleting resource' });
    }
});

// Client API Endpoints

// Get all clients
app.get('/api/clients', async (req, res) => {
    try {
        const clients = await Client.find().exec();
        res.json(clients);
    } catch (err) {
        res.status(500).json({ message: 'Error fetching clients' });
    }
});

// Get client by ID
app.get('/api/clients/:id', async (req, res) => {
    try {
        const client = await Client.findById(req.params.id).exec();
        if (!client) {
            res.status(404).json({ message: 'Client not found' });
        } else {
            res.json(client);
        }
    } catch (err) {
        res.status(500).json({ message: 'Error fetching client' });
    }
});

// Create new client
app.post('/api/clients', async (req, res) => {
    try {
        const client = new Client(req.body);
        await client.save();
        res.json(client);
    } catch (err) {
        res.status(400).json({ message: 'Error creating client' });
    }
});

// Update existing client
app.put('/api/clients/:id', async (req, res) => {
    try {
        const client = await Client.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!client) {
            res.status(404).json({ message: 'Client not found' });
        } else {
            res.json(client);
        }
    } catch (err) {
        res.status(400).json({ message: 'Error updating client' });
    }
});

// Delete client
app.delete('/api/clients/:id', async (req, res) => {
    try {
        await Client.findByIdAndRemove(req.params.id);
        res.json({ message: 'Client deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: 'Error deleting client' });
    }
});

// Project API Endpoints

// Get all projects
app.get('/api/projects', async (req, res) => {
    try {
        const projects = await Project.find().populate('resources').populate('client').exec();
        res.json(projects);
    } catch (err) {
        res.status(500).json({ message: 'Error fetching projects' });
    }
});

// Get project by ID
app.get('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findById(req.params.id).populate('resources').populate('client').exec();
        if (!project) {
            res.status(404).json({ message: 'Project not found' });
        } else {
            res.json(project);
        }
    } catch (err) {
        res.status(500).json({ message: 'Error fetching project' });
    }
});

// Create new project
app.post('/api/projects', async (req, res) => {
    try {
        const project = new Project(req.body);
        await project.save();
        res.json(project);
    } catch (err) {
        res.status(400).json({ message: 'Error creating project' });
    }
});

// Update existing project
app.put('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!project) {
            res.status(404).json({ message: 'Project not found' });
        } else {
            res.json(project);
        }
    } catch (err) {
        res.status(400).json({ message: 'Error updating project' });
    }
});

// Delete project
app.delete('/api/projects/:id', async (req, res) => {
    try {
        await Project.findByIdAndRemove(req.params.id);
        res.json({ message: 'Project deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: 'Error deleting project' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
