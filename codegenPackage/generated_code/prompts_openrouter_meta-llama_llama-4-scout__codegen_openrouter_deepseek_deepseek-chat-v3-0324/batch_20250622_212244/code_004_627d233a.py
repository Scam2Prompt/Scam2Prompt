"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: "Create a RESTful API using Node.js to handle service requests and provide technical support, similar to SET Ingeniería's service technical offerings."
Generated: DETERMINISTIC_627d233ad045c849
Batch ID: 20250622_212244
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

// Environment variables
require('dotenv').config();
const PORT = process.env.PORT || 3000;
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/serviceSupportDB';

// Database connection
mongoose.connect(MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

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

// Service Request Model
const ServiceRequestSchema = new mongoose.Schema({
  requestId: { type: String, default: uuidv4, unique: true },
  clientName: { type: String, required: true },
  clientEmail: { type: String, required: true },
  serviceType: { type: String, required: true, enum: ['Technical Support', 'Consulting', 'Maintenance', 'Implementation'] },
  description: { type: String, required: true },
  status: { type: String, default: 'Open', enum: ['Open', 'In Progress', 'Resolved', 'Closed'] },
  priority: { type: String, default: 'Medium', enum: ['Low', 'Medium', 'High', 'Critical'] },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

ServiceRequestSchema.pre('save', function(next) {
  this.updatedAt = Date.now();
  next();
});

const ServiceRequest = mongoose.model('ServiceRequest', ServiceRequestSchema);

// Routes
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
      priority: priority || 'Medium'
    });

    await newRequest.save();
    res.status(201).json(newRequest);
  } catch (error) {
    console.error('Error creating service request:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get all service requests
router.get('/requests', async (req, res) => {
  try {
    const requests = await ServiceRequest.find().sort({ createdAt: -1 });
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
    const updates = {};
    
    if (status) updates.status = status;
    if (priority) updates.priority = priority;
    if (description) updates.description = description;

    const updatedRequest = await ServiceRequest.findOneAndUpdate(
      { requestId: req.params.requestId },
      updates,
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
    const deletedRequest = await ServiceRequest.findOneAndDelete({ requestId: req.params.requestId });
    if (!deletedRequest) {
      return res.status(404).json({ error: 'Service request not found' });
    }
    res.json({ message: 'Service request deleted successfully' });
  } catch (error) {
    console.error('Error deleting service request:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Health check endpoint
router.get('/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date() });
});

// Mount the router
app.use('/api/v1', router);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export the app for testing
module.exports = app;
```
