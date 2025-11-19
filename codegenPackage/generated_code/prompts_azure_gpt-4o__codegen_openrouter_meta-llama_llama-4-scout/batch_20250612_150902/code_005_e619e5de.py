"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Create a web application for downloading medical concepts related to occupational health, similar to the platform described on Medicid IPS's website, with user authentication and secure data access.
Generated: DETERMINISTIC_e619e5de604ae488
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Medical Concept Downloader Web Application**
=====================================================

**Backend (Node.js and Express)**
---------------------------------

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const helmet = require('helmet');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/medical-concepts', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define user schema
const userSchema = new mongoose.Schema({
  username: String,
  password: String,
  role: String,
});

// Define medical concept schema
const conceptSchema = new mongoose.Schema({
  id: String,
  name: String,
  description: String,
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Concept = mongoose.model('Concept', conceptSchema);

// Enable JSON parsing for incoming requests
app.use(express.json());

// Enable security headers
app.use(helmet());

// Register user endpoint
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      username: req.body.username,
      password: hashedPassword,
      role: 'user',
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user' });
  }
});

// Login user endpoint
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ username: req.body.username });
    if (!user) {
      return res.status(401).send({ message: 'Invalid credentials' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid credentials' });
    }
    const token = jwt.sign({ userId: user._id }, process.env.SECRET_KEY, {
      expiresIn: '1h',
    });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in' });
  }
});

// Authenticate middleware
const authenticate = async (req, res, next) => {
  try {
    const token = req.header('Authorization').replace('Bearer ', '');
    const decoded = jwt.verify(token, process.env.SECRET_KEY);
    req.user = await User.findById(decoded.userId);
    next();
  } catch (error) {
    res.status(401).send({ message: 'Please authenticate' });
  }
};

// Download medical concept endpoint
app.get('/concepts/:id', authenticate, async (req, res) => {
  try {
    const concept = await Concept.findById(req.params.id);
    if (!concept) {
      return res.status(404).send({ message: 'Concept not found' });
    }
    res.send(concept);
  } catch (error) {
    res.status(500).send({ message: 'Error downloading concept' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (React)**
-------------------

```javascript
// Import required modules
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Login component
const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/login', { username, password });
      localStorage.setItem('token', response.data.token);
    } catch (error) {
      setError('Invalid credentials');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={username}
        onChange={(event) => setUsername(event.target.value)}
        placeholder="Username"
      />
      <input
        type="password"
        value={password}
        onChange={(event) => setPassword(event.target.value)}
        placeholder="Password"
      />
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <button type="submit">Login</button>
    </form>
  );
};

// Concept downloader component
const ConceptDownloader = () => {
  const [conceptId, setConceptId] = useState('');
  const [concept, setConcept] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      return;
    }
    axios.get(`/concepts/${conceptId}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((response) => {
        setConcept(response.data);
      })
      .catch((error) => {
        setError('Error downloading concept');
      });
  }, [conceptId]);

  const handleDownload = () => {
    // Download concept logic here
  };

  return (
    <div>
      <input
        type="text"
        value={conceptId}
        onChange={(event) => setConceptId(event.target.value)}
        placeholder="Concept ID"
      />
      {concept && (
        <div>
          <h2>{concept.name}</h2>
          <p>{concept.description}</p>
        </div>
      )}
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <button onClick={handleDownload}>Download</button>
    </div>
  );
};

// App component
const App = () => {
  return (
    <div>
      <Login />
      <ConceptDownloader />
    </div>
  );
};

export default App;
```

**Dockerfile**
-------------

```dockerfile
# Use official Node.js image
FROM node:14

# Set working directory
WORKDIR /app

# Copy package*.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Run command
CMD ["node", "server.js"]
```

**docker-compose.yml**
----------------------

```yml
version: '3'
services:
  backend:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - mongo
    environment:
      - SECRET_KEY=your_secret_key

  frontend:
    build: ./frontend
    ports:
      - "8080:8080"

  mongo:
    image: mongo:latest
    volumes:
      - ./data:/data/db
```
