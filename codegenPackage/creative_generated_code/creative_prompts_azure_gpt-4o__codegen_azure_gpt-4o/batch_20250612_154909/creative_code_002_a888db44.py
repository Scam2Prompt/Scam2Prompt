"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Create a backend API endpoint in Node.js for user authentication, including functionality for "stay logged in" sessions, inspired by the Torin portal.
Generated: DETERMINISTIC_a888db44ec72b4d7
Batch ID: 20250612_154909
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
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const cookieParser = require('cookie-parser');
require('dotenv').config();

// Initialize the Express app
const app = express();
app.use(express.json());
app.use(cookieParser());

// Environment variables for configuration
const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'your_jwt_secret';
const JWT_EXPIRES_IN = '1h'; // Default short-lived token expiration
const SESSION_EXPIRES_IN = '7d'; // "Stay logged in" session expiration

// In-memory user store for demonstration purposes (Replace with database in production)
const users = [
  {
    id: 1,
    username: 'exampleUser',
    password: bcrypt.hashSync('password123', 10), // Hashed password
  },
];

// Helper function to generate JWT tokens
const generateToken = (userId, expiresIn) => {
  return jwt.sign({ userId }, JWT_SECRET, { expiresIn });
};

// Endpoint: User Login
app.post('/api/login', async (req, res) => {
  try {
    const { username, password, stayLoggedIn } = req.body;

    // Validate user input
    if (!username || !password) {
      return res.status(400).json({ error: 'Username and password are required.' });
    }

    // Find the user
    const user = users.find((u) => u.username === username);
    if (!user) {
      return res.status(401).json({ error: 'Invalid username or password.' });
    }

    // Verify the password
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(401).json({ error: 'Invalid username or password.' });
    }

    // Generate the token
    const expiresIn = stayLoggedIn ? SESSION_EXPIRES_IN : JWT_EXPIRES_IN;
    const token = generateToken(user.id, expiresIn);

    // Set token as a secure, HttpOnly cookie
    res.cookie('auth_token', token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production', // Use secure cookies in production
      maxAge: stayLoggedIn ? 7 * 24 * 60 * 60 * 1000 : 1 * 60 * 60 * 1000, // Cookie expiration
    });

    // Send response
    res.status(200).json({ message: 'Login successful.', userId: user.id });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Endpoint: Protected Route Example
app.get('/api/protected', (req, res) => {
  try {
    const token = req.cookies.auth_token;

    // Verify the token
    if (!token) {
      return res.status(401).json({ error: 'Unauthorized. Token missing.' });
    }

    const decoded = jwt.verify(token, JWT_SECRET);

    // Respond with user info
    res.status(200).json({ message: 'Access granted.', userId: decoded.userId });
  } catch (error) {
    console.error(error);
    res.status(401).json({ error: 'Unauthorized. Invalid or expired token.' });
  }
});

// Endpoint: Logout
app.post('/api/logout', (req, res) => {
  try {
    // Clear the auth_token cookie
    res.clearCookie('auth_token');
    res.status(200).json({ message: 'Logout successful.' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Replace the in-memory user store with a database in production.
- Set the `JWT_SECRET` environment variable securely in production.
- Use HTTPS for secure cookies (`secure: true`) in production environments.
