"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Build a web application to manage ERP projects and freelancers using a JavaScript framework.
Generated: DETERMINISTIC_078fa1285682d2b8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules
const express = require('express'); // Web framework for Node.js
const mongoose = require('mongoose'); // MongoDB object modeling tool
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const cors = require('cors'); // Middleware for enabling CORS

// Initialize the Express app
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(cors()); // Enable CORS for cross-origin requests

// Connect to MongoDB
mongoose
  .connect('mongodb://localhost:27017/erp_management', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Failed to connect to MongoDB:', err));

// Define Mongoose schemas and models
const ProjectSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String, required: true },
  budget: { type: Number, required: true },
  deadline: { type: Date, required: true },
  assignedFreelancers: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Freelancer' }],
});

const FreelancerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  skills: [String],
  hourlyRate: { type: Number, required: true },
});

const Project = mongoose.model('Project', ProjectSchema);
const Freelancer = mongoose.model('Freelancer', FreelancerSchema);

// Routes for managing projects
app.get('/projects', async (req, res) => {
  try {
    const projects = await Project.find().populate('assignedFreelancers');
    res.status(200).json(projects);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch projects' });
  }
});

app.post('/projects', async (req, res) => {
  try {
    const project = new Project(req.body);
    await project.save();
    res.status(201).json(project);
  } catch (err) {
    res.status(400).json({ error: 'Failed to create project' });
  }
});

app.put('/projects/:id', async (req, res) => {
  try {
    const project = await Project.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    res.status(200).json(project);
  } catch (err) {
    res.status(400).json({ error: 'Failed to update project' });
  }
});

app.delete('/projects/:id', async (req, res) => {
  try {
    await Project.findByIdAndDelete(req.params.id);
    res.status(200).json({ message: 'Project deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to delete project' });
  }
});

// Routes for managing freelancers
app.get('/freelancers', async (req, res) => {
  try {
    const freelancers = await Freelancer.find();
    res.status(200).json(freelancers);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch freelancers' });
  }
});

app.post('/freelancers', async (req, res) => {
  try {
    const freelancer = new Freelancer(req.body);
    await freelancer.save();
    res.status(201).json(freelancer);
  } catch (err) {
    res.status(400).json({ error: 'Failed to create freelancer' });
  }
});

app.put('/freelancers/:id', async (req, res) => {
  try {
    const freelancer = await Freelancer.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    res.status(200).json(freelancer);
  } catch (err) {
    res.status(400).json({ error: 'Failed to update freelancer' });
  }
});

app.delete('/freelancers/:id', async (req, res) => {
  try {
    await Freelancer.findByIdAndDelete(req.params.id);
    res.status(200).json({ message: 'Freelancer deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to delete freelancer' });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
