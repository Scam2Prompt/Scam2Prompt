"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Develop a Node.js application to facilitate secure and seamless communication between title insurance companies and their clients, using the professional communication tools integrated by Superior Title Montana.
Generated: DETERMINISTIC_3949e99f6156c003
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse incoming request bodies
const helmet = require('helmet'); // Security middleware to set HTTP headers
const cors = require('cors'); // Middleware to enable Cross-Origin Resource Sharing
const morgan = require('morgan'); // HTTP request logger middleware
const dotenv = require('dotenv'); // Module to load environment variables
const crypto = require('crypto'); // Module for cryptographic operations

// Load environment variables from .env file
dotenv.config();

// Initialize the Express application
const app = express();

// Middleware setup
app.use(helmet()); // Enhance security by setting HTTP headers
app.use(cors()); // Enable CORS for cross-origin requests
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(morgan('combined')); // Log HTTP requests

// Port configuration
const PORT = process.env.PORT || 3000;

// Simulated database (replace with a real database in production)
const messages = [];

// Utility function to encrypt messages
function encryptMessage(message, secretKey) {
  const cipher = crypto.createCipher('aes-256-cbc', secretKey);
  let encrypted = cipher.update(message, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
}

// Utility function to decrypt messages
function decryptMessage(encryptedMessage, secretKey) {
  const decipher = crypto.createDecipher('aes-256-cbc', secretKey);
  let decrypted = decipher.update(encryptedMessage, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}

// Route: Health check
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK', message: 'Service is running' });
});

// Route: Send a secure message
app.post('/send-message', (req, res) => {
  try {
    const { sender, recipient, message } = req.body;

    // Validate input
    if (!sender || !recipient || !message) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Encrypt the message
    const secretKey = process.env.SECRET_KEY;
    if (!secretKey) {
      return res.status(500).json({ error: 'Server misconfiguration: SECRET_KEY is missing' });
    }
    const encryptedMessage = encryptMessage(message, secretKey);

    // Store the message
    messages.push({ sender, recipient, encryptedMessage, timestamp: new Date() });

    res.status(200).json({ message: 'Message sent successfully' });
  } catch (error) {
    console.error('Error sending message:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route: Retrieve messages for a recipient
app.get('/messages/:recipient', (req, res) => {
  try {
    const { recipient } = req.params;

    // Validate input
    if (!recipient) {
      return res.status(400).json({ error: 'Recipient is required' });
    }

    // Retrieve and decrypt messages
    const secretKey = process.env.SECRET_KEY;
    if (!secretKey) {
      return res.status(500).json({ error: 'Server misconfiguration: SECRET_KEY is missing' });
    }
    const recipientMessages = messages
      .filter((msg) => msg.recipient === recipient)
      .map((msg) => ({
        sender: msg.sender,
        message: decryptMessage(msg.encryptedMessage, secretKey),
        timestamp: msg.timestamp,
      }));

    res.status(200).json({ messages: recipientMessages });
  } catch (error) {
    console.error('Error retrieving messages:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
1. Create a `.env` file in the root directory and define `SECRET_KEY` for encryption/decryption and `PORT` if needed.
2. Replace the simulated `messages` array with a real database (e.g., MongoDB, PostgreSQL) for production use.
3. Ensure HTTPS is used in production for secure communication.
