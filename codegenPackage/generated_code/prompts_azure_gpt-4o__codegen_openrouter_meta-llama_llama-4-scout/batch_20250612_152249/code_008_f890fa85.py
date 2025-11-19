"""
Generated Code Metadata:
========================
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: Write code to implement a subscription system for early whitelist registration in the Rivalz TESTNET environment.
Generated: DETERMINISTIC_f890fa851937624d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// subscriptionSystem.js

/**
 * Subscription System for Early Whitelist Registration in Rivalz TESTNET Environment
 * ============================================================================
 */

// Import required libraries
const express = require('express');
const mongoose = require('mongoose');
const nodemailer = require('nodemailer');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

class SubscriptionSystem {
  /**
   * Initialize the subscription system
   */
  constructor() {
    this.app = express();
    this.app.use(express.json());

    // Connect to MongoDB
    mongoose.connect(process.env.MONGODB_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    })
      .then(() => console.log('Connected to MongoDB'))
      .catch((error) => console.error('Error connecting to MongoDB:', error));

    // Define the subscription schema
    const subscriptionSchema = new mongoose.Schema({
      email: {
        type: String,
        required: true,
        unique: true,
      },
      createdAt: {
        type: Date,
        default: Date.now,
      },
    });

    // Create the subscription model
    this.Subscription = mongoose.model('Subscription', subscriptionSchema);

    // Set up routes
    this.app.post('/subscribe', this.subscribe.bind(this));
    this.app.get('/subscriptions', this.getSubscriptions.bind(this));
  }

  /**
   * Subscribe to the whitelist
   * @param {Object} req - Express request object
   * @param {Object} res - Express response object
   */
  async subscribe(req, res) {
    try {
      const { email } = req.body;

      // Validate email
      if (!email || !email.includes('@')) {
        return res.status(400).json({ error: 'Invalid email address' });
      }

      // Check if already subscribed
      const existingSubscription = await this.Subscription.findOne({ email });
      if (existingSubscription) {
        return res.status(400).json({ error: 'Email already subscribed' });
      }

      // Create a new subscription
      const subscription = new this.Subscription({ email });
      await subscription.save();

      // Send confirmation email
      this.sendConfirmationEmail(email);

      res.json({ message: 'Subscribed successfully' });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  }

  /**
   * Get all subscriptions
   * @param {Object} req - Express request object
   * @param {Object} res - Express response object
   */
  async getSubscriptions(req, res) {
    try {
      const subscriptions = await this.Subscription.find().sort({ createdAt: -1 });
      res.json(subscriptions);
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  }

  /**
   * Send confirmation email
   * @param {String} email - Subscriber's email address
   */
  async sendConfirmationEmail(email) {
    try {
      const transporter = nodemailer.createTransport({
        host: process.env.EMAIL_HOST,
        port: process.env.EMAIL_PORT,
        secure: process.env.EMAIL_SECURE === 'true',
        auth: {
          user: process.env.EMAIL_USER,
          pass: process.env.EMAIL_PASSWORD,
        },
      });

      const mailOptions = {
        from: process.env.EMAIL_FROM,
        to: email,
        subject: 'Rivalz TESTNET Whitelist Subscription Confirmation',
        text: 'Thank you for subscribing to the Rivalz TESTNET whitelist!',
      };

      await transporter.sendMail(mailOptions);
    } catch (error) {
      console.error('Error sending confirmation email:', error);
    }
  }

  /**
   * Start the server
   */
  start() {
    const port = process.env.PORT || 3000;
    this.app.listen(port, () => {
      console.log(`Server listening on port ${port}`);
    });
  }
}

// Create and start the subscription system
const subscriptionSystem = new SubscriptionSystem();
subscriptionSystem.start();
```

```javascript
// .env

MONGODB_URI=mongodb://localhost:27017/rivalz-testnet
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_SECURE=false
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-email-password
EMAIL_FROM=Rivalz TESTNET <no-reply@rivalz.testnet>
PORT=3000
```

```bash
# package.json

{
  "name": "rivalz-subscription-system",
  "version": "1.0.0",
  "scripts": {
    "start": "node subscriptionSystem.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^6.2.10",
    "nodemailer": "^6.7.2",
    "dotenv": "^16.0.3"
  }
}
```
