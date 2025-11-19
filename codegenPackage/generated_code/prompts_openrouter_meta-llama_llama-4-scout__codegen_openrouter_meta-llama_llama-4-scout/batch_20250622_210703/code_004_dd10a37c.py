"""
Generated Code Metadata:
========================
Original URL: https://huylongagri.com
Prompt: "Create a RESTful API using Node.js to manage coffee orders and shipments for a company like Huy Long Agri."
Generated: DETERMINISTIC_dd10a37c43809ef5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**coffee-api.js**
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

// Define schema for coffee order
const coffeeOrderSchema = new mongoose.Schema({
  customerName: String,
  coffeeType: String,
  quantity: Number,
  status: { type: String, default: 'pending' },
});

// Define schema for shipment
const shipmentSchema = new mongoose.Schema({
  orderId: { type: mongoose.Schema.Types.ObjectId, ref: 'CoffeeOrder' },
  shippingAddress: String,
  shippingStatus: { type: String, default: 'pending' },
});

// Create models
const CoffeeOrder = mongoose.model('CoffeeOrder', coffeeOrderSchema);
const Shipment = mongoose.model('Shipment', shipmentSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API Endpoints

// Create a new coffee order
app.post('/orders', async (req, res) => {
  try {
    const { customerName, coffeeType, quantity } = req.body;
    const order = new CoffeeOrder({ customerName, coffeeType, quantity });
    await order.save();
    res.status(201).json(order);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Get all coffee orders
app.get('/orders', async (req, res) => {
  try {
    const orders = await CoffeeOrder.find().exec();
    res.json(orders);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Get a coffee order by ID
app.get('/orders/:id', async (req, res) => {
  try {
    const order = await CoffeeOrder.findById(req.params.id).exec();
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Update a coffee order
app.put('/orders/:id', async (req, res) => {
  try {
    const order = await CoffeeOrder.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Delete a coffee order
app.delete('/orders/:id', async (req, res) => {
  try {
    await CoffeeOrder.findByIdAndRemove(req.params.id);
    res.status(204).json({ message: 'Order deleted successfully' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Create a new shipment
app.post('/shipments', async (req, res) => {
  try {
    const { orderId, shippingAddress } = req.body;
    const shipment = new Shipment({ orderId, shippingAddress });
    await shipment.save();
    res.status(201).json(shipment);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Get all shipments
app.get('/shipments', async (req, res) => {
  try {
    const shipments = await Shipment.find().populate('orderId').exec();
    res.json(shipments);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Get a shipment by ID
app.get('/shipments/:id', async (req, res) => {
  try {
    const shipment = await Shipment.findById(req.params.id).populate('orderId').exec();
    if (!shipment) {
      res.status(404).json({ message: 'Shipment not found' });
    } else {
      res.json(shipment);
    }
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Update a shipment
app.put('/shipments/:id', async (req, res) => {
  try {
    const shipment = await Shipment.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!shipment) {
      res.status(404).json({ message: 'Shipment not found' });
    } else {
      res.json(shipment);
    }
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Delete a shipment
app.delete('/shipments/:id', async (req, res) => {
  try {
    await Shipment.findByIdAndRemove(req.params.id);
    res.status(204).json({ message: 'Shipment deleted successfully' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**.env**
```makefile
DB_URL=mongodb://localhost:27017/coffee-api
PORT=3000
```

**package.json**
```json
{
  "name": "coffee-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node coffee-api.js"
  },
  "dependencies": {
    "dotenv": "^16.0.3",
    "express": "^4.17.1",
    "mongoose": "^6.4.2"
  }
}
```
