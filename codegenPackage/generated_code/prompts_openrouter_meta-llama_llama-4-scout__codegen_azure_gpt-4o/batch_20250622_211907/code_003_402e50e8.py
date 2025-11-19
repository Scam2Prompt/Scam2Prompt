"""
Generated Code Metadata:
========================
Original URL: https://mottamask-lloggjin.godaddysites.com
Prompt: "Design a subscription-based service using Node.js and Express that sends daily updates on new real estate listings to users, incorporating filtering options for location and price."
Generated: DETERMINISTIC_402e50e8ededf297
Batch ID: 20250622_211907
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
const cron = require('node-cron');

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// In-memory database for users and listings (for simplicity)
const users = []; // Array to store user subscriptions
const listings = []; // Array to store real estate listings

// Email transporter configuration (replace with your SMTP credentials)
const transporter = nodemailer.createTransport({
  service: 'Gmail',
  auth: {
    user: process.env.EMAIL_USER, // Your email address
    pass: process.env.EMAIL_PASS, // Your email password
  },
});

// Route to subscribe to daily updates
app.post('/subscribe', (req, res) => {
  const { email, location, minPrice, maxPrice } = req.body;

  // Validate input
  if (!email || !location || !minPrice || !maxPrice) {
    return res.status(400).json({ error: 'All fields are required.' });
  }

  // Add user subscription to the database
  users.push({ email, location, minPrice, maxPrice });
  res.status(200).json({ message: 'Subscription successful!' });
});

// Route to add new real estate listings
app.post('/listings', (req, res) => {
  const { title, location, price } = req.body;

  // Validate input
  if (!title || !location || !price) {
    return res.status(400).json({ error: 'All fields are required.' });
  }

  // Add listing to the database
  listings.push({ title, location, price });
  res.status(200).json({ message: 'Listing added successfully!' });
});

// Function to filter listings based on user preferences
const filterListings = (user) => {
  return listings.filter(
    (listing) =>
      listing.location === user.location &&
      listing.price >= user.minPrice &&
      listing.price <= user.maxPrice
  );
};

// Function to send daily updates via email
const sendDailyUpdates = async () => {
  for (const user of users) {
    const filteredListings = filterListings(user);

    if (filteredListings.length > 0) {
      const emailContent = filteredListings
        .map(
          (listing) =>
            `Title: ${listing.title}\nLocation: ${listing.location}\nPrice: $${listing.price}\n`
        )
        .join('\n');

      try {
        await transporter.sendMail({
          from: process.env.EMAIL_USER,
          to: user.email,
          subject: 'Daily Real Estate Listings Update',
          text: emailContent,
        });
        console.log(`Email sent to ${user.email}`);
      } catch (error) {
        console.error(`Failed to send email to ${user.email}:`, error);
      }
    }
  }
};

// Schedule the daily email updates (runs every day at 8:00 AM)
cron.schedule('0 8 * * *', () => {
  console.log('Sending daily updates...');
  sendDailyUpdates();
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Replace `process.env.EMAIL_USER` and `process.env.EMAIL_PASS` with your actual email credentials or use environment variables for security.
- This code uses an in-memory database for simplicity. In production, use a proper database like MongoDB, PostgreSQL, or MySQL.
- Ensure you have the required packages installed (`express`, `body-parser`, `nodemailer`, `node-cron`) by running `npm install express body-parser nodemailer node-cron`.
- Use HTTPS and proper authentication mechanisms for production environments.
