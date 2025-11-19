"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Create a RESTful API in Node.js to manage orders and inventory of construction equipment and attachments like Hydraulic Breaker and Pile Driver.
Generated: DETERMINISTIC_9b5e8de2a66aa271
Batch ID: 20250622_211609
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
  useUnifiedTopology: true
});

// Define schema for equipment and attachments
const equipmentSchema = new mongoose.Schema({
  name: String,
  type: String,
  quantity: Number,
  description: String
});

const orderSchema = new mongoose.Schema({
  equipment: { type: mongoose.Schema.Types.ObjectId, ref: 'Equipment' },
  customer: String,
  orderDate: Date,
  status: String
});

// Create models
const Equipment = mongoose.model('Equipment', equipmentSchema);
const Order = mongoose.model('Order', orderSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API Endpoints

// Get all equipment
app.get('/api/equipment', async (req, res) => {
  try {
    const equipment = await Equipment.find().exec();
    res.json(equipment);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching equipment' });
  }
});

// Get equipment by ID
app.get('/api/equipment/:id', async (req, res) => {
  try {
    const equipment = await Equipment.findById(req.params.id).exec();
    if (!equipment) {
      res.status(404).json({ message: 'Equipment not found' });
    } else {
      res.json(equipment);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching equipment' });
  }
});

// Create new equipment
app.post('/api/equipment', async (req, res) => {
  try {
    const equipment = new Equipment(req.body);
    await equipment.save();
    res.json(equipment);
  } catch (err) {
    res.status(400).json({ message: 'Error creating equipment' });
  }
});

// Update existing equipment
app.put('/api/equipment/:id', async (req, res) => {
  try {
    const equipment = await Equipment.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!equipment) {
      res.status(404).json({ message: 'Equipment not found' });
    } else {
      res.json(equipment);
    }
  } catch (err) {
    res.status(400).json({ message: 'Error updating equipment' });
  }
});

// Delete equipment
app.delete('/api/equipment/:id', async (req, res) => {
  try {
    await Equipment.findByIdAndRemove(req.params.id);
    res.json({ message: 'Equipment deleted successfully' });
  } catch (err) {
    res.status(404).json({ message: 'Equipment not found' });
  }
});

// Get all orders
app.get('/api/orders', async (req, res) => {
  try {
    const orders = await Order.find().populate('equipment').exec();
    res.json(orders);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching orders' });
  }
});

// Get order by ID
app.get('/api/orders/:id', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id).populate('equipment').exec();
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
app.post('/api/orders', async (req, res) => {
  try {
    const order = new Order(req.body);
    await order.save();
    res.json(order);
  } catch (err) {
    res.status(400).json({ message: 'Error creating order' });
  }
});

// Update existing order
app.put('/api/orders/:id', async (req, res) => {
  try {
    const order = await Order.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (err) {
    res.status(400).json({ message: 'Error updating order' });
  }
});

// Delete order
app.delete('/api/orders/:id', async (req, res) => {
  try {
    await Order.findByIdAndRemove(req.params.id);
    res.json({ message: 'Order deleted successfully' });
  } catch (err) {
    res.status(404).json({ message: 'Order not found' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// models/equipment.js (if you want to separate models into different files)
// Import mongoose
const mongoose = require('mongoose');

// Define schema for equipment and attachments
const equipmentSchema = new mongoose.Schema({
  name: String,
  type: String,
  quantity: Number,
  description: String
});

// Create model
const Equipment = mongoose.model('Equipment', equipmentSchema);

// Export model
module.exports = Equipment;
```

```javascript
// models/order.js (if you want to separate models into different files)
// Import mongoose
const mongoose = require('mongoose');

// Define schema for order
const orderSchema = new mongoose.Schema({
  equipment: { type: mongoose.Schema.Types.ObjectId, ref: 'Equipment' },
  customer: String,
  orderDate: Date,
  status: String
});

// Create model
const Order = mongoose.model('Order', orderSchema);

// Export model
module.exports = Order;
```

```javascript
// .env (example environment variables)
// DB_URL=mongodb://localhost:27017/construction-equipment
// PORT=3000
```
