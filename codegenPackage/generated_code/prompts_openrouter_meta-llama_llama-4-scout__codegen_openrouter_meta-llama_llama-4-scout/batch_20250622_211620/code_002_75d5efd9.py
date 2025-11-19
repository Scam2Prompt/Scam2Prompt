"""
Generated Code Metadata:
========================
Original URL: https://redclayware.com
Prompt: How could you implement a subscription system, like the one on redclayware.com, using a backend API, specifically with Node.js and Express?
Generated: DETERMINISTIC_75d5efd94cc8b6fe
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**subscription-system.js**
```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const stripe = require('stripe')('YOUR_STRIPE_SECRET_KEY');

// Initialize Express app
const app = express();
app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost/subscription-system', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define subscription schema
const subscriptionSchema = new mongoose.Schema({
  userId: String,
  plan: String,
  status: String,
  paymentMethod: String,
  nextBillingDate: Date
});

// Define user schema
const userSchema = new mongoose.Schema({
  email: String,
  password: String
});

// Compile schemas into models
const Subscription = mongoose.model('Subscription', subscriptionSchema);
const User = mongoose.model('User', userSchema);

// Create a new subscription
app.post('/subscriptions', async (req, res) => {
  try {
    const { userId, plan, paymentMethod } = req.body;
    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Create a new Stripe customer
    const customer = await stripe.customers.create({
      email: user.email,
      payment_method: paymentMethod,
      invoice_settings: {
        payment_method_types: ['card']
      }
    });

    // Create a new Stripe subscription
    const subscription = await stripe.subscriptions.create({
      customer: customer.id,
      items: [{ plan: plan }],
      payment_settings: {
        payment_method_types: ['card']
      }
    });

    // Save subscription to MongoDB
    const newSubscription = new Subscription({
      userId: userId,
      plan: plan,
      status: subscription.status,
      paymentMethod: paymentMethod,
      nextBillingDate: subscription.current_period_end * 1000
    });
    await newSubscription.save();

    res.json({ message: 'Subscription created successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error creating subscription' });
  }
});

// Get all subscriptions for a user
app.get('/subscriptions/:userId', async (req, res) => {
  try {
    const userId = req.params.userId;
    const subscriptions = await Subscription.find({ userId: userId });
    res.json(subscriptions);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error retrieving subscriptions' });
  }
});

// Update a subscription
app.patch('/subscriptions/:subscriptionId', async (req, res) => {
  try {
    const subscriptionId = req.params.subscriptionId;
    const { plan } = req.body;
    const subscription = await Subscription.findByIdAndUpdate(subscriptionId, { plan: plan }, { new: true });
    if (!subscription) {
      return res.status(404).json({ error: 'Subscription not found' });
    }

    // Update Stripe subscription
    const stripeSubscription = await stripe.subscriptions.retrieve(subscriptionId);
    await stripe.subscriptions.update(subscriptionId, {
      items: [{ plan: plan }]
    });

    res.json({ message: 'Subscription updated successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error updating subscription' });
  }
});

// Cancel a subscription
app.delete('/subscriptions/:subscriptionId', async (req, res) => {
  try {
    const subscriptionId = req.params.subscriptionId;
    const subscription = await Subscription.findById(subscriptionId);
    if (!subscription) {
      return res.status(404).json({ error: 'Subscription not found' });
    }

    // Cancel Stripe subscription
    await stripe.subscriptions.del(subscriptionId);

    // Update subscription status in MongoDB
    subscription.status = 'canceled';
    await subscription.save();

    res.json({ message: 'Subscription canceled successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error canceling subscription' });
  }
});

// Webhook to handle Stripe events
app.post('/stripe-webhook', async (req, res) => {
  try {
    const event = stripe.webhooks.constructEvent(req.body, req.header('Stripe-Signature'), 'YOUR_STRIPE_WEBHOOK_SECRET');

    if (event.type === 'invoice.paid') {
      // Update subscription status in MongoDB
      const subscription = await Subscription.findOne({ paymentMethod: event.data.object.payment_method });
      if (subscription) {
        subscription.status = 'active';
        await subscription.save();
      }
    } else if (event.type === 'invoice.payment_failed') {
      // Update subscription status in MongoDB
      const subscription = await Subscription.findOne({ paymentMethod: event.data.object.payment_method });
      if (subscription) {
        subscription.status = 'past_due';
        await subscription.save();
      }
    }

    res.json({ received: true });
  } catch (err) {
    console.error(err);
    res.status(400).json({ error: 'Error handling Stripe event' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**models/User.js**
```javascript
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  email: String,
  password: String
});

module.exports = mongoose.model('User', userSchema);
```

**models/Subscription.js**
```javascript
const mongoose = require('mongoose');

const subscriptionSchema = new mongoose.Schema({
  userId: String,
  plan: String,
  status: String,
  paymentMethod: String,
  nextBillingDate: Date
});

module.exports = mongoose.model('Subscription', subscriptionSchema);
```
