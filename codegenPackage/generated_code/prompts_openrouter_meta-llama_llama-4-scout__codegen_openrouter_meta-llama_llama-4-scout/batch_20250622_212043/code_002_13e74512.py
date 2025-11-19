"""
Generated Code Metadata:
========================
Original URL: https://europarquets.be
Prompt: Generate a RESTful API in Node.js for managing orders and services offered by a company that restores wooden surfaces using aerogommage techniques.
Generated: DETERMINISTIC_13e74512a389b4ff
Batch ID: 20250622_212043
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

// Define schema for services
const serviceSchema = new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
});

// Define schema for orders
const orderSchema = new mongoose.Schema({
  customerName: String,
  service: { type: mongoose.Schema.Types.ObjectId, ref: 'Service' },
  status: String,
});

// Create models
const Service = mongoose.model('Service', serviceSchema);
const Order = mongoose.model('Order', orderSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Get all services
app.get('/services', async (req, res) => {
  try {
    const services = await Service.find().exec();
    res.json(services);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching services' });
  }
});

// Get service by ID
app.get('/services/:id', async (req, res) => {
  try {
    const service = await Service.findById(req.params.id).exec();
    if (!service) {
      res.status(404).json({ message: 'Service not found' });
    } else {
      res.json(service);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching service' });
  }
});

// Create new service
app.post('/services', async (req, res) => {
  try {
    const service = new Service(req.body);
    await service.save();
    res.json(service);
  } catch (err) {
    res.status(400).json({ message: 'Error creating service' });
  }
});

// Update existing service
app.put('/services/:id', async (req, res) => {
  try {
    const service = await Service.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!service) {
      res.status(404).json({ message: 'Service not found' });
    } else {
      res.json(service);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error updating service' });
  }
});

// Delete service
app.delete('/services/:id', async (req, res) => {
  try {
    await Service.findByIdAndRemove(req.params.id);
    res.json({ message: 'Service deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting service' });
  }
});

// Get all orders
app.get('/orders', async (req, res) => {
  try {
    const orders = await Order.find().populate('service').exec();
    res.json(orders);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching orders' });
  }
});

// Get order by ID
app.get('/orders/:id', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id).populate('service').exec();
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching order' });
  }
});

// Create new order
app.post('/orders', async (req, res) => {
  try {
    const order = new Order(req.body);
    await order.save();
    res.json(order);
  } catch (err) {
    res.status(400).json({ message: 'Error creating order' });
  }
});

// Update existing order
app.put('/orders/:id', async (req, res) => {
  try {
    const order = await Order.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error updating order' });
  }
});

// Delete order
app.delete('/orders/:id', async (req, res) => {
  try {
    await Order.findByIdAndRemove(req.params.id);
    res.json({ message: 'Order deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting order' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
