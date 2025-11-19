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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware setup
app.use(helmet());
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Models
const User = mongoose.model('User', new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  role: { type: String, enum: ['admin', 'community_worker', 'parent'], default: 'parent' },
  phone: { type: String },
  address: { type: String },
  createdAt: { type: Date, default: Date.now }
}));

const Report = mongoose.model('Report', new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  title: { type: String, required: true },
  description: { type: String, required: true },
  location: { type: String, required: true },
  severity: { type: String, enum: ['low', 'medium', 'high'], default: 'medium' },
  status: { type: String, enum: ['pending', 'investigating', 'resolved'], default: 'pending' },
  reporterId: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
}));

const Resource = mongoose.model('Resource', new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  title: { type: String, required: true },
  description: { type: String, required: true },
  url: { type: String, required: true },
  category: { type: String, enum: ['education', 'health', 'legal', 'safety'], required: true },
  createdAt: { type: Date, default: Date.now }
}));

// Authentication middleware
const authenticate = (req, res, next) => {
  const token = req.header('Authorization')?.replace('Bearer ', '');
  if (!token) return res.status(401).send({ error: 'Authentication required' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).send({ error: 'Invalid token' });
  }
};

// Authorization middleware
const authorize = (roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).send({ error: 'Access denied' });
    }
    next();
  };
};

// Routes
app.post('/api/auth/register', async (req, res) => {
  try {
    const { name, email, password, role, phone, address } = req.body;
    
    // Validate input
    if (!name || !email || !password) {
      return res.status(400).send({ error: 'Name, email, and password are required' });
    }

    // Check if user exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).send({ error: 'Email already in use' });
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create user
    const user = new User({
      name,
      email,
      password: hashedPassword,
      role: role || 'parent',
      phone,
      address
    });

    await user.save();

    // Generate token
    const token = jwt.sign({ id: user._id, role: user.role }, process.env.JWT_SECRET, {
      expiresIn: '7d'
    });

    res.status(201).send({ user: { id: user._id, name: user.name, email: user.email, role: user.role }, token });
  } catch (err) {
    res.status(500).send({ error: 'Registration failed' });
  }
});

app.post('/api/auth/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    // Validate input
    if (!email || !password) {
      return res.status(400).send({ error: 'Email and password are required' });
    }

    // Find user
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).send({ error: 'Invalid credentials' });
    }

    // Check password
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(401).send({ error: 'Invalid credentials' });
    }

    // Generate token
    const token = jwt.sign({ id: user._id, role: user.role }, process.env.JWT_SECRET, {
      expiresIn: '7d'
    });

    res.send({ user: { id: user._id, name: user.name, email: user.email, role: user.role }, token });
  } catch (err) {
    res.status(500).send({ error: 'Login failed' });
  }
});

// Report routes
app.post('/api/reports', authenticate, async (req, res) => {
  try {
    const { title, description, location, severity } = req.body;

    // Validate input
    if (!title || !description || !location) {
      return res.status(400).send({ error: 'Title, description, and location are required' });
    }

    // Create report
    const report = new Report({
      title,
      description,
      location,
      severity: severity || 'medium',
      reporterId: req.user.id
    });

    await report.save();

    res.status(201).send(report);
  } catch (err) {
    res.status(500).send({ error: 'Failed to create report' });
  }
});

app.get('/api/reports', authenticate, async (req, res) => {
  try {
    let query = {};
    
    // Community workers can only see reports from their area
    if (req.user.role === 'community_worker') {
      query = { status: { $ne: 'resolved' } };
    }
    
    // Parents can only see their own reports
    if (req.user.role === 'parent') {
      query = { reporterId: req.user.id };
    }

    const reports = await Report.find(query).sort({ createdAt: -1 });
    res.send(reports);
  } catch (err) {
    res.status(500).send({ error: 'Failed to fetch reports' });
  }
});

app.put('/api/reports/:id', authenticate, authorize(['admin', 'community_worker']), async (req, res) => {
  try {
    const { status } = req.body;
    const report = await Report.findByIdAndUpdate(
      req.params.id,
      { status, updatedAt: Date.now() },
      { new: true }
    );

    if (!report) {
      return res.status(404).send({ error: 'Report not found' });
    }

    res.send(report);
  } catch (err) {
    res.status(500).send({ error: 'Failed to update report' });
  }
});

// Resource routes
app.post('/api/resources', authenticate, authorize(['admin']), async (req, res) => {
  try {
    const { title, description, url, category } = req.body;

    // Validate input
    if (!title || !description || !url || !category) {
      return res.status(400).send({ error: 'All fields are required' });
    }

    const resource = new Resource({
      title,
      description,
      url,
      category
    });

    await resource.save();
    res.status(201).send(resource);
  } catch (err) {
    res.status(500).send({ error: 'Failed to create resource' });
  }
});

app.get('/api/resources', async (req, res) => {
  try {
    const { category } = req.query;
    let query = {};
