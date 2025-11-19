"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Develop a Node.js API to handle ticket booking requests, including endpoints for submitting the form and retrieving booking confirmations via email or SMS.
Generated: DETERMINISTIC_a86373ebd443f1e4
Batch ID: 20250622_212001
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
const twilio = require('twilio');
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Database mock (in production, use a real database like MongoDB or PostgreSQL)
let bookings = [];

// Twilio client setup
const twilioClient = twilio(
  process.env.TWILIO_ACCOUNT_SID,
  process.env.TWILIO_AUTH_TOKEN
);

// Nodemailer transporter setup
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS
  }
});

/**
 * POST /api/bookings - Create a new booking
 * Request body: { name, email, phone, eventId, tickets }
 */
app.post('/api/bookings', async (req, res) => {
  try {
    const { name, email, phone, eventId, tickets } = req.body;

    // Validate request
    if (!name || !email || !phone || !eventId || !tickets) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Create booking object
    const booking = {
      id: uuidv4(),
      name,
      email,
      phone,
      eventId,
      tickets,
      status: 'confirmed',
      createdAt: new Date().toISOString()
    };

    // Store booking
    bookings.push(booking);

    // Send confirmation email
    await sendConfirmationEmail(booking);

    // Send confirmation SMS
    await sendConfirmationSMS(booking);

    res.status(201).json(booking);
  } catch (error) {
    console.error('Booking error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * GET /api/bookings/:id - Get booking by ID
 */
app.get('/api/bookings/:id', (req, res) => {
  try {
    const booking = bookings.find(b => b.id === req.params.id);
    
    if (!booking) {
      return res.status(404).json({ error: 'Booking not found' });
    }

    res.json(booking);
  } catch (error) {
    console.error('Get booking error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * Send confirmation email
 * @param {Object} booking - Booking object
 */
async function sendConfirmationEmail(booking) {
  try {
    const mailOptions = {
      from: process.env.EMAIL_USER,
      to: booking.email,
      subject: 'Your Booking Confirmation',
      html: `
        <h1>Booking Confirmation</h1>
        <p>Thank you, ${booking.name}, for your booking!</p>
        <p>Booking ID: ${booking.id}</p>
        <p>Event ID: ${booking.eventId}</p>
        <p>Tickets: ${booking.tickets}</p>
      `
    };

    await transporter.sendMail(mailOptions);
  } catch (error) {
    console.error('Email sending error:', error);
    throw error;
  }
}

/**
 * Send confirmation SMS
 * @param {Object} booking - Booking object
 */
async function sendConfirmationSMS(booking) {
  try {
    await twilioClient.messages.create({
      body: `Your booking ${booking.id} for event ${booking.eventId} is confirmed. Tickets: ${booking.tickets}`,
      from: process.env.TWILIO_PHONE_NUMBER,
      to: booking.phone
    });
  } catch (error) {
    console.error('SMS sending error:', error);
    throw error;
  }
}

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

// Export app for testing
module.exports = app;
```

Note: You'll need to create a `.env` file with the following variables:
```
PORT=3000
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
```

Also, make sure to install the required dependencies:
```
npm install express body-parser nodemailer twilio uuid cors dotenv
```
