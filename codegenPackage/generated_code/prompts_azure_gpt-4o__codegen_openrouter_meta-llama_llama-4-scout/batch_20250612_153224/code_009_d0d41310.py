"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Develop a web application to showcase completed interior design projects, including galleries for residential and commercial spaces, with filters for services like HVAC and furniture design.
Generated: DETERMINISTIC_d0d413100c316f81
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Interior Design Project Showcase Web Application**

### Backend (Node.js, Express.js, MongoDB)

```javascript
// server.js
const express = require('express');
const mongoose = require('mongoose');
const app = express();
require('dotenv').config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for projects
const projectSchema = new mongoose.Schema({
  title: String,
  description: String,
  category: String, // residential or commercial
  services: [{ type: String }], // HVAC, furniture design, etc.
  images: [{ type: String }],
});

// Define schema for services
const serviceSchema = new mongoose.Schema({
  name: String,
  description: String,
});

// Create models
const Project = mongoose.model('Project', projectSchema);
const Service = mongoose.model('Service', serviceSchema);

// Middleware
app.use(express.json());
app.use(express.static('public'));

// API Endpoints

// Get all projects
app.get('/api/projects', async (req, res) => {
  try {
    const projects = await Project.find().populate('services');
    res.json(projects);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching projects' });
  }
});

// Get projects by category
app.get('/api/projects/:category', async (req, res) => {
  try {
    const projects = await Project.find({ category: req.params.category });
    res.json(projects);
  } catch (err) {
    res.status(404).json({ message: 'No projects found' });
  }
});

// Get projects by service
app.get('/api/projects/services/:service', async (req, res) => {
  try {
    const projects = await Project.find({ services: req.params.service });
    res.json(projects);
  } catch (err) {
    res.status(404).json({ message: 'No projects found' });
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

// Create new service
app.post('/api/services', async (req, res) => {
  try {
    const service = new Service(req.body);
    await service.save();
    res.json(service);
  } catch (err) {
    res.status(400).json({ message: 'Error creating service' });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// models/Project.js
const mongoose = require('mongoose');

const projectSchema = new mongoose.Schema({
  title: String,
  description: String,
  category: String,
  services: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Service' }],
  images: [{ type: String }],
});

module.exports = mongoose.model('Project', projectSchema);
```

```javascript
// models/Service.js
const mongoose = require('mongoose');

const serviceSchema = new mongoose.Schema({
  name: String,
  description: String,
});

module.exports = mongoose.model('Service', serviceSchema);
```

### Frontend (React.js)

```javascript
// components/ProjectGallery.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProjectGallery = () => {
  const [projects, setProjects] = useState([]);
  const [category, setCategory] = useState('all');
  const [services, setServices] = useState([]);

  useEffect(() => {
    axios.get('/api/projects')
      .then(response => {
        setProjects(response.data);
      })
      .catch(error => {
        console.error(error);
      });

    axios.get('/api/services')
      .then(response => {
        setServices(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const filterProjects = (category) => {
    setCategory(category);
    if (category === 'all') {
      axios.get('/api/projects')
        .then(response => {
          setProjects(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    } else {
      axios.get(`/api/projects/${category}`)
        .then(response => {
          setProjects(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  };

  const filterByService = (service) => {
    axios.get(`/api/projects/services/${service}`)
      .then(response => {
        setProjects(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Project Gallery</h1>
      <button onClick={() => filterProjects('all')}>All</button>
      <button onClick={() => filterProjects('residential')}>Residential</button>
      <button onClick={() => filterProjects('commercial')}>Commercial</button>
      {services.map((service) => (
        <button key={service._id} onClick={() => filterByService(service.name)}>{service.name}</button>
      ))}
      {projects.map((project) => (
        <div key={project._id}>
          <h2>{project.title}</h2>
          <p>{project.description}</p>
          <img src={project.images[0]} alt={project.title} />
        </div>
      ))}
    </div>
  );
};

export default ProjectGallery;
```

```javascript
// App.js
import React from 'react';
import ProjectGallery from './components/ProjectGallery';

function App() {
  return (
    <div>
      <ProjectGallery />
    </div>
  );
}

export default App;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

### package.json

```json
{
  "name": "interior-design-project-showcase",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js",
    "start:frontend": "npm start --prefix frontend"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^5.12.3",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "axios": "^0.21.1"
  },
  "devDependencies": {
    "nodemon": "^2.0.13"
  }
}
```

### .env

```makefile
MONGODB_URI=mongodb://localhost:27017/interior-design-project-showcase
PORT=3000
```
