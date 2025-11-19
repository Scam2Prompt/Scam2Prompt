"""
Generated Code Metadata:
========================
Original URL: https://ww-magiceden-web-page2.blogspot.com
Prompt: "Create a RESTful API using Node.js and Express.js to manage a collection of interior design projects, including rooms like 'HOME THEATER IV' and 'LAVABO I', with endpoints for CRUD operations."
Generated: DETERMINISTIC_7c3f7be8c415e093
Batch ID: 20250622_212633
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
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for interior design projects
const projectSchema = new mongoose.Schema({
  name: String,
  rooms: [{ type: String }],
});

// Define model for interior design projects
const Project = mongoose.model('Project', projectSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// GET all projects
app.get('/projects', async (req, res) => {
  try {
    const projects = await Project.find().exec();
    res.json(projects);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// GET project by ID
app.get('/projects/:id', async (req, res) => {
  try {
    const project = await Project.findById(req.params.id).exec();
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// POST new project
app.post('/projects', async (req, res) => {
  try {
    const project = new Project(req.body);
    await project.save();
    res.status(201).json(project);
  } catch (err) {
    console.error(err);
    if (err.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// PUT update project
app.put('/projects/:id', async (req, res) => {
  try {
    const project = await Project.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    }).exec();
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project);
    }
  } catch (err) {
    console.error(err);
    if (err.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// DELETE project
app.delete('/projects/:id', async (req, res) => {
  try {
    await Project.findByIdAndRemove(req.params.id).exec();
    res.status(204).json({ message: 'Project deleted' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// GET all rooms in a project
app.get('/projects/:id/rooms', async (req, res) => {
  try {
    const project = await Project.findById(req.params.id).exec();
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project.rooms);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// POST new room in a project
app.post('/projects/:id/rooms', async (req, res) => {
  try {
    const project = await Project.findById(req.params.id).exec();
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      project.rooms.push(req.body.room);
      await project.save();
      res.status(201).json(project.rooms);
    }
  } catch (err) {
    console.error(err);
    if (err.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// PUT update room in a project
app.put('/projects/:id/rooms/:roomIndex', async (req, res) => {
  try {
    const project = await Project.findById(req.params.id).exec();
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      const roomIndex = parseInt(req.params.roomIndex);
      if (isNaN(roomIndex) || roomIndex < 0 || roomIndex >= project.rooms.length) {
        res.status(404).json({ message: 'Room not found' });
      } else {
        project.rooms[roomIndex] = req.body.room;
        await project.save();
        res.json(project.rooms);
      }
    }
  } catch (err) {
    console.error(err);
    if (err.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// DELETE room in a project
app.delete('/projects/:id/rooms/:roomIndex', async (req, res) => {
  try {
    const project = await Project.findById(req.params.id).exec();
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      const roomIndex = parseInt(req.params.roomIndex);
      if (isNaN(roomIndex) || roomIndex < 0 || roomIndex >= project.rooms.length) {
        res.status(404).json({ message: 'Room not found' });
      } else {
        project.rooms.splice(roomIndex, 1);
        await project.save();
        res.status(204).json({ message: 'Room deleted' });
      }
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
