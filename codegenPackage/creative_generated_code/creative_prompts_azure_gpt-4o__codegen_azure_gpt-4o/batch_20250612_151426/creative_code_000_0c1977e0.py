"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-prime-kongz.web.app
Prompt: Write a script to integrate Solana wallet authentication for accessing the Atlas3 PRIME KONGZ whitelist raffle application.
Generated: DETERMINISTIC_0c1977e04c3ac427
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready code for integrating Solana wallet authentication for accessing the Atlas3 PRIME KONGZ whitelist raffle application.

```javascript
// Import required libraries
const express = require('express'); // Web server framework
const cors = require('cors'); // Enable CORS for cross-origin resource sharing
const bodyParser = require('body-parser'); // Parse incoming JSON requests
const nacl = require('tweetnacl'); // Used for signature verification
const bs58 = require('bs58'); // Base58 encoding/decoding for Solana public keys and signatures

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware configuration
app.use(cors()); // Enable CORS
app.use(bodyParser.json()); // Parse JSON payloads

// POST endpoint for Solana wallet authentication
app.post('/auth', async (req, res) => {
  try {
    // Extract the request payload
    const { publicKey, signature, message } = req.body;

    // Validate input data
    if (!publicKey || !signature || !message) {
      return res.status(400).json({ error: 'Invalid request. Missing publicKey, signature, or message.' });
    }

    // Decode public key and signature from Base58
    const decodedPublicKey = bs58.decode(publicKey);
    const decodedSignature = bs58.decode(signature);

    // Verify the signature against the message and public key
    const isValidSignature = nacl.sign.detached.verify(
      new TextEncoder().encode(message), // Convert message to Uint8Array
      decodedSignature,                 // Detected signature Uint8Array
      decodedPublicKey                  // Detected publicKey Uint8Array
    );

    if (!isValidSignature) {
      return res.status(401).json({ error: 'Signature verification failed. Access denied.' });
    }

    // If authentication is successful, grant access to the whitelist raffle
    res.status(200).json({ message: 'Authentication successful. Access granted to Atlas3 PRIME KONGZ whitelist raffle.' });
  } catch (error) {
    // Handle any unexpected errors
    console.error('Error during authentication:', error);
    res.status(500).json({ error: 'Internal server error. Please try again later.' });
  }
});

// Start the Express server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

Make sure to install the required packages before running the script using the following command:

```bash
npm install express cors body-parser tweetnacl bs58
```
