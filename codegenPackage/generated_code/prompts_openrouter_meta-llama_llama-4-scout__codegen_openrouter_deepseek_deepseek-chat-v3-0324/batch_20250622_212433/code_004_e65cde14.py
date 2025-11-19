"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Create a RESTful API in Node.js to manage inquiries and applications for dental education programs, such as the Especialidad en Ortodoncia y Ortopedia Maxilofacial at INESO."
Generated: DETERMINISTIC_e65cde14a7a6c644
Batch ID: 20250622_212433
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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { validationResult, check } = require('express-validator');

// Initialize Express app
const app = express();

// Environment variables
require('dotenv').config();

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Middleware
app.use(cors());
app.use(helmet());
app.use(bodyParser.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Define Application Schema
const applicationSchema = new mongoose.Schema({
  firstName: { type: String, required: true },
  lastName: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String, required: true },
  program: { type: String, required: true, default: 'Especialidad en Ortodoncia y Ortopedia Maxilofacial' },
  educationLevel: { type: String, required: true },
  workExperience: { type: String, required: true },
  motivation: { type: String, required: true },
  status: { type: String, default: 'Pending', enum: ['Pending', 'Reviewed', 'Accepted', 'Rejected'] },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Define Inquiry Schema
const inquirySchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  phone: { type: String, required: true },
  message: { type: String, required: true },
  program: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

// Create models
const Application = mongoose.model('Application', applicationSchema);
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Validation middleware for application
const validateApplication = [
  check('firstName').not().isEmpty().withMessage('First name is required'),
  check('lastName').not().isEmpty().withMessage('Last name is required'),
  check('email').isEmail().withMessage('Valid email is required'),
  check('phone').not().isEmpty().withMessage('Phone number is required'),
  check('educationLevel').not().isEmpty().withMessage('Education level is required'),
  check('workExperience').not().isEmpty().withMessage('Work experience is required'),
  check('motivation').not().isEmpty().withMessage('Motivation statement is required')
];

// Validation middleware for inquiry
const validateInquiry = [
  check('name').not().isEmpty().withMessage('Name is required'),
  check('email').isEmail().withMessage('Valid email is required'),
  check('phone').not().isEmpty().withMessage('Phone number is required'),
  check('message').not().isEmpty().withMessage('Message is required'),
  check('program').not().isEmpty().withMessage('Program is required')
];

// Routes

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Create new application
app.post('/api/applications', validateApplication, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const application = new Application(req.body);
    await application.save();
    res.status(201).json(application);
  } catch (err) {
    if (err.code === 11000) {
      res.status(400).json({ error: 'Email already exists in our system' });
    } else {
      res.status(500).json({ error: 'Server error' });
    }
  }
});

// Get all applications (admin only)
app.get('/api/applications', async (req, res) => {
  try {
    const applications = await Application.find().sort({ createdAt: -1 });
    res.json(applications);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Get single application
app.get('/api/applications/:id', async (req, res) => {
  try {
    const application = await Application.findById(req.params.id);
    if (!application) {
      return res.status(404).json({ error: 'Application not found' });
    }
    res.json(application);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Update application status (admin only)
app.patch('/api/applications/:id', async (req, res) => {
  try {
    const application = await Application.findByIdAndUpdate(
      req.params.id,
      { status: req.body.status, updatedAt: Date.now() },
      { new: true }
    );
    if (!application) {
      return res.status(404).json({ error: 'Application not found' });
    }
    res.json(application);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Create new inquiry
app.post('/api/inquiries', validateInquiry, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const inquiry = new Inquiry(req.body);
    await inquiry.save();
    res.status(201).json(inquiry);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Get all inquiries (admin only)
app.get('/api/inquiries', async (req, res) => {
  try {
    const inquiries = await Inquiry.find().sort({ createdAt: -1 });
    res.json(inquiries);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing
```
