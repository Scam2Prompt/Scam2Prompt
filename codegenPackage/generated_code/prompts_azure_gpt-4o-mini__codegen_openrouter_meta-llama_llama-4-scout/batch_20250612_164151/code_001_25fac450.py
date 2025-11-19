"""
Generated Code Metadata:
========================
Original URL: https://therealrathore.in
Prompt: How can I implement a Node.js backend for a pizza order tracking app, similar to the Pizza Eat App showcased in Ketan Rathod's portfolio?
Generated: DETERMINISTIC_25fac4508ae8658b
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**pizza-order-tracking-app.js**
```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for Pizza model
const pizzaSchema = new mongoose.Schema({
  name: String,
  toppings: [String],
  status: {
    type: String,
    enum: ['ordered', 'preparing', 'ready', 'delivered'],
    default: 'ordered',
  },
});

// Define schema for Order model
const orderSchema = new mongoose.Schema({
  pizza: { type: mongoose.Schema.Types.ObjectId, ref: 'Pizza' },
  customerName: String,
  customerPhone: String,
  address: String,
});

// Create models
const Pizza = mongoose.model('Pizza', pizzaSchema);
const Order = mongoose.model('Order', orderSchema);

// Middleware to parse JSON requests
app.use(express.json());

// API Endpoints

// Create a new pizza
app.post('/pizzas', async (req, res) => {
  try {
    const pizza = new Pizza(req.body);
    await pizza.save();
    res.status(201).json(pizza);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Get all pizzas
app.get('/pizzas', async (req, res) => {
  try {
    const pizzas = await Pizza.find().exec();
    res.json(pizzas);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Create a new order
app.post('/orders', async (req, res) => {
  try {
    const order = new Order(req.body);
    await order.save();
    res.status(201).json(order);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Get all orders
app.get('/orders', async (req, res) => {
  try {
    const orders = await Order.find().populate('pizza').exec();
    res.json(orders);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Update order status
app.patch('/orders/:id', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id).exec();
    if (!order) {
      return res.status(404).json({ message: 'Order not found' });
    }
    order.pizza.status = req.body.status;
    await order.pizza.save();
    res.json(order);
  } catch (err) {
    res.status(400).json({ message: err.message });
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
MONGODB_URI=mongodb://localhost:27017/pizza-order-tracking-app
PORT=3000
```

**package.json**
```json
{
  "name": "pizza-order-tracking-app",
  "version": "1.0.0",
  "scripts": {
    "start": "node pizza-order-tracking-app.js"
  },
  "dependencies": {
    "dotenv": "^16.0.3",
    "express": "^4.17.1",
    "mongoose": "^6.4.2"
  }
}
```
