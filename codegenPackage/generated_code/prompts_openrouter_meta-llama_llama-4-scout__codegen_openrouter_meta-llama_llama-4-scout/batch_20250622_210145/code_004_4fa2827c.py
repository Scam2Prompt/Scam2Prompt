"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Design a simple backend API using Node.js and Express to manage subscriptions and send periodic updates about a blog or product called Sensible Optimism.
Generated: DETERMINISTIC_4fa2827c933f104c
Batch ID: 20250622_210145
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
const nodemailer = require('nodemailer');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/sensible-optimism', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for subscription model
const subscriptionSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  frequency: { type: String, required: true, enum: ['daily', 'weekly', 'monthly'] }
});

// Create subscription model
const Subscription = mongoose.model('Subscription', subscriptionSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Endpoint to create a new subscription
app.post('/subscribe', async (req, res) => {
  try {
    const { email, frequency } = req.body;
    if (!email || !frequency) {
      return res.status(400).send({ error: 'Email and frequency are required' });
    }
    const existingSubscription = await Subscription.findOne({ email });
    if (existingSubscription) {
      return res.status(400).send({ error: 'Email already subscribed' });
    }
    const subscription = new Subscription({ email, frequency });
    await subscription.save();
    res.send({ message: 'Subscribed successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal server error' });
  }
});

// Endpoint to get all subscriptions
app.get('/subscriptions', async (req, res) => {
  try {
    const subscriptions = await Subscription.find().exec();
    res.send(subscriptions);
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal server error' });
  }
});

// Endpoint to update a subscription
app.patch('/subscriptions/:email', async (req, res) => {
  try {
    const { email } = req.params;
    const { frequency } = req.body;
    if (!frequency) {
      return res.status(400).send({ error: 'Frequency is required' });
    }
    const subscription = await Subscription.findOneAndUpdate({ email }, { frequency }, { new: true });
    if (!subscription) {
      return res.status(404).send({ error: 'Subscription not found' });
    }
    res.send(subscription);
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal server error' });
  }
});

// Endpoint to delete a subscription
app.delete('/subscriptions/:email', async (req, res) => {
  try {
    const { email } = req.params;
    await Subscription.findOneAndRemove({ email });
    res.send({ message: 'Subscription deleted successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal server error' });
  }
});

// Function to send updates to subscribers
async function sendUpdates() {
  try {
    const subscriptions = await Subscription.find().exec();
    const transporter = nodemailer.createTransport({
      host: 'smtp.example.com',
      port: 587,
      auth: {
        user: 'username',
        pass: 'password'
      }
    });
    subscriptions.forEach(subscription => {
      const mailOptions = {
        from: 'Sensible Optimism <info@sensible-optimism.com>',
        to: subscription.email,
        subject: 'Your weekly update from Sensible Optimism',
        text: 'Here is your update...'
      };
      transporter.sendMail(mailOptions, error => {
        if (error) {
          console.error(error);
        } else {
          console.log(`Update sent to ${subscription.email}`);
        }
      });
    });
  } catch (error) {
    console.error(error);
  }
}

// Send updates periodically
setInterval(sendUpdates, 604800000); // 604800000 = 7 days in milliseconds

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
