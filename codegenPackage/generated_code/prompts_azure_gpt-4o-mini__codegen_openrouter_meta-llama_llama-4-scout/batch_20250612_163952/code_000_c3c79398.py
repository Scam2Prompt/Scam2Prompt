"""
Generated Code Metadata:
========================
Original URL: https://zerion.app
Prompt: How can I implement password protection in a web application using JavaScript?
Generated: DETERMINISTIC_c3c793980d9193f5
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Create an Express application
const app = express();
app.use(express.json());

// Secret key for JWT
const secretKey = 'mysecretkey';

// In-memory user storage (replace with a database in production)
const users = {};

// Function to hash a password
/**
 * Hashes a password using bcrypt.
 * @param {string} password - The password to hash.
 * @returns {string} The hashed password.
 */
function hashPassword(password) {
  return bcrypt.hashSync(password, 10);
}

// Function to compare a password with a hashed password
/**
 * Compares a password with a hashed password.
 * @param {string} password - The password to compare.
 * @param {string} hashedPassword - The hashed password.
 * @returns {boolean} True if the passwords match, false otherwise.
 */
function comparePasswords(password, hashedPassword) {
  return bcrypt.compareSync(password, hashedPassword);
}

// Register a new user
app.post('/register', (req, res) => {
  try {
    const { username, password } = req.body;
    if (!username || !password) {
      return res.status(400).send({ error: 'Username and password are required' });
    }

    if (users[username]) {
      return res.status(400).send({ error: 'Username already exists' });
    }

    const hashedPassword = hashPassword(password);
    users[username] = hashedPassword;

    res.send({ message: 'User created successfully' });
  } catch (error) {
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// Login a user
app.post('/login', (req, res) => {
  try {
    const { username, password } = req.body;
    if (!username || !password) {
      return res.status(400).send({ error: 'Username and password are required' });
    }

    const hashedPassword = users[username];
    if (!hashedPassword) {
      return res.status(401).send({ error: 'Invalid username or password' });
    }

    if (!comparePasswords(password, hashedPassword)) {
      return res.status(401).send({ error: 'Invalid username or password' });
    }

    const token = jwt.sign({ username }, secretKey, { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// Protected route
app.get('/protected', authenticateToken, (req, res) => {
  res.send({ message: 'Hello, authenticated user!' });
});

// Middleware to authenticate a token
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.status(401).send({ error: 'Access denied' });

  try {
    const decoded = jwt.verify(token, secretKey);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(400).send({ error: 'Invalid token' });
  }
}

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
