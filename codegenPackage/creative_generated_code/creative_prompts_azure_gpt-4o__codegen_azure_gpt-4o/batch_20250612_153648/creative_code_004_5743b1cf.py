"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solanax-novocaine1926.vercel.app
Prompt: Create a Solana-powered application that enables users to upload and update token metadata using the Scaffold framework.
Generated: DETERMINISTIC_5743b1cf2c0e0dd2
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: app.js
// Description: Solana-powered application to upload and update token metadata using Scaffold framework.
// Pre-requisites: Install dependencies using `npm install @solana/web3.js @solana/spl-token @solana/spl-token-metadata`.

const express = require('express'); // Web framework for REST API
const bodyParser = require('body-parser'); // Middleware to parse JSON requests
const { Connection, PublicKey, Keypair } = require('@solana/web3.js'); // Solana's Web3 library
const { createMetadataAccount } = require('@solana/spl-token-metadata'); // Metadata management
const fs = require('fs'); // For reading secrets and key files

const app = express();
app.use(bodyParser.json());

// Load environment variables (e.g., Solana cluster URL and secret keys)
// Ensure the environment variables are set in a `.env` file or process environment.
const connection = new Connection(process.env.SOLANA_CLUSTER_URL, 'confirmed'); // Solana RPC connection
const secretKey = Uint8Array.from(JSON.parse(fs.readFileSync('./wallet.json'))); // Path to wallet keypair
const wallet = Keypair.fromSecretKey(secretKey); // Wallet keypair

// Endpoint: Upload Token Metadata
app.post('/upload-metadata', async (req, res) => {
  try {
    const { tokenMintAddress, metadata } = req.body;

    // Input validation
    if (!tokenMintAddress || !metadata) {
      return res.status(400).json({ error: 'Token mint address and metadata are required.' });
    }

    // Parse token mint address
    const mintPublicKey = new PublicKey(tokenMintAddress);

    // Create metadata account for the token
    const metadataTransaction = await createMetadataAccount(
      connection,
      wallet.publicKey,
      wallet,
      mintPublicKey,
      metadata
    );

    // Send transaction
    const transactionSignature = await connection.sendTransaction(metadataTransaction, [wallet], {
      skipPreflight: true,
    });

    // Confirm transaction
    await connection.confirmTransaction(transactionSignature);

    res.status(200).json({
      message: 'Metadata uploaded successfully.',
      transactionSignature: transactionSignature,
      metadata: metadata,
    });
  } catch (error) {
    console.error('Error uploading metadata:', error);
    res.status(500).json({ error: 'Failed to upload metadata.' });
  }
});

// Endpoint: Update Token Metadata
app.put('/update-metadata', async (req, res) => {
  try {
    const { tokenMintAddress, updatedMetadata } = req.body;

    // Input validation
    if (!tokenMintAddress || !updatedMetadata) {
      return res.status(400).json({ error: 'Token mint address and updated metadata are required.' });
    }

    // Parse token mint address
    const mintPublicKey = new PublicKey(tokenMintAddress);

    // Update metadata account
    const metadataTransaction = await createMetadataAccount(
      connection, // Solana connection
      wallet.publicKey, // Wallet public key
      wallet, // Wallet Keypair
      mintPublicKey, // Token mint address
      updatedMetadata // New metadata
    );

    // Send transaction
    const transactionSignature = await connection.sendTransaction(metadataTransaction, [wallet], {
      skipPreflight: true,
    });

    // Confirm transaction
    await connection.confirmTransaction(transactionSignature);

    res.status(200).json({
      message: 'Metadata updated successfully.',
      transactionSignature: transactionSignature,
      updatedMetadata: updatedMetadata,
    });
  } catch (error) {
    console.error('Error updating metadata:', error);
    res.status(500).json({ error: 'Failed to update metadata.' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
 * Notes:
 * 1. The `createMetadataAccount` function is assumed to handle both creation and updating of metadata.
 *    You might need to customize this depending on the actual Solana SPL Metadata library implementation.
 * 2. Always keep your wallet secret key (`wallet.json`) secure. Avoid exposing it publicly.
 * 3. The application assumes the correct metadata format as per Solana's SPL Metadata standard.
 */
```
