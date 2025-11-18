"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wl-usdh-mint.web.app
Prompt: Create a Solana-based minting dApp that differentiates between whitelist and public minting prices, ensuring free minting rights for eligible token holders.
Generated: DETERMINISTIC_c18af29f80ffa7ce
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Solana Web3 and other libraries
const { Connection, PublicKey, Keypair, Transaction, SystemProgram } = require('@solana/web3.js');
const { TOKEN_PROGRAM_ID, getOrCreateAssociatedTokenAccount, mintTo } = require('@solana/spl-token');
const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');
dotenv.config();

// Load environment variables
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private Key of the Mint Account
const MINT_ADDRESS = process.env.MINT_ADDRESS; // Address of the SPL token to mint
const CLUSTER_URL = process.env.CLUSTER_URL; // Solana Cluster URL
const WHITELIST_ADDRESS = process.env.WHITELIST_ADDRESS; // Address of whitelist manager (can be a program or data storage)
const WHITELIST_PRICE = parseFloat(process.env.WHITELIST_PRICE || 0.1); // Minting price for whitelist (in SOL)
const PUBLIC_PRICE = parseFloat(process.env.PUBLIC_PRICE || 0.5); // Minting price for public (in SOL)

// Initialize Solana connection
const connection = new Connection(CLUSTER_URL, 'confirmed');
const mintAuthority = Keypair.fromSecretKey(Buffer.from(JSON.parse(PRIVATE_KEY)));
const mintAddress = new PublicKey(MINT_ADDRESS);

// Initialize Express server
const app = express();
app.use(bodyParser.json());

// Middleware for error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Endpoint: Mint token
app.post('/mint', async (req, res) => {
  try {
    const { userPubKey, isWhitelist } = req.body;

    if (!userPubKey) {
      return res.status(400).json({ error: 'userPubKey is required' });
    }

    // Parse user's public key
    const userPublicKey = new PublicKey(userPubKey);

    // Determine the price based on whitelist status
    const price = isWhitelist ? WHITELIST_PRICE : PUBLIC_PRICE;

    // Verify if user is eligible for whitelist (placeholder logic; implement your own logic)
    if (isWhitelist) {
      const isEligible = await checkWhitelistEligibility(userPublicKey);
      if (!isEligible) {
        return res.status(403).json({ error: 'User is not eligible for whitelist minting' });
      }
    }

    // Create a transaction to deduct SOL from the user as payment
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: userPublicKey,
        toPubkey: mintAuthority.publicKey,
        lamports: price * 1e9, // Convert SOL to lamports
      })
    );

    // Send transaction for payment (to be signed by user on frontend)
    const serializedTransaction = transaction.serialize({ verifySignatures: false });
    res.json({ transaction: serializedTransaction.toString('base64') });

    // After payment, mint the token
    const tokenAccount = await getOrCreateAssociatedTokenAccount(
      connection,
      mintAuthority,
      mintAddress,
      userPublicKey
    );

    // Mint the token to user's associated account
    const signature = await mintTo(
      connection,
      mintAuthority,
      mintAddress,
      tokenAccount.address,
      mintAuthority,
      1 // Mint 1 token
    );

    res.json({ success: true, signature });
  } catch (error) {
    console.error('Error minting token:', error);
    res.status(500).json({ error: 'Error minting token' });
  }
});

// Placeholder: Function to check if user is eligible for whitelist
async function checkWhitelistEligibility(userPublicKey) {
  // Add your whitelist eligibility logic here
  // Example: Query a database or on-chain data
  return true;
}

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

**Note:**
- Ensure environment variables are properly configured in a `.env` file.
- Replace `checkWhitelistEligibility` with your custom whitelist check logic.
- Frontend must be used to sign transactions before sending them to the backend for final execution.
