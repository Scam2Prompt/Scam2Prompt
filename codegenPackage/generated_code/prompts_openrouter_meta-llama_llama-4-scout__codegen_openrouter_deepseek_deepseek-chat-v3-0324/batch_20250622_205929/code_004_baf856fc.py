"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Create a RESTful API using Node.js and Express.js to provide access to construction project data, similar to the project data presented on the Sadad Engineering and Construction Company website.
Generated: DETERMINISTIC_baf856fcdce9928c
Batch ID: 20250622_205929
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
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Project Schema
const projectSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
        trim: true
    },
    description: {
        type: String,
        required: true,
        trim: true
    },
    location: {
        type: String,
        required: true,
        trim: true
    },
    client: {
        type: String,
        required: true,
        trim: true
    },
    startDate: {
        type: Date,
        required: true
    },
    endDate: {
        type: Date,
        required: false
    },
    status: {
        type: String,
        enum: ['planned', 'ongoing', 'completed'],
        default: 'planned'
    },
    images: [{
        type: String,
        trim: true
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

// Update timestamps on save
projectSchema.pre('save', function(next) {
    this.updatedAt = Date.now();
    next();
});

// Project Model
const Project = mongoose.model('Project', projectSchema);

// Routes
const router = express.Router();

/**
 * @route GET /api/projects
 * @description Get all projects
 * @access Public
 */
router.get('/projects', async (req, res) => {
    try {
        const projects = await Project.find().sort({ createdAt: -1 });
        res.json(projects);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

/**
 * @route GET /api/projects/:id
 * @description Get a single project by ID
 * @access Public
 */
router.get('/projects/:id', async (req, res) => {
    try {
        const project = await Project.findById(req.params.id);
        if (!project) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.json(project);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

/**
 * @route POST /api/projects
 * @description Create a new project
 * @access Private (should be protected in production)
 */
router.post('/projects', async (req, res) => {
    const project = new Project({
        title: req.body.title,
        description: req.body.description,
        location: req.body.location,
        client: req.body.client,
        startDate: req.body.startDate,
        endDate: req.body.endDate,
        status: req.body.status,
        images: req.body.images
    });

    try {
        const newProject = await project.save();
        res.status(201).json(newProject);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

/**
 * @route PUT /api/projects/:id
 * @description Update a project
 * @access Private (should be protected in production)
 */
router.put('/projects/:id', async (req, res) => {
    try {
        const project = await Project.findByIdAndUpdate(
            req.params.id,
            req.body,
            { new: true, runValidators: true }
        );
        
        if (!project) {
            return res.status(404).json({ message: 'Project not found' });
        }
        
        res.json(project);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

/**
 * @route DELETE /api/projects/:id
 * @description Delete a project
 * @access Private (should be protected in production)
 */
router.delete('/projects/:id', async (req, res) => {
    try {
        const project = await Project.findByIdAndDelete(req.params.id);
        
        if (!project) {
            return res.status(404).json({ message: 'Project not found' });
        }
        
        res.json({ message: 'Project deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Mount routes
app.use('/api', router);

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

// Export app for testing
module.exports = app;
```
