"""
Generated Code Metadata:
========================
Original URL: https://paymentsbot.site
Prompt: "How to secure a payment bot admin panel with authentication and authorization using JavaScript libraries?"
Generated: DETERMINISTIC_bf153c82182514a7
Batch ID: 20250622_211032
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
const app = express();
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const helmet = require('helmet');

// Configure express to use JSON body parsing
app.use(express.json());
app.use(helmet());

// Define a secret key for JWT signing
const secretKey = 'your-secret-key';

// Define a User model
class User {
  constructor(id, username, password, role) {
    this.id = id;
    this.username = username;
    this.password = password;
    this.role = role;
  }
}

// In-memory user storage (replace with a database in production)
const users = [
  new User(1, 'admin', bcrypt.hashSync('password', 10), 'admin'),
];

// Authentication middleware
function authenticate(req, res, next) {
  try {
    // Get the Authorization header
    const authHeader = req.header('Authorization');
    if (!authHeader) {
      throw new Error('Unauthorized');
    }

    // Verify the JWT token
    const token = authHeader.split(' ')[1];
    const decoded = jwt.verify(token, secretKey);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).send({ error: 'Unauthorized' });
  }
}

// Authorization middleware
function authorize(roles) {
  return (req, res, next) => {
    try {
      if (!req.user) {
        throw new Error('Unauthorized');
      }

      // Check if the user has the required role
      if (!roles.includes(req.user.role)) {
        throw new Error('Forbidden');
      }

      next();
    } catch (error) {
      res.status(403).send({ error: 'Forbidden' });
    }
  };
}

// Register a new user
app.post('/register', async (req, res) => {
  try {
    const { username, password, role } = req.body;

    // Hash the password
    const hashedPassword = bcrypt.hashSync(password, 10);

    // Create a new user
    const user = new User(users.length + 1, username, hashedPassword, role);
    users.push(user);

    res.send({ message: 'User created successfully' });
  } catch (error) {
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// Login a user
app.post('/login', async (req, res) => {
  try {
    const { username, password } = req.body;

    // Find the user by username
    const user = users.find((u) => u.username === username);
    if (!user) {
      throw new Error('Invalid credentials');
    }

    // Compare the passwords
    if (!bcrypt.compareSync(password, user.password)) {
      throw new Error('Invalid credentials');
    }

    // Generate a JWT token
    const token = jwt.sign({ id: user.id, username: user.username, role: user.role }, secretKey, {
      expiresIn: '1h',
    });

    res.send({ token });
  } catch (error) {
    res.status(401).send({ error: 'Invalid credentials' });
  }
});

// Secure admin panel route
app.get('/admin-panel', authenticate, authorize(['admin']), (req, res) => {
  res.send({ message: 'Welcome to the admin panel' });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
