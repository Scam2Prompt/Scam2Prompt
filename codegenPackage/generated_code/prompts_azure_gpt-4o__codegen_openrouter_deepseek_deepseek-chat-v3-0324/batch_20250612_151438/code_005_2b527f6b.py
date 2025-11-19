"""
Generated Code Metadata:
========================
Original URL: https://oppomobile.id
Prompt: Create a REST API in Node.js for a system and software development team, similar to the one mentioned on oppomobile.id.
Generated: DETERMINISTIC_2b527f6b21a8cbbb
Batch ID: 20250612_151438
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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Configure environment variables
require('dotenv').config();

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Middleware
app.use(cors());
app.use(helmet());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Models
const TeamMember = mongoose.model('TeamMember', new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  name: { type: String, required: true },
  role: { type: String, required: true },
  skills: { type: [String], required: true },
  projects: { type: [String], default: [] },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
}));

const Project = mongoose.model('Project', new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  name: { type: String, required: true },
  description: { type: String, required: true },
  technologies: { type: [String], required: true },
  teamMembers: { type: [String], default: [] },
  status: { type: String, enum: ['planning', 'in-progress', 'completed', 'on-hold'], default: 'planning' },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
}));

// Routes
const router = express.Router();

// Team Members API
router.route('/team-members')
  .get(async (req, res) => {
    try {
      const teamMembers = await TeamMember.find();
      res.json(teamMembers);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .post(async (req, res) => {
    try {
      const newMember = new TeamMember(req.body);
      const savedMember = await newMember.save();
      res.status(201).json(savedMember);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

router.route('/team-members/:id')
  .get(async (req, res) => {
    try {
      const member = await TeamMember.findById(req.params.id);
      if (!member) return res.status(404).json({ error: 'Team member not found' });
      res.json(member);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .put(async (req, res) => {
    try {
      const updatedMember = await TeamMember.findByIdAndUpdate(
        req.params.id,
        { ...req.body, updatedAt: Date.now() },
        { new: true }
      );
      if (!updatedMember) return res.status(404).json({ error: 'Team member not found' });
      res.json(updatedMember);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const deletedMember = await TeamMember.findByIdAndDelete(req.params.id);
      if (!deletedMember) return res.status(404).json({ error: 'Team member not found' });
      res.json({ message: 'Team member deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Projects API
router.route('/projects')
  .get(async (req, res) => {
    try {
      const projects = await Project.find();
      res.json(projects);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .post(async (req, res) => {
    try {
      const newProject = new Project(req.body);
      const savedProject = await newProject.save();
      res.status(201).json(savedProject);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

router.route('/projects/:id')
  .get(async (req, res) => {
    try {
      const project = await Project.findById(req.params.id);
      if (!project) return res.status(404).json({ error: 'Project not found' });
      res.json(project);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .put(async (req, res) => {
    try {
      const updatedProject = await Project.findByIdAndUpdate(
        req.params.id,
        { ...req.body, updatedAt: Date.now() },
        { new: true }
      );
      if (!updatedProject) return res.status(404).json({ error: 'Project not found' });
      res.json(updatedProject);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const deletedProject = await Project.findByIdAndDelete(req.params.id);
      if (!deletedProject) return res.status(404).json({ error: 'Project not found' });
      res.json({ message: 'Project deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Assign team member to project
router.route('/projects/:projectId/assign/:memberId')
  .post(async (req, res) => {
    try {
      const project = await Project.findById(req.params.projectId);
      const member = await TeamMember.findById(req.params.memberId);
      
      if (!project || !member) {
        return res.status(404).json({ error: 'Project or team member not found' });
      }

      if (!project.teamMembers.includes(req.params.memberId)) {
        project.teamMembers.push(req.params.memberId);
        await project.save();
      }

      if (!member.projects.includes(req.params.projectId)) {
        member.projects.push(req.params.projectId);
        await member.save();
      }

      res.json({ message: 'Team member assigned to project successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// API versioning
app.use('/api/v1', router);

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
