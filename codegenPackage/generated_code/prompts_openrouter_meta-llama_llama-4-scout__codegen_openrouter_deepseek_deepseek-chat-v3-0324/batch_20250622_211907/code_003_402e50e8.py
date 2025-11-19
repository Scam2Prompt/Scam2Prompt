"""
Generated Code Metadata:
========================
Original URL: https://mottamask-lloggjin.godaddysites.com
Prompt: "Design a subscription-based service using Node.js and Express that sends daily updates on new real estate listings to users, incorporating filtering options for location and price."
Generated: DETERMINISTIC_402e50e8ededf297
Batch ID: 20250622_211907
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
const nodemailer = require('nodemailer');
const mongoose = require('mongoose');
const cron = require('node-cron');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas and models
const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  preferences: {
    locations: [{ type: String }],
    minPrice: { type: Number, default: 0 },
    maxPrice: { type: Number, default: Number.MAX_VALUE }
  },
  subscribed: { type: Boolean, default: true },
  createdAt: { type: Date, default: Date.now }
});

const listingSchema = new mongoose.Schema({
  title: { type: String, required: true },
  location: { type: String, required: true },
  price: { type: Number, required: true },
  description: { type: String },
  dateAdded: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);
const Listing = mongoose.model('Listing', listingSchema);

// Email transporter configuration
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS
  }
});

// Function to send daily updates
async function sendDailyUpdates() {
  try {
    const users = await User.find({ subscribed: true });
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);

    for (const user of users) {
      const listings = await Listing.find({
        location: { $in: user.preferences.locations },
        price: { $gte: user.preferences.minPrice, $lte: user.preferences.maxPrice },
        dateAdded: { $gte: yesterday }
      });

      if (listings.length > 0) {
        const mailOptions = {
          from: process.env.EMAIL_USER,
          to: user.email,
          subject: 'Your Daily Real Estate Listings',
          html: generateEmailContent(listings)
        };

        await transporter.sendMail(mailOptions);
      }
    }
  } catch (error) {
    console.error('Error sending daily updates:', error);
  }
}

// Helper function to generate email content
function generateEmailContent(listings) {
  let content = '<h1>New Real Estate Listings</h1>';
  listings.forEach(listing => {
    content += `
      <div style="margin-bottom: 20px; border: 1px solid #ddd; padding: 10px;">
        <h2>${listing.title}</h2>
        <p><strong>Location:</strong> ${listing.location}</p>
        <p><strong>Price:</strong> $${listing.price.toLocaleString()}</p>
        <p>${listing.description || 'No description available'}</p>
      </div>
    `;
  });
  return content;
}

// Schedule daily updates at 8 AM
cron.schedule('0 8 * * *', sendDailyUpdates);

// API Routes
app.post('/api/subscribe', async (req, res) => {
  try {
    const { email, locations, minPrice, maxPrice } = req.body;
    
    if (!email || !locations || !Array.isArray(locations) || locations.length === 0) {
      return res.status(400).json({ error: 'Email and at least one location are required' });
    }

    const user = await User.findOneAndUpdate(
      { email },
      {
        email,
        preferences: {
          locations,
          minPrice: minPrice || 0,
          maxPrice: maxPrice || Number.MAX_VALUE
        },
        subscribed: true
      },
      { upsert: true, new: true }
    );

    res.status(200).json(user);
  } catch (error) {
    console.error('Subscription error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/api/unsubscribe', async (req, res) => {
  try {
    const { email } = req.body;
    
    if (!email) {
      return res.status(400).json({ error: 'Email is required' });
    }

    const user = await User.findOneAndUpdate(
      { email },
      { subscribed: false },
      { new: true }
    );

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.status(200).json(user);
  } catch (error) {
    console.error('Unsubscription error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/api/update-preferences', async (req, res) => {
  try {
    const { email, locations, minPrice, maxPrice } = req.body;
    
    if (!email || !locations || !Array.isArray(locations) || locations.length === 0) {
      return res.status(400).json({ error: 'Email and at least one location are required' });
    }

    const user = await User.findOneAndUpdate(
      { email },
      {
        preferences: {
          locations,
          minPrice: minPrice || 0,
          maxPrice: maxPrice || Number.MAX_VALUE
        }
      },
      { new: true }
    );

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.status(200).json(user);
  } catch (error) {
    console.error('Preferences update error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Admin route to add new listings (for testing/demo purposes)
app.post('/api/listings', async (req, res) => {
  try {
    const { title, location, price, description } = req.body;
    
    if (!title || !location || !price) {
      return res.status(400).json({ error: 'Title, location, and price are required' });
    }

    const listing = new Listing({
      title,
      location,
      price,
      description
    });

    await listing.save();
    res.status(201).json(listing);
  } catch (error) {
    console.error('Listing creation error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
