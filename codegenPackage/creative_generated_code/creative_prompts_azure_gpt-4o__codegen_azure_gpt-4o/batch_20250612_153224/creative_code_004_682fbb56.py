"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recuperacionjc.com
Prompt: Write code for a newsletter subscription feature that matches the design and functionality described on the Recuperación JC website.
Generated: DETERMINISTIC_682fbb56f97b6fe7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s the code for a newsletter subscription feature, assuming the backend is implemented in Node.js with Express and the database used is MongoDB. The frontend is kept minimal for demonstration purposes.

### Backend Code (`server.js`)
```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize the Express app
const app = express();

// Setup middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Connect to MongoDB database
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected successfully'))
  .catch(error => {
    console.error('MongoDB connection error:', error);
    process.exit(1);
  });

// Define the schema for newsletter subscriptions
const subscriptionSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    match: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
  },
  subscribedAt: {
    type: Date,
    default: Date.now,
  },
});

// Create the model for newsletter subscriptions
const Subscription = mongoose.model('Subscription', subscriptionSchema);

// API endpoint to handle newsletter subscriptions
app.post('/api/subscribe', async (req, res) => {
  try {
    const { email } = req.body;

    // Validate input
    if (!email) {
      return res.status(400).json({ message: 'Email is required.' });
    }

    // Create a new subscription
    const newSubscription = new Subscription({ email });

    // Save to the database
    await newSubscription.save();

    return res.status(201).json({ message: 'Subscription successful!' });
  } catch (error) {
    if (error.code === 11000) {
      // Duplicate email error
      return res.status(409).json({ message: 'Email is already subscribed.' });
    }
    console.error('Error during subscription:', error);
    return res.status(500).json({ message: 'Internal server error.' });
  }
});

// Serve the frontend
app.get('/', (req, res) => {
  res.send(`
    <html>
      <head>
        <title>Newsletter Subscription</title>
      </head>
      <body>
        <h1>Subscribe to our Newsletter</h1>
        <form action="/api/subscribe" method="POST">
          <input type="email" name="email" placeholder="Enter your email" required />
          <button type="submit">Subscribe</button>
        </form>
      </body>
    </html>
  `);
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
```

### Environment Variables (`.env`)
```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/newsletter
PORT=5000
```

### Frontend Code (HTML snippet served by the backend `GET /`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Newsletter Subscription</title>
</head>
<body>
  <h1>Subscribe to our Newsletter</h1>
  <form action="/api/subscribe" method="POST">
    <input type="email" name="email" placeholder="Enter your email" required />
    <button type="submit">Subscribe</button>
  </form>
</body>
</html>
```

> **Note:** Ensure MongoDB is properly set up and the database URL in `.env` is correctly configured.
