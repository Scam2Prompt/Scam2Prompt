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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');
const mongoose = require('mongoose');
const validator = require('validator');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

// Initialize Express app
const app = express();

// Apply security middleware
app.use(helmet());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
}).then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// Define Order Schema
const orderSchema = new mongoose.Schema({
  orderId: { type: String, required: true, unique: true },
  customerId: { type: String, required: true },
  items: [{
    productId: { type: String, required: true },
    name: { type: String, required: true },
    quantity: { type: Number, required: true, min: 1 },
    price: { type: Number, required: true, min: 0 }
  }],
  totalAmount: { type: Number, required: true, min: 0 },
  shippingAddress: {
    street: { type: String, required: true },
    city: { type: String, required: true },
    state: { type: String, required: true },
    zipCode: { type: String, required: true },
    country: { type: String, required: true }
  },
  paymentStatus: { type: String, enum: ['pending', 'completed', 'failed'], default: 'pending' },
  paymentId: { type: String },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Create Order model
const Order = mongoose.model('Order', orderSchema);

// Input validation middleware
const validateOrderInput = (req, res, next) => {
  const { items, shippingAddress, customerId } = req.body;

  if (!items || !Array.isArray(items) || items.length === 0) {
    return res.status(400).json({ error: 'At least one item is required' });
  }

  if (!shippingAddress || !shippingAddress.street || !shippingAddress.city || 
      !shippingAddress.state || !shippingAddress.zipCode || !shippingAddress.country) {
    return res.status(400).json({ error: 'Complete shipping address is required' });
  }

  if (!customerId || !validator.isAlphanumeric(customerId)) {
    return res.status(400).json({ error: 'Valid customer ID is required' });
  }

  for (const item of items) {
    if (!item.productId || !item.name || !item.quantity || !item.price) {
      return res.status(400).json({ error: 'Each item must have productId, name, quantity, and price' });
    }
    if (item.quantity < 1) {
      return res.status(400).json({ error: 'Quantity must be at least 1' });
    }
    if (item.price <= 0) {
      return res.status(400).json({ error: 'Price must be greater than 0' });
    }
  }

  next();
};

// Create order endpoint
app.post('/api/orders', validateOrderInput, async (req, res) => {
  try {
    const { items, shippingAddress, customerId } = req.body;
    const totalAmount = items.reduce((sum, item) => sum + (item.price * item.quantity), 0);

    const order = new Order({
      orderId: uuidv4(),
      customerId,
      items,
      totalAmount,
      shippingAddress,
      paymentStatus: 'pending'
    });

    await order.save();
    res.status(201).json(order);
  } catch (error) {
    console.error('Error creating order:', error);
    res.status(500).json({ error: 'Failed to create order' });
  }
});

// Process payment endpoint
app.post('/api/orders/:orderId/pay', async (req, res) => {
  try {
    const { orderId } = req.params;
    const { paymentMethodId } = req.body;

    if (!paymentMethodId) {
      return res.status(400).json({ error: 'Payment method ID is required' });
    }

    const order = await Order.findOne({ orderId });
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    if (order.paymentStatus === 'completed') {
      return res.status(400).json({ error: 'Order already paid' });
    }

    // Create payment intent with Stripe
    const paymentIntent = await stripe.paymentIntents.create({
      amount: Math.round(order.totalAmount * 100), // Convert to cents
      currency: 'usd',
      payment_method: paymentMethodId,
      confirm: true,
      description: `Payment for order ${order.orderId}`,
      metadata: { orderId: order.orderId }
    });

    if (paymentIntent.status !== 'succeeded') {
      throw new Error('Payment failed');
    }

    // Update order with payment details
    order.paymentStatus = 'completed';
    order.paymentId = paymentIntent.id;
    order.updatedAt = new Date();
    await order.save();

    res.json({ 
      success: true, 
      orderId: order.orderId,
      paymentId: paymentIntent.id 
    });
  } catch (error) {
    console.error('Payment processing error:', error);
    
    // Update order status if payment failed
    if (error.type === 'StripeCardError') {
      await Order.updateOne(
        { orderId: req.params.orderId },
        { $set: { paymentStatus: 'failed', updatedAt: new Date() } }
      );
    }

    res.status(500).json({ 
      error: 'Payment processing failed',
      details: error.message 
    });
  }
});

// Get order details endpoint
app.get('/api/orders/:orderId', async (req, res) => {
  try {
    const { orderId } = req.params;
    const order = await Order.findOne({ orderId });

    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    res.json(order);
  } catch (error) {
    console.error('Error fetching order:', error);
    res.status(500).json({ error: 'Failed to fetch order' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
