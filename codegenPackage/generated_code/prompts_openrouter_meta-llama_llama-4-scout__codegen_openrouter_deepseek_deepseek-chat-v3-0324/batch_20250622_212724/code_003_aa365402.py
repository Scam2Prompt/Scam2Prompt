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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');
const { validationResult } = require('express-validator');
const { check } = require('express-validator');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect('mongodb://localhost:27017/psicologos_oruro', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Member Schema
const memberSchema = new mongoose.Schema({
  firstName: { type: String, required: true },
  lastName: { type: String, required: true },
  licenseNumber: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String },
  specialization: { type: String },
  membershipStatus: { 
    type: String, 
    required: true,
    enum: ['active', 'inactive', 'suspended', 'pending'],
    default: 'pending'
  },
  joinDate: { type: Date, default: Date.now },
  renewalDate: { type: Date },
  address: {
    street: String,
    city: String,
    state: String,
    zipCode: String
  }
});

// Member Model
const Member = mongoose.model('Member', memberSchema);

// Validation rules for member creation
const createMemberValidation = [
  check('firstName').not().isEmpty().withMessage('First name is required'),
  check('lastName').not().isEmpty().withMessage('Last name is required'),
  check('licenseNumber').not().isEmpty().withMessage('License number is required'),
  check('email').isEmail().withMessage('Valid email is required'),
  check('membershipStatus').isIn(['active', 'inactive', 'suspended', 'pending'])
    .withMessage('Invalid membership status')
];

// Validation rules for member update
const updateMemberValidation = [
  check('firstName').optional().not().isEmpty().withMessage('First name cannot be empty'),
  check('lastName').optional().not().isEmpty().withMessage('Last name cannot be empty'),
  check('licenseNumber').optional().not().isEmpty().withMessage('License number cannot be empty'),
  check('email').optional().isEmail().withMessage('Valid email is required'),
  check('membershipStatus').optional().isIn(['active', 'inactive', 'suspended', 'pending'])
    .withMessage('Invalid membership status')
];

// Routes
/**
 * @route GET /api/members
 * @description Get all members
 * @access Public
 */
app.get('/api/members', async (req, res) => {
  try {
    const members = await Member.find();
    res.json(members);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

/**
 * @route GET /api/members/:id
 * @description Get a single member by ID
 * @access Public
 */
app.get('/api/members/:id', async (req, res) => {
  try {
    const member = await Member.findById(req.params.id);
    if (!member) {
      return res.status(404).json({ message: 'Member not found' });
    }
    res.json(member);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

/**
 * @route POST /api/members
 * @description Create a new member
 * @access Public
 */
app.post('/api/members', createMemberValidation, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  const member = new Member(req.body);

  try {
    const newMember = await member.save();
    res.status(201).json(newMember);
  } catch (err) {
    if (err.code === 11000) {
      res.status(400).json({ message: 'Duplicate field value (email or license number already exists)' });
    } else {
      res.status(400).json({ message: err.message });
    }
  }
});

/**
 * @route PUT /api/members/:id
 * @description Update a member
 * @access Public
 */
app.put('/api/members/:id', updateMemberValidation, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const member = await Member.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!member) {
      return res.status(404).json({ message: 'Member not found' });
    }
    res.json(member);
  } catch (err) {
    if (err.code === 11000) {
      res.status(400).json({ message: 'Duplicate field value (email or license number already exists)' });
    } else {
      res.status(400).json({ message: err.message });
    }
  }
});

/**
 * @route DELETE /api/members/:id
 * @description Delete a member
 * @access Public
 */
app.delete('/api/members/:id', async (req, res) => {
  try {
    const member = await Member.findByIdAndDelete(req.params.id);
    if (!member) {
      return res.status(404).json({ message: 'Member not found' });
    }
    res.json({ message: 'Member deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

/**
 * @route GET /api/members/status/:status
 * @description Get members by status
 * @access Public
 */
app.get('/api/members/status/:status', async (req, res) => {
  try {
    const members = await Member.find({ membershipStatus: req.params.status });
    res.json(members);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something went wrong!' });
});

// Server configuration
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
