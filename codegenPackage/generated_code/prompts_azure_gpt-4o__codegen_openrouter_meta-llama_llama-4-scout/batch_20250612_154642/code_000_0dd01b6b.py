"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: Write code to create a web-based application that showcases architectural projects, inspired by Études' approach to merging creativity and functionality.
Generated: DETERMINISTIC_0dd01b6b98617565
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Project Structure**
```markdown
project/
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
|---- utils/
|       |---- helpers.js
|---- package.json
```

**package.json**
```json
{
  "name": "architectural-projects",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4",
    "mongoose": "^5.10.15"
  }
}
```

**config/database.js**
```javascript
// config/database.js
const mongoose = require('mongoose');

const dbUrl = 'mongodb://localhost:27017/architectural-projects';

mongoose.connect(dbUrl, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

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
  image: {
    type: String,
    required: true
  },
  createdAt: {
    type: Date,
    default: Date.now
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
    const projects = await Project.find().sort('-createdAt');
    res.json(projects);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching projects' });
  }
};

exports.getProjectById = async (req, res) => {
  try {
    const project = await Project.findById(req.params.id);
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching project' });
  }
};

exports.createProject = async (req, res) => {
  try {
    const project = new Project(req.body);
    await project.save();
    res.json(project);
  } catch (err) {
    res.status(400).json({ message: 'Error creating project' });
  }
};

exports.updateProject = async (req, res) => {
  try {
    const project = await Project.findByIdAndUpdate(req.params.id, req.body, {
      new: true
    });
    if (!project) {
      res.status(404).json({ message: 'Project not found' });
    } else {
      res.json(project);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error updating project' });
  }
};

exports.deleteProject = async (req, res) => {
  try {
    await Project.findByIdAndRemove(req.params.id);
    res.json({ message: 'Project deleted successfully' });
  } catch (err) {
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
router.get('/projects/:id', projectController.getProjectById);
router.post('/projects', projectController.createProject);
router.put('/projects/:id', projectController.updateProject);
router.delete('/projects/:id', projectController.deleteProject);

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
  <title>Architectural Projects</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Architectural Projects</h1>
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
            <img src="${project.image}" alt="${project.title}">
          `;
          projectsContainer.appendChild(projectCard);
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
body {
  font-family: Arial, sans-serif;
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

.project-card h2 {
  margin-top: 0;
}
```
