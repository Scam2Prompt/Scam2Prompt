"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Generate a RESTful API in Node.js for a cleaning services platform, including endpoints for creating, reading, updating, and deleting customer information and service requests.
Generated: DETERMINISTIC_474de0c3a778d052
Batch ID: 20250622_205523
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
require('dotenv').config();

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

// Define schemas
const customerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String, required: true },
  address: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

const serviceRequestSchema = new mongoose.Schema({
  customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'Customer', required: true },
  serviceType: { type: String, required: true },
  date: { type: Date, required: true },
  time: { type: String, required: true },
  status: { type: String, default: 'Pending' },
  notes: { type: String },
  createdAt: { type: Date, default: Date.now }
});

// Define models
const Customer = mongoose.model('Customer', customerSchema);
const ServiceRequest = mongoose.model('ServiceRequest', serviceRequestSchema);

// Customer Routes
app.route('/api/customers')
  // Get all customers
  .get(async (req, res) => {
    try {
      const customers = await Customer.find();
      res.json(customers);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Create new customer
  .post(async (req, res) => {
    try {
      const newCustomer = new Customer(req.body);
      const savedCustomer = await newCustomer.save();
      res.status(201).json(savedCustomer);
    } catch (err) {
      if (err.code === 11000) {
        res.status(400).json({ error: 'Email already exists' });
      } else {
        res.status(400).json({ error: err.message });
      }
    }
  });

app.route('/api/customers/:id')
  // Get single customer
  .get(async (req, res) => {
    try {
      const customer = await Customer.findById(req.params.id);
      if (!customer) {
        return res.status(404).json({ error: 'Customer not found' });
      }
      res.json(customer);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Update customer
  .put(async (req, res) => {
    try {
      const updatedCustomer = await Customer.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true, runValidators: true }
      );
      if (!updatedCustomer) {
        return res.status(404).json({ error: 'Customer not found' });
      }
      res.json(updatedCustomer);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  // Delete customer
  .delete(async (req, res) => {
    try {
      const deletedCustomer = await Customer.findByIdAndDelete(req.params.id);
      if (!deletedCustomer) {
        return res.status(404).json({ error: 'Customer not found' });
      }
      res.json({ message: 'Customer deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Service Request Routes
app.route('/api/service-requests')
  // Get all service requests
  .get(async (req, res) => {
    try {
      const serviceRequests = await ServiceRequest.find().populate('customerId');
      res.json(serviceRequests);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Create new service request
  .post(async (req, res) => {
    try {
      const newServiceRequest = new ServiceRequest(req.body);
      const savedServiceRequest = await newServiceRequest.save();
      res.status(201).json(savedServiceRequest);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

app.route('/api/service-requests/:id')
  // Get single service request
  .get(async (req, res) => {
    try {
      const serviceRequest = await ServiceRequest.findById(req.params.id).populate('customerId');
      if (!serviceRequest) {
        return res.status(404).json({ error: 'Service request not found' });
      }
      res.json(serviceRequest);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Update service request
  .put(async (req, res) => {
    try {
      const updatedServiceRequest = await ServiceRequest.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true, runValidators: true }
      );
      if (!updatedServiceRequest) {
        return res.status(404).json({ error: 'Service request not found' });
      }
      res.json(updatedServiceRequest);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  // Delete service request
  .delete(async (req, res) => {
    try {
      const deletedServiceRequest = await ServiceRequest.findByIdAndDelete(req.params.id);
      if (!deletedServiceRequest) {
        return res.status(404).json({ error: 'Service request not found' });
      }
      res.json({ message: 'Service request deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Get service requests by customer ID
app.get('/api/customers/:id/service-requests', async (req, res) => {
  try {
    const serviceRequests = await ServiceRequest.find({ customerId: req.params.id });
    res.json(serviceRequests);
  } catch (err) {
    res.status(500).json({ error: err.message });
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
