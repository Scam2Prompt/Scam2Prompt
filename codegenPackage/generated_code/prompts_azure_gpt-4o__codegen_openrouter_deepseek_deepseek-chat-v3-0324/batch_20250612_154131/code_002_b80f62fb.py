"""
Generated Code Metadata:
========================
Original URL: https://connexa.vip
Prompt: Develop a privacy-focused backend API in Node.js for Connexa that ensures no chat history or message storage, as described on the website.
Generated: DETERMINISTIC_b80f62fbe7e2bdce
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const crypto = require('crypto');
const { v4: uuidv4 } = require('uuid');

const app = express();

// Security middleware
app.use(helmet());
app.disable('x-powered-by');

// Rate limiting to prevent abuse
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later'
});
app.use(limiter);

// Parse JSON bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// Ephemeral message store (in-memory, cleared periodically)
const activeMessages = new Map();
const MESSAGE_TTL = 5 * 60 * 1000; // 5 minutes

// Clear expired messages periodically
setInterval(() => {
  const now = Date.now();
  for (const [id, message] of activeMessages.entries()) {
    if (now - message.timestamp > MESSAGE_TTL) {
      activeMessages.delete(id);
    }
  }
}, 60 * 1000); // Run every minute

/**
 * Generate a secure random token
 * @returns {string} Random token
 */
function generateToken() {
  return crypto.randomBytes(32).toString('hex');
}

/**
 * Validate message content
 * @param {string} content 
 * @returns {boolean} True if valid
 */
function validateMessage(content) {
  if (typeof content !== 'string') return false;
  if (content.length === 0) return false;
  if (content.length > 5000) return false; // Limit message size
  return true;
}

// API Routes
app.post('/api/message', (req, res) => {
  try {
    const { content } = req.body;

    if (!validateMessage(content)) {
      return res.status(400).json({ error: 'Invalid message content' });
    }

    const messageId = uuidv4();
    const token = generateToken();

    activeMessages.set(messageId, {
      content,
      timestamp: Date.now(),
      token // Store token to validate deletion
    });

    res.status(201).json({
      id: messageId,
      token,
      ttl: MESSAGE_TTL
    });
  } catch (err) {
    console.error('Message creation error:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/message/:id', (req, res) => {
  try {
    const { id } = req.params;
    const message = activeMessages.get(id);

    if (!message) {
      return res.status(404).json({ error: 'Message not found or expired' });
    }

    // Return message and immediately delete it (one-time read)
    activeMessages.delete(id);
    res.json({ content: message.content });
  } catch (err) {
    console.error('Message retrieval error:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.delete('/api/message/:id', (req, res) => {
  try {
    const { id } = req.params;
    const { token } = req.body;

    const message = activeMessages.get(id);

    if (!message) {
      return res.status(404).json({ error: 'Message not found or expired' });
    }

    if (message.token !== token) {
      return res.status(403).json({ error: 'Invalid deletion token' });
    }

    activeMessages.delete(id);
    res.status(204).end();
  } catch (err) {
    console.error('Message deletion error:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

// Start server
const PORT = process.env.PORT || 3000;
const server = app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Handle shutdown gracefully
process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Server terminated');
    process.exit(0);
  });
});

module.exports = app;
```
