"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Generate a RESTful API in Node.js for a moving company to manage services like asansörlü nakliye (elevator-based moving) and küçük nakliye işleri (small moving jobs).
Generated: DETERMINISTIC_beb1eef900b5eb2c
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
mongoose.connect(process.env.MONGODB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for services
const serviceSchema = new mongoose.Schema({
  type: String, // asansörlü nakliye or küçük nakliye işleri
  description: String,
  price: Number,
  status: String, // pending, in_progress, completed
});

// Define schema for customers
const customerSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
});

// Define schema for orders
const orderSchema = new mongoose.Schema({
  customer: { type: mongoose.Schema.Types.ObjectId, ref: 'Customer' },
  service: { type: mongoose.Schema.Types.ObjectId, ref: 'Service' },
  address: String,
  date: Date,
  status: String, // pending, in_progress, completed
});

// Create models
const Service = mongoose.model('Service', serviceSchema);
const Customer = mongoose.model('Customer', customerSchema);
const Order = mongoose.model('Order', orderSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API Endpoints

// Services
app.get('/services', async (req, res) => {
  try {
    const services = await Service.find().exec();
    res.json(services);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching services' });
  }
});

app.post('/services', async (req, res) => {
  try {
    const service = new Service(req.body);
    await service.save();
    res.json(service);
  } catch (err) {
    res.status(400).json({ message: 'Error creating service' });
  }
});

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
    res.status(400).json({ message: 'Error updating service' });
  }
});

app.delete('/services/:id', async (req, res) => {
  try {
    await Service.findByIdAndRemove(req.params.id);
    res.json({ message: 'Service deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting service' });
  }
});

// Customers
app.get('/customers', async (req, res) => {
  try {
    const customers = await Customer.find().exec();
    res.json(customers);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching customers' });
  }
});

app.post('/customers', async (req, res) => {
  try {
    const customer = new Customer(req.body);
    await customer.save();
    res.json(customer);
  } catch (err) {
    res.status(400).json({ message: 'Error creating customer' });
  }
});

app.get('/customers/:id', async (req, res) => {
  try {
    const customer = await Customer.findById(req.params.id).exec();
    if (!customer) {
      res.status(404).json({ message: 'Customer not found' });
    } else {
      res.json(customer);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching customer' });
  }
});

app.put('/customers/:id', async (req, res) => {
  try {
    const customer = await Customer.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!customer) {
      res.status(404).json({ message: 'Customer not found' });
    } else {
      res.json(customer);
    }
  } catch (err) {
    res.status(400).json({ message: 'Error updating customer' });
  }
});

app.delete('/customers/:id', async (req, res) => {
  try {
    await Customer.findByIdAndRemove(req.params.id);
    res.json({ message: 'Customer deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting customer' });
  }
});

// Orders
app.get('/orders', async (req, res) => {
  try {
    const orders = await Order.find().populate('customer').populate('service').exec();
    res.json(orders);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching orders' });
  }
});

app.post('/orders', async (req, res) => {
  try {
    const order = new Order(req.body);
    await order.save();
    res.json(order);
  } catch (err) {
    res.status(400).json({ message: 'Error creating order' });
  }
});

app.get('/orders/:id', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id).populate('customer').populate('service').exec();
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching order' });
  }
});

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
    res.status(400).json({ message: 'Error updating order' });
  }
});

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
