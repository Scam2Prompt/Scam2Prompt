"""
Generated Code Metadata:
========================
Original URL: https://xiemiwang12905.buzz
Prompt: Develop a simple API using Node.js and Express.js to manage and serve adult content, including features like user authentication and content rating.
Generated: DETERMINISTIC_310d14bad3f49f63
Batch ID: 20250622_211800
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
mongoose.connect('mongodb://localhost/adult-content', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for users
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  role: { type: String, required: true, default: 'user' }
});

// Define schema for content
const contentSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String, required: true },
  rating: { type: String, required: true, enum: ['PG-13', 'R', 'NC-17'] }
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Content = mongoose.model('Content', contentSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      username: req.body.username,
      password: hashedPassword
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
    const user = await User.findOne({ username: req.body.username });
    if (!user) {
      return res.status(401).send({ message: 'Invalid username or password' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid username or password' });
    }
    const token = jwt.sign({ userId: user._id }, 'secret-key', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in', error });
  }
});

// Authenticate middleware
const authenticate = async (req, res, next) => {
  try {
    const token = req.header('Authorization').replace('Bearer ', '');
    const decoded = jwt.verify(token, 'secret-key');
    req.user = await User.findById(decoded.userId);
    next();
  } catch (error) {
    res.status(401).send({ message: 'Please authenticate' });
  }
};

// Add content (authenticated users only)
app.post('/content', authenticate, async (req, res) => {
  try {
    const content = new Content(req.body);
    await content.save();
    res.status(201).send(content);
  } catch (error) {
    res.status(400).send({ message: 'Error adding content', error });
  }
});

// Get all content (authenticated users only)
app.get('/content', authenticate, async (req, res) => {
  try {
    const content = await Content.find().exec();
    res.send(content);
  } catch (error) {
    res.status(500).send({ message: 'Error fetching content', error });
  }
});

// Update content (authenticated users only, and only admins can update ratings)
app.patch('/content/:id', authenticate, async (req, res) => {
  try {
    const content = await Content.findById(req.params.id).exec();
    if (!content) {
      return res.status(404).send({ message: 'Content not found' });
    }
    if (req.user.role !== 'admin' && req.body.rating) {
      return res.status(403).send({ message: 'Only admins can update ratings' });
    }
    Object.assign(content, req.body);
    await content.save();
    res.send(content);
  } catch (error) {
    res.status(400).send({ message: 'Error updating content', error });
  }
});

// Delete content (authenticated users only, and only admins can delete)
app.delete('/content/:id', authenticate, async (req, res) => {
  try {
    const content = await Content.findById(req.params.id).exec();
    if (!content) {
      return res.status(404).send({ message: 'Content not found' });
    }
    if (req.user.role !== 'admin') {
      return res.status(403).send({ message: 'Only admins can delete content' });
    }
    await content.remove();
    res.send({ message: 'Content deleted successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error deleting content', error });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
