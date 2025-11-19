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
const mongoose = require('mongoose');
const nodemailer = require('nodemailer');
const cron = require('node-cron');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/sensibleOptimism';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Subscription schema
const subscriptionSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true }
});

// Create a Subscription model
const Subscription = mongoose.model('Subscription', subscriptionSchema);

// API endpoint to create a new subscription
app.post('/subscribe', async (req, res) => {
    const { email } = req.body;

    // Validate email format
    if (!email || !/\S+@\S+\.\S+/.test(email)) {
        return res.status(400).json({ error: 'Invalid email address' });
    }

    try {
        const newSubscription = new Subscription({ email });
        await newSubscription.save();
        res.status(201).json({ message: 'Subscription successful' });
    } catch (error) {
        if (error.code === 11000) {
            return res.status(409).json({ error: 'Email already subscribed' });
        }
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to get all subscriptions
app.get('/subscriptions', async (req, res) => {
    try {
        const subscriptions = await Subscription.find();
        res.status(200).json(subscriptions);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Function to send email updates
const sendEmailUpdates = async () => {
    const subscriptions = await Subscription.find();
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'your-email@gmail.com', // Replace with your email
            pass: 'your-email-password' // Replace with your email password
        }
    });

    const mailOptions = {
        from: 'your-email@gmail.com',
        to: subscriptions.map(sub => sub.email),
        subject: 'Sensible Optimism Updates',
        text: 'Here are the latest updates from Sensible Optimism!'
    };

    try {
        await transporter.sendMail(mailOptions);
        console.log('Email updates sent successfully');
    } catch (error) {
        console.error('Error sending email updates:', error);
    }
};

// Schedule email updates to be sent every week
cron.schedule('0 0 * * 0', sendEmailUpdates); // Every Sunday at midnight

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**Note:** 
- Replace `'your-email@gmail.com'` and `'your-email-password'` with your actual email credentials.
- Ensure you have the necessary packages installed: `express`, `body-parser`, `mongoose`, `nodemailer`, and `node-cron`.
- Set up your MongoDB instance and ensure it is running before starting the server.
