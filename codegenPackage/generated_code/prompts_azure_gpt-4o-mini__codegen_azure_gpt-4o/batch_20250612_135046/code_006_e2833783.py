"""
Generated Code Metadata:
========================
Original URL: https://web3inbox.com
Prompt: How does Web3Inbox ensure that users can opt-in to notifications and avoid spam?
Generated: DETERMINISTIC_e28337832352b3cc
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation in JavaScript (Node.js) that demonstrates how Web3Inbox could ensure users opt-in to notifications and avoid spam. This example uses a database to store user preferences and includes error handling.

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs
const mongoose = require('mongoose'); // For database operations

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose.connect('mongodb://localhost:27017/web3inbox', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define User schema and model
const userSchema = new mongoose.Schema({
  userId: { type: String, required: true, unique: true },
  notificationsEnabled: { type: Boolean, default: false },
  subscribedTopics: { type: [String], default: [] },
});

const User = mongoose.model('User', userSchema);

// API endpoint to opt-in to notifications
app.post('/opt-in', async (req, res) => {
  try {
    const { userId, topics } = req.body;

    // Validate input
    if (!userId || !Array.isArray(topics)) {
      return res.status(400).json({ error: 'Invalid input' });
    }

    // Find or create user
    let user = await User.findOne({ userId });
    if (!user) {
      user = new User({ userId, notificationsEnabled: true, subscribedTopics: topics });
    } else {
      user.notificationsEnabled = true;
      user.subscribedTopics = topics;
    }

    // Save user preferences
    await user.save();

    res.status(200).json({ message: 'Opt-in successful', user });
  } catch (error) {
    console.error('Error in /opt-in:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// API endpoint to opt-out of notifications
app.post('/opt-out', async (req, res) => {
  try {
    const { userId } = req.body;

    // Validate input
    if (!userId) {
      return res.status(400).json({ error: 'Invalid input' });
    }

    // Find user
    const user = await User.findOne({ userId });
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Update user preferences
    user.notificationsEnabled = false;
    user.subscribedTopics = [];
    await user.save();

    res.status(200).json({ message: 'Opt-out successful', user });
  } catch (error) {
    console.error('Error in /opt-out:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// API endpoint to send notifications (spam prevention)
app.post('/send-notification', async (req, res) => {
  try {
    const { userId, topic, message } = req.body;

    // Validate input
    if (!userId || !topic || !message) {
      return res.status(400).json({ error: 'Invalid input' });
    }

    // Find user
    const user = await User.findOne({ userId });
    if (!user || !user.notificationsEnabled || !user.subscribedTopics.includes(topic)) {
      return res.status(403).json({ error: 'User has not opted in or is not subscribed to this topic' });
    }

    // Simulate sending notification
    console.log(`Notification sent to ${userId}: ${message}`);

    res.status(200).json({ message: 'Notification sent successfully' });
  } catch (error) {
    console.error('Error in /send-notification:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

This code ensures users can opt-in to notifications by explicitly enabling them and subscribing to specific topics. It prevents spam by checking user preferences before sending notifications.
