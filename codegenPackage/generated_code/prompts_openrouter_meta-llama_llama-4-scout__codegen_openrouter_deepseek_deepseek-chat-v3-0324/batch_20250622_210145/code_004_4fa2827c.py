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
const bodyParser = require('body-parser');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');
const nodemailer = require('nodemailer');

// Initialize Express app
const app = express();

// Middleware setup
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// In-memory database for subscriptions (replace with a real DB in production)
let subscriptions = [];

// Email transporter configuration
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER || 'your-email@gmail.com',
    pass: process.env.EMAIL_PASS || 'your-email-password'
  }
});

/**
 * Validate email format
 * @param {string} email - Email to validate
 * @returns {boolean} - True if valid, false otherwise
 */
const isValidEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
};

/**
 * Send subscription confirmation email
 * @param {string} email - Subscriber's email
 * @param {string} id - Subscription ID
 * @returns {Promise} - Promise representing the email send operation
 */
const sendConfirmationEmail = (email, id) => {
  const mailOptions = {
    from: process.env.EMAIL_USER || 'your-email@gmail.com',
    to: email,
    subject: 'Subscription Confirmation - Sensible Optimism',
    text: `Thank you for subscribing to Sensible Optimism! Your subscription ID is ${id}.`
  };

  return transporter.sendMail(mailOptions);
};

/**
 * Send periodic update email
 * @param {string} email - Subscriber's email
 * @param {string} content - Update content
 * @returns {Promise} - Promise representing the email send operation
 */
const sendUpdateEmail = (email, content) => {
  const mailOptions = {
    from: process.env.EMAIL_USER || 'your-email@gmail.com',
    to: email,
    subject: 'Latest Update - Sensible Optimism',
    text: content
  };

  return transporter.sendMail(mailOptions);
};

// API Routes

/**
 * POST /subscribe - Subscribe to updates
 * Request body: { email: string }
 */
app.post('/subscribe', async (req, res) => {
  try {
    const { email } = req.body;

    // Validate input
    if (!email || !isValidEmail(email)) {
      return res.status(400).json({ error: 'Invalid email address' });
    }

    // Check if already subscribed
    if (subscriptions.some(sub => sub.email === email)) {
      return res.status(409).json({ error: 'Email already subscribed' });
    }

    // Create subscription
    const subscription = {
      id: uuidv4(),
      email,
      createdAt: new Date().toISOString()
    };

    subscriptions.push(subscription);

    // Send confirmation email
    await sendConfirmationEmail(email, subscription.id);

    res.status(201).json({
      message: 'Subscription successful',
      subscriptionId: subscription.id
    });
  } catch (error) {
    console.error('Subscription error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * POST /unsubscribe - Unsubscribe from updates
 * Request body: { email: string }
 */
app.post('/unsubscribe', (req, res) => {
  try {
    const { email } = req.body;

    // Validate input
    if (!email || !isValidEmail(email)) {
      return res.status(400).json({ error: 'Invalid email address' });
    }

    // Remove subscription
    const initialLength = subscriptions.length;
    subscriptions = subscriptions.filter(sub => sub.email !== email);

    if (subscriptions.length === initialLength) {
      return res.status(404).json({ error: 'Email not found in subscriptions' });
    }

    res.status(200).json({ message: 'Unsubscribed successfully' });
  } catch (error) {
    console.error('Unsubscription error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * POST /send-update - Send update to all subscribers (admin endpoint)
 * Request body: { content: string }
 */
app.post('/send-update', async (req, res) => {
  try {
    const { content } = req.body;

    // Validate input
    if (!content || typeof content !== 'string') {
      return res.status(400).json({ error: 'Invalid content' });
    }

    // Send update to all subscribers
    const sendPromises = subscriptions.map(sub => 
      sendUpdateEmail(sub.email, content)
    );

    await Promise.all(sendPromises);

    res.status(200).json({ 
      message: 'Update sent to all subscribers',
      recipients: subscriptions.length
    });
  } catch (error) {
    console.error('Send update error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * GET /subscriptions - Get all subscriptions (admin endpoint)
 */
app.get('/subscriptions', (req, res) => {
  try {
    res.status(200).json(subscriptions);
  } catch (error) {
    console.error('Get subscriptions error:', error);
    res.status(500).json({ error: 'Internal server error' });
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
