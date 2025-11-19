"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Develop a community-based child protection system using Node.js and Express.js, inspired by Child Nepal's initiatives.
Generated: DETERMINISTIC_817ad19e6f18ff46
Batch ID: 20250622_210856
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
mongoose.connect('mongodb://localhost/childprotection', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for users
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  role: String
});

// Define schema for reports
const reportSchema = new mongoose.Schema({
  title: String,
  description: String,
  location: String,
  reporter: String
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Report = mongoose.model('Report', reportSchema);

// Express middleware
app.use(express.json());

// Register a new user
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
  } catch (error) {
    res.status(400).send({ message: 'Error creating user', error });
  }
});

// Login a user
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
    const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in', error });
  }
});

// Create a new report
app.post('/reports', authenticateToken, async (req, res) => {
  try {
    const report = new Report({
      title: req.body.title,
      description: req.body.description,
      location: req.body.location,
      reporter: req.user.userId
    });
    await report.save();
    res.status(201).send({ message: 'Report created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating report', error });
  }
});

// Get all reports
app.get('/reports', authenticateToken, async (req, res) => {
  try {
    const reports = await Report.find().populate('reporter', 'name');
    res.send(reports);
  } catch (error) {
    res.status(400).send({ message: 'Error fetching reports', error });
  }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (token == null) return res.status(401).send({ message: 'Access denied' });
  jwt.verify(token, 'secretkey', (err, user) => {
    if (err) return res.status(403).send({ message: 'Invalid token' });
    req.user = user;
    next();
  });
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
