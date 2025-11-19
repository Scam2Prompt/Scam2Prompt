"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiger-b75.pages.dev
Prompt: Write a code snippet that demonstrates how to securely communicate between wallets and Dapps as described on the BABY TIGER KING website.
Generated: DETERMINISTIC_6c1ab464f92f657e
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const ethers = require('ethers'); // Ethereum library for wallet and DApp interactions
const express = require('express'); // Web server for DApp backend
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests

// Initialize Express app
const app = express();
app.use(bodyParser.json()); // Use JSON parser for API requests

// Setting up a secure communication between wallet and DApp
const PORT = process.env.PORT || 3000; // Use environment variable or default port

// Example private key (DO NOT hardcode this in production, use environment variables)
const PRIVATE_KEY = process.env.SIGNER_PRIVATE_KEY;
if (!PRIVATE_KEY) {
  throw new Error("Environment variable SIGNER_PRIVATE_KEY is required.");
}

// Create wallet instance using the private key
const wallet = new ethers.Wallet(PRIVATE_KEY);

// Route to handle signing messages securely
app.post('/sign-message', async (req, res) => {
  try {
    // Validate incoming request
    const { message } = req.body;
    if (!message) {
      return res.status(400).json({ error: 'Message is required!' });
    }

    // Sign the message using the wallet's private key
    const signature = await wallet.signMessage(message);

    // Return the signature to the client
    res.json({ message, signature });
  } catch (error) {
    // Handle errors
    console.error('Error signing message:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to verify signed message (optional for demonstrating communication)
app.post('/verify-signature', async (req, res) => {
  try {
    // Validate incoming request
    const { message, signature } = req.body;
    if (!message || !signature) {
      return res.status(400).json({ error: 'Message and signature are required!' });
    }

    // Recover the address from the signed message
    const recoveredAddress = ethers.utils.verifyMessage(message, signature);

    // Validate if address matches the wallet's address
    const isValid = recoveredAddress === wallet.address;

    // Respond with verification result
    res.json({ valid: isValid, recoveredAddress });
  } catch (error) {
    // Handle errors
    console.error('Error verifying signature:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the Express server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
 * Best Practices Followed:
 * 1. Securely handle private keys using environment variables.
 * 2. Validate input data to prevent malicious payloads.
 * 3. Proper error handling to ensure robust API responses.
 * 4. Use cryptographic signing and verification for secure wallet-DApp communication.
 * 5. Modular code for scalability and maintainability.
 *
 * To interact securely between wallets and DApps:
 * - Ensure the DApp backend signs the messages using a secure private key.
 * - Verify the signatures on the wallet side using the recovered address.
 */
```
