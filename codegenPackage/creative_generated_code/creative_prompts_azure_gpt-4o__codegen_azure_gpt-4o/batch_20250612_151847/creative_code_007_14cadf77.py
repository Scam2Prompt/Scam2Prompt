"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solanaclaims.web.app
Prompt: Generate a pitch-ready prototype for a Solana-based web3 startup, adhering to the Hyperdrive Hackathon's five-week bootstrapping timeline.
Generated: DETERMINISTIC_14cadf77ea8257d9
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages and libraries
const { Connection, PublicKey, clusterApiUrl, Keypair } = require('@solana/web3.js');
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const dotenv = require('dotenv');
const fs = require('fs');

// Load environment variables for sensitive data
dotenv.config();

// Initialize Express app
const app = express();
app.use(bodyParser.json());
app.use(cors());

// Establish connection to the Solana devnet
const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

// Generate a new Solana keypair to be used for the prototype
const secretKeyPath = process.env.SECRET_KEY_PATH || './secret-key.json';
let secretKey;
if (fs.existsSync(secretKeyPath)) {
  // Load keypair from file if it exists
  secretKey = JSON.parse(fs.readFileSync(secretKeyPath).toString());
} else {
  // Create new keypair and save it to file
  const keypair = Keypair.generate();
  secretKey = Array.from(keypair.secretKey);
  fs.writeFileSync(secretKeyPath, JSON.stringify(secretKey));
}
const keypair = Keypair.fromSecretKey(Uint8Array.from(secretKey));

// Public key derived from the keypair
const publicKey = keypair.publicKey.toString();

// API Endpoint: Health Check
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK', message: 'API is running' });
});

// API Endpoint: Get wallet balance
app.get('/balance', async (req, res) => {
  try {
    const balance = await connection.getBalance(keypair.publicKey);
    res.status(200).json({
      publicKey,
      balance: balance / 1e9, // Convert lamports to SOL
    });
  } catch (error) {
    console.error('Error fetching balance:', error);
    res.status(500).json({
      error: 'Failed to fetch wallet balance',
      details: error.message,
    });
  }
});

// API Endpoint: Airdrop SOL (for testing purposes)
app.post('/airdrop', async (req, res) => {
  try {
    const airdropSignature = await connection.requestAirdrop(keypair.publicKey, 1e9); // 1 SOL
    await connection.confirmTransaction(airdropSignature);
    res.status(200).json({
      message: 'Airdrop successful',
      publicKey,
      transactionSignature: airdropSignature,
    });
  } catch (error) {
    console.error('Error during airdrop:', error);
    res.status(500).json({
      error: 'Airdrop failed',
      details: error.message,
    });
  }
});

// API Endpoint: Send SOL to another wallet
app.post('/send', async (req, res) => {
  const { recipient, amount } = req.body;

  // Validate request parameters
  if (!recipient || !amount) {
    return res.status(400).json({
      error: 'Invalid request parameters. "recipient" and "amount" are required.',
    });
  }

  try {
    // Create a transaction to send SOL
    const transaction = await connection.getRecentBlockhash().then(({ blockhash }) => {
      const transferTransaction = new Transaction().add(
        SystemProgram.transfer({
          fromPubkey: keypair.publicKey,
          toPubkey: new PublicKey(recipient),
          lamports: amount * 1e9, // Convert SOL to lamports
        })
      );
      transferTransaction.recentBlockhash = blockhash;
      transferTransaction.feePayer = keypair.publicKey;
      return transferTransaction;
    });

    // Sign and send the transaction
    const signedTransaction = await connection.sendTransaction(transaction, [keypair]);
    res.status(200).json({
      message: 'Transaction successful',
      transactionSignature: signedTransaction,
    });
  } catch (error) {
    console.error('Error during transaction:', error);
    res.status(500).json({
      error: 'Transaction failed',
      details: error.message,
    });
  }
});

// Start Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  console.log(`Connected wallet public key: ${publicKey}`);
});
```
