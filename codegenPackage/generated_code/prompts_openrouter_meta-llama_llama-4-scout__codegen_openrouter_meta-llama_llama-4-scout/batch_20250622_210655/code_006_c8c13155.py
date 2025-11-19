"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "Create a RESTful API using Node.js to handle dumpster rental requests, including customer registration and order management."
Generated: DETERMINISTIC_c8c13155d0bd7ee8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**dumpster-rental-api.js**
```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/dumpster-rental', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for customer model
const customerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true }
});

// Define schema for order model
const orderSchema = new mongoose.Schema({
  customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'Customer', required: true },
  dumpsterSize: { type: String, required: true },
  rentalDuration: { type: String, required: true },
  status: { type: String, default: 'pending' }
});

// Compile schemas into models
const Customer = mongoose.model('Customer', customerSchema);
const Order = mongoose.model('Order', orderSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register customer
app.post('/customers', async (req, res) => {
  try {
    const { name, email, password } = req.body;
    if (!name || !email || !password) {
      return res.status(400).send({ message: 'Please provide all required fields' });
    }

    const existingCustomer = await Customer.findOne({ email });
    if (existingCustomer) {
      return res.status(400).send({ message: 'Customer already exists' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const customer = new Customer({ name, email, password: hashedPassword });
    await customer.save();
    res.send({ message: 'Customer created successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).send({ message: 'Error creating customer' });
  }
});

// Login customer
app.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    if (!email || !password) {
      return res.status(400).send({ message: 'Please provide all required fields' });
    }

    const customer = await Customer.findOne({ email });
    if (!customer) {
      return res.status(401).send({ message: 'Invalid credentials' });
    }

    const isValidPassword = await bcrypt.compare(password, customer.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid credentials' });
    }

    const token = jwt.sign({ customerId: customer._id }, 'secret-key', { expiresIn: '1h' });
    res.send({ token });
  } catch (err) {
    console.error(err);
    res.status(500).send({ message: 'Error logging in' });
  }
});

// Create order
app.post('/orders', authenticateToken, async (req, res) => {
  try {
    const { dumpsterSize, rentalDuration } = req.body;
    if (!dumpsterSize || !rentalDuration) {
      return res.status(400).send({ message: 'Please provide all required fields' });
    }

    const order = new Order({ customerId: req.customer._id, dumpsterSize, rentalDuration });
    await order.save();
    res.send({ message: 'Order created successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).send({ message: 'Error creating order' });
  }
});

// Get all orders for a customer
app.get('/orders', authenticateToken, async (req, res) => {
  try {
    const orders = await Order.find({ customerId: req.customer._id });
    res.send(orders);
  } catch (err) {
    console.error(err);
    res.status(500).send({ message: 'Error fetching orders' });
  }
});

// Update order status
app.patch('/orders/:orderId', authenticateToken, async (req, res) => {
  try {
    const orderId = req.params.orderId;
    const { status } = req.body;
    if (!status) {
      return res.status(400).send({ message: 'Please provide status' });
    }

    const order = await Order.findByIdAndUpdate(orderId, { status }, { new: true });
    if (!order) {
      return res.status(404).send({ message: 'Order not found' });
    }

    res.send({ message: 'Order updated successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).send({ message: 'Error updating order' });
  }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.status(401).send({ message: 'Access denied' });

  try {
    const decoded = jwt.verify(token, 'secret-key');
    req.customer = decoded;
    next();
  } catch (err) {
    res.status(400).send({ message: 'Invalid token' });
  }
}

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```

**package.json**
```json
{
  "name": "dumpster-rental-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node dumpster-rental-api.js"
  },
  "dependencies": {
    "bcrypt": "^5.0.1",
    "express": "^4.17.1",
    "jsonwebtoken": "^8.5.1",
    "mongoose": "^5.12.3"
  }
}
```
