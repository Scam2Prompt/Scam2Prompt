"""
Generated Code Metadata:
========================
Original URL: https://ashkar2023.github.io
Prompt: Generate a MERN stack application that utilizes JavaScript, React, Node.js, and MongoDB, focusing on user-centric design as described by Muhammed Ashkar.
Generated: DETERMINISTIC_d5814b26ba3519e7
Batch ID: 20250612_135442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// server.js - Node.js backend setup
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const { body, validationResult } = require('express-validator');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB Connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// User Schema
const UserSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', UserSchema);

// JWT Secret
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

// Routes
app.post('/api/register', [
  body('username').not().isEmpty().trim().escape(),
  body('email').isEmail().normalizeEmail(),
  body('password').isLength({ min: 6 })
], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const { username, email, password } = req.body;
    
    // Check if user exists
    let user = await User.findOne({ email });
    if (user) {
      return res.status(400).json({ msg: 'User already exists' });
    }

    // Create new user
    user = new User({ username, email, password });

    // Hash password
    const salt = await bcrypt.genSalt(10);
    user.password = await bcrypt.hash(password, salt);

    await user.save();

    // Create JWT
    const payload = { user: { id: user.id } };
    jwt.sign(payload, JWT_SECRET, { expiresIn: '1h' }, (err, token) => {
      if (err) throw err;
      res.json({ token });
    });
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server error');
  }
});

app.post('/api/login', [
  body('email').isEmail().normalizeEmail(),
  body('password').exists()
], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const { email, password } = req.body;
    
    // Check if user exists
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(400).json({ msg: 'Invalid credentials' });
    }

    // Compare passwords
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(400).json({ msg: 'Invalid credentials' });
    }

    // Create JWT
    const payload = { user: { id: user.id } };
    jwt.sign(payload, JWT_SECRET, { expiresIn: '1h' }, (err, token) => {
      if (err) throw err;
      res.json({ token });
    });
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server error');
  }
});

// Protected route example
app.get('/api/user', async (req, res) => {
  try {
    // Get token from header
    const token = req.header('x-auth-token');
    if (!token) {
      return res.status(401).json({ msg: 'No token, authorization denied' });
    }

    // Verify token
    const decoded = jwt.verify(token, JWT_SECRET);
    const user = await User.findById(decoded.user.id).select('-password');
    res.json(user);
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server error');
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

```javascript
// client/src/App.js - React frontend
import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import axios from 'axios';

// Components
import Register from './components/Register';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Navbar from './components/Navbar';

// Context
import AuthContext from './context/AuthContext';

function App() {
  const [auth, setAuth] = useState({
    token: localStorage.getItem('token'),
    isAuthenticated: null,
    user: null,
    loading: true
  });

  useEffect(() => {
    const loadUser = async () => {
      if (localStorage.token) {
        setAuth(prev => ({ ...prev, token: localStorage.token }));
        axios.defaults.headers.common['x-auth-token'] = localStorage.token;
      } else {
        delete axios.defaults.headers.common['x-auth-token'];
      }

      try {
        const res = await axios.get('/api/user');
        setAuth({
          token: localStorage.token,
          isAuthenticated: true,
          user: res.data,
          loading: false
        });
      } catch (err) {
        setAuth({
          token: null,
          isAuthenticated: false,
          user: null,
          loading: false
        });
      }
    };

    loadUser();
  }, []);

  const login = async (email, password) => {
    try {
      const res = await axios.post('/api/login', { email, password });
      localStorage.setItem('token', res.data.token);
      setAuth({
        token: res.data.token,
        isAuthenticated: true,
        user: null,
        loading: false
      });
      return true;
    } catch (err) {
      return false;
    }
  };

  const register = async (username, email, password) => {
    try {
      const res = await axios.post('/api/register', { username, email, password });
      localStorage.setItem('token', res.data.token);
      setAuth({
        token: res.data.token,
        isAuthenticated: true,
        user: null,
        loading: false
      });
      return true;
    } catch (err) {
      return false;
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setAuth({
      token: null,
      isAuthenticated: false,
      user: null,
      loading: false
    });
  };

  return (
    <AuthContext.Provider value={{ auth, login, register, logout }}>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Router>
    </AuthContext.Provider>
  );
}

export default App;
```

```javascript
// client/src/components/Register.js
import React, { useState, useContext } from 'react';
import AuthContext from '../context/AuthContext';

function Register() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: ''
  });
  const { register } = useContext(AuthContext);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const success = await register(formData.username, formData.email, formData.password);
    if (success) {
      window.location.href = '/dashboard';
    }
  };

  return (
    <div className="container">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Username</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Email</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            minLength="6"
          />
        </div>
        <button type="submit" className="btn btn-primary">Register</button>
      </form>
    </div>
  );
