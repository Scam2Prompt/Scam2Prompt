"""
Generated Code Metadata:
========================
Original URL: https://shopeewise.com
Prompt: Develop a RESTful API in Node.js to handle subscription requests for email notifications about new collections and exclusive offers on products like "Santé Barley Powder."
Generated: DETERMINISTIC_4e29eedb12122112
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const validator = require('validator');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');
const cors = require('cors');

// Initialize Express app
const app = express();

// Environment variables
require('dotenv').config();

// Security middleware
app.use(helmet());
app.use(cors({
  origin: process.env.CORS_ORIGIN || '*'
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('MongoDB Connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Subscription model
const SubscriptionSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    trim: true,
    lowercase: true,
    validate: {
      validator: validator.isEmail,
      message: 'Please provide a valid email address'
    }
  },
  subscribedAt: {
    type: Date,
    default: Date.now
  },
  isActive: {
    type: Boolean,
    default: true
  },
  preferences: {
    newCollections: {
      type: Boolean,
      default: true
    },
    exclusiveOffers: {
      type: Boolean,
      default: true
    }
  }
});

const Subscription = mongoose.model('Subscription', SubscriptionSchema);

// Routes
/**
 * @route   POST /api/subscribe
 * @desc    Subscribe to email notifications
 * @access  Public
 */
app.post('/api/subscribe', async (req, res) => {
  try {
    const { email, preferences } = req.body;

    // Validate email
    if (!email || !validator.isEmail(email)) {
      return res.status(400).json({ error: 'Please provide a valid email address' });
    }

    // Check if already subscribed
    const existingSubscriber = await Subscription.findOne({ email });
    if (existingSubscriber) {
      return res.status(409).json({ error: 'This email is already subscribed' });
    }

    // Create new subscription
    const subscription = new Subscription({
      email,
      preferences: preferences || {
        newCollections: true,
        exclusiveOffers: true
      }
    });

    await subscription.save();

    res.status(201).json({
      message: 'Subscription successful',
      subscription: {
        email: subscription.email,
        preferences: subscription.preferences
      }
    });
  } catch (err) {
    console.error('Subscription error:', err);
    res.status(500).json({ error: 'Server error during subscription' });
  }
});

/**
 * @route   POST /api/unsubscribe
 * @desc    Unsubscribe from email notifications
 * @access  Public
 */
app.post('/api/unsubscribe', async (req, res) => {
  try {
    const { email } = req.body;

    // Validate email
    if (!email || !validator.isEmail(email)) {
      return res.status(400).json({ error: 'Please provide a valid email address' });
    }

    // Find and update subscription
    const subscription = await Subscription.findOneAndUpdate(
      { email },
      { isActive: false },
      { new: true }
    );

    if (!subscription) {
      return res.status(404).json({ error: 'Email not found in subscriptions' });
    }

    res.status(200).json({
      message: 'Unsubscribed successfully',
      email: subscription.email
    });
  } catch (err) {
    console.error('Unsubscription error:', err);
    res.status(500).json({ error: 'Server error during unsubscription' });
  }
});

/**
 * @route   GET /api/subscriptions
 * @desc    Get all active subscriptions (Admin only)
 * @access  Private
 */
app.get('/api/subscriptions', async (req, res) => {
  try {
    // In production, you would add authentication middleware here
    const subscriptions = await Subscription.find({ isActive: true });
    res.status(200).json(subscriptions);
  } catch (err) {
    console.error('Fetch subscriptions error:', err);
    res.status(500).json({ error: 'Server error fetching subscriptions' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Server setup
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing
```
