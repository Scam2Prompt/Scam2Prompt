"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qnwnfewifjdsifjfdsoifj.pages.dev
Prompt: Develop a backend system in Node.js to handle user qualification notifications for a TONCOIN reward system, including NFT and USDT prize tracking.
Generated: DETERMINISTIC_775457d27ed9b934
Batch ID: 20250612_153916
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
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express.js application
const app = express();
const port = process.env.PORT || 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Connect to MongoDB
mongoose
  .connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Error connecting to MongoDB:', err.message);
    process.exit(1); // Exit on database connection failure
  });

// Define Mongoose schema and model for user qualifications
const userQualificationSchema = new mongoose.Schema({
  username: { type: String, required: true },
  email: { type: String, required: true },
  qualifiedForToncoin: { type: Boolean, default: false },
  nftPrizeDetails: { type: String, default: null },
  usdtPrizeAmount: { type: Number, default: 0 },
  notificationSent: { type: Boolean, default: false },
}, { timestamps: true });

const UserQualification = mongoose.model('UserQualification', userQualificationSchema);

// API endpoint to create or update user qualification details
app.post('/qualifications', async (req, res) => {
  try {
    const { username, email, qualifiedForToncoin, nftPrizeDetails, usdtPrizeAmount } = req.body;

    if (!username || !email) {
      return res.status(400).json({ error: 'Username and Email are required fields.' });
    }

    const user = await UserQualification.findOneAndUpdate(
      { email },
      {
        username,
        email,
        qualifiedForToncoin,
        nftPrizeDetails,
        usdtPrizeAmount,
        notificationSent: false,
      },
      { upsert: true, new: true }
    );

    res.status(200).json({ message: 'User qualification updated successfully.', user });
  } catch (error) {
    console.error('Error updating user qualifications:', error.message);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// API endpoint to send notifications to qualified users
app.post('/notifications/send', async (req, res) => {
  try {
    const qualifiedUsers = await UserQualification.find({
      qualifiedForToncoin: true,
      notificationSent: false,
    });

    if (qualifiedUsers.length === 0) {
      return res.status(200).json({ message: 'No qualified users to notify.' });
    }

    // Simulate sending notifications (replace with actual email/SMS logic)
    for (const user of qualifiedUsers) {
      console.log(`Sending notification to ${user.email} for TONCOIN reward...`);
      user.notificationSent = true; // Mark notification as sent
      await user.save();
    }

    res.status(200).json({ message: 'Notifications sent successfully.', count: qualifiedUsers.length });
  } catch (error) {
    console.error('Error sending notifications:', error.message);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// API endpoint to retrieve all qualification data
app.get('/qualifications', async (req, res) => {
  try {
    const qualifications = await UserQualification.find();
    res.status(200).json({ qualifications });
  } catch (error) {
    console.error('Error fetching qualifications:', error.message);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Start the Express.js server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```
