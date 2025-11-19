"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Build a web application to manage ERP projects and freelancers using a JavaScript framework.
Generated: DETERMINISTIC_078fa1285682d2b8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// server.js - Backend using Express.js
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { errors } = require('celebrate');
const { requestLogger, errorLogger } = require('./middleware/logger');
const errorHandler = require('./middleware/errorHandler');
const routes = require('./routes');

const app = express();
const PORT = process.env.PORT || 5000;

// Security middleware
app.use(helmet());
app.use(cors({
  origin: process.env.CORS_ORIGIN || '*'
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Body parsing
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Logging
app.use(requestLogger);

// Routes
app.use('/api', routes);

// Error logging
app.use(errorLogger);

// Celebrate error handling
app.use(errors());

// Custom error handler
app.use(errorHandler);

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// routes/index.js
const express = require('express');
const router = express.Router();
const authRoutes = require('./auth');
const projectRoutes = require('./projects');
const freelancerRoutes = require('./freelancers');
const { authenticate } = require('../middleware/auth');

router.use('/auth', authRoutes);
router.use('/projects', authenticate, projectRoutes);
router.use('/freelancers', authenticate, freelancerRoutes);

module.exports = router;

// routes/projects.js
const express = require('express');
const router = express.Router();
const { celebrate, Joi } = require('celebrate');
const Project = require('../models/Project');
const { authorizeProject } = require('../middleware/auth');

// Create project
router.post('/', celebrate({
  body: Joi.object({
    name: Joi.string().required(),
    description: Joi.string().required(),
    budget: Joi.number().min(0).required(),
    deadline: Joi.date().iso().required(),
    status: Joi.string().valid('planned', 'active', 'completed', 'cancelled').default('planned')
  })
}), async (req, res, next) => {
  try {
    const project = new Project({
      ...req.body,
      createdBy: req.user._id
    });
    await project.save();
    res.status(201).json(project);
  } catch (err) {
    next(err);
  }
});

// Get all projects
router.get('/', async (req, res, next) => {
  try {
    const projects = await Project.find({ createdBy: req.user._id });
    res.json(projects);
  } catch (err) {
    next(err);
  }
});

// Get single project
router.get('/:id', authorizeProject, async (req, res, next) => {
  try {
    const project = await Project.findById(req.params.id);
    if (!project) {
      return res.status(404).json({ message: 'Project not found' });
    }
    res.json(project);
  } catch (err) {
    next(err);
  }
});

// Update project
router.put('/:id', authorizeProject, celebrate({
  body: Joi.object({
    name: Joi.string(),
    description: Joi.string(),
    budget: Joi.number().min(0),
    deadline: Joi.date().iso(),
    status: Joi.string().valid('planned', 'active', 'completed', 'cancelled')
  })
}), async (req, res, next) => {
  try {
    const project = await Project.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true, runValidators: true }
    );
    res.json(project);
  } catch (err) {
    next(err);
  }
});

// Delete project
router.delete('/:id', authorizeProject, async (req, res, next) => {
  try {
    await Project.findByIdAndDelete(req.params.id);
    res.status(204).end();
  } catch (err) {
    next(err);
  }
});

module.exports = router;

// routes/freelancers.js
const express = require('express');
const router = express.Router();
const { celebrate, Joi } = require('celebrate');
const Freelancer = require('../models/Freelancer');

// Create freelancer
router.post('/', celebrate({
  body: Joi.object({
    name: Joi.string().required(),
    email: Joi.string().email().required(),
    skills: Joi.array().items(Joi.string()).required(),
    hourlyRate: Joi.number().min(0).required(),
    availability: Joi.string().valid('full-time', 'part-time', 'contract').required()
  })
}), async (req, res, next) => {
  try {
    const freelancer = new Freelancer({
      ...req.body,
      addedBy: req.user._id
    });
    await freelancer.save();
    res.status(201).json(freelancer);
  } catch (err) {
    next(err);
  }
});

// Get all freelancers
router.get('/', async (req, res, next) => {
  try {
    const freelancers = await Freelancer.find({ addedBy: req.user._id });
    res.json(freelancers);
  } catch (err) {
    next(err);
  }
});

// Get single freelancer
router.get('/:id', async (req, res, next) => {
  try {
    const freelancer = await Freelancer.findById(req.params.id);
    if (!freelancer) {
      return res.status(404).json({ message: 'Freelancer not found' });
    }
    res.json(freelancer);
  } catch (err) {
    next(err);
  }
});

// Update freelancer
router.put('/:id', celebrate({
  body: Joi.object({
    name: Joi.string(),
    email: Joi.string().email(),
    skills: Joi.array().items(Joi.string()),
    hourlyRate: Joi.number().min(0),
    availability: Joi.string().valid('full-time', 'part-time', 'contract')
  })
}), async (req, res, next) => {
  try {
    const freelancer = await Freelancer.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true, runValidators: true }
    );
    res.json(freelancer);
  } catch (err) {
    next(err);
  }
});

// Delete freelancer
router.delete('/:id', async (req, res, next) => {
  try {
    await Freelancer.findByIdAndDelete(req.params.id);
    res.status(204).end();
  } catch (err) {
    next(err);
  }
});

module.exports = router;

// routes/auth.js
const express = require('express');
const router = express.Router();
const { celebrate, Joi } = require('celebrate');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');

// Register
router.post('/register', celebrate({
  body: Joi.object({
    name: Joi.string().required(),
    email: Joi.string().email().required(),
    password: Joi.string().min(6).required()
  })
}), async (req, res, next) => {
  try {
    const { name, email, password } = req.body;
    
    // Check if user exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({ message: 'User already exists' });
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(password, 12);
    
    // Create user
    const user = new User({
      name,
      email,
      password: hashedPassword
    });
    
    await user.save();
    
    // Generate token
    const token = jwt.sign(
      { userId: user._id },
      process.env.JWT_SECRET,
      { expiresIn: '1h' }
    );
    
    res.status(201).json({ token, userId: user._id });
  } catch (err) {
    next(err);
  }
});

// Login
router.post('/login', celebrate({
  body: Joi.object({
    email: Joi.string().email().required(),
    password: Joi.string().required()
  })
}), async (req, res, next) => {
  try {
    const { email, password } = req.body;
    
    // Find user
    const user = await User.findOne({ email });
