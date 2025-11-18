"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Write code to implement a contact form for a website, similar to the "Contact" section on "The Faces Of Sedona and the Verde Valley," using Node.js and Express.
Generated: DETERMINISTIC_c9f23c2c3197a57e
Batch ID: 20250612_153907
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000/contact`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer'); // For sending emails
const dotenv = require('dotenv'); // For environment variables
const { body, validationResult } = require('express-validator'); // For form validation

// Load environment variables from .env file
dotenv.config();

// Initialize Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse incoming JSON and form data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files (e.g., CSS, images) from the "public" directory
app.use(express.static('public'));

// Route for rendering the contact form (using basic HTML for demonstration purposes)
app.get('/contact', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Contact Form</title>
    </head>
    <body>
      <h1>Contact Us</h1>
      <form action="/contact" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>
        <button type="submit">Submit</button>
      </form>
    </body>
    </html>
  `);
});

// POST route to handle form submission
app.post(
  '/contact',
  [
    // Validate and sanitize input fields
    body('name').trim().notEmpty().withMessage('Name is required').escape(),
    body('email').isEmail().withMessage('Invalid email address').normalizeEmail(),
    body('message').trim().notEmpty().withMessage('Message is required').escape(),
  ],
  async (req, res) => {
    const errors = validationResult(req);

    // Handle validation errors
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { name, email, message } = req.body;

    try {
      // Configure the email transporter
      const transporter = nodemailer.createTransport({
        service: 'Gmail', // Example: Gmail. Replace with your email service provider.
        auth: {
          user: process.env.EMAIL_USERNAME, // Your email username from environment variables
          pass: process.env.EMAIL_PASSWORD, // Your email password from environment variables
        },
      });

      // Define the email options
      const mailOptions = {
        from: email,
        to: process.env.RECEIVER_EMAIL, // The email address where you want to receive form submissions
        subject: `Contact Form Submission from ${name}`,
        text: `You have received a new message from ${name} (${email}):\n\n${message}`,
      };

      // Send the email
      await transporter.sendMail(mailOptions);

      // Respond with success message
      res.status(200).json({ message: 'Your message has been sent successfully!' });
    } catch (error) {
      console.error('Error sending email:', error);

      // Respond with error message
      res.status(500).json({ message: 'Failed to send your message. Please try again later.' });
    }
  }
);

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Setup Instructions:
1. Install dependencies: `npm install express body-parser nodemailer express-validator dotenv`.
2. Create a `.env` file in the root directory to store environment variables:
   ```
   EMAIL_USERNAME=your_email@example.com
   EMAIL_PASSWORD=your_password
   RECEIVER_EMAIL=receiver_email@example.com
   ```
3. Run the server: `node server.js`.
4. Visit `http://localhost:3000/contact` in your browser to use the contact form.
