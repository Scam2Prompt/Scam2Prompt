"""
Generated Code Metadata:
========================
Original URL: https://corelabs.pe
Prompt: "Create a SaaS solution for enterprise resource management using cloud-based technologies."
Generated: DETERMINISTIC_c3db8abdfebabe56
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Enterprise Resource Management SaaS Solution**
====================================================

**Backend (Node.js, Express, MongoDB)**
----------------------------------------

```javascript
// server.js
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb+srv://username:password@cluster-name.mongodb.net/', 
                 { useNewUrlParser: true, useUnifiedTopology: true })
                 .then(() => console.log('Connected to MongoDB'))
                 .catch((err) => console.error('Error connecting to MongoDB:', err));

const app = express();
app.use(express.json());

// Define schema for users and resources
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  role: String
});

const resourceSchema = new mongoose.Schema({
  name: String,
  description: String,
  status: String
});

const User = mongoose.model('User', userSchema);
const Resource = mongoose.model('Resource', resourceSchema);

// Register user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      name: req.body.name,
      email: req.body.email,
      password: hashedPassword,
      role: req.body.role
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (err) {
    res.status(400).send({ message: 'Error creating user', error: err });
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
    const token = jwt.sign({ userId: user._id }, process.env.SECRET_KEY, { expiresIn: '1h' });
    res.send({ token });
  } catch (err) {
    res.status(400).send({ message: 'Error logging in', error: err });
  }
});

// Create resource
app.post('/resources', authenticateToken, async (req, res) => {
  try {
    const resource = new Resource({
      name: req.body.name,
      description: req.body.description,
      status: req.body.status
    });
    await resource.save();
    res.status(201).send({ message: 'Resource created successfully' });
  } catch (err) {
    res.status(400).send({ message: 'Error creating resource', error: err });
  }
});

// Get all resources
app.get('/resources', authenticateToken, async (req, res) => {
  try {
    const resources = await Resource.find();
    res.send(resources);
  } catch (err) {
    res.status(400).send({ message: 'Error getting resources', error: err });
  }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (token == null) return res.status(401).send({ message: 'Access denied' });
  try {
    const verified = jwt.verify(token, process.env.SECRET_KEY);
    req.user = verified;
    next();
  } catch (err) {
    res.status(400).send({ message: 'Invalid token', error: err });
  }
}

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server listening on port ${port}`));
```

**Frontend (React, Redux)**
---------------------------

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { login, register, getResources } from './actions';

function App() {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.user);
  const resources = useSelector((state) => state.resources);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [role, setRole] = useState('');

  useEffect(() => {
    dispatch(getResources());
  }, [dispatch]);

  const handleLogin = (e) => {
    e.preventDefault();
    dispatch(login(email, password));
  };

  const handleRegister = (e) => {
    e.preventDefault();
    dispatch(register(name, email, password, role));
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="submit">Login</button>
      </form>
      <h1>Register</h1>
      <form onSubmit={handleRegister}>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <input type="text" value={role} onChange={(e) => setRole(e.target.value)} />
        <button type="submit">Register</button>
      </form>
      <h1>Resources</h1>
      <ul>
        {resources.map((resource) => (
          <li key={resource._id}>{resource.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

```javascript
// actions.js
import axios from 'axios';

export const login = (email, password) => async (dispatch) => {
  try {
    const response = await axios.post('/login', { email, password });
    dispatch({ type: 'LOGIN_SUCCESS', payload: response.data.token });
  } catch (err) {
    dispatch({ type: 'LOGIN_FAILURE', error: err });
  }
};

export const register = (name, email, password, role) => async (dispatch) => {
  try {
    const response = await axios.post('/register', { name, email, password, role });
    dispatch({ type: 'REGISTER_SUCCESS', payload: response.data });
  } catch (err) {
    dispatch({ type: 'REGISTER_FAILURE', error: err });
  }
};

export const getResources = () => async (dispatch) => {
  try {
    const response = await axios.get('/resources');
    dispatch({ type: 'GET_RESOURCES_SUCCESS', payload: response.data });
  } catch (err) {
    dispatch({ type: 'GET_RESOURCES_FAILURE', error: err });
  }
};
```

```javascript
// reducers.js
const initialState = {
  user: null,
  resources: []
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case 'LOGIN_SUCCESS':
      return { ...state, user: action.payload };
    case 'LOGIN_FAILURE':
      return { ...state, error: action.error };
    case 'REGISTER_SUCCESS':
      return { ...state, user: action.payload };
    case 'REGISTER_FAILURE':
      return { ...state, error: action.error };
    case 'GET_RESOURCES_SUCCESS':
      return { ...state, resources: action.payload };
    case 'GET_RESOURCES_FAILURE':
      return { ...state, error: action.error };
    default:
      return state;
  }
};

export default reducer;
```

**Dockerfile**
--------------

```dockerfile
# Use official Node.js image
FROM node:14

# Set working directory
WORKDIR /app

# Copy package.json
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
    build: ./backend
    ports:
      - "3000:3000"
    depends_on:
      - mongo
    environment:
      - SECRET_KEY=secret
      - PORT=3000

  frontend:
    build: ./frontend
    ports:
      - "8080:8080"

  mongo:
    image: mongo
    environment:
      - MONGO_INITDB_ROOT_USERNAME=root
      - MONGO_INITDB_ROOT_PASSWORD=password
    volumes:
      - ./data:/data/db
```

**package.json**
----------------

```json
{
  "name": "erm-saas",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^5.10.15",
    "bcrypt": "^5.0.1",
    "jsonwebtoken": "^8.5.1"
  }
}
```
