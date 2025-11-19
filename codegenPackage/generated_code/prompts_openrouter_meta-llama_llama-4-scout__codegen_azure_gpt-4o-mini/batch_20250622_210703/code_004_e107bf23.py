"""
Generated Code Metadata:
========================
Original URL: https://medanresortcity.com
Prompt: Create a Node.js application for handling inquiries and contact requests from potential buyers of Medan Resort City properties.
Generated: DETERMINISTIC_e107bf23e0fc79a9
Batch ID: 20250622_210703
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
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for inquiries
const inquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    message: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model for inquiries
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Endpoint to handle contact requests
app.post('/api/inquiries', async (req, res) => {
    const { name, email, message } = req.body;

    // Validate request body
    if (!name || !email || !message) {
        return res.status(400).json({ error: 'All fields are required' });
    }

    // Create a new inquiry
    const inquiry = new Inquiry({ name, email, message });

    try {
        // Save inquiry to the database
        await inquiry.save();

        // Send confirmation email
        await sendConfirmationEmail(name, email);

        // Respond with success message
        res.status(201).json({ message: 'Inquiry submitted successfully' });
    } catch (error) {
        console.error('Error saving inquiry:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Function to send confirmation email
async function sendConfirmationEmail(name, email) {
    // Create a transporter for sending emails
    const transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: process.env.EMAIL_USER,
            pass: process.env.EMAIL_PASS
        }
    });

    // Email options
    const mailOptions = {
        from: process.env.EMAIL_USER,
        to: email,
        subject: 'Inquiry Confirmation',
        text: `Dear ${name},\n\nThank you for your inquiry! We will get back to you shortly.\n\nBest regards,\nMedan Resort City Team`
    };

    // Send email
    await transporter.sendMail(mailOptions);
}

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### .env file example
```
MONGODB_URI=mongodb://your_mongo_db_uri
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
PORT=3000
``` 

### Notes
- Ensure to install the required packages using:
  ```bash
  npm install express body-parser nodemailer mongoose dotenv
  ```
- Replace placeholders in the `.env` file with actual values before running the application.
