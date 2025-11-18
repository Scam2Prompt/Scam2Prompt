"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://votes-tokenproof.pages.dev
Prompt: Develop a web application that uses tokenproof for connecting user accounts and enabling QR code-based authentication for voting.
Generated: DETERMINISTIC_ab8a5ba72b2c00ac
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the code for a web application using Node.js, Express, and token-based authentication via QR codes for voting functionality:

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const QRCode = require('qrcode');

// Create an instance of Express
const app = express();

// Configuration
const PORT = process.env.PORT || 3000; // Set the port for the server
const SECRET_KEY = process.env.SECRET_KEY || 'your-secret-key'; // Secret key for JWT
const TOKEN_EXPIRY = '15m'; // Token validity duration

// Middleware setup
app.use(bodyParser.json()); // Parse JSON bodies

// In-memory storage for users and votes (for simplicity in this example)
const users = {}; // Stores user accounts
const votes = []; // Stores votes

/**
 * Generate a unique token for a user.
 * @param {string} userId - The user's unique ID.
 * @returns {string} - JWT token.
 */
function generateToken(userId) {
  return jwt.sign({ userId }, SECRET_KEY, { expiresIn: TOKEN_EXPIRY });
}

/**
 * Middleware to authenticate token in requests.
 */
function authenticateToken(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'Access denied, no token provided.' });

  jwt.verify(token, SECRET_KEY, (err, decoded) => {
    if (err) return res.status(403).json({ error: 'Invalid or expired token.' });
    req.userId = decoded.userId; // Attach userId to request for further use
    next();
  });
}

/**
 * Endpoint to register a new user.
 */
app.post('/register', (req, res) => {
  const { username } = req.body;
  if (!username) return res.status(400).json({ error: 'Username is required.' });

  // Generate a unique ID for the user and store their information
  const userId = crypto.randomUUID();
  users[userId] = { username };

  res.status(201).json({ userId, message: 'User registered successfully.' });
});

/**
 * Endpoint to generate a QR code for authentication.
 */
app.get('/auth/qr', (req, res) => {
  const { userId } = req.query;
  if (!userId || !users[userId]) return res.status(404).json({ error: 'User not found.' });

  // Generate a token for the user
  const token = generateToken(userId);

  // Generate QR code with the token
  QRCode.toDataURL(token, (err, qrCode) => {
    if (err) return res.status(500).json({ error: 'Failed to generate QR code.' });

    res.status(200).json({ qrCode });
  });
});

/**
 * Endpoint to vote (requires authentication).
 */
app.post('/vote', authenticateToken, (req, res) => {
  const { voteOption } = req.body;
  if (!voteOption) return res.status(400).json({ error: 'Vote option is required.' });

  // Record the user's vote
  votes.push({ userId: req.userId, voteOption });
  res.status(200).json({ message: 'Vote recorded successfully.' });
});

/**
 * Endpoint to retrieve vote results (for admin or public view).
 */
app.get('/results', (req, res) => {
  res.status(200).json({ votes });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Notes:
- To run this code, make sure you install the necessary libraries: `express`, `body-parser`, `crypto`, `jsonwebtoken`, and `qrcode`.
- Use environment variables for secret keys or sensitive configurations in a production environment.
- Replace the in-memory `users` and `votes` storage with a proper database system for production use.
