"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Create a JavaScript function that allows users to register and log in to a music streaming service similar to Radio S, focusing on user experience and security.
Generated: DETERMINISTIC_b07eae2d5a3d2a3d
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const { v4: uuidv4 } = require('uuid');

// In-memory database for demonstration (replace with a real DB in production)
const usersDB = {};

// Configuration
const config = {
  saltRounds: 10,
  jwtSecret: 'your-secret-key-here', // In production, use environment variables
  tokenExpiry: '24h'
};

/**
 * Registers a new user
 * @param {string} email - User's email
 * @param {string} password - User's password
 * @param {string} username - User's display name
 * @returns {Promise<Object>} - The created user object without sensitive data
 * @throws {Error} - If registration fails
 */
async function registerUser(email, password, username) {
  try {
    // Validate input
    if (!email || !password || !username) {
      throw new Error('All fields (email, password, username) are required');
    }

    if (usersDB[email]) {
      throw new Error('User already exists');
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(password, config.saltRounds);
    const userId = uuidv4();

    // Store user
    usersDB[email] = {
      id: userId,
      email,
      password: hashedPassword,
      username,
      createdAt: new Date().toISOString(),
      favorites: []
    };

    // Return user without sensitive data
    return {
      id: userId,
      email,
      username,
      createdAt: usersDB[email].createdAt
    };
  } catch (error) {
    console.error('Registration error:', error);
    throw new Error(`Registration failed: ${error.message}`);
  }
}

/**
 * Logs in a user and returns a JWT token
 * @param {string} email - User's email
 * @param {string} password - User's password
 * @returns {Promise<string>} - JWT token
 * @throws {Error} - If login fails
 */
async function loginUser(email, password) {
  try {
    // Validate input
    if (!email || !password) {
      throw new Error('Both email and password are required');
    }

    const user = usersDB[email];
    if (!user) {
      throw new Error('User not found');
    }

    // Verify password
    const passwordMatch = await bcrypt.compare(password, user.password);
    if (!passwordMatch) {
      throw new Error('Invalid credentials');
    }

    // Generate JWT token
    const token = jwt.sign(
      {
        id: user.id,
        email: user.email,
        username: user.username
      },
      config.jwtSecret,
      { expiresIn: config.tokenExpiry }
    );

    return token;
  } catch (error) {
    console.error('Login error:', error);
    throw new Error(`Login failed: ${error.message}`);
  }
}

/**
 * Middleware to authenticate JWT token
 * @param {Object} req - Express request object
 * @param {Object} res - Express response object
 * @param {Function} next - Express next middleware function
 */
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.sendStatus(401);
  }

  jwt.verify(token, config.jwtSecret, (err, user) => {
    if (err) {
      return res.sendStatus(403);
    }
    req.user = user;
    next();
  });
}

module.exports = {
  registerUser,
  loginUser,
  authenticateToken
};
```
