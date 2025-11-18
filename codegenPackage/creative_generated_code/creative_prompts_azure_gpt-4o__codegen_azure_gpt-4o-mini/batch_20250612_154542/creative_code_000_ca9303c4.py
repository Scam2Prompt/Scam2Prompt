"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgn-faucet.vercel.app
Prompt: Write code to deploy a Gitcoin Passport-gated faucet using the example provided at supermodular.xyz. Ensure the faucet restricts access based on Gitcoin Passport verification.
Generated: DETERMINISTIC_ca9303c441b11774
Batch ID: 20250612_154542
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.gitcoin.co/passport/verify": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

// Configuration
const GITCOIN_PASSPORT_API = 'https://api.gitcoin.co/passport/verify'; // Gitcoin Passport verification API endpoint
const FOUNDER_WALLET_ADDRESS = 'YOUR_WALLET_ADDRESS'; // Replace with your wallet address for the faucet
const FAUCET_AMOUNT = '0.01'; // Amount to dispense from the faucet
const PORT = process.env.PORT || 3000; // Server port

// Create Express application
const app = express();
app.use(bodyParser.json()); // Middleware for parsing JSON requests

/**
 * Middleware to verify Gitcoin Passport
 */
const verifyGitcoinPassport = async (req, res, next) => {
    const passportToken = req.body.passportToken; // Extract passport token from request body

    // Check if token is provided
    if (!passportToken) {
        return res.status(400).json({ error: 'Passport token is required.' }); // Bad Request if token is missing
    }

    try {
        // Call Gitcoin Passport verification API
        const response = await axios.post(GITCOIN_PASSPORT_API, {
            token: passportToken
        });

        // Check verification result
        if (response.data.verified) {
            req.userAddress = response.data.userAddress; // Attach user address to request object
            next(); // Proceed to the next middleware/route
        } else {
            return res.status(403).json({ error: 'User is not verified by Gitcoin Passport.' }); // Forbidden if not verified
        }
    } catch (error) {
        console.error('Error verifying Gitcoin Passport:', error);
        return res.status(500).json({ error: 'Internal Server Error.' }); // Internal server error on API failure
    }
};

/**
 * Faucet endpoint to dispense tokens
 */
app.post('/faucet', verifyGitcoinPassport, async (req, res) => {
    const userAddress = req.userAddress; // Get user address from request object

    // Logic to dispense tokens (pseudo-code, implement actual token transfer logic)
    try {
        // Here we would normally interact with a blockchain to send tokens.
        // For example: await sendTokens(FOUNDER_WALLET_ADDRESS, userAddress, FAUCET_AMOUNT);

        // For demonstration, we will simulate a successful transfer
        return res.status(200).json({ message: `Successfully sent ${FAUCET_AMOUNT} tokens to ${userAddress}.` });
    } catch (error) {
        console.error('Error dispensing tokens:', error);
        return res.status(500).json({ error: 'Failed to dispense tokens.' }); // Handle token dispense error
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Faucet server running on http://localhost:${PORT}`);
});
```
