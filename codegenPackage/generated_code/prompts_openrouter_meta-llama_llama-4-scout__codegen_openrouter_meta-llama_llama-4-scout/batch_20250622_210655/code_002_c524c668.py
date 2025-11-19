"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Generate a code snippet in JavaScript to create a donation system for supporting environmental organizations like Čuvari Šare, including payment gateway integration and transaction tracking.
Generated: DETERMINISTIC_c524c6687b9bf977
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// donation-system.js

/**
 * Donation System for supporting environmental organizations
 * 
 * @author [Your Name]
 */

// Import required libraries
const express = require('express');
const stripe = require('stripe')('YOUR_STRIPE_SECRET_KEY'); // Replace with your Stripe secret key
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/donation-system', { useNewUrlParser: true, useUnifiedTopology: true });

// Define the Donation model
const donationSchema = new mongoose.Schema({
  amount: Number,
  organization: String,
  transactionId: String,
  status: String
});

const Donation = mongoose.model('Donation', donationSchema);

// Create an Express app
const app = express();
app.use(express.json());

// Define a function to create a donation
async function createDonation(req, res) {
  try {
    const { amount, organization } = req.body;
    if (!amount || !organization) {
      return res.status(400).send({ error: 'Amount and organization are required' });
    }

    // Create a Stripe payment intent
    const paymentIntent = await stripe.paymentIntents.create({
      amount: Math.round(amount * 100), // Convert to cents
      currency: 'eur', // Replace with your desired currency
      payment_method_types: ['card']
    });

    // Create a new donation document
    const donation = new Donation({
      amount,
      organization,
      transactionId: paymentIntent.id,
      status: 'pending'
    });

    // Save the donation document
    await donation.save();

    // Return the payment intent client secret
    res.send({ clientSecret: paymentIntent.client_secret });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Failed to create donation' });
  }
}

// Define a function to handle Stripe webhook events
async function handleWebhook(req, res) {
  try {
    const event = stripe.webhooks.constructEvent(req.body, req.header('Stripe-Signature'), 'YOUR_STRIPE_WEBHOOK_SECRET');

    if (event.type === 'payment_intent.succeeded') {
      const paymentIntent = event.data.object;
      const donation = await Donation.findOne({ transactionId: paymentIntent.id });

      if (donation) {
        donation.status = 'success';
        await donation.save();
      }
    } else if (event.type === 'payment_intent.failed') {
      const paymentIntent = event.data.object;
      const donation = await Donation.findOne({ transactionId: paymentIntent.id });

      if (donation) {
        donation.status = 'failed';
        await donation.save();
      }
    }

    res.send({ received: true });
  } catch (error) {
    console.error(error);
    res.status(400).send({ error: 'Invalid request' });
  }
}

// Define routes
app.post('/donations', createDonation);
app.post('/stripe/webhook', handleWebhook);

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
