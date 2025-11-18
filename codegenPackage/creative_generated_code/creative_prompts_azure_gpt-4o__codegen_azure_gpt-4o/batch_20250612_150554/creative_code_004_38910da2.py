"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletauthenticator.vercel.app
Prompt: Write a script to implement wallet authentication in a web app using a JavaScript framework, inspired by Wallet Authenticator's approach.
Generated: DETERMINISTIC_38910da2bbe0cf4b
Batch ID: 20250612_150554
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
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
// Import necessary dependencies
import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import { ethers } from 'ethers';

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// In-memory store for simplicity (use a proper database in production)
const nonceStore = {};

// Generate random nonce for wallet authentication
const generateNonce = () => Math.floor(Math.random() * 1e6).toString();

// Endpoint to request a nonce for wallet authentication
app.post('/auth/request-nonce', (req, res) => {
  try {
    const { walletAddress } = req.body;

    // Validate wallet address
    if (!ethers.utils.isAddress(walletAddress)) {
      return res.status(400).json({ error: 'Invalid wallet address' });
    }

    // Generate and store nonce
    const nonce = generateNonce();
    nonceStore[walletAddress] = nonce;

    // Return nonce to client
    res.json({ nonce });
  } catch (error) {
    console.error('Error generating nonce:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint to verify signed message and authenticate user
app.post('/auth/verify', async (req, res) => {
  try {
    const { walletAddress, signedMessage } = req.body;

    // Validate request body
    if (!walletAddress || !signedMessage) {
      return res.status(400).json({ error: 'Wallet address and signed message are required' });
    }

    // Retrieve the stored nonce for the wallet address
    const nonce = nonceStore[walletAddress];
    if (!nonce) {
      return res.status(400).json({ error: 'No nonce found for this wallet address' });
    }

    // Verify the signed message against the nonce
    const recoveredAddress = ethers.utils.verifyMessage(nonce, signedMessage);
    if (recoveredAddress.toLowerCase() !== walletAddress.toLowerCase()) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    // Authentication successful
    // Generate a session token or similar (omitted for simplicity)
    // Clear the used nonce
    delete nonceStore[walletAddress];

    res.json({ success: true, message: 'Authentication successful' });
  } catch (error) {
    console.error('Error verifying signature:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Wallet authentication server running on http://localhost:${PORT}`);
});
```
