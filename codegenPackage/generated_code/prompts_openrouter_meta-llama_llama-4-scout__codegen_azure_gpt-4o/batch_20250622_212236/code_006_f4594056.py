"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Develop a Node.js server-side application to handle contact form submissions from the Sakura Dance Studio website, including email notifications and data storage.
Generated: DETERMINISTIC_f4594056a0b9ec2f
Batch ID: 20250622_212236
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
require('dotenv').config(); // For environment variables

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON and form data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// MongoDB connection setup
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('MongoDB connection error:', err);
    process.exit(1); // Exit process if DB connection fails
  });

// Define Mongoose schema and model for contact form submissions
const contactSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  message: { type: String, required: true },
  submittedAt: { type: Date, default: Date.now },
});

const Contact = mongoose.model('Contact', contactSchema);

// Configure Nodemailer transporter
const transporter = nodemailer.createTransport({
  service: 'gmail', // Use your email service provider
  auth: {
    user: process.env.EMAIL_USER, // Your email address
    pass: process.env.EMAIL_PASS, // Your email password or app-specific password
  },
});

// Route to handle contact form submissions
app.post('/submit', async (req, res) => {
  const { name, email, message } = req.body;

  // Validate input
  if (!name || !email || !message) {
    return res.status(400).json({ error: 'All fields are required.' });
  }

  try {
    // Save submission to the database
    const newContact = new Contact({ name, email, message });
    await newContact.save();

    // Send email notification
    const mailOptions = {
      from: process.env.EMAIL_USER,
      to: process.env.NOTIFY_EMAIL, // Admin email to receive notifications
      subject: 'New Contact Form Submission',
      text: `You have a new contact form submission:\n\nName: ${name}\nEmail: ${email}\nMessage: ${message}`,
    };

    await transporter.sendMail(mailOptions);

    // Respond to the client
    res.status(200).json({ message: 'Your message has been sent successfully!' });
  } catch (error) {
    console.error('Error handling contact form submission:', error);
    res.status(500).json({ error: 'An error occurred. Please try again later.' });
  }
});

// Default route for health check
app.get('/', (req, res) => {
  res.status(200).send('Sakura Dance Studio Contact Form API is running.');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Ensure you create a `.env` file with the following variables:
  ```
  PORT=3000
  MONGO_URI=your_mongodb_connection_string
  EMAIL_USER=your_email_address
  EMAIL_PASS=your_email_password
  NOTIFY_EMAIL=admin_email_to_receive_notifications
  ```
- Install required dependencies using:
  ```
  npm install express body-parser nodemailer mongoose dotenv
  ```
