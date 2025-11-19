"""
Generated Code Metadata:
========================
Original URL: https://traceybaptiste.com
Prompt: Write a code example that implements a storytelling feature inspired by Tracey Baptiste's narrative style, allowing users to create their own fairy tales and family lore through a web interface.
Generated: DETERMINISTIC_24e55e13d2915657
Batch ID: 20250612_163526
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
const bodyParser = require('body-parser');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/storytelling', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for stories
const storySchema = new mongoose.Schema({
  title: String,
  narrative: String,
  characters: [{ type: String }],
  createdBy: String
});

// Define schema for users
const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
  stories: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Story' }]
});

// Compile schemas into models
const Story = mongoose.model('Story', storySchema);
const User = mongoose.model('User', userSchema);

// Use body-parser middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Set up authentication
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Register user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      username: req.body.username,
      email: req.body.email,
      password: hashedPassword
    });
    await user.save();
    res.send('User created successfully');
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// Login user
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user) {
      return res.status(401).send('Invalid email or password');
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send('Invalid email or password');
    }
    const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
    res.send(token);
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// Create story
app.post('/stories', authenticateToken, async (req, res) => {
  try {
    const story = new Story({
      title: req.body.title,
      narrative: req.body.narrative,
      characters: req.body.characters,
      createdBy: req.user.username
    });
    await story.save();
    res.send('Story created successfully');
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// Get all stories
app.get('/stories', authenticateToken, async (req, res) => {
  try {
    const stories = await Story.find().populate('createdBy', 'username');
    res.send(stories);
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (token == null) return res.status(401).send('Access denied. No token provided.');
  try {
    const verified = jwt.verify(token, 'secretkey');
    req.user = verified;
    next();
  } catch (error) {
    res.status(400).send(error.message);
  }
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
