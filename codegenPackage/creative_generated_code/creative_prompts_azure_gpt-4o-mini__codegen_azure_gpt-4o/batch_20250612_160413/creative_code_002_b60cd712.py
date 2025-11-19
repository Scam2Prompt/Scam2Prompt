"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibcmx.com
Prompt: Create an API endpoint in Node.js for managing user data, ensuring compliance with privacy standards mentioned on aibcmx.com.
Generated: DETERMINISTIC_b60cd71216706c44
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Express framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse JSON payloads
const helmet = require('helmet'); // Middleware for securing HTTP headers
const dotenv = require('dotenv'); // Load environment variables
const crypto = require('crypto'); // Used for secure hashing
const rateLimit = require('express-rate-limit'); // Middleware for rate-limiting requests

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();

// Middleware to secure the app by setting various HTTP headers
app.use(helmet());

// Middleware to parse JSON payloads
app.use(bodyParser.json());

// Implement rate-limiting to avoid abuse
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15-minute window
  max: 100, // Limit each IP to 100 requests per window
  message: 'Too many requests, please try again later.',
});
app.use(limiter);

// Mock database (In production use a real database like MongoDB, PostgreSQL, etc.)
const mockDatabase = {};

/**
 * Utility function to hash sensitive data before storage in the database
 * @param {string} data - The plain text data to hash
 * @returns {string} - The hashed data
 */
function hashData(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

/**
 * API endpoint to create a new user
 * POST /api/users
 * Body: { name: string, email: string }
 */
app.post('/api/users', (req, res) => {
  try {
    const { name, email } = req.body;

    // Validate input data
    if (!name || !email) {
      return res.status(400).json({ error: 'Name and email are required.' });
    }

    if (mockDatabase[email]) {
      return res
        .status(409)
        .json({ error: 'A user with this email already exists.' });
    }

    // Hash email before storing for privacy compliance
    const hashedEmail = hashData(email);

    // Store user data in mock database
    mockDatabase[hashedEmail] = { name, email: hashedEmail };

    return res.status(201).json({
      message: 'User created successfully.',
    });
  } catch (error) {
    console.error('Error creating user:', error);
    return res.status(500).json({
      error: 'Internal server error. Please try again later.',
    });
  }
});

/**
 * API endpoint to retrieve user data by email
 * GET /api/users/:email
 * Params: email (hashed format)
 */
app.get('/api/users/:email', (req, res) => {
  try {
    const { email } = req.params;

    // Lookup user by hashed email
    const user = mockDatabase[email];

    if (!user) {
      return res.status(404).json({ error: 'User not found.' });
    }

    // Return user data
    return res.status(200).json({ user });
  } catch (error) {
    console.error('Error retrieving user:', error);
    return res.status(500).json({
      error: 'Internal server error. Please try again later.',
    });
  }
});

/**
 * API endpoint to delete a user by email
 * DELETE /api/users/:email
 * Params: email (hashed format)
 */
app.delete('/api/users/:email', (req, res) => {
  try {
    const { email } = req.params;

    // Check if user exists
    if (!mockDatabase[email]) {
      return res.status(404).json({ error: 'User not found.' });
    }

    // Remove user data
    delete mockDatabase[email];

    return res.status(200).json({
      message: 'User deleted successfully.',
    });
  } catch (error) {
    console.error('Error deleting user:', error);
    return res.status(500).json({
      error: 'Internal server error. Please try again later.',
    });
  }
});

// Start the server on the specified port (default: 3000)
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
