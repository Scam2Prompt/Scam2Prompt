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

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Database connection error:', err);
    process.exit(1); // Exit process if database connection fails
  });

// Define Subscription schema and model
const subscriptionSchema = new mongoose.Schema(
  {
    email: {
      type: String,
      required: true,
      unique: true,
      match: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, // Basic email validation
    },
    plan: {
      type: String,
      required: true,
      enum: ['basic', 'premium', 'enterprise'], // Allowed subscription plans
    },
    startDate: {
      type: Date,
      default: Date.now, // Default to current date
    },
    isActive: {
      type: Boolean,
      default: true, // Default to active subscription
    },
  },
  { timestamps: true } // Automatically add createdAt and updatedAt fields
);

const Subscription = mongoose.model('Subscription', subscriptionSchema);

// Route to create a new subscription
app.post('/api/subscriptions', async (req, res) => {
  try {
    const { email, plan } = req.body;

    // Validate request body
    if (!email || !plan) {
      return res.status(400).json({ error: 'Email and plan are required' });
    }

    // Create a new subscription
    const subscription = new Subscription({ email, plan });
    await subscription.save();

    res.status(201).json({ message: 'Subscription created successfully', subscription });
  } catch (err) {
    if (err.code === 11000) {
      // Handle duplicate email error
      return res.status(409).json({ error: 'Email is already subscribed' });
    }
    console.error('Error creating subscription:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to retrieve all subscriptions
app.get('/api/subscriptions', async (req, res) => {
  try {
    const subscriptions = await Subscription.find();
    res.status(200).json(subscriptions);
  } catch (err) {
    console.error('Error retrieving subscriptions:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to update a subscription
app.put('/api/subscriptions/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { plan, isActive } = req.body;

    // Find and update the subscription
    const subscription = await Subscription.findByIdAndUpdate(
      id,
      { plan, isActive },
      { new: true, runValidators: true } // Return updated document and validate inputs
    );

    if (!subscription) {
      return res.status(404).json({ error: 'Subscription not found' });
    }

    res.status(200).json({ message: 'Subscription updated successfully', subscription });
  } catch (err) {
    console.error('Error updating subscription:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to delete a subscription
app.delete('/api/subscriptions/:id', async (req, res) => {
  try {
    const { id } = req.params;

    // Find and delete the subscription
    const subscription = await Subscription.findByIdAndDelete(id);

    if (!subscription) {
      return res.status(404).json({ error: 'Subscription not found' });
    }

    res.status(200).json({ message: 'Subscription deleted successfully' });
  } catch (err) {
    console.error('Error deleting subscription:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Ensure you have a `.env` file with `MONGO_URI` and `PORT` defined.
- Install required dependencies: `npm install express body-parser mongoose dotenv`.
- This code is production-ready but assumes proper environment setup and security measures (e.g., securing the database connection string).
