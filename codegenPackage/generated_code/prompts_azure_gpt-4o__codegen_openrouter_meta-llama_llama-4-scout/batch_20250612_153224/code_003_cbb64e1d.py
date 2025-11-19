"""
Generated Code Metadata:
========================
Original URL: https://wordpress.armelin.media
Prompt: Develop a web application that mimics the functionality of the Études Architect App, including features for collaboration, project showcasing, and architectural resource sharing.
Generated: DETERMINISTIC_cbb64e1dc63eba0e
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-username/etudes-architect-app.git`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Études Architect App Web Application**
=====================================

**Backend (Node.js, Express.js)**
--------------------------------

```javascript
// server.js
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/etudes-architect', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define user model
const User = mongoose.model('User', {
  name: String,
  email: String,
  password: String,
});

// Define project model
const Project = mongoose.model('Project', {
  title: String,
  description: String,
  images: [{ type: String }],
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
});

// Define resource model
const Resource = mongoose.model('Resource', {
  title: String,
  description: String,
  url: String,
});

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Register user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      name: req.body.name,
      email: req.body.email,
      password: hashedPassword,
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user' });
  }
});

// Login user
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ userId: user._id }, 'secret-key', {
      expiresIn: '1h',
    });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in' });
  }
});

// Create project
app.post('/projects', authenticate, async (req, res) => {
  try {
    const project = new Project({
      title: req.body.title,
      description: req.body.description,
      images: req.body.images,
      userId: req.user._id,
    });
    await project.save();
    res.status(201).send({ message: 'Project created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating project' });
  }
});

// Get all projects
app.get('/projects', authenticate, async (req, res) => {
  try {
    const projects = await Project.find().populate('userId', 'name email');
    res.send(projects);
  } catch (error) {
    res.status(400).send({ message: 'Error getting projects' });
  }
});

// Create resource
app.post('/resources', authenticate, async (req, res) => {
  try {
    const resource = new Resource({
      title: req.body.title,
      description: req.body.description,
      url: req.body.url,
    });
    await resource.save();
    res.status(201).send({ message: 'Resource created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating resource' });
  }
});

// Get all resources
app.get('/resources', authenticate, async (req, res) => {
  try {
    const resources = await Resource.find();
    res.send(resources);
  } catch (error) {
    res.status(400).send({ message: 'Error getting resources' });
  }
});

// Authentication middleware
function authenticate(req, res, next) {
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).send({ message: 'Access denied' });
  }
  try {
    const decoded = jwt.verify(token, 'secret-key');
    req.user = decoded;
    next();
  } catch (error) {
    res.status(400).send({ message: 'Invalid token' });
  }
}

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

**Frontend (React.js)**
------------------------

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [projects, setProjects] = useState([]);
  const [resources, setResources] = useState([]);
  const [token, setToken] = useState('');

  useEffect(() => {
    axios.get('/projects', {
      headers: {
        Authorization: token,
      },
    })
      .then((response) => {
        setProjects(response.data);
      })
      .catch((error) => {
        console.error(error);
      });

    axios.get('/resources', {
      headers: {
        Authorization: token,
      },
    })
      .then((response) => {
        setResources(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, [token]);

  const handleLogin = (email, password) => {
    axios.post('/login', { email, password })
      .then((response) => {
        setToken(response.data.token);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleCreateProject = (title, description, images) => {
    axios.post('/projects', { title, description, images }, {
      headers: {
        Authorization: token,
      },
    })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleCreateResource = (title, description, url) => {
    axios.post('/resources', { title, description, url }, {
      headers: {
        Authorization: token,
      },
    })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Études Architect App</h1>
      <button onClick={() => handleLogin('email', 'password')}>Login</button>
      <form onSubmit={(event) => {
        event.preventDefault();
        handleCreateProject(event.target.title.value, event.target.description.value, event.target.images.value);
      }}>
        <input type="text" name="title" placeholder="Title" />
        <input type="text" name="description" placeholder="Description" />
        <input type="text" name="images" placeholder="Images" />
        <button type="submit">Create Project</button>
      </form>
      <form onSubmit={(event) => {
        event.preventDefault();
        handleCreateResource(event.target.title.value, event.target.description.value, event.target.url.value);
      }}>
        <input type="text" name="title" placeholder="Title" />
        <input type="text" name="description" placeholder="Description" />
        <input type="text" name="url" placeholder="URL" />
        <button type="submit">Create Resource</button>
      </form>
      <h2>Projects</h2>
      <ul>
        {projects.map((project) => (
          <li key={project._id}>{project.title}</li>
        ))}
      </ul>
      <h2>Resources</h2>
      <ul>
        {resources.map((resource) => (
          <li key={resource._id}>{resource.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

**package.json**
-----------------

```json
{
  "name": "etudes-architect-app",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js",
    "client": "npm start --prefix client"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^5.12.3",
    "bcrypt": "^5.0.1",
    "jsonwebtoken": "^8.5.1",
    "axios": "^0.21.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "devDependencies": {
    "nodemon": "^2.0.7"
  }
}
```

**README.md**
--------------

```markdown
# Études Architect App

A web application for collaboration, project showcasing, and architectural resource sharing.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/etudes-architect-app.git`
2. Install dependencies: `npm install`
3. Start the server: `npm start`
4. Start the client: `npm run client`

## Features

* User registration and login
* Project creation and showcasing
* Resource creation and sharing
* Authentication and authorization

## Technologies Used

* Node.js
* Express.js
* MongoDB
* Mongoose
* Bcrypt
* JSON Web Tokens
* React.js
* Axios
```
