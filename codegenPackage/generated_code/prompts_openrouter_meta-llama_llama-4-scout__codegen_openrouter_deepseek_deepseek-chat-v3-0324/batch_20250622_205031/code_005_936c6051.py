"""
Generated Code Metadata:
========================
Original URL: https://www.coupangeatsplus.info
Prompt: Design a simple backend API using Node.js to manage customer applications and support requests for a service like 쿠팡이츠플러스, including handling of additional zone charges.
Generated: DETERMINISTIC_936c6051515c71f9
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready Node.js backend API for managing customer applications and support requests with zone charges:

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const Joi = require('joi');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');

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
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/coupang_eats_plus', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Mongoose schemas
const customerApplicationSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String, required: true },
  address: { type: String, required: true },
  zone: { type: String, required: true },
  status: { type: String, default: 'pending', enum: ['pending', 'approved', 'rejected'] },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const supportRequestSchema = new mongoose.Schema({
  customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'CustomerApplication', required: true },
  type: { type: String, required: true, enum: ['delivery', 'payment', 'service', 'other'] },
  description: { type: String, required: true },
  status: { type: String, default: 'open', enum: ['open', 'in_progress', 'resolved'] },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const zoneChargeSchema = new mongoose.Schema({
  zoneName: { type: String, required: true, unique: true },
  additionalCharge: { type: Number, required: true, min: 0 },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Mongoose models
const CustomerApplication = mongoose.model('CustomerApplication', customerApplicationSchema);
const SupportRequest = mongoose.model('SupportRequest', supportRequestSchema);
const ZoneCharge = mongoose.model('ZoneCharge', zoneChargeSchema);

// Joi validation schemas
const customerApplicationValidationSchema = Joi.object({
  name: Joi.string().required(),
  email: Joi.string().email().required(),
  phone: Joi.string().required(),
  address: Joi.string().required(),
  zone: Joi.string().required()
});

const supportRequestValidationSchema = Joi.object({
  customerId: Joi.string().required(),
  type: Joi.string().valid('delivery', 'payment', 'service', 'other').required(),
  description: Joi.string().required()
});

const zoneChargeValidationSchema = Joi.object({
  zoneName: Joi.string().required(),
  additionalCharge: Joi.number().min(0).required()
});

// Utility functions
const validateRequest = (schema) => {
  return (req, res, next) => {
    const { error } = schema.validate(req.body);
    if (error) {
      return res.status(400).json({ error: error.details[0].message });
    }
    next();
  };
};

const handleErrors = (res, error) => {
  console.error(error);
  res.status(500).json({ error: 'Internal server error' });
};

// Routes
// Customer Applications
app.post('/api/customers', validateRequest(customerApplicationValidationSchema), async (req, res) => {
  try {
    const customer = new CustomerApplication(req.body);
    await customer.save();
    res.status(201).json(customer);
  } catch (error) {
    if (error.code === 11000) {
      return res.status(400).json({ error: 'Email already exists' });
    }
    handleErrors(res, error);
  }
});

app.get('/api/customers', async (req, res) => {
  try {
    const customers = await CustomerApplication.find();
    res.json(customers);
  } catch (error) {
    handleErrors(res, error);
  }
});

app.get('/api/customers/:id', async (req, res) => {
  try {
    const customer = await CustomerApplication.findById(req.params.id);
    if (!customer) {
      return res.status(404).json({ error: 'Customer not found' });
    }
    res.json(customer);
  } catch (error) {
    handleErrors(res, error);
  }
});

app.put('/api/customers/:id', validateRequest(customerApplicationValidationSchema), async (req, res) => {
  try {
    const customer = await CustomerApplication.findByIdAndUpdate(
      req.params.id,
      { ...req.body, updatedAt: Date.now() },
      { new: true }
    );
    if (!customer) {
      return res.status(404).json({ error: 'Customer not found' });
    }
    res.json(customer);
  } catch (error) {
    handleErrors(res, error);
  }
});

// Support Requests
app.post('/api/support-requests', validateRequest(supportRequestValidationSchema), async (req, res) => {
  try {
    const supportRequest = new SupportRequest(req.body);
    await supportRequest.save();
    res.status(201).json(supportRequest);
  } catch (error) {
    handleErrors(res, error);
  }
});

app.get('/api/support-requests', async (req, res) => {
  try {
    const supportRequests = await SupportRequest.find().populate('customerId');
    res.json(supportRequests);
  } catch (error) {
    handleErrors(res, error);
  }
});

app.put('/api/support-requests/:id', async (req, res) => {
  try {
    const { status } = req.body;
    if (!status || !['open', 'in_progress', 'resolved'].includes(status)) {
      return res.status(400).json({ error: 'Invalid status' });
    }
    
    const supportRequest = await SupportRequest.findByIdAndUpdate(
      req.params.id,
      { status, updatedAt: Date.now() },
      { new: true }
    ).populate('customerId');
    
    if (!supportRequest) {
      return res.status(404).json({ error: 'Support request not found' });
    }
    res.json(supportRequest);
  } catch (error) {
    handleErrors(res, error);
  }
});

// Zone Charges
app.post('/api/zone-charges', validateRequest(zoneChargeValidationSchema), async (req, res) => {
  try {
    const zoneCharge = new ZoneCharge(req.body);
    await zoneCharge.save();
    res.status(201).json(zoneCharge);
  } catch (error) {
    if (error.code === 11000) {
      return res.status(400).json({ error: 'Zone already exists' });
    }
    handleErrors(res, error);
  }
});

app.get('/api/zone-charges', async (req, res) => {
  try {
    const zoneCharges = await ZoneCharge.find();
    res.json(zoneCharges);
  } catch (error) {
    handleErrors(res, error);
  }
});

app.put('/api/zone-charges/:id', validateRequest(zoneChargeValidationSchema), async (req, res) => {
  try {
    const zoneCharge = await ZoneCharge.findByIdAndUpdate(
      req.params.id,
      { ...req.body, updatedAt: Date.now() },
      { new: true }
    );
    if (!zoneCharge) {
      return res.status(404).json({ error: 'Zone charge not found' });
    }
    res.json(zoneCharge);
  } catch (error) {
    handleErrors(res, error);
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

// Export for testing
module.exports = app;
```
