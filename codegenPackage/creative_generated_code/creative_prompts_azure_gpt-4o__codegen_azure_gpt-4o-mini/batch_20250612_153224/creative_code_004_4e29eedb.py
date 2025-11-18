"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Develop a RESTful API in Node.js to handle subscription requests for email notifications about new collections and exclusive offers on products like "Santé Barley Powder."
Generated: DETERMINISTIC_4e29eedb12122112
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required packages
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const nodemailer = require('nodemailer');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/subscriptions';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected...'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for subscription requests
const subscriptionSchema = new mongoose.Schema({
    email: {
        type: String,
        required: true,
        unique: true,
        match: /.+\@.+\..+/ // Simple email validation
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Create a model for the subscription schema
const Subscription = mongoose.model('Subscription', subscriptionSchema);

// POST endpoint to handle subscription requests
app.post('/subscribe', async (req, res) => {
    const { email } = req.body;

    // Validate email
    if (!email || !email.match(/.+\@.+\..+/)) {
        return res.status(400).json({ error: 'Invalid email address' });
    }

    try {
        // Create a new subscription
        const subscription = new Subscription({ email });
        await subscription.save();

        // Send the confirmation email (mock implementation)
        await sendConfirmationEmail(email);

        return res.status(201).json({ message: `Successfully subscribed ${email}` });
    } catch (err) {
        console.error('Error saving subscription:', err);
        if (err.code === 11000) {
            // Duplicate key error
            return res.status(409).json({ error: 'Email already subscribed' });
        }
        return res.status(500).json({ error: 'An error occurred while subscribing' });
    }
});

// Function to send a confirmation email
async function sendConfirmationEmail(email) {
    // Configure the email transporter
    const transporter = nodemailer.createTransport({
        service: 'gmail', // Example: using Gmail
        auth: {
            user: process.env.EMAIL_USER, // Your email
            pass: process.env.EMAIL_PASS  // Your email password or app password
        }
    });

    // Email options
    const mailOptions = {
        from: process.env.EMAIL_USER,
        to: email,
        subject: 'Subscription Confirmation',
        text: 'Thank you for subscribing! You will now receive updates on new collections and exclusive offers.'
    };

    // Send email
    return transporter.sendMail(mailOptions)
        .then(() => console.log('Email sent to:', email))
        .catch(err => console.error('Email sending error:', err));
}

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Make sure to install required packages using:
  ```bash
  npm install express body-parser mongoose nodemailer
  ```
- Replace `process.env.EMAIL_USER` and `process.env.EMAIL_PASS` with appropriate configurations for your email service.
- Ensure MongoDB is running and accessible at the provided URI.
