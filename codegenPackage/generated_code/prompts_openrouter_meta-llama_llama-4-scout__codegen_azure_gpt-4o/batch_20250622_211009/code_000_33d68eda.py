"""
Generated Code Metadata:
========================
Original URL: https://sunny-pastelito-21f63f.netlify.app
Prompt: "Generate JavaScript code to implement a token claim link feature similar to Linkdrop."
Generated: DETERMINISTIC_33d68eda22ea74b6
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Token Claim Link Feature
 * This script implements a token claim link feature similar to Linkdrop.
 * Users can generate claim links and redeem tokens using the link.
 */

// Import necessary libraries (e.g., crypto for secure token generation)
const crypto = require('crypto');
const express = require('express');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// In-memory storage for claim links and tokens (use a database in production)
const claimLinks = {};

// Generate a secure token
function generateToken() {
  return crypto.randomBytes(32).toString('hex');
}

/**
 * Endpoint to create a claim link
 * Request body: { amount: number }
 * Response: { claimLink: string }
 */
app.post('/create-claim-link', (req, res) => {
  try {
    const { amount } = req.body;

    // Validate input
    if (!amount || typeof amount !== 'number' || amount <= 0) {
      return res.status(400).json({ error: 'Invalid amount provided.' });
    }

    // Generate a unique token
    const token = generateToken();

    // Store the token and associated amount
    claimLinks[token] = { amount, claimed: false };

    // Generate the claim link
    const claimLink = `${req.protocol}://${req.get('host')}/claim/${token}`;

    res.status(201).json({ claimLink });
  } catch (error) {
    console.error('Error creating claim link:', error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

/**
 * Endpoint to claim tokens using a claim link
 * URL parameter: token
 * Response: { message: string, amount?: number }
 */
app.get('/claim/:token', (req, res) => {
  try {
    const { token } = req.params;

    // Check if the token exists
    const claimData = claimLinks[token];
    if (!claimData) {
      return res.status(404).json({ error: 'Invalid or expired claim link.' });
    }

    // Check if the token has already been claimed
    if (claimData.claimed) {
      return res.status(400).json({ error: 'This claim link has already been used.' });
    }

    // Mark the token as claimed
    claimData.claimed = true;

    res.status(200).json({ message: 'Tokens successfully claimed!', amount: claimData.amount });
  } catch (error) {
    console.error('Error claiming tokens:', error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

/**
 * Start the server
 */
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
