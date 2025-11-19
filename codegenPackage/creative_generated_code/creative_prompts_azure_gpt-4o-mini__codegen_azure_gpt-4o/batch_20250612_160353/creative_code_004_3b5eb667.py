"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgn-faucet.vercel.app
Prompt: How do I modify the existing code of the Gitcoin Passport Gated Faucet to add new features?
Generated: DETERMINISTIC_3b5eb6678719ec9a
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the updated code for adding new features to the Gitcoin Passport Gated Faucet. This example assumes you are working with a Node.js-based application using the Express.js framework and a MongoDB database. The new feature adds a "rate-limiting" mechanism to prevent abuse of the faucet.

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const rateLimit = require('express-rate-limit');

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database configuration
const DB_URI = process.env.DB_URI || 'mongodb://localhost/gitcoin-faucet';
mongoose.connect(DB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for user requests to the faucet
const userSchema = new mongoose.Schema({
  address: { type: String, required: true, unique: true },
  lastRequestTime: { type: Date, required: true },
  passportScore: { type: Number, required: true },
});

const User = mongoose.model('User', userSchema);

// Define a rate-limiting middleware for the faucet (e.g., limit to 1 request per 1 hour)
const faucetLimiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 1, // Limit each IP to 1 request per windowMs
  message: 'Rate limit exceeded. Please try again later.',
});

// Endpoint to request tokens from the faucet
app.post('/request-tokens', faucetLimiter, async (req, res) => {
  try {
    const { address, passportScore } = req.body;

    // Validate input
    if (!address || !passportScore) {
      return res.status(400).json({ error: 'Address and passport score are required.' });
    }

    // Check if the address already exists in the database
    const user = await User.findOne({ address });
    const currentTime = new Date();

    if (user) {
      const timeDiff = (currentTime - user.lastRequestTime) / 1000 / 60; // Time difference in minutes

      // Ensure the user waits for the rate-limiting period to request again
      if (timeDiff < 60) {
        return res.status(429).json({ error: 'Too many requests. Please wait before requesting again.' });
      }

      // Update lastRequestTime for the user
      user.lastRequestTime = currentTime;
      await user.save();
    } else {
      // Save new user data into the database
      const newUser = new User({
        address,
        passportScore,
        lastRequestTime: currentTime,
      });
      await newUser.save();
    }

    // Logic to check passport score and dispense tokens
    if (passportScore >= 50) {
      return res.status(200).json({ message: 'Tokens successfully dispensed.' });
    } else {
      return res.status(403).json({ error: 'Insufficient passport score.' });
    }
  } catch (error) {
    console.error('Error during token request:', error);
    return res.status(500).json({ error: 'An internal server error occurred.' });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).send('Gitcoin Faucet is running!');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Key Features Added:
1. **Rate Limiting:** To restrict abuse, rate-limiting is introduced using the `express-rate-limit` package.
2. **Passport Score Validation:** Enhanced logic to validate the user's passport score before dispensing tokens.
3. **Database Integration:** Ensures that user requests are logged and managed efficiently using MongoDB.

Ensure you install the required dependencies before running the code:
```bash
npm install express body-parser mongoose express-rate-limit
```

Write environment variables (`PORT`, `DB_URI`) in a `.env` file or your preferred configuration method.
