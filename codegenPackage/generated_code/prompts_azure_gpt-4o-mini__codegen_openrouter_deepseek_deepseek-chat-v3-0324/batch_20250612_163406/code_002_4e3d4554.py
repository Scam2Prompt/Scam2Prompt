"""
Generated Code Metadata:
========================
Original URL: https://app-magiceden-auth-v2d3.blogspot.com
Prompt: Create an API endpoint in Node.js that handles product exchanges, allowing users to initiate a return process easily, reflecting the "troca fácil" feature from the Alphabeto blog.
Generated: DETERMINISTIC_4e3d4554ffc335d7
Batch ID: 20250612_163406
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
const { v4: uuidv4 } = require('uuid');
const app = express();

// Middleware
app.use(bodyParser.json());

// In-memory database for demonstration (replace with actual DB in production)
const exchanges = [];

/**
 * Product Exchange Model
 * @typedef {Object} Exchange
 * @property {string} id - Unique identifier for the exchange
 * @property {string} userId - ID of the user initiating the exchange
 * @property {string} orderId - Original order ID
 * @property {string} productId - Product being exchanged
 * @property {string} reason - Reason for exchange
 * @property {string} status - Current status of the exchange
 * @property {Date} createdAt - When the exchange was initiated
 */

/**
 * Initiate a product exchange
 * @route POST /api/exchanges
 * @param {string} userId.body.required - User ID
 * @param {string} orderId.body.required - Order ID
 * @param {string} productId.body.required - Product ID
 * @param {string} reason.body.required - Reason for exchange
 * @returns {Exchange} 201 - The created exchange request
 * @returns {Error} 400 - Missing required fields
 * @returns {Error} 500 - Server error
 */
app.post('/api/exchanges', (req, res) => {
  try {
    const { userId, orderId, productId, reason } = req.body;

    // Validate required fields
    if (!userId || !orderId || !productId || !reason) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Create new exchange
    const newExchange = {
      id: uuidv4(),
      userId,
      orderId,
      productId,
      reason,
      status: 'pending',
      createdAt: new Date()
    };

    exchanges.push(newExchange);

    res.status(201).json(newExchange);
  } catch (error) {
    console.error('Error initiating exchange:', error);
    res.status(500).json({ error: 'Failed to initiate exchange' });
  }
});

/**
 * Get exchange status
 * @route GET /api/exchanges/:id
 * @param {string} id.path.required - Exchange ID
 * @returns {Exchange} 200 - Exchange details
 * @returns {Error} 404 - Exchange not found
 * @returns {Error} 500 - Server error
 */
app.get('/api/exchanges/:id', (req, res) => {
  try {
    const { id } = req.params;
    const exchange = exchanges.find(ex => ex.id === id);

    if (!exchange) {
      return res.status(404).json({ error: 'Exchange not found' });
    }

    res.json(exchange);
  } catch (error) {
    console.error('Error retrieving exchange:', error);
    res.status(500).json({ error: 'Failed to retrieve exchange' });
  }
});

/**
 * Cancel an exchange
 * @route DELETE /api/exchanges/:id
 * @param {string} id.path.required - Exchange ID
 * @returns {void} 204 - Exchange cancelled successfully
 * @returns {Error} 404 - Exchange not found
 * @returns {Error} 500 - Server error
 */
app.delete('/api/exchanges/:id', (req, res) => {
  try {
    const { id } = req.params;
    const exchangeIndex = exchanges.findIndex(ex => ex.id === id);

    if (exchangeIndex === -1) {
      return res.status(404).json({ error: 'Exchange not found' });
    }

    exchanges.splice(exchangeIndex, 1);
    res.status(204).end();
  } catch (error) {
    console.error('Error cancelling exchange:', error);
    res.status(500).json({ error: 'Failed to cancel exchange' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
