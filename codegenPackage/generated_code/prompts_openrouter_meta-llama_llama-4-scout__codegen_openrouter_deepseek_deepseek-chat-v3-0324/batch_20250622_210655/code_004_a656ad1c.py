"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Create a RESTful API using Node.js to handle customer requests for air conditioning cleaning and maintenance services, inspired by شركة إنجاز's offerings in جدة.
Generated: DETERMINISTIC_a656ad1c2b866a43
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
const Joi = require('joi');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/ac_services', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Customer Schema
const customerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  phone: { type: String, required: true },
  email: { type: String },
  address: { type: String, required: true },
  serviceType: { type: String, required: true, enum: ['cleaning', 'maintenance', 'repair'] },
  acType: { type: String, required: true, enum: ['split', 'window', 'central'] },
  preferredDate: { type: Date, required: true },
  notes: { type: String },
  status: { type: String, default: 'pending', enum: ['pending', 'confirmed', 'completed', 'cancelled'] },
  createdAt: { type: Date, default: Date.now }
});

// Create Customer Model
const Customer = mongoose.model('Customer', customerSchema);

// Validation schema for customer requests
const customerValidationSchema = Joi.object({
  name: Joi.string().min(3).max(50).required(),
  phone: Joi.string().min(10).max(15).required(),
  email: Joi.string().email(),
  address: Joi.string().min(5).max(200).required(),
  serviceType: Joi.string().valid('cleaning', 'maintenance', 'repair').required(),
  acType: Joi.string().valid('split', 'window', 'central').required(),
  preferredDate: Joi.date().greater('now').required(),
  notes: Joi.string().max(500)
});

// Routes
/**
 * @route GET /api/health
 * @description Health check endpoint
 */
app.get('/api/health', (req, res) => {
  res.status(200).json({ status: 'healthy' });
});

/**
 * @route POST /api/customers
 * @description Create a new service request
 */
app.post('/api/customers', async (req, res) => {
  try {
    // Validate request body
    const { error } = customerValidationSchema.validate(req.body);
    if (error) {
      return res.status(400).json({ error: error.details[0].message });
    }

    // Create new customer
    const customer = new Customer(req.body);
    await customer.save();

    res.status(201).json({
      message: 'Service request created successfully',
      data: customer
    });
  } catch (err) {
    console.error('Error creating service request:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * @route GET /api/customers
 * @description Get all service requests
 */
app.get('/api/customers', async (req, res) => {
  try {
    const customers = await Customer.find().sort({ createdAt: -1 });
    res.status(200).json(customers);
  } catch (err) {
    console.error('Error fetching service requests:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * @route GET /api/customers/:id
 * @description Get a specific service request
 */
app.get('/api/customers/:id', async (req, res) => {
  try {
    const customer = await Customer.findById(req.params.id);
    if (!customer) {
      return res.status(404).json({ error: 'Service request not found' });
    }
    res.status(200).json(customer);
  } catch (err) {
    console.error('Error fetching service request:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * @route PUT /api/customers/:id/status
 * @description Update service request status
 */
app.put('/api/customers/:id/status', async (req, res) => {
  try {
    const { status } = req.body;
    if (!['pending', 'confirmed', 'completed', 'cancelled'].includes(status)) {
      return res.status(400).json({ error: 'Invalid status value' });
    }

    const customer = await Customer.findByIdAndUpdate(
      req.params.id,
      { status },
      { new: true }
    );

    if (!customer) {
      return res.status(404).json({ error: 'Service request not found' });
    }

    res.status(200).json({
      message: 'Status updated successfully',
      data: customer
    });
  } catch (err) {
    console.error('Error updating service request:', err);
    res.status(500).json({ error: 'Internal server error' });
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
```
