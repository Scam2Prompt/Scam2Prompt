"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Develop a Node.js application to build a RESTful API for managing logistics operations, including services like import/export clearing, forwarding, and pre-financing.
Generated: DETERMINISTIC_853efa75626dc149
Batch ID: 20250622_210655
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
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware setup
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());
app.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect('mongodb://localhost:27017/logistics-api', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas
const OperationSchema = new mongoose.Schema({
  operationId: { type: String, default: uuidv4, unique: true },
  type: { type: String, enum: ['import', 'export', 'forwarding', 'pre-financing'], required: true },
  status: { type: String, enum: ['pending', 'in-progress', 'completed', 'cancelled'], default: 'pending' },
  client: { type: String, required: true },
  details: { type: Object, required: true },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Add indexes
OperationSchema.index({ operationId: 1 });
OperationSchema.index({ client: 1 });
OperationSchema.index({ type: 1 });

// Create model
const Operation = mongoose.model('Operation', OperationSchema);

// API Routes
const router = express.Router();

/**
 * @route GET /api/operations
 * @desc Get all operations
 * @access Public
 */
router.get('/operations', async (req, res) => {
  try {
    const operations = await Operation.find();
    res.json(operations);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

/**
 * @route GET /api/operations/:id
 * @desc Get single operation
 * @access Public
 */
router.get('/operations/:id', async (req, res) => {
  try {
    const operation = await Operation.findOne({ operationId: req.params.id });
    if (!operation) {
      return res.status(404).json({ error: 'Operation not found' });
    }
    res.json(operation);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

/**
 * @route POST /api/operations
 * @desc Create new operation
 * @access Public
 */
router.post('/operations', async (req, res) => {
  try {
    const { type, client, details } = req.body;
    
    if (!type || !client || !details) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const operation = new Operation({
      type,
      client,
      details
    });

    await operation.save();
    res.status(201).json(operation);
  } catch (err) {
    if (err.name === 'ValidationError') {
      return res.status(400).json({ error: err.message });
    }
    res.status(500).json({ error: 'Server error' });
  }
});

/**
 * @route PUT /api/operations/:id
 * @desc Update operation
 * @access Public
 */
router.put('/operations/:id', async (req, res) => {
  try {
    const { status, details } = req.body;
    
    const operation = await Operation.findOne({ operationId: req.params.id });
    if (!operation) {
      return res.status(404).json({ error: 'Operation not found' });
    }

    if (status) operation.status = status;
    if (details) operation.details = details;
    operation.updatedAt = new Date();

    await operation.save();
    res.json(operation);
  } catch (err) {
    if (err.name === 'ValidationError') {
      return res.status(400).json({ error: err.message });
    }
    res.status(500).json({ error: 'Server error' });
  }
});

/**
 * @route DELETE /api/operations/:id
 * @desc Delete operation
 * @access Public
 */
router.delete('/operations/:id', async (req, res) => {
  try {
    const operation = await Operation.findOneAndDelete({ operationId: req.params.id });
    if (!operation) {
      return res.status(404).json({ error: 'Operation not found' });
    }
    res.json({ message: 'Operation deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Mount router
app.use('/api', router);

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

// Export app for testing
module.exports = app;
```
