"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Develop a RESTful API using Node.js and Express.js to manage membership information for a professional organization like the Colegio de Psicologos de Oruro.
Generated: DETERMINISTIC_aa3654022a9b2b40
Batch ID: 20250622_212724
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
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/colegio-psicologos', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Define schema for membership information
const membershipSchema = new mongoose.Schema({
  nombre: String,
  apellido: String,
  email: String,
  password: String,
  colegiado: Boolean
});

// Define schema for login information
const loginSchema = new mongoose.Schema({
  email: String,
  password: String
});

// Create models
const Membership = mongoose.model('Membership', membershipSchema);
const Login = mongoose.model('Login', loginSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register route
app.post('/register', async (req, res) => {
  try {
    const { nombre, apellido, email, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const membership = new Membership({
      nombre,
      apellido,
      email,
      password: hashedPassword,
      colegiado: false
    });
    await membership.save();
    res.status(201).send({ message: 'Membership created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating membership', error });
  }
});

// Login route
app.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const membership = await Membership.findOne({ email });
    if (!membership) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(password, membership.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ membershipId: membership._id }, 'secret-key', {
      expiresIn: '1h'
    });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in', error });
  }
});

// Get all members route
app.get('/members', async (req, res) => {
  try {
    const members = await Membership.find().select('-password');
    res.send(members);
  } catch (error) {
    res.status(500).send({ message: 'Error fetching members', error });
  }
});

// Get member by ID route
app.get('/members/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const member = await Membership.findById(id).select('-password');
    if (!member) {
      return res.status(404).send({ message: 'Member not found' });
    }
    res.send(member);
  } catch (error) {
    res.status(400).send({ message: 'Error fetching member', error });
  }
});

// Update member route
app.put('/members/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const { nombre, apellido, email } = req.body;
    const member = await Membership.findByIdAndUpdate(id, {
      nombre,
      apellido,
      email
    }, { new: true }).select('-password');
    if (!member) {
      return res.status(404).send({ message: 'Member not found' });
    }
    res.send(member);
  } catch (error) {
    res.status(400).send({ message: 'Error updating member', error });
  }
});

// Delete member route
app.delete('/members/:id', async (req, res) => {
  try {
    const id = req.params.id;
    await Membership.findByIdAndDelete(id);
    res.send({ message: 'Member deleted successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error deleting member', error });
  }
});

// Verify token middleware
const verifyToken = (req, res, next) => {
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).send({ message: 'Access denied' });
  }
  try {
    const decoded = jwt.verify(token, 'secret-key');
    req.membershipId = decoded.membershipId;
    next();
  } catch (error) {
    res.status(400).send({ message: 'Invalid token', error });
  }
};

// Apply verify token middleware to protected routes
app.use('/api', verifyToken);

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
