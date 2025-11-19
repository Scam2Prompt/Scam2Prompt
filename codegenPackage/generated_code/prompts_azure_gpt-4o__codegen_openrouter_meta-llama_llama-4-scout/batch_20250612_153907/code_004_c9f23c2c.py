"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Write code to implement a contact form for a website, similar to the "Contact" section on "The Faces Of Sedona and the Verde Valley," using Node.js and Express.
Generated: DETERMINISTIC_c9f23c2c3197a57e
Batch ID: 20250612_153907
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
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Create an Express application
const app = express();

// Use body-parser middleware to parse JSON and URL-encoded bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Define contact form route
app.post('/contact', async (req, res) => {
  try {
    // Validate form data
    if (!req.body.name || !req.body.email || !req.body.message) {
      return res.status(400).json({ error: 'Please fill out all fields.' });
    }

    // Create a transporter object for sending emails
    const transporter = nodemailer.createTransport({
      host: process.env.EMAIL_HOST,
      port: process.env.EMAIL_PORT,
      secure: process.env.EMAIL_SECURE === 'true',
      auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASSWORD,
      },
    });

    // Define email options
    const mailOptions = {
      from: req.body.email,
      to: process.env.RECEIVER_EMAIL,
      subject: `Contact Form Submission from ${req.body.name}`,
      text: req.body.message,
    };

    // Send the email
    await transporter.sendMail(mailOptions);

    // Return a success response
    res.json({ message: 'Message sent successfully!' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to send message.' });
  }
});

// Define a route for the contact form page
app.get('/contact', (req, res) => {
  res.sendFile(__dirname + '/contact.html');
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```html
<!-- contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Us</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    form {
      max-width: 500px;
      margin: 40px auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    label {
      display: block;
      margin-bottom: 10px;
    }
    input, textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
    }
    button[type="submit"] {
      background-color: #4CAF50;
      color: #fff;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    button[type="submit"]:hover {
      background-color: #3e8e41;
    }
  </style>
</head>
<body>
  <form id="contact-form" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>

    <button type="submit">Send Message</button>
  </form>

  <div id="response"></div>

  <script>
    const form = document.getElementById('contact-form');
    const responseDiv = document.getElementById('response');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(form);

      try {
        const response = await fetch('/contact', {
          method: 'POST',
          body: formData,
        });

        const data = await response.json();

        if (data.message) {
          responseDiv.textContent = data.message;
          form.reset();
        } else {
          responseDiv.textContent = data.error;
        }
      } catch (error) {
        console.error(error);
      }
    });
  </script>
</body>
</html>
```

```bash
# .env file
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_SECURE=false
EMAIL_USER=your-email@example.com
EMAIL_PASSWORD=your-email-password
RECEIVER_EMAIL=receiver-email@example.com
```
