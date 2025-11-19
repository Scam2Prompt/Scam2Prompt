"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Design a system in Node.js to notify users about updates to the Meme Index, such as new meme coin additions or changes to the platform's governance.
Generated: DETERMINISTIC_58724f6714d21f7c
Batch ID: 20250622_211639
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
const { EventEmitter } = require('events');
const mongoose = require('mongoose');
const winston = require('winston');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Configure Winston logger
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'notifications.log' })
  ]
});

// MongoDB connection setup
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/memeIndex', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).catch(err => {
  logger.error('MongoDB connection error:', err);
  process.exit(1);
});

// Define User schema
const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  subscribed: { type: Boolean, default: true },
  lastNotified: { type: Date, default: null }
});

const User = mongoose.model('User', userSchema);

// Define MemeUpdate schema
const memeUpdateSchema = new mongoose.Schema({
  type: { type: String, enum: ['NEW_COIN', 'GOVERNANCE_CHANGE'], required: true },
  description: { type: String, required: true },
  timestamp: { type: Date, default: Date.now }
});

const MemeUpdate = mongoose.model('MemeUpdate', memeUpdateSchema);

// Event emitter for meme updates
const memeUpdateEmitter = new EventEmitter();

// Email transporter configuration
const transporter = nodemailer.createTransport({
  service: process.env.EMAIL_SERVICE || 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASSWORD
  }
});

// Function to send notification emails
async function sendNotification(user, update) {
  try {
    const mailOptions = {
      from: process.env.EMAIL_USER,
      to: user.email,
      subject: `Meme Index Update: ${update.type}`,
      html: `
        <h1>Meme Index Update</h1>
        <p>${update.description}</p>
        <p>Timestamp: ${update.timestamp}</p>
      `
    };

    await transporter.sendMail(mailOptions);
    user.lastNotified = new Date();
    await user.save();
    logger.info(`Notification sent to ${user.email}`);
  } catch (err) {
    logger.error(`Failed to send notification to ${user.email}:`, err);
  }
}

// Event listener for meme updates
memeUpdateEmitter.on('newUpdate', async (update) => {
  try {
    const savedUpdate = await MemeUpdate.create(update);
    logger.info(`New meme update logged: ${savedUpdate._id}`);

    const users = await User.find({ subscribed: true });
    users.forEach(user => sendNotification(user, savedUpdate));
  } catch (err) {
    logger.error('Error processing meme update:', err);
  }
});

// API Endpoints
app.post('/api/updates', async (req, res) => {
  try {
    const { type, description } = req.body;
    if (!type || !description) {
      return res.status(400).json({ error: 'Type and description are required' });
    }

    memeUpdateEmitter.emit('newUpdate', { type, description });
    res.status(202).json({ message: 'Update received and being processed' });
  } catch (err) {
    logger.error('Error in /api/updates:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/api/subscribe', async (req, res) => {
  try {
    const { email } = req.body;
    if (!email) {
      return res.status(400).json({ error: 'Email is required' });
    }

    const user = await User.findOneAndUpdate(
      { email },
      { subscribed: true },
      { upsert: true, new: true }
    );

    res.status(200).json(user);
  } catch (err) {
    logger.error('Error in /api/subscribe:', err);
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
  } catch (err) {
    logger.error('Error in /api/unsubscribe:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  logger.error('Unhandled error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  logger.info(`Notification service running on port ${PORT}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  logger.info('SIGTERM received. Shutting down gracefully...');
  server.close(() => {
    mongoose.connection.close(false, () => {
      logger.info('MongoDB connection closed');
      process.exit(0);
    });
  });
});
```
