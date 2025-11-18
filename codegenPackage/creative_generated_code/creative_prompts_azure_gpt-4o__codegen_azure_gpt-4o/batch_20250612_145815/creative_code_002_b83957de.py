"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Generate a script in Node.js to handle subscription payments and invite friends functionality, modeled after services like Rentsy.
Generated: DETERMINISTIC_b83957de9e95f05d
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const stripe = require('stripe')('your-stripe-secret-key'); // Replace with your Stripe secret key
const nodemailer = require('nodemailer');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Payment processing logic using Stripe
app.post('/subscribe', async (req, res) => {
  try {
    const { email, paymentMethodId, planId } = req.body;

    // Validate input
    if (!email || !paymentMethodId || !planId) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Create Stripe customer
    const customer = await stripe.customers.create({
      email,
      payment_method: paymentMethodId,
      invoice_settings: {
        default_payment_method: paymentMethodId,
      },
    });

    // Create subscription
    const subscription = await stripe.subscriptions.create({
      customer: customer.id,
      items: [{ plan: planId }],
      expand: ['latest_invoice.payment_intent'],
    });

    // Send success response
    res.status(200).json({
      message: 'Subscription created successfully!',
      subscriptionId: subscription.id,
    });
  } catch (error) {
    console.error('Error processing subscription:', error.message);
    res.status(500).json({ error: 'An error occurred while processing your subscription' });
  }
});

// Invite friends functionality
app.post('/invite', async (req, res) => {
  try {
    const { senderEmail, recipientEmail, message } = req.body;

    // Validate input
    if (!senderEmail || !recipientEmail || !message) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Configure mail transporter
    const transporter = nodemailer.createTransport({
      service: 'gmail', // Use a valid email service, e.g., Gmail, Outlook
      auth: {
        user: process.env.EMAIL_USERNAME, // Your email address
        pass: process.env.EMAIL_PASSWORD, // Your email password
      },
    });

    // Email options
    const mailOptions = {
      from: senderEmail,
      to: recipientEmail,
      subject: 'You have been invited!',
      text: message,
    };

    // Send email
    await transporter.sendMail(mailOptions);

    // Send success response
    res.status(200).json({ message: 'Invitation sent successfully!' });
  } catch (error) {
    console.error('Error sending invitation:', error.message);
    res.status(500).json({ error: 'An error occurred while sending the invitation' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

This script provides subscription functionality using Stripe and an invite friends feature using Nodemailer. Ensure you have appropriate credentials and environment variables (e.g., Stripe secret key, email username/password) set up before running the script.
