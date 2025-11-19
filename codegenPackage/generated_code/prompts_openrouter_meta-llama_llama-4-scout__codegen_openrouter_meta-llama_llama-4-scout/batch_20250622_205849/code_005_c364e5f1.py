"""
Generated Code Metadata:
========================
Original URL: https://www.revoke.expert
Prompt: Generate a code snippet in Node.js for revoking a JSON Web Token (JWT) by blacklisting it.
Generated: DETERMINISTIC_c364e5f16fd5d90e
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// jwt-blacklist.js

/**
 * Module dependencies.
 */
const express = require('express');
const jwt = require('jsonwebtoken');
const redis = require('redis');

// Create a Redis client
const client = redis.createClient({
  host: 'localhost',
  port: 6379,
});

/**
 * Blacklist class for managing JWT blacklisting.
 */
class Blacklist {
  /**
   * Initialize the blacklist.
   */
  constructor() {
    this.client = client;
  }

  /**
   * Add a JWT to the blacklist.
   * @param {string} token - The JWT to blacklist.
   * @param {number} expiresIn - The number of seconds until the token expires.
   * @returns {Promise<void>}
   */
  async add(token, expiresIn) {
    try {
      await this.client.set(token, '', 'EX', expiresIn);
    } catch (error) {
      throw new Error(`Failed to add token to blacklist: ${error.message}`);
    }
  }

  /**
   * Check if a JWT is blacklisted.
   * @param {string} token - The JWT to check.
   * @returns {Promise<boolean>}
   */
  async isBlacklisted(token) {
    try {
      const result = await this.client.exists(token);
      return result === 1;
    } catch (error) {
      throw new Error(`Failed to check token blacklist status: ${error.message}`);
    }
  }
}

// Create an Express app
const app = express();

// Create a blacklist instance
const blacklist = new Blacklist();

/**
 * Middleware to check if a JWT is blacklisted.
 * @param {express.Request} req - The Express request.
 * @param {express.Response} res - The Express response.
 * @param {express.NextFunction} next - The Express next function.
 */
const isBlacklistedMiddleware = async (req, res, next) => {
  try {
    const token = req.header('Authorization').replace('Bearer ', '');
    if (await blacklist.isBlacklisted(token)) {
      return res.status(401).json({ error: 'Token blacklisted' });
    }
    next();
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
};

// Example usage
app.use(express.json());

// Generate a JWT
const generateToken = (payload) => {
  return jwt.sign(payload, 'secret', { expiresIn: '1h' });
};

// Revoke a JWT by blacklisting it
app.post('/revoke', async (req, res) => {
  try {
    const token = req.body.token;
    if (!token) {
      return res.status(400).json({ error: 'Token is required' });
    }
    await blacklist.add(token, 3600); // blacklist for 1 hour
    res.json({ message: 'Token revoked' });
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Protected route
app.get('/protected', isBlacklistedMiddleware, (req, res) => {
  res.json({ message: 'Hello, World!' });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
