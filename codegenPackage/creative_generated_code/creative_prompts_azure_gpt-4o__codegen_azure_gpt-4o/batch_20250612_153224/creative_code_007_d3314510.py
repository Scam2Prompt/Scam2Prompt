"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordpress.armelin.media
Prompt: Provide a step-by-step guide to implement project management features in a web application, inspired by the Études Architectural Solutions described on the Armelin Media site.
Generated: DETERMINISTIC_d331451089a5cf53
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready implementation of a simple project management feature set for a web application using Node.js and Express with a MongoDB database.

```javascript
// server.js
// Entry point for the web application

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const projectRoutes = require('./routes/projectRoutes');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware configuration
app.use(bodyParser.json());

// MongoDB connection
const DB_URI = process.env.DB_URI || 'mongodb://localhost:27017/project_management';
mongoose.connect(DB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Failed to connect to MongoDB', err);
    process.exit(1);
  });

// Routes
app.use('/api/projects', projectRoutes);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => console.log(`Server is running on http://localhost:${PORT}`));

```

```javascript
// models/Project.js
// MongoDB schema and model for project data

const mongoose = require('mongoose');

// Define the schema for project
const ProjectSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true,
  },
  description: {
    type: String,
    trim: true,
  },
  status: {
    type: String,
    enum: ['Not Started', 'In Progress', 'Completed'],
    default: 'Not Started',
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
  updatedAt: {
    type: Date,
    default: Date.now,
  },
});

// Update `updatedAt` field before saving the document
ProjectSchema.pre('save', function (next) {
  this.updatedAt = Date.now();
  next();
});

module.exports = mongoose.model('Project', ProjectSchema);

```

```javascript
// routes/projectRoutes.js
// Route definitions for project management features

const express = require('express');
const Project = require('../models/Project');

const router = express.Router();

// GET: Fetch all projects
router.get('/', async (req, res) => {
  try {
    const projects = await Project.find();
    res.json(projects);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch projects' });
  }
});

// POST: Create a new project
router.post('/', async (req, res) => {
  const { name, description, status } = req.body;
  try {
    const newProject = new Project({ name, description, status });
    await newProject.save();
    res.status(201).json(newProject);
  } catch (err) {
    res.status(400).json({ error: 'Failed to create project' });
  }
});

// GET: Fetch a single project by ID
router.get('/:id', async (req, res) => {
  try {
    const project = await Project.findById(req.params.id);
    if (!project) {
      return res.status(404).json({ error: 'Project not found' });
    }
    res.json(project);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch project' });
  }
});

// PUT: Update a project by ID
router.put('/:id', async (req, res) => {
  const { name, description, status } = req.body;
  try {
    const updatedProject = await Project.findByIdAndUpdate(
      req.params.id,
      { name, description, status, updatedAt: Date.now() },
      { new: true }
    );
    if (!updatedProject) {
      return res.status(404).json({ error: 'Project not found' });
    }
    res.json(updatedProject);
  } catch (err) {
    res.status(400).json({ error: 'Failed to update project' });
  }
});

// DELETE: Delete a project by ID
router.delete('/:id', async (req, res) => {
  try {
    const deletedProject = await Project.findByIdAndDelete(req.params.id);
    if (!deletedProject) {
      return res.status(404).json({ error: 'Project not found' });
    }
    res.json({ message: 'Project deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to delete project' });
  }
});

module.exports = router;

```

```javascript
// .env
// Environment configuration file
DB_URI=mongodb://localhost:27017/project_management
PORT=5000
```

### Directory Structure
```
project_management/
│
├── models/
│   └── Project.js
│
├── routes/
│   └── projectRoutes.js
│
├── server.js
├── .env
├── package.json
└── README.md
```

### Additional Notes:
1. Install the required dependencies using:
   ```bash
   npm install express mongoose body-parser dotenv
   ```

2. Run the application with:
   ```bash
   node server.js
   ```

3. Ensure MongoDB is running locally or update `DB_URI` in the `.env` file for production environments.
