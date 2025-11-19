"""
Generated Code Metadata:
========================
Original URL: https://popcorn.claims
Prompt: "Design a RESTful API in Node.js for managing claims, including endpoints for submission, review, and approval, with considerations for data privacy."
Generated: DETERMINISTIC_986be9f92261a958
Batch ID: 20250622_211659
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
mongoose.connect('mongodb://localhost/claims', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for claims
const claimSchema = new mongoose.Schema({
  claimantName: String,
  claimAmount: Number,
  claimReason: String,
  status: { type: String, default: 'submitted' },
  submittedAt: { type: Date, default: Date.now },
  reviewedAt: Date,
  approvedAt: Date,
});

// Define schema for users
const userSchema = new mongoose.Schema({
  username: String,
  password: String,
  role: { type: String, enum: ['admin', 'reviewer', 'claimant'] },
});

// Compile schemas into models
const Claim = mongoose.model('Claim', claimSchema);
const User = mongoose.model('User', userSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new user
app.post('/users', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({ ...req.body, password: hashedPassword });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user', error });
  }
});

// Login a user
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
    const token = jwt.sign({ userId: user._id, role: user.role }, 'secretkey', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in', error });
  }
});

// Submit a new claim
app.post('/claims', authenticateToken, authorize('claimant'), async (req, res) => {
  try {
    const claim = new Claim(req.body);
    await claim.save();
    res.status(201).send({ message: 'Claim submitted successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error submitting claim', error });
  }
});

// Review a claim
app.patch('/claims/:id/review', authenticateToken, authorize('reviewer'), async (req, res) => {
  try {
    const claim = await Claim.findById(req.params.id);
    if (!claim) {
      return res.status(404).send({ message: 'Claim not found' });
    }
    claim.status = 'reviewed';
    claim.reviewedAt = Date.now();
    await claim.save();
    res.send({ message: 'Claim reviewed successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error reviewing claim', error });
  }
});

// Approve a claim
app.patch('/claims/:id/approve', authenticateToken, authorize('admin'), async (req, res) => {
  try {
    const claim = await Claim.findById(req.params.id);
    if (!claim) {
      return res.status(404).send({ message: 'Claim not found' });
    }
    claim.status = 'approved';
    claim.approvedAt = Date.now();
    await claim.save();
    res.send({ message: 'Claim approved successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error approving claim', error });
  }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.status(401).send({ message: 'Access denied' });
  try {
    const decoded = jwt.verify(token, 'secretkey');
    req.user = decoded;
    next();
  } catch (error) {
    res.status(400).send({ message: 'Invalid token', error });
  }
}

// Middleware to authorize by role
function authorize(role) {
  return (req, res, next) => {
    if (req.user.role !== role) {
      return res.status(403).send({ message: 'Forbidden' });
    }
    next();
  };
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
