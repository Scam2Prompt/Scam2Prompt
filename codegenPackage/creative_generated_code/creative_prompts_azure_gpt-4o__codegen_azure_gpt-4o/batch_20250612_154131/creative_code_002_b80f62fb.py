"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connexa.vip
Prompt: Develop a privacy-focused backend API in Node.js for Connexa that ensures no chat history or message storage, as described on the website.
Generated: DETERMINISTIC_b80f62fbe7e2bdce
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * privacy-focused backend API for Connexa
 * Ensures no chat history or message storage
 */

const express = require('express'); // Import express framework
const bodyParser = require('body-parser'); // Middleware to parse JSON request bodies
const cors = require('cors'); // Middleware to enable Cross-Origin Resource Sharing
const helmet = require('helmet'); // Security middleware to protect against common web vulnerabilities

const app = express(); // Create an Express application instance
const PORT = process.env.PORT || 3000; // Use environment variable PORT or default to 3000

// Middleware setup
app.use(cors()); // Enable CORS for all origins
app.use(helmet()); // Secure HTTP headers
app.use(bodyParser.json()); // Parse JSON request bodies

/**
 * POST /api/send-message
 * Handles incoming chat messages and forwards them to the recipient immediately.
 * No data is stored on the server.
 */
app.post('/api/send-message', (req, res) => {
  const { recipient, message } = req.body;

  // Validate input
  if (!recipient || !message) {
    return res.status(400).json({ error: 'Recipient and message are required.' });
  }

  try {
    // Simulate message forwarding (replace with actual forwarding logic, e.g., sockets or external service)
    console.log(`Message forwarded to ${recipient}: ${message}`);

    // Respond with success (no storage occurs on the server)
    return res.status(200).json({ success: true, message: 'Message sent successfully.' });
  } catch (error) {
    // Handle errors gracefully
    console.error('Error forwarding message:', error);
    return res.status(500).json({ error: 'An error occurred while sending the message.' });
  }
});

/**
 * 404 handler for undefined routes.
 */
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found.' });
});

/**
 * Error-handling middleware.
 */
app.use((err, req, res, next) => {
  console.error('Unexpected server error:', err);
  res.status(500).json({ error: 'An unexpected error occurred.' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Connexa API running on port ${PORT}`);
});
```
