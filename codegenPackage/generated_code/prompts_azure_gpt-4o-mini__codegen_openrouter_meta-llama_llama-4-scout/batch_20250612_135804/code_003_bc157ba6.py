"""
Generated Code Metadata:
========================
Original URL: https://nasti.ck.page
Prompt: Describe how to create a simple web application that allows users to sign up for an NFT newsletter, inspired by the Nasti page.
Generated: DETERMINISTIC_bc157ba6c2262165
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**NFT Newsletter Signup Web Application**
======================================

**dependencies:**

* `express`: ^4.17.1
* `mongodb`: ^3.6.4
* `nodemailer`: ^6.4.11

**app.js**
```javascript
// Import dependencies
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const nodemailer = require('nodemailer');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/nft-newsletter', { useNewUrlParser: true, useUnifiedTopology: true });

// Define NFTNewsletter model
const nftNewsletterSchema = new mongoose.Schema({
  email: { type: String, unique: true, required: true }
});
const NFTNewsletter = mongoose.model('NFTNewsletter', nftNewsletterSchema);

// Set up Express middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Set up Nodemailer transporter
const transporter = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 587,
  secure: false, // or 'STARTTLS'
  auth: {
    user: 'your-email@gmail.com',
    pass: 'your-password'
  }
});

// Signup endpoint
app.post('/signup', async (req, res) => {
  try {
    const { email } = req.body;
    if (!email) {
      return res.status(400).send({ error: 'Email is required' });
    }

    // Check if email already exists
    const existingSubscriber = await NFTNewsletter.findOne({ email });
    if (existingSubscriber) {
      return res.status(400).send({ error: 'Email already subscribed' });
    }

    // Create new subscriber
    const subscriber = new NFTNewsletter({ email });
    await subscriber.save();

    // Send confirmation email
    const mailOptions = {
      from: 'your-email@gmail.com',
      to: email,
      subject: 'NFT Newsletter Confirmation',
      text: 'Thank you for subscribing to our NFT newsletter!'
    };
    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.error(error);
      } else {
        console.log(`Email sent: ${info.response}`);
      }
    });

    res.send({ message: 'Subscribed successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**package.json**
```json
{
  "name": "nft-newsletter",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4",
    "nodemailer": "^6.4.11"
  }
}
```

**index.html** (example usage)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NFT Newsletter Signup</title>
</head>
<body>
  <h1>NFT Newsletter Signup</h1>
  <form id="signup-form">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <button type="submit">Signup</button>
  </form>

  <script>
    const form = document.getElementById('signup-form');
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const email = document.getElementById('email').value;
      const response = await fetch('/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
      });
      const data = await response.json();
      console.log(data);
    });
  </script>
</body>
</html>
```
