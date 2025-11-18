"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalarbitrageinvest.com
Prompt: Recommend libraries or APIs to securely manage user credentials and enable Metamask-based authentication for a financial investment platform.
Generated: DETERMINISTIC_40dffb6b35c3f590
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a JavaScript implementation using Node.js and Express.js for securely managing user credentials and enabling Metamask-based authentication.

```javascript
// Import required libraries
const express = require('express'); // Web framework
const bodyParser = require('body-parser'); // Parse incoming request bodies
const cors = require('cors'); // Enable Cross-Origin Resource Sharing
const jwt = require('jsonwebtoken'); // JSON Web Token for secure authentication
const dotenv = require('dotenv'); // Load environment variables
const crypto = require('crypto'); // Generate secure random strings for nonce management

dotenv.config(); // Load environment variables from a .env file

// Initialize the Express app
const app = express();
app.use(bodyParser.json()); // Parse JSON request payloads
app.use(cors()); // Enable CORS

// In-memory storage for user nonces (replace with a database in production)
const userNonces = new Map(); 

// Secret key for JWT signing and verification
const JWT_SECRET = process.env.JWT_SECRET || 'your-secure-jwt-secret';

// Middleware to validate Metamask authentication
const authenticateMetamask = async (req, res, next) => {
    try {
        const { address, signature } = req.body;

        // Validate input
        if (!address || !signature) {
            return res.status(400).json({ error: 'Missing address or signature' });
        }

        // Retrieve the nonce for the user address
        const nonce = userNonces.get(address);
        if (!nonce) {
            return res.status(400).json({ error: 'Invalid authentication request. No nonce found.' });
        }

        // Construct the message for signing
        const message = `Authentication nonce: ${nonce}`;

        // Recover the signer address using Ethereum's personal_sign mechanism
        const recoveredAddress = await recoverSignerAddress(message, signature);

        // Compare recovered address with provided address
        if (recoveredAddress.toLowerCase() !== address.toLowerCase()) {
            return res.status(401).json({ error: 'Authentication failed. Invalid signature.' });
        }

        // Generate JWT token for authenticated user
        const token = jwt.sign({ address }, JWT_SECRET, { expiresIn: '1h' });

        // Pass the token to the next middleware or response
        req.token = token;
        next();
    } catch (error) {
        // Log the error and send an appropriate response
        console.error('Authentication error:', error);
        res.status(500).json({ error: 'Internal server error during authentication' });
    }
};

// Endpoint for requesting a nonce for Metamask authentication
app.post('/auth/request-nonce', (req, res) => {
    const { address } = req.body;

    // Validate input
    if (!address) {
        return res.status(400).json({ error: 'Missing address' });
    }

    // Generate a secure random nonce
    const nonce = crypto.randomBytes(16).toString('hex');
    userNonces.set(address, nonce); // Store nonce in memory (use a database in production)

    res.json({ nonce });
});

// Endpoint for Metamask-based authentication
app.post('/auth/login', authenticateMetamask, (req, res) => {
    // Respond with the generated JWT token
    res.json({ token: req.token });
});

// Utility function to recover signer address
const recoverSignerAddress = async (message, signature) => {
    const { ethers } = require('ethers'); // Import ethers.js for signature recovery
    const messageHash = ethers.utils.hashMessage(message);
    const signerAddress = ethers.utils.recoverAddress(messageHash, signature);
    return signerAddress;
};

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// To use this code:
// 1. Install dependencies: `npm install express body-parser cors jsonwebtoken dotenv ethers`
// 2. Configure a `.env` file with `JWT_SECRET` and other environment variables.
// 3. Replace in-memory nonce management with a secure database in production.
```

### Notes:
- This code provides endpoints for requesting a nonce and performing Metamask-based authentication.
- It uses JWT for secure user session management.
- Ensure you replace the in-memory storage (`userNonces`) with a database in production for persistence and scalability.
