"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.net
Prompt: Create a RESTful API in Node.js to manage environmental policies and goals for an organization focused on Umweltschutz, incorporating features similar to those implied on the website.
Generated: DETERMINISTIC_b7ea0d940644c4f8
Batch ID: 20250622_204803
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
const cors = require('cors');
const dotenv = require('dotenv');
const { validationResult } = require('express-validator');
const { check } = require('express-validator');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Policy Schema
const policySchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true
  },
  description: {
    type: String,
    required: true,
    trim: true
  },
  category: {
    type: String,
    required: true,
    enum: ['energy', 'waste', 'water', 'biodiversity', 'transport']
  },
  targetDate: {
    type: Date,
    required: true
  },
  status: {
    type: String,
    required: true,
    enum: ['planned', 'in-progress', 'completed', 'delayed'],
    default: 'planned'
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Define Goal Schema
const goalSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  description: {
    type: String,
    required: true,
    trim: true
  },
  targetValue: {
    type: Number,
    required: true
  },
  currentValue: {
    type: Number,
    required: true,
    default: 0
  },
  unit: {
    type: String,
    required: true
  },
  deadline: {
    type: Date,
    required: true
  },
  relatedPolicies: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Policy'
  }],
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Create models
const Policy = mongoose.model('Policy', policySchema);
const Goal = mongoose.model('Goal', goalSchema);

// Validation middleware for Policy
const validatePolicy = [
  check('title').not().isEmpty().withMessage('Title is required'),
  check('description').not().isEmpty().withMessage('Description is required'),
  check('category').isIn(['energy', 'waste', 'water', 'biodiversity', 'transport']).withMessage('Invalid category'),
  check('targetDate').isISO8601().withMessage('Invalid date format'),
  check('status').optional().isIn(['planned', 'in-progress', 'completed', 'delayed'])
];

// Validation middleware for Goal
const validateGoal = [
  check('name').not().isEmpty().withMessage('Name is required'),
  check('description').not().isEmpty().withMessage('Description is required'),
  check('targetValue').isNumeric().withMessage('Target value must be a number'),
  check('currentValue').optional().isNumeric().withMessage('Current value must be a number'),
  check('unit').not().isEmpty().withMessage('Unit is required'),
  check('deadline').isISO8601().withMessage('Invalid date format')
];

// Routes for Policies
app.route('/api/policies')
  .get(async (req, res) => {
    try {
      const policies = await Policy.find();
      res.json(policies);
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  })
  .post(validatePolicy, async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    try {
      const policy = new Policy(req.body);
      await policy.save();
      res.status(201).json(policy);
    } catch (err) {
      res.status(400).json({ message: err.message });
    }
  });

app.route('/api/policies/:id')
  .get(async (req, res) => {
    try {
      const policy = await Policy.findById(req.params.id);
      if (!policy) {
        return res.status(404).json({ message: 'Policy not found' });
      }
      res.json(policy);
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  })
  .put(validatePolicy, async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    try {
      const policy = await Policy.findByIdAndUpdate(
        req.params.id,
        { ...req.body, updatedAt: Date.now() },
        { new: true }
      );
      if (!policy) {
        return res.status(404).json({ message: 'Policy not found' });
      }
      res.json(policy);
    } catch (err) {
      res.status(400).json({ message: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const policy = await Policy.findByIdAndDelete(req.params.id);
      if (!policy) {
        return res.status(404).json({ message: 'Policy not found' });
      }
      res.json({ message: 'Policy deleted successfully' });
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  });

// Routes for Goals
app.route('/api/goals')
  .get(async (req, res) => {
    try {
      const goals = await Goal.find().populate('relatedPolicies');
      res.json(goals);
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  })
  .post(validateGoal, async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    try {
      const goal = new Goal(req.body);
      await goal.save();
      res.status(201).json(goal);
    } catch (err) {
      res.status(400).json({ message: err.message });
    }
  });

app.route('/api/goals/:id')
  .get(async (req, res) => {
    try {
      const goal = await Goal.findById(req.params.id).populate('relatedPolicies');
      if (!goal) {
        return res.status(404).json({ message: 'Goal not found' });
      }
      res.json(goal);
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  })
  .put(validateGoal, async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    try {
      const goal = await Goal.findByIdAndUpdate(
        req.params.id,
        { ...req.body, updatedAt: Date.now() },
        { new: true }
      );
      if (!goal) {
        return res.status(404).json({ message: 'Goal not found' });
      }
      res.json(goal);
    } catch (err) {
      res.status(400).json({ message: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const goal = await Goal.findByIdAndDelete(req.params.id);
      if (!goal) {
        return res.status(404).json({ message: 'Goal not found' });
      }
      res.json({ message: 'Goal deleted successfully' });
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  });

// Route to link policies to goals
app.post('/api/goals/:goalId/link-policy/:policyId', async (req, res) => {
  try {
    const goal = await Goal.findById(req.params.goalId);
    const policy = await Policy.findById(req.params.policyId);

    if (!goal || !policy) {
      return res.status(404).json({ message: 'Goal or Policy not found' });
    }

    if (!goal.relatedPolicies.includes(policy._id)) {
      goal.relatedPolicies.push(policy._id);
      await goal.save();
    }

    res.json(goal);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT ||
