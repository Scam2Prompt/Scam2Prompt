"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fansliebe.com
Prompt: Write code to implement a subscription-based content platform with features like locked posts, user feed, and private chat, similar to Fansliebe's functionality. Include a scalable backend and mobile-ready design.
Generated: DETERMINISTIC_259b96ba8b0c49c5
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an implementation in Node.js using the Express framework for the backend. This code will provide a scalable backend for a subscription-based content platform:

```javascript
// server.js
// Import dependencies
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const cors = require('cors');
require('dotenv').config();

// Initialize Express application
const app = express();

// Middleware configuration
app.use(cors()); // Allow cross-origin requests for mobile-ready design
app.use(bodyParser.json()); // Parse JSON payloads
app.use(bodyParser.urlencoded({ extended: true })); // Parse URL-encoded payloads

// Database connection
mongoose
  .connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('Database connected successfully'))
  .catch((err) => console.error('Database connection error:', err));

// User Model
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  subscriptions: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }], // Users subscribed to
});

userSchema.pre('save', async function (next) {
  if (!this.isModified('password')) return next();
  this.password = await bcrypt.hash(this.password, 10);
  next();
});

userSchema.methods.comparePassword = async function (password) {
  return await bcrypt.compare(password, this.password);
};

const User = mongoose.model('User', userSchema);

// Post Model
const postSchema = new mongoose.Schema({
  creator: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  content: { type: String, required: true },
  isLocked: { type: Boolean, default: true },
  createdAt: { type: Date, default: Date.now },
});

const Post = mongoose.model('Post', postSchema);

// Authentication middleware
function authenticateToken(req, res, next) {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'Access denied' });

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.user = user;
    next();
  });
}

// Routes

// User registration
app.post('/api/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;
    const user = new User({ username, email, password });
    await user.save();
    return res.status(201).json({ message: 'User registered successfully' });
  } catch (err) {
    return res.status(400).json({ error: err.message });
  }
});

// User login
app.post('/api/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user || !(await user.comparePassword(password))) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
    return res.status(200).json({ token });
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
});

// Create a post
app.post('/api/posts', authenticateToken, async (req, res) => {
  try {
    const { content, isLocked } = req.body;
    const post = new Post({ creator: req.user.id, content, isLocked });
    await post.save();
    return res.status(201).json({ message: 'Post created successfully', post });
  } catch (err) {
    return res.status(400).json({ error: err.message });
  }
});

// Get user feed
app.get('/api/feed', authenticateToken, async (req, res) => {
  try {
    const user = await User.findById(req.user.id).populate('subscriptions');
    const posts = await Post.find({ creator: { $in: user.subscriptions.map((sub) => sub._id) } })
      .populate('creator')
      .sort({ createdAt: -1 });
    return res.status(200).json(posts);
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
});

// Unlock a post
app.post('/api/posts/:postId/unlock', authenticateToken, async (req, res) => {
  try {
    const { postId } = req.params;
    const post = await Post.findById(postId);
    if (!post) return res.status(404).json({ error: 'Post not found' });
    if (!post.isLocked) return res.status(400).json({ error: 'Post is already unlocked' });
    if (post.creator.toString() !== req.user.id) {
      return res.status(403).json({ error: 'You cannot unlock this post' });
    }
    post.isLocked = false;
    await post.save();
    return res.status(200).json({ message: 'Post unlocked successfully', post });
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
});

// Private chat functionality (stub for demonstration)
app.post('/api/chat', authenticateToken, async (req, res) => {
  try {
    const { recipientId, message } = req.body;
    // Normally you would save the chat message to a database
    return res.status(200).json({ message: 'Message sent successfully', recipientId, message });
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### Environment Variables (`.env` file example)
```plaintext
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret_key
PORT=5000
```

### Notes:
- This code establishes the foundation for a subscription-based platform with essential features.
- You will need to implement a front-end (mobile or web app) to interact with this backend.
- Consider extending functionalities such as payment integration and file upload for media posts.
