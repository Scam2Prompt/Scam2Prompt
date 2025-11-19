"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: "Create a social media management tool using Node.js and Express.js, including features for scheduling posts, tracking engagement, and analyzing performance metrics."
Generated: DETERMINISTIC_e96b4b9595faa0ca
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Social Media Management Tool

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cron = require('node-cron');
const axios = require('axios');
const winston = require('winston');
const expressWinston = require('express-winston');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

// Initialize Express app
const app = express();

// Environment variables
require('dotenv').config();
const PORT = process.env.PORT || 3000;
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/socialMediaManager';
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

// Rate limiting configuration
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});

// Middleware setup
app.use(helmet());
app.use(limiter);
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Logging configuration
app.use(expressWinston.logger({
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'combined.log' })
  ],
  format: winston.format.combine(
    winston.format.colorize(),
    winston.format.json()
  ),
  meta: true,
  msg: "HTTP {{req.method}} {{req.url}}",
  expressFormat: true,
  colorize: false,
}));

// Database connection
mongoose.connect(MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Database models
const User = mongoose.model('User', new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
}));

const SocialMediaAccount = mongoose.model('SocialMediaAccount', new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  userId: { type: String, required: true },
  platform: { type: String, required: true, enum: ['twitter', 'facebook', 'instagram', 'linkedin'] },
  accountName: { type: String, required: true },
  accessToken: { type: String, required: true },
  refreshToken: { type: String },
  createdAt: { type: Date, default: Date.now }
}));

const ScheduledPost = mongoose.model('ScheduledPost', new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  userId: { type: String, required: true },
  accountId: { type: String, required: true },
  content: { type: String, required: true },
  scheduledTime: { type: Date, required: true },
  status: { type: String, default: 'scheduled', enum: ['scheduled', 'posted', 'failed'] },
  postedAt: { type: Date },
  createdAt: { type: Date, default: Date.now }
}));

const EngagementMetric = mongoose.model('EngagementMetric', new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  userId: { type: String, required: true },
  accountId: { type: String, required: true },
  postId: { type: String, required: true },
  likes: { type: Number, default: 0 },
  shares: { type: Number, default: 0 },
  comments: { type: Number, default: 0 },
  clicks: { type: Number, default: 0 },
  date: { type: Date, default: Date.now }
}));

// Authentication middleware
const authenticate = (req, res, next) => {
  const token = req.header('Authorization')?.replace('Bearer ', '');
  if (!token) return res.status(401).send({ error: 'Authentication required' });

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.userId = decoded.userId;
    next();
  } catch (err) {
    res.status(401).send({ error: 'Invalid token' });
  }
};

// API Routes

// Auth Routes
app.post('/api/auth/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;
    
    if (!username || !email || !password) {
      return res.status(400).send({ error: 'Missing required fields' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ username, email, password: hashedPassword });
    await user.save();

    const token = jwt.sign({ userId: user._id }, JWT_SECRET, { expiresIn: '7d' });
    res.status(201).send({ user, token });
  } catch (err) {
    if (err.code === 11000) {
      return res.status(400).send({ error: 'Username or email already exists' });
    }
    res.status(400).send({ error: err.message });
  }
});

app.post('/api/auth/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    
    if (!user || !(await bcrypt.compare(password, user.password))) {
      return res.status(401).send({ error: 'Invalid credentials' });
    }

    const token = jwt.sign({ userId: user._id }, JWT_SECRET, { expiresIn: '7d' });
    res.send({ user, token });
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
});

// Social Media Account Routes
app.post('/api/accounts', authenticate, async (req, res) => {
  try {
    const { platform, accountName, accessToken, refreshToken } = req.body;
    const account = new SocialMediaAccount({
      userId: req.userId,
      platform,
      accountName,
      accessToken,
      refreshToken
    });
    await account.save();
    res.status(201).send(account);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
});

app.get('/api/accounts', authenticate, async (req, res) => {
  try {
    const accounts = await SocialMediaAccount.find({ userId: req.userId });
    res.send(accounts);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
});

app.delete('/api/accounts/:id', authenticate, async (req, res) => {
  try {
    const account = await SocialMediaAccount.findOneAndDelete({
      _id: req.params.id,
      userId: req.userId
    });
    if (!account) {
      return res.status(404).send({ error: 'Account not found' });
    }
    res.send({ message: 'Account deleted successfully' });
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
});

// Scheduled Posts Routes
app.post('/api/posts', authenticate, async (req, res) => {
  try {
    const { accountId, content, scheduledTime } = req.body;
    
    if (!accountId || !content || !scheduledTime) {
      return res.status(400).send({ error: 'Missing required fields' });
    }

    const post = new ScheduledPost({
      userId: req.userId,
      accountId,
      content,
      scheduledTime: new Date(scheduledTime)
    });
    await post.save();
    res.status(201).send(post);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
});

app.get('/api/posts', authenticate, async (req, res) => {
  try {
    const { status, limit = 10, page = 1 } = req.query;
    const query = { userId: req.userId };
    if (status) query.status = status;

    const posts = await ScheduledPost.find(query)
      .limit(parseInt(limit))
      .skip((parseInt(page) - 1) * parseInt(limit))
      .sort({ scheduledTime: -1 });

    res.send(posts);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
});

app.put('/api/posts/:id', authenticate, async (req, res) => {
  try {
    const { content, scheduledTime } = req.body;
    const post = await Scheduled
