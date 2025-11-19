"""
Generated Code Metadata:
========================
Original URL: https://7054company.github.io
Prompt: Create a REST API in Node.js for a company like 7054Company to manage consulting and development service requests.
Generated: DETERMINISTIC_f65f5887f1398a48
Batch ID: 20250612_154215
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

// Configure environment variables
require('dotenv').config();

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  serverSelectionTimeoutMS: 5000
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => console.log('Connected to MongoDB'));

// Middleware
app.use(cors());
app.use(helmet());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Service Request Schema
const serviceRequestSchema = new mongoose.Schema({
  requestId: { type: String, default: uuidv4, unique: true },
  clientName: { type: String, required: true },
  clientEmail: { type: String, required: true },
  serviceType: { 
    type: String, 
    required: true,
    enum: ['consulting', 'development', 'training', 'support']
  },
  description: { type: String, required: true },
  status: { 
    type: String, 
    default: 'open',
    enum: ['open', 'in-progress', 'completed', 'cancelled']
  },
  priority: {
    type: String,
    default: 'medium',
    enum: ['low', 'medium', 'high', 'critical']
  },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Add indexes for better query performance
serviceRequestSchema.index({ clientEmail: 1 });
serviceRequestSchema.index({ status: 1 });
serviceRequestSchema.index({ priority: 1 });

// Update the updatedAt field before saving
serviceRequestSchema.pre('save', function(next) {
  this.updatedAt = Date.now();
  next();
});

const ServiceRequest = mongoose.model('ServiceRequest', serviceRequestSchema);

// API Routes
const router = express.Router();

// Create a new service request
router.post('/requests', async (req, res) => {
  try {
    const { clientName, clientEmail, serviceType, description, priority } = req.body;
    
    if (!clientName || !clientEmail || !serviceType || !description) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const newRequest = new ServiceRequest({
      clientName,
      clientEmail,
      serviceType,
      description,
      priority: priority || 'medium'
    });

    const savedRequest = await newRequest.save();
    res.status(201).json(savedRequest);
  } catch (error) {
    console.error('Error creating service request:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get all service requests
router.get('/requests', async (req, res) => {
  try {
    const { status, priority } = req.query;
    const filter = {};
    
    if (status) filter.status = status;
    if (priority) filter.priority = priority;

    const requests = await ServiceRequest.find(filter).sort({ createdAt: -1 });
    res.json(requests);
  } catch (error) {
    console.error('Error fetching service requests:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get a specific service request
router.get('/requests/:requestId', async (req, res) => {
  try {
    const request = await ServiceRequest.findOne({ requestId: req.params.requestId });
    
    if (!request) {
      return res.status(404).json({ error: 'Service request not found' });
    }
    
    res.json(request);
  } catch (error) {
    console.error('Error fetching service request:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Update a service request
router.put('/requests/:requestId', async (req, res) => {
  try {
    const { status, priority, description } = req.body;
    const updateFields = {};
    
    if (status) updateFields.status = status;
    if (priority) updateFields.priority = priority;
    if (description) updateFields.description = description;

    const updatedRequest = await ServiceRequest.findOneAndUpdate(
      { requestId: req.params.requestId },
      updateFields,
      { new: true }
    );

    if (!updatedRequest) {
      return res.status(404).json({ error: 'Service request not found' });
    }

    res.json(updatedRequest);
  } catch (error) {
    console.error('Error updating service request:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Delete a service request
router.delete('/requests/:requestId', async (req, res) => {
  try {
    const deletedRequest = await ServiceRequest.findOneAndDelete({ 
      requestId: req.params.requestId 
    });

    if (!deletedRequest) {
      return res.status(404).json({ error: 'Service request not found' });
    }

    res.json({ message: 'Service request deleted successfully' });
  } catch (error) {
    console.error('Error deleting service request:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Mount the router
app.use('/api', router);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```
