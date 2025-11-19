"""
Generated Code Metadata:
========================
Original URL: https://lsinterior.com.my
Prompt: Generate a code snippet for a web application that allows users to request home renovation services, including features for space planning and project management.
Generated: DETERMINISTIC_6479bb2d9d9dd5c1
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Home Renovation Service Request Web Application**
=====================================================

**Backend (Node.js, Express.js)**
---------------------------------

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/home-renovation', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for user model
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
});

// Define schema for service request model
const serviceRequestSchema = new mongoose.Schema({
  userId: String,
  spaceType: String,
  spaceSize: String,
  renovationType: String,
  description: String,
  status: String,
});

// Define schema for project model
const projectSchema = new mongoose.Schema({
  serviceRequestId: String,
  projectManagerId: String,
  status: String,
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const ServiceRequest = mongoose.model('ServiceRequest', serviceRequestSchema);
const Project = mongoose.model('Project', projectSchema);

// Middleware to parse JSON bodies
app.use(express.json());

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
    const token = jwt.sign({ userId: user._id }, 'secretkey', {
      expiresIn: '1h',
    });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in' });
  }
});

// Request home renovation service
app.post('/service-requests', authenticateToken, async (req, res) => {
  try {
    const serviceRequest = new ServiceRequest({
      userId: req.user.userId,
      spaceType: req.body.spaceType,
      spaceSize: req.body.spaceSize,
      renovationType: req.body.renovationType,
      description: req.body.description,
      status: 'pending',
    });
    await serviceRequest.save();
    res.status(201).send({ message: 'Service request created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating service request' });
  }
});

// Get all service requests for a user
app.get('/service-requests', authenticateToken, async (req, res) => {
  try {
    const serviceRequests = await ServiceRequest.find({ userId: req.user.userId });
    res.send(serviceRequests);
  } catch (error) {
    res.status(400).send({ message: 'Error fetching service requests' });
  }
});

// Create project for a service request
app.post('/projects', authenticateToken, async (req, res) => {
  try {
    const project = new Project({
      serviceRequestId: req.body.serviceRequestId,
      projectManagerId: req.body.projectManagerId,
      status: 'in_progress',
    });
    await project.save();
    res.status(201).send({ message: 'Project created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating project' });
  }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
  const token = req.header('x-auth-token');
  if (!token) {
    return res.status(401).send({ message: 'Access denied' });
  }
  try {
    const decoded = jwt.verify(token, 'secretkey');
    req.user = decoded;
    next();
  } catch (error) {
    res.status(400).send({ message: 'Invalid token' });
  }
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (React.js)**
------------------------

```javascript
// Import required modules
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Register user
const Register = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/register', {
        name,
        email,
        password,
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
      </label>
      <br />
      <label>
        Email:
        <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Register</button>
    </form>
  );
};

// Login user
const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/login', {
        email,
        password,
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email:
        <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Login</button>
    </form>
  );
};

// Request home renovation service
const ServiceRequestForm = () => {
  const [spaceType, setSpaceType] = useState('');
  const [spaceSize, setSpaceSize] = useState('');
  const [renovationType, setRenovationType] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const token = localStorage.getItem('token');
      const response = await axios.post('/service-requests', {
        spaceType,
        spaceSize,
        renovationType,
        description,
      }, {
        headers: {
          'x-auth-token': token,
        },
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Space Type:
        <input type="text" value={spaceType} onChange={(event) => setSpaceType(event.target.value)} />
      </label>
      <br />
      <label>
        Space Size:
        <input type="text" value={spaceSize} onChange={(event) => setSpaceSize(event.target.value)} />
      </label>
      <br />
      <label>
        Renovation Type:
        <input type="text" value={renovationType} onChange={(event) => setRenovationType(event.target.value)} />
      </label>
      <br />
      <label>
        Description:
        <textarea value={description} onChange={(event) => setDescription(event.target.value)} />
      </label>
      <br />
      <button type="submit">Request Service</button>
    </form>
  );
};
```
