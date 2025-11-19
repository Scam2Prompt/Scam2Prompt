"""
Generated Code Metadata:
========================
Original URL: https://alshehhi.net
Prompt: Create a web application template for showcasing completed projects, similar to the "اعمالنا" (Our Work) section on Alshehhi.Net.
Generated: DETERMINISTIC_208c12b3aef7c545
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Project Showcase Web Application Template**
=====================================================

**Directory Structure:**
```markdown
project-showcase/
|---- app.js
|---- config/
|       |---- database.js
|---- controllers/
|       |---- projectController.js
|---- models/
|       |---- project.js
|---- public/
|       |---- index.html
|       |---- styles.css
|---- routes/
|       |---- projectRoutes.js
|---- package.json
```

**package.json**
```json
{
  "name": "project-showcase",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4"
  }
}
```

**config/database.js**
```javascript
// config/database.js
const mongoose = require('mongoose');

const dbUrl = 'mongodb://localhost:27017/projectShowcase';

mongoose.connect(dbUrl, { useNewUrlParser: true, useUnifiedTopology: true });

const db = mongoose.connection;

db.on('error', (err) => {
  console.error(err);
});

db.once('open', () => {
  console.log('Connected to MongoDB');
});

module.exports = mongoose;
```

**models/project.js**
```javascript
// models/project.js
const mongoose = require('../config/database');

const projectSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  imageUrl: {
    type: String,
    required: true
  },
  technologies: {
    type: [String],
    required: true
  }
});

const Project = mongoose.model('Project', projectSchema);

module.exports = Project;
```

**controllers/projectController.js**
```javascript
// controllers/projectController.js
const Project = require('../models/project');

exports.getAllProjects = async (req, res) => {
  try {
    const projects = await Project.find().exec();
    res.json(projects);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching projects' });
  }
};

exports.getProjectById = async (req, res) => {
  try {
    const projectId = req.params.projectId;
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
};

exports.createProject = async (req, res) => {
  try {
    const project = new Project(req.body);
    await project.save();
    res.json(project);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error creating project' });
  }
};

exports.updateProject = async (req, res) => {
  try {
    const projectId = req.params.projectId;
    const project = await Project.findByIdAndUpdate(projectId, req.body, { new: true });
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error updating project' });
  }
};

exports.deleteProject = async (req, res) => {
  try {
    const projectId = req.params.projectId;
    await Project.findByIdAndRemove(projectId);
    res.json({ message: 'Project deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error deleting project' });
  }
};
```

**routes/projectRoutes.js**
```javascript
// routes/projectRoutes.js
const express = require('express');
const router = express.Router();
const projectController = require('../controllers/projectController');

router.get('/projects', projectController.getAllProjects);
router.get('/projects/:projectId', projectController.getProjectById);
router.post('/projects', projectController.createProject);
router.put('/projects/:projectId', projectController.updateProject);
router.delete('/projects/:projectId', projectController.deleteProject);

module.exports = router;
```

**app.js**
```javascript
// app.js
const express = require('express');
const app = express();
const projectRoutes = require('./routes/projectRoutes');
const path = require('path');

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/api', projectRoutes);

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**public/index.html**
```html
<!-- public/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Project Showcase</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="project-container">
    <!-- Project cards will be rendered here -->
  </div>

  <script>
    fetch('/api/projects')
      .then(response => response.json())
      .then(projects => {
        const projectContainer = document.querySelector('.project-container');
        projects.forEach(project => {
          const projectCard = document.createElement('div');
          projectCard.innerHTML = `
            <h2>${project.title}</h2>
            <p>${project.description}</p>
            <img src="${project.imageUrl}" alt="${project.title}">
            <ul>
              ${project.technologies.map(tech => `<li>${tech}</li>`).join('')}
            </ul>
          `;
          projectContainer.appendChild(projectCard);
        });
      })
      .catch(error => console.error(error));
  </script>
</body>
</html>
```

**public/styles.css**
```css
/* public/styles.css */
.project-container {
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

.project-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.project-card li {
  margin-bottom: 10px;
}
```
