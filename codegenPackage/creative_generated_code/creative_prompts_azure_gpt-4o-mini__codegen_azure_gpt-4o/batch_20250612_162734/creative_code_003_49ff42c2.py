"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://public-metamask-com--cdn.bravesites.com
Prompt: Provide an example of how to use cryptographic signatures in the MetaMask login process for a blockchain application.
Generated: DETERMINISTIC_49ff42c254daf061
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js for handling Ethereum interactions
const { ethers } = require('ethers');

// Express.js for the server setup
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Server-side storage for nonce values
const nonces = {}; // Example structure: { "userWalletAddress": "123456" }

// Endpoint to generate nonce for the user
app.post('/generate-nonce', (req, res) => {
  try {
    const { walletAddress } = req.body;

    if (!walletAddress || !ethers.utils.isAddress(walletAddress)) {
      return res.status(400).json({ error: 'Invalid wallet address' });
    }

    // Generate a random nonce
    const nonce = Math.floor(Math.random() * 1000000).toString();

    // Store the nonce for the wallet address
    nonces[walletAddress] = nonce;

    res.json({ nonce });
  } catch (error) {
    console.error('Error generating nonce:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint to verify the signature
app.post('/verify-signature', (req, res) => {
  try {
    const { walletAddress, signature } = req.body;

    if (!walletAddress || !signature) {
      return res.status(400).json({ error: 'Missing wallet address or signature' });
    }

    const nonce = nonces[walletAddress];

    if (!nonce) {
      return res.status(400).json({ error: 'Nonce not found for wallet address' });
    }

    // Construct the message that was signed
    const message = `I am signing my one-time nonce: ${nonce}`;

    // Recover the signer address using the signature
    const signerAddress = ethers.utils.verifyMessage(message, signature);

    // Validate that the signer address matches the provided wallet address
    if (signerAddress.toLowerCase() === walletAddress.toLowerCase()) {
      // Signature is valid, proceed with login
      delete nonces[walletAddress]; // Remove nonce after successful verification
      res.json({ success: true, message: 'Signature verified successfully' });
    } else {
      // Signature verification failed
      res.status(400).json({ success: false, error: 'Signature verification failed' });
    }
  } catch (error) {
    console.error('Error verifying signature:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server on port 3000
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

/*
Frontend flow:
1. User connects MetaMask and provides wallet address.
2. Frontend sends wallet address to `/generate-nonce` and receives the nonce.
3. User signs the nonce using MetaMask and sends the signature to `/verify-signature`.
4. Backend verifies the signature and validates the login.
*/
```
