"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kriptmart.com
Prompt: Write backend code in Node.js to handle user sign-up and login requests for a system with email, passkey, Google, and Apple authentication options.
Generated: DETERMINISTIC_9265f431c6213d0d
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const AppleStrategy = require('passport-apple');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Simulated database for demonstration purposes
const users = [];

// Environment variables (placeholder values for demonstration purposes)
const JWT_SECRET = 'your_jwt_secret'; // Replace with your actual secret key
const GOOGLE_CLIENT_ID = 'your_google_client_id';
const GOOGLE_CLIENT_SECRET = 'your_google_client_secret';
const APPLE_CLIENT_ID = 'your_apple_client_id';
const APPLE_CLIENT_SECRET = 'your_apple_client_secret';

// Passport configuration for Google authentication
passport.use(
  new GoogleStrategy(
    {
      clientID: GOOGLE_CLIENT_ID,
      clientSecret: GOOGLE_CLIENT_SECRET,
      callbackURL: '/auth/google/callback',
    },
    (accessToken, refreshToken, profile, done) => {
      const user = users.find((user) => user.email === profile.emails[0].value);
      if (user) {
        return done(null, user);
      }

      // Create new user if not already registered
      const newUser = {
        id: profile.id,
        email: profile.emails[0].value,
        name: profile.displayName,
        provider: 'Google',
      };
      users.push(newUser);
      return done(null, newUser);
    }
  )
);

// Passport configuration for Apple authentication
passport.use(
  new AppleStrategy(
    {
      clientID: APPLE_CLIENT_ID,
      teamID: 'your_team_id', // Replace with your team ID
      keyID: 'your_key_id', // Replace with your key ID
      privateKeyString: `
-----BEGIN PRIVATE KEY-----
your_private_key
-----END PRIVATE KEY-----
      `, // Replace with your private key
      callbackURL: '/auth/apple/callback',
    },
    (accessToken, refreshToken, idToken, profile, done) => {
      const user = users.find((user) => user.email === profile.email);
      if (user) {
        return done(null, user);
      }

      // Create new user if not already registered
      const newUser = {
        id: profile.id,
        email: profile.email,
        name: profile.name,
        provider: 'Apple',
      };
      users.push(newUser);
      return done(null, newUser);
    }
  )
);

// Middleware for handling user sign-up
app.post('/signup', async (req, res) => {
  try {
    const { email, passkey } = req.body;

    // Validate input
    if (!email || !passkey) {
      return res.status(400).json({ message: 'Email and passkey are required' });
    }

    // Check if the user already exists
    const existingUser = users.find((user) => user.email === email);
    if (existingUser) {
      return res.status(400).json({ message: 'User already exists' });
    }

    // Hash the passkey for secure storage
    const hashedPasskey = await bcrypt.hash(passkey, 10);

    // Create a new user
    const newUser = { email, passkey: hashedPasskey, provider: 'Local' };
    users.push(newUser);

    res.status(201).json({ message: 'User created successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Middleware for handling user login
app.post('/login', async (req, res) => {
  try {
    const { email, passkey } = req.body;

    // Validate input
    if (!email || !passkey) {
      return res.status(400).json({ message: 'Email and passkey are required' });
    }

    // Find the user by email
    const user = users.find((u) => u.email === email);
    if (!user) {
      return res.status(400).json({ message: 'Invalid email or passkey' });
    }

    // Compare the provided passkey with the stored hashed passkey
    const isMatch = await bcrypt.compare(passkey, user.passkey);
    if (!isMatch) {
      return res.status(400).json({ message: 'Invalid email or passkey' });
    }

    // Generate JWT token
    const token = jwt.sign({ email: user.email }, JWT_SECRET, { expiresIn: '1h' });

    res.status(200).json({ token });
  } catch (error) {
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Routes for Google authentication
app.get('/auth/google', passport.authenticate('google', { scope: ['profile', 'email'] }));
app.get(
  '/auth/google/callback',
  passport.authenticate('google', { session: false }),
  (req, res) => {
    // Generate JWT token for the authenticated user
    const token = jwt.sign({ email: req.user.email }, JWT_SECRET, { expiresIn: '1h' });
    res.status(200).json({ token });
  }
);

// Routes for Apple authentication
app.get('/auth/apple', passport.authenticate('apple'));
app.post(
  '/auth/apple/callback',
  passport.authenticate('apple', { session: false }),
  (req, res) => {
    // Generate JWT token for the authenticated user
    const token = jwt.sign({ email: req.user.email }, JWT_SECRET, { expiresIn: '1h' });
    res.status(200).json({ token });
  }
);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
