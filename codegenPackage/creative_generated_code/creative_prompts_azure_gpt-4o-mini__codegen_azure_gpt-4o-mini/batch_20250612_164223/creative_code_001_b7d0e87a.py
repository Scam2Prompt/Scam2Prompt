"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braveser.com
Prompt: How can I implement the Brave browser's reward system in a web application to allow users to earn BAT tokens for viewing ads?
Generated: DETERMINISTIC_b7d0e87ab96b95c3
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const jwt = require('jsonwebtoken');

// Constants
const PORT = process.env.PORT || 3000;
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/brave-rewards';
const JWT_SECRET = process.env.JWT_SECRET || 'your_jwt_secret';

// Initialize Express app
const app = express();

// Middleware
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect(MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// User schema and model
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  batTokens: { type: Number, default: 0 },
  adsViewed: { type: Number, default: 0 }
});
const User = mongoose.model('User', userSchema);

// Middleware to authenticate users using JWT
const authenticateJWT = (req, res, next) => {
  const token = req.header('x-auth-token');
  if (!token) return res.sendStatus(403);

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// API to register a new user
app.post('/register', async (req, res) => {
  const { username } = req.body;

  try {
    const newUser = new User({ username });
    await newUser.save();
    
    // Create JWT token
    const token = jwt.sign({ username: newUser.username }, JWT_SECRET);
    res.json({ token, batTokens: newUser.batTokens });
  } catch (error) {
    console.error('Registration error:', error);
    res.status(500).send('Internal Server Error');
  }
});

// API to simulate viewing an ad and earning BAT tokens
app.post('/view-ad', authenticateJWT, async (req, res) => {
  try {
    const user = await User.findOne({ username: req.user.username });
    
    // Update user's BAT tokens and ads viewed
    user.batTokens += 0.5; // Earn 0.5 BAT for viewing an ad
    user.adsViewed += 1;
    await user.save();
    
    res.json({ message: 'Ad viewed successfully', batTokens: user.batTokens });
  } catch (error) {
    console.error('Error viewing ad:', error);
    res.status(500).send('Internal Server Error');
  }
});

// API to check BAT token balance
app.get('/balance', authenticateJWT, async (req, res) => {
  try {
    const user = await User.findOne({ username: req.user.username });
    if (!user) return res.status(404).send('User not found');

    res.json({ batTokens: user.batTokens });
  } catch (error) {
    console.error('Error fetching balance:', error);
    res.status(500).send('Internal Server Error');
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

**Note**: Ensure to set up your environment variables for `MONGODB_URI` and `JWT_SECRET` before running the application. Additionally, this code assumes a basic understanding of how to run a Node.js application.
