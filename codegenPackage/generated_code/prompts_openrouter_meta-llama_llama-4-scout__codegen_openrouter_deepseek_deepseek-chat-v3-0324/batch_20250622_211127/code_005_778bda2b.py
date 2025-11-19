"""
Generated Code Metadata:
========================
Original URL: https://metmaskwlletlgiin.godaddysites.com
Prompt: Create a simple Node.js server to handle MetaMask wallet login requests, similar to what might be expected from the functionality hinted at on metmask wllet lgiin.
Generated: DETERMINISTIC_778bda2b448685b7
Batch ID: 20250622_211127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const cors = require('cors');
const { ethers } = require('ethers');
const jwt = require('jsonwebtoken');

const app = express();
const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key-here';

// Middleware
app.use(cors());
app.use(express.json());

/**
 * Verifies a signed message from MetaMask and returns a JWT token if valid
 * @param {string} address - Ethereum address
 * @param {string} signature - Signed message
 * @param {string} originalMessage - Original message that was signed
 * @returns {boolean} - Returns true if signature is valid
 */
const verifySignature = (address, signature, originalMessage) => {
  try {
    const recoveredAddress = ethers.utils.verifyMessage(originalMessage, signature);
    return recoveredAddress.toLowerCase() === address.toLowerCase();
  } catch (error) {
    return false;
  }
};

/**
 * Generates a JWT token for authenticated users
 * @param {string} address - Ethereum address
 * @returns {string} - JWT token
 */
const generateToken = (address) => {
  return jwt.sign({ address }, JWT_SECRET, { expiresIn: '1h' });
};

// Login endpoint
app.post('/api/login', async (req, res) => {
  try {
    const { address, signature, message } = req.body;

    if (!address || !signature || !message) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    if (!verifySignature(address, signature, message)) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    const token = generateToken(address);
    return res.status(200).json({ token });
  } catch (error) {
    console.error('Login error:', error);
    return res.status(500).json({ error: 'Internal server error' });
  }
});

// Protected route example
app.get('/api/protected', (req, res) => {
  try {
    const authHeader = req.headers['authorization'];
    if (!authHeader) {
      return res.status(401).json({ error: 'Authorization header missing' });
    }

    const token = authHeader.split(' ')[1];
    if (!token) {
      return res.status(401).json({ error: 'Token missing' });
    }

    jwt.verify(token, JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.status(401).json({ error: 'Invalid token' });
      }
      return res.status(200).json({ message: `Welcome ${decoded.address}` });
    });
  } catch (error) {
    console.error('Protected route error:', error);
    return res.status(500).json({ error: 'Internal server error' });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
```
