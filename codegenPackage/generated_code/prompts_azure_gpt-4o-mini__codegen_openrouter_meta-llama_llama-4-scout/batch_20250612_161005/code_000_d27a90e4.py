"""
Generated Code Metadata:
========================
Original URL: https://cem-ac.org
Prompt: Generate a code snippet for a web application that showcases artistic projects related to cinematography and stage arts in Mexico, emphasizing cultural responsibility.
Generated: DETERMINISTIC_d27a90e43755dffe
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Mexico Art Showcase Web Application**
=====================================

### Project Structure

```markdown
mexico-art-showcase/
|---- app.js
|---- models/
|       |---- Project.js
|---- routes/
|       |---- projects.js
|---- public/
|       |---- index.html
|       |---- styles.css
|---- package.json
```

### package.json

```json
{
  "name": "mexico-art-showcase",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4"
  },
  "scripts": {
    "start": "node app.js"
  }
}
```

### models/Project.js

```javascript
// Import mongoose for MongoDB interactions
const mongoose = require('mongoose');

// Define the project schema
const projectSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String, required: true },
  imageUrl: { type: String, required: true },
  category: { type: String, enum: ['cinematography', 'stageArts'], required: true },
  culturalResponsibility: { type: Boolean, default: false }
});

// Create and export the Project model
const Project = mongoose.model('Project', projectSchema);
module.exports = Project;
```

### routes/projects.js

```javascript
// Import express for routing
const express = require('express');
const router = express.Router();

// Import Project model
const Project = require('../models/Project');

// Get all projects
router.get('/', async (req, res) => {
  try {
    const projects = await Project.find().exec();
    res.json(projects);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching projects' });
  }
});

// Get project by ID
router.get('/:id', async (req, res) => {
  try {
    const projectId = req.params.id;
    const project = await Project.findById(projectId).exec();
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching project' });
  }
});

// Create a new project
router.post('/', async (req, res) => {
  try {
    const project = new Project(req.body);
    await project.save();
    res.json(project);
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error creating project' });
  }
});

// Update an existing project
router.put('/:id', async (req, res) => {
  try {
    const projectId = req.params.id;
    const project = await Project.findByIdAndUpdate(projectId, req.body, { new: true });
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project);
    }
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error updating project' });
  }
});

// Delete a project
router.delete('/:id', async (req, res) => {
  try {
    const projectId = req.params.id;
    await Project.findByIdAndRemove(projectId);
    res.json({ message: 'Project deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(404).json({ message: 'Project not found' });
  }
});

module.exports = router;
```

### app.js

```javascript
// Import express for the application
const express = require('express');
const app = express();

// Import mongoose for MongoDB interactions
const mongoose = require('mongoose');

// Import project routes
const projectRoutes = require('./routes/projects');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/mexico-art-showcase', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('Error connecting to MongoDB:', err));

// Middleware
app.use(express.json());
app.use(express.static('public'));

// Routes
app.use('/api/projects', projectRoutes);

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

### public/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mexico Art Showcase</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Mexico Art Showcase</h1>
  <div id="projects-container"></div>

  <script>
    fetch('/api/projects')
      .then(response => response.json())
      .then(projects => {
        const projectsContainer = document.getElementById('projects-container');
        projects.forEach(project => {
          const projectCard = document.createElement('div');
          projectCard.innerHTML = `
            <h2>${project.title}</h2>
            <p>${project.description}</p>
            <img src="${project.imageUrl}" alt="${project.title}">
          `;
          projectsContainer.appendChild(projectCard);
        });
      })
      .catch(error => console.error('Error fetching projects:', error));
  </script>
</body>
</html>
```

### public/styles.css

```css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

#projects-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.project-card {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project-card img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}
```
