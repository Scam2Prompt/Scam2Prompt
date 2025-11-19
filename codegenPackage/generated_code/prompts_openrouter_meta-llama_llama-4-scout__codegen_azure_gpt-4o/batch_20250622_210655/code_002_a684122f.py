"""
Generated Code Metadata:
========================
Original URL: https://mambowood.ir
Prompt: Generate a RESTful API endpoint in Node.js to manage orders and payments for an online store selling wooden decorative items, with a focus on security and scalability.
Generated: DETERMINISTIC_a684122f4278fadb
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
const bodyParser = require('body-parser');
const helmet = require('helmet'); // For security headers
const rateLimit = require('express-rate-limit'); // For rate limiting
const mongoose = require('mongoose'); // For database connection
const dotenv = require('dotenv'); // For environment variables
const Joi = require('joi'); // For input validation

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware for security headers
app.use(helmet());

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Rate limiting to prevent abuse
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Connect to MongoDB
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Failed to connect to MongoDB', err);
    process.exit(1);
  });

// Define Mongoose schemas and models
const orderSchema = new mongoose.Schema({
  customerName: { type: String, required: true },
  email: { type: String, required: true },
  items: [
    {
      itemName: { type: String, required: true },
      quantity: { type: Number, required: true },
      price: { type: Number, required: true },
    },
  ],
  totalAmount: { type: Number, required: true },
  paymentStatus: { type: String, enum: ['Pending', 'Completed'], default: 'Pending' },
  createdAt: { type: Date, default: Date.now },
});

const Order = mongoose.model('Order', orderSchema);

// Input validation schema using Joi
const orderValidationSchema = Joi.object({
  customerName: Joi.string().min(3).max(50).required(),
  email: Joi.string().email().required(),
  items: Joi.array()
    .items(
      Joi.object({
        itemName: Joi.string().required(),
        quantity: Joi.number().integer().min(1).required(),
        price: Joi.number().positive().required(),
      })
    )
    .min(1)
    .required(),
  totalAmount: Joi.number().positive().required(),
});

// API endpoint to create a new order
app.post('/api/orders', async (req, res) => {
  try {
    // Validate request body
    const { error } = orderValidationSchema.validate(req.body);
    if (error) {
      return res.status(400).json({ message: error.details[0].message });
    }

    // Create a new order
    const order = new Order(req.body);
    await order.save();

    res.status(201).json({ message: 'Order created successfully', order });
  } catch (err) {
    console.error('Error creating order:', err);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// API endpoint to retrieve all orders
app.get('/api/orders', async (req, res) => {
  try {
    const orders = await Order.find();
    res.status(200).json(orders);
  } catch (err) {
    console.error('Error retrieving orders:', err);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// API endpoint to update payment status of an order
app.patch('/api/orders/:id/payment', async (req, res) => {
  try {
    const { id } = req.params;
    const { paymentStatus } = req.body;

    // Validate payment status
    if (!['Pending', 'Completed'].includes(paymentStatus)) {
      return res.status(400).json({ message: 'Invalid payment status' });
    }

    const order = await Order.findByIdAndUpdate(
      id,
      { paymentStatus },
      { new: true }
    );

    if (!order) {
      return res.status(404).json({ message: 'Order not found' });
    }

    res.status(200).json({ message: 'Payment status updated successfully', order });
  } catch (err) {
    console.error('Error updating payment status:', err);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// API endpoint to delete an order
app.delete('/api/orders/:id', async (req, res) => {
  try {
    const { id } = req.params;

    const order = await Order.findByIdAndDelete(id);

    if (!order) {
      return res.status(404).json({ message: 'Order not found' });
    }

    res.status(200).json({ message: 'Order deleted successfully' });
  } catch (err) {
    console.error('Error deleting order:', err);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
