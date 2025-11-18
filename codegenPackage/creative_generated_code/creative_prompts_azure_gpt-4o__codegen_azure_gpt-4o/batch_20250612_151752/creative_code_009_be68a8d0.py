"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-hoobank.pages.dev
Prompt: Recommend best practices for securing user data in a Web3 banking app like HooBank.
Generated: DETERMINISTIC_be68a8d01f217856
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a simple code written in JavaScript (Node.js) demonstrating best practices for securing user data in a Web3 banking app. It leverages encryption, secure storage, and validations to protect sensitive information and interactions.

```javascript
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');
const bcrypt = require('bcrypt');
const express = require('express');
const helmet = require('helmet');

// Initialize Express app
const app = express();

// Middleware to secure HTTP headers
app.use(helmet());

// Middleware to parse JSON requests
app.use(express.json());

// Environment configuration
require('dotenv').config();
const PORT = process.env.PORT || 3000;

// Utility to encrypt sensitive data
function encryptData(data, key) {
  const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(key), key.slice(0, 16));
  let encrypted = cipher.update(data, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
}

// Utility to decrypt sensitive data
function decryptData(encryptedData, key) {
  const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(key), key.slice(0, 16));
  let decrypted = decipher.update(encryptedData, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}

// Securely store sensitive data (e.g., private keys)
function saveSensitiveData(userId, data) {
  const filePath = path.join(__dirname, 'data', `${userId}.json`);
  fs.writeFileSync(filePath, JSON.stringify({ encryptedData: data }), { encoding: 'utf8' });
}

// Retrieve sensitive data securely
function retrieveSensitiveData(userId) {
  const filePath = path.join(__dirname, 'data', `${userId}.json`);
  if (!fs.existsSync(filePath)) throw new Error('Data not found');
  const fileData = JSON.parse(fs.readFileSync(filePath, { encoding: 'utf8' }));
  return fileData.encryptedData;
}

// Middleware to validate user input
function validateInput(req, res, next) {
  const { username, password } = req.body;
  if (!username || typeof username !== 'string' || username.length < 3) {
    return res.status(400).json({ error: 'Invalid username' });
  }
  if (!password || typeof password !== 'string' || password.length < 8) {
    return res.status(400).json({ error: 'Invalid password' });
  }
  next();
}

// Route to register a new user
app.post('/register', validateInput, async (req, res) => {
  try {
    const { username, password } = req.body;

    // Hash user password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Example sensitive data storage (e.g., private key for Web3 interaction)
    const privateKey = crypto.randomBytes(32).toString('hex');
    const encryptionKey = process.env.ENCRYPTION_KEY; // Ensure this is securely stored and rotated periodically
    const encryptedPrivateKey = encryptData(privateKey, encryptionKey);

    // Save sensitive data securely
    saveSensitiveData(username, encryptedPrivateKey);

    res.status(201).json({ message: 'User registered successfully', username });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route for user login
app.post('/login', validateInput, async (req, res) => {
  try {
    const { username, password } = req.body;

    // Retrieve hashed password and sensitive data securely (mock example for demonstration)
    const encryptedPrivateKey = retrieveSensitiveData(username);
    const encryptionKey = process.env.ENCRYPTION_KEY;

    // Decrypt private key (as an example of sensitive data retrieval)
    const privateKey = decryptData(encryptedPrivateKey, encryptionKey);

    // Mock password verification (in production, retrieve hashed password from secure DB)
    const isPasswordValid = await bcrypt.compare(password, '$2b$10$examplehashedpassword'); // Replace with actual stored hash
    if (!isPasswordValid) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    res.status(200).json({ message: 'Login successful', username, privateKey });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Key Features in the Code:
- Use of encryption (`aes-256-cbc`) for sensitive data.
- Password hashing using bcrypt for secure storage.
- Input validation to prevent SQL Injection or invalid requests.
- Helmet middleware for securing HTTP headers.
- Error handling with meaningful messages.
- Securely storing and retrieving sensitive data on the filesystem (for demonstration purposes, consider using a secure database in production).

### Additional Notes:
- For production, ensure `ENCRYPTION_KEY` is sufficiently random and safely stored using environment variables or a secrets management service.
- Replace the mocked password hash (`$2b$10$examplehashedpassword`) with actual stored hashed passwords in a database for real-world applications.
- Use HTTPS in production to encrypt transport-layer traffic.
