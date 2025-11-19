"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Develop a RESTful API using Node.js and Express.js to manage customer requests for home maintenance services, including services like gas installation and painting.
Generated: DETERMINISTIC_9d38ce9a0923025a
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
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for customer requests
const customerRequestSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
  service: String,
  description: String,
  status: { type: String, default: 'pending' },
});

// Define schema for services
const serviceSchema = new mongoose.Schema({
  name: String,
  description: String,
});

// Create models
const CustomerRequest = mongoose.model('CustomerRequest', customerRequestSchema);
const Service = mongoose.model('Service', serviceSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to create a new customer request
app.post('/requests', async (req, res) => {
  try {
    const { name, email, phone, service, description } = req.body;
    if (!name || !email || !phone || !service || !description) {
      return res.status(400).json({ message: 'All fields are required' });
    }
    const customerRequest = new CustomerRequest({ name, email, phone, service, description });
    await customerRequest.save();
    res.status(201).json(customerRequest);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get all customer requests
app.get('/requests', async (req, res) => {
  try {
    const customerRequests = await CustomerRequest.find().exec();
    res.json(customerRequests);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get a customer request by ID
app.get('/requests/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const customerRequest = await CustomerRequest.findById(id).exec();
    if (!customerRequest) {
      return res.status(404).json({ message: 'Customer request not found' });
    }
    res.json(customerRequest);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update a customer request
app.put('/requests/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const { name, email, phone, service, description, status } = req.body;
    const customerRequest = await CustomerRequest.findByIdAndUpdate(id, { name, email, phone, service, description, status }, { new: true });
    if (!customerRequest) {
      return res.status(404).json({ message: 'Customer request not found' });
    }
    res.json(customerRequest);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete a customer request
app.delete('/requests/:id', async (req, res) => {
  try {
    const id = req.params.id;
    await CustomerRequest.findByIdAndDelete(id).exec();
    res.status(204).json({ message: 'Customer request deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to create a new service
app.post('/services', async (req, res) => {
  try {
    const { name, description } = req.body;
    if (!name || !description) {
      return res.status(400).json({ message: 'All fields are required' });
    }
    const service = new Service({ name, description });
    await service.save();
    res.status(201).json(service);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get all services
app.get('/services', async (req, res) => {
  try {
    const services = await Service.find().exec();
    res.json(services);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get a service by ID
app.get('/services/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const service = await Service.findById(id).exec();
    if (!service) {
      return res.status(404).json({ message: 'Service not found' });
    }
    res.json(service);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update a service
app.put('/services/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const { name, description } = req.body;
    const service = await Service.findByIdAndUpdate(id, { name, description }, { new: true });
    if (!service) {
      return res.status(404).json({ message: 'Service not found' });
    }
    res.json(service);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete a service
app.delete('/services/:id', async (req, res) => {
  try {
    const id = req.params.id;
    await Service.findByIdAndDelete(id).exec();
    res.status(204).json({ message: 'Service deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
