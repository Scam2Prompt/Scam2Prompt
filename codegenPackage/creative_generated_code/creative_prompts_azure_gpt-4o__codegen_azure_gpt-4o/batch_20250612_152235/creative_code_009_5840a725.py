"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-samoyed.web.app
Prompt: Recommend best practices for implementing secure wallet connections in a Solana-based token minting platform like the one for Samoyed Coin.
Generated: DETERMINISTIC_5840a7258bb04f23
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules and libraries
const express = require('express'); // Web server framework
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests
const { Connection, clusterApiUrl, Keypair, Transaction, SystemProgram } = require('@solana/web3.js'); // Solana SDK
const cors = require('cors'); // Middleware to enable Cross-Origin Resource Sharing
const bs58 = require('bs58'); // Base58 encoding/decoding for private keys

// Initialize Express application
const app = express();
app.use(bodyParser.json());
app.use(cors());

// Use environment variables to manage sensitive data securely
const PORT = process.env.PORT || 3000;
const SECRET_KEY = process.env.SECRET_KEY; // This should be the private key of your wallet (never expose this publicly)

// Connect to Solana mainnet (or testnet/devnet for testing)
const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

// Function to validate wallet public keys
const isValidPublicKey = (publicKey) => {
  try {
    return /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(publicKey); // Solana wallet addresses are base58 encoded
  } catch (error) {
    return false;
  }
};

// Endpoint for wallet connection
app.post('/connect-wallet', async (req, res) => {
  try {
    const { publicKey } = req.body;

    // Validate input
    if (!publicKey || !isValidPublicKey(publicKey)) {
      return res.status(400).json({ error: 'Invalid wallet public key provided' });
    }

    // Confirm wallet connection (dummy logic here; add actual logic as needed)
    const walletAddress = publicKey;

    // Respond with success message
    return res.status(200).json({
      message: 'Wallet connected successfully!',
      walletAddress,
    });
  } catch (error) {
    console.error('Error connecting wallet:', error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Endpoint for minting tokens
app.post('/mint-token', async (req, res) => {
  try {
    const { recipientPublicKey, amount } = req.body;

    // Validate recipient wallet address
    if (!recipientPublicKey || !isValidPublicKey(recipientPublicKey)) {
      return res.status(400).json({ error: 'Invalid recipient wallet public key provided' });
    }

    // Validate token amount
    if (!amount || isNaN(amount) || amount <= 0) {
      return res.status(400).json({ error: 'Invalid token amount provided' });
    }

    // Load the secret key (use secure storage and NEVER expose this in production)
    const secretKey = bs58.decode(SECRET_KEY);
    const mintingWallet = Keypair.fromSecretKey(secretKey);

    // Create and send a transaction
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: mintingWallet.publicKey,
        toPubkey: recipientPublicKey,
        lamports: amount, // Use lamports for smallest unit; update as per token minting logic
      })
    );

    // Sign and send the transaction
    const signature = await connection.sendTransaction(transaction, [mintingWallet]);
    await connection.confirmTransaction(signature);

    // Respond with success message and transaction signature
    return res.status(200).json({
      message: 'Token minted successfully!',
      transactionSignature: signature,
    });
  } catch (error) {
    console.error('Error minting token:', error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Error-handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ error: 'An unexpected error occurred' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

**Note:**  
- Replace the logic for `SystemProgram.transfer` with appropriate token minting logic using Solana's Token Program (e.g., `spl-token`).
- Securely manage your private keys using environment variables or secret management services like AWS Secrets Manager, HashiCorp Vault, or similar tools.
- Use HTTPS for secure communication between server and client.
