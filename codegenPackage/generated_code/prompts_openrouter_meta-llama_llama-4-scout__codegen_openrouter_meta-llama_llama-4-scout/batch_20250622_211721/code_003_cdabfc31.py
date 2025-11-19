"""
Generated Code Metadata:
========================
Original URL: https://soulfn.lol
Prompt: Create a simple e-commerce API using Node.js to sell Fortnite accounts, similar to Soul's offerings, with pricing options and instant delivery.
Generated: DETERMINISTIC_cdabfc319355827c
Batch ID: 20250622_211721
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
const stripe = require('stripe')('sk_test_key'); // Replace with your Stripe secret key
const cors = require('cors');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/fortnite-accounts', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for Fortnite account
const accountSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
  level: Number,
  skins: [String],
  price: Number
});

// Define schema for Order
const orderSchema = new mongoose.Schema({
  account: { type: mongoose.Schema.Types.ObjectId, ref: 'Account' },
  customer: String,
  paymentMethod: String,
  status: String
});

// Create models
const Account = mongoose.model('Account', accountSchema);
const Order = mongoose.model('Order', orderSchema);

// Enable CORS and JSON parsing
app.use(cors());
app.use(express.json());

// Get all accounts
app.get('/accounts', async (req, res) => {
  try {
    const accounts = await Account.find().exec();
    res.json(accounts);
  } catch (err) {
    res.status(500).json({ message: 'Failed to retrieve accounts' });
  }
});

// Get account by ID
app.get('/accounts/:id', async (req, res) => {
  try {
    const account = await Account.findById(req.params.id).exec();
    if (!account) {
      res.status(404).json({ message: 'Account not found' });
    } else {
      res.json(account);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to retrieve account' });
  }
});

// Create order
app.post('/orders', async (req, res) => {
  try {
    const account = await Account.findById(req.body.accountId).exec();
    if (!account) {
      res.status(404).json({ message: 'Account not found' });
    } else {
      const order = new Order({
        account: account._id,
        customer: req.body.customer,
        paymentMethod: req.body.paymentMethod,
        status: 'pending'
      });
      await order.save();
      res.json(order);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to create order' });
  }
});

// Make payment
app.post('/pay', async (req, res) => {
  try {
    const order = await Order.findById(req.body.orderId).exec();
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else if (order.status !== 'pending') {
      res.status(400).json({ message: 'Order is not pending' });
    } else {
      const paymentIntent = await stripe.paymentIntents.create({
        amount: order.account.price * 100,
        currency: 'usd',
        payment_method_types: ['card']
      });
      res.json({ clientSecret: paymentIntent.client_secret });
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to create payment intent' });
  }
});

// Webhook for Stripe payment intent
app.post('/stripe-webhook', async (req, res) => {
  try {
    const event = stripe.webhooks.constructEvent(req.body, req.header('Stripe-Signature'), 'wh_secret_key'); // Replace with your Stripe webhook secret
    if (event.type === 'payment_intent.succeeded') {
      const order = await Order.findById(event.data.object.metadata.orderId).exec();
      if (order) {
        order.status = 'paid';
        await order.save();
        // Send account details to customer
        const account = await Account.findById(order.account).exec();
        // Replace with your email service
        // sendEmail(order.customer, account);
      }
    }
    res.json({ received: true });
  } catch (err) {
    res.status(400).json({ message: 'Webhook failed' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
