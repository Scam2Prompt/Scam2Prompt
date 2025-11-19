"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: "Develop a Node.js application to manage orders and inventory for a printing company like Detalj Reklam, including features for tracking orders and updating stock levels."
Generated: DETERMINISTIC_67ab7aa98afceacb
Batch ID: 20250622_210243
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
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for orders
const orderSchema = new mongoose.Schema({
  orderId: String,
  customerName: String,
  orderDate: Date,
  product: String,
  quantity: Number,
  status: String,
});

// Define schema for inventory
const inventorySchema = new mongoose.Schema({
  product: String,
  stockLevel: Number,
});

// Create models
const Order = mongoose.model('Order', orderSchema);
const Inventory = mongoose.model('Inventory', inventorySchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Get all orders
app.get('/orders', async (req, res) => {
  try {
    const orders = await Order.find().exec();
    res.json(orders);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching orders' });
  }
});

// Get order by ID
app.get('/orders/:id', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id).exec();
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching order' });
  }
});

// Create new order
app.post('/orders', async (req, res) => {
  try {
    const { orderId, customerName, orderDate, product, quantity, status } = req.body;
    const order = new Order({ orderId, customerName, orderDate, product, quantity, status });
    await order.save();
    // Update inventory levels
    const inventory = await Inventory.findOne({ product }).exec();
    if (inventory) {
      inventory.stockLevel -= quantity;
      await inventory.save();
    } else {
      console.error(`Product ${product} not found in inventory`);
    }
    res.json(order);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error creating order' });
  }
});

// Update existing order
app.put('/orders/:id', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id).exec();
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      order.set(req.body);
      await order.save();
      res.json(order);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error updating order' });
  }
});

// Delete order
app.delete('/orders/:id', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id).exec();
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      await order.remove();
      res.json({ message: 'Order deleted successfully' });
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error deleting order' });
  }
});

// Get all inventory
app.get('/inventory', async (req, res) => {
  try {
    const inventory = await Inventory.find().exec();
    res.json(inventory);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching inventory' });
  }
});

// Update inventory levels
app.put('/inventory/:product', async (req, res) => {
  try {
    const inventory = await Inventory.findOne({ product: req.params.product }).exec();
    if (!inventory) {
      res.status(404).json({ message: 'Product not found in inventory' });
    } else {
      inventory.stockLevel = req.body.stockLevel;
      await inventory.save();
      res.json(inventory);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error updating inventory' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// models/Order.js (if you want to separate models in their own files)
// import mongoose from 'mongoose';

// const orderSchema = new mongoose.Schema({
//   orderId: String,
//   customerName: String,
//   orderDate: Date,
//   product: String,
//   quantity: Number,
//   status: String,
// });

// export default mongoose.model('Order', orderSchema);
```

```javascript
// models/Inventory.js (if you want to separate models in their own files)
// import mongoose from 'mongoose';

// const inventorySchema = new mongoose.Schema({
//   product: String,
//   stockLevel: Number,
// });

// export default mongoose.model('Inventory', inventorySchema);
```

```json
// .env (example)
// DB_URL=mongodb://localhost:27017/printing-company
// PORT=3000
```
