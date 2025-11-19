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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas
const ResourceSchema = new mongoose.Schema({
  name: { type: String, required: true },
  type: { type: String, required: true },
  quantity: { type: Number, required: true },
  cost: { type: Number, required: true },
  projectId: { type: mongoose.Schema.Types.ObjectId, ref: 'Project' }
}, { timestamps: true });

const ClientSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String },
  address: { type: String }
}, { timestamps: true });

const ProjectSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String },
  startDate: { type: Date, required: true },
  endDate: { type: Date },
  clientId: { type: mongoose.Schema.Types.ObjectId, ref: 'Client' },
  status: { type: String, enum: ['planned', 'in-progress', 'completed'], default: 'planned' }
}, { timestamps: true });

// Create models
const Resource = mongoose.model('Resource', ResourceSchema);
const Client = mongoose.model('Client', ClientSchema);
const Project = mongoose.model('Project', ProjectSchema);

// Routes for Clients
app.get('/api/clients', async (req, res) => {
  try {
    const clients = await Client.find();
    res.json(clients);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.post('/api/clients', async (req, res) => {
  const client = new Client(req.body);
  try {
    const newClient = await client.save();
    res.status(201).json(newClient);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.get('/api/clients/:id', async (req, res) => {
  try {
    const client = await Client.findById(req.params.id);
    if (!client) return res.status(404).json({ message: 'Client not found' });
    res.json(client);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.put('/api/clients/:id', async (req, res) => {
  try {
    const updatedClient = await Client.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );
    if (!updatedClient) return res.status(404).json({ message: 'Client not found' });
    res.json(updatedClient);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.delete('/api/clients/:id', async (req, res) => {
  try {
    const deletedClient = await Client.findByIdAndDelete(req.params.id);
    if (!deletedClient) return res.status(404).json({ message: 'Client not found' });
    res.json({ message: 'Client deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Routes for Projects
app.get('/api/projects', async (req, res) => {
  try {
    const projects = await Project.find().populate('clientId');
    res.json(projects);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.post('/api/projects', async (req, res) => {
  const project = new Project(req.body);
  try {
    const newProject = await project.save();
    res.status(201).json(newProject);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.get('/api/projects/:id', async (req, res) => {
  try {
    const project = await Project.findById(req.params.id).populate('clientId');
    if (!project) return res.status(404).json({ message: 'Project not found' });
    res.json(project);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.put('/api/projects/:id', async (req, res) => {
  try {
    const updatedProject = await Project.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    ).populate('clientId');
    if (!updatedProject) return res.status(404).json({ message: 'Project not found' });
    res.json(updatedProject);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.delete('/api/projects/:id', async (req, res) => {
  try {
    const deletedProject = await Project.findByIdAndDelete(req.params.id);
    if (!deletedProject) return res.status(404).json({ message: 'Project not found' });
    res.json({ message: 'Project deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Routes for Resources
app.get('/api/projects/:projectId/resources', async (req, res) => {
  try {
    const resources = await Resource.find({ projectId: req.params.projectId });
    res.json(resources);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.post('/api/projects/:projectId/resources', async (req, res) => {
  const resource = new Resource({
    ...req.body,
    projectId: req.params.projectId
  });
  try {
    const newResource = await resource.save();
    res.status(201).json(newResource);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.get('/api/resources/:id', async (req, res) => {
  try {
    const resource = await Resource.findById(req.params.id);
    if (!resource) return res.status(404).json({ message: 'Resource not found' });
    res.json(resource);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.put('/api/resources/:id', async (req, res) => {
  try {
    const updatedResource = await Resource.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );
    if (!updatedResource) return res.status(404).json({ message: 'Resource not found' });
    res.json(updatedResource);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.delete('/api/resources/:id', async (req, res) => {
  try {
    const deletedResource = await Resource.findByIdAndDelete(req.params.id);
    if (!deletedResource) return res.status(404).json({ message: 'Resource not found' });
    res.json({ message: 'Resource deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
