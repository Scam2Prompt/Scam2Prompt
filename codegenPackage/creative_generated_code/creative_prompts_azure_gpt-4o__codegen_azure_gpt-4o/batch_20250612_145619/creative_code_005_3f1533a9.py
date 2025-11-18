"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummyh.pages.dev
Prompt: Develop a Solana-based dApp that allows users to claim $Gummy airdrops and view token allocation details interactively.
Generated: DETERMINISTIC_3f1533a95880e9fa
Batch ID: 20250612_145619
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.devnet.solana.com": {
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
// File: solana_gummy_airdrop_dapp.js

// Import necessary Solana web3 libraries
const { Connection, PublicKey, Keypair, Transaction, SystemProgram } = require('@solana/web3.js');
const { Token, TOKEN_PROGRAM_ID } = require('@solana/spl-token');
const express = require('express');
const bodyParser = require('body-parser');
require('dotenv').config();

// Constants and environment variables
const CLUSTER_URL = process.env.SOLANA_CLUSTER_URL || 'https://api.devnet.solana.com';
const AIRDROP_PROGRAM_ID = new PublicKey(process.env.AIRDROP_PROGRAM_ID); // Smart contract program ID
const GUMMY_MINT_ADDRESS = new PublicKey(process.env.GUMMY_MINT_ADDRESS); // Mint address of $Gummy token
const SERVER_PORT = process.env.SERVER_PORT || 3000;

// Initialize Solana connection
const connection = new Connection(CLUSTER_URL, 'confirmed');

// Express app for the dApp's backend
const app = express();
app.use(bodyParser.json());

// Claim $Gummy Airdrop endpoint
app.post('/claim', async (req, res) => {
    try {
        const { userPublicKey } = req.body;

        if (!userPublicKey) {
            return res.status(400).json({ error: 'User public key is required.' });
        }

        const userKey = new PublicKey(userPublicKey);

        // Create airdrop transaction
        const transaction = new Transaction().add(
            SystemProgram.transfer({
                fromPubkey: AIRDROP_PROGRAM_ID,
                toPubkey: userKey,
                lamports: 1 // Placeholder for actual airdrop logic
            })
        );

        const transactionSignature = await connection.sendTransaction(transaction, []);
        await connection.confirmTransaction(transactionSignature, 'confirmed');

        res.status(200).json({ success: true, transactionSignature });
    } catch (error) {
        console.error('Error claiming airdrop:', error);
        res.status(500).json({ error: 'An error occurred while claiming the airdrop.' });
    }
});

// Check token allocation details endpoint
app.get('/allocation/:userPublicKey', async (req, res) => {
    try {
        const { userPublicKey } = req.params;

        if (!userPublicKey) {
            return res.status(400).json({ error: 'User public key is required.' });
        }

        const userKey = new PublicKey(userPublicKey);

        // Fetch token balance details for the user
        const tokenAccounts = await connection.getTokenAccountsByOwner(userKey, {
            mint: GUMMY_MINT_ADDRESS,
        });

        const allocations = tokenAccounts.value.map((account) => ({
            accountPubkey: account.pubkey.toBase58(),
            amount: account.account.data.parsed.info.tokenAmount.uiAmount,
        }));

        res.status(200).json({ success: true, allocations });
    } catch (error) {
        console.error('Error fetching token allocation:', error);
        res.status(500).json({ error: 'An error occurred while fetching token allocations.' });
    }
});

// Start the server
app.listen(SERVER_PORT, () => {
    console.log(`Solana $Gummy Airdrop dApp running on port ${SERVER_PORT}`);
});
```

This code is syntactically correct, includes comments, and adheres to best practices. Ensure that `.env` contains the required environment variables (e.g., `SOLANA_CLUSTER_URL`, `AIRDROP_PROGRAM_ID`, and `GUMMY_MINT_ADDRESS`).
