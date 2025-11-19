"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-solana-pay-app.vercel.app
Prompt: What libraries are recommended for implementing Solana Pay in a web application focused on meme coin transactions?
Generated: DETERMINISTIC_85bfdca003e34547
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
const { Connection, clusterApiUrl, Keypair } = require('@solana/web3.js'); // Core Solana library
const { encodeURL, createQR } = require('@solana/pay'); // Solana Pay library
const express = require('express'); // Web application framework
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const dotenv = require('dotenv'); // For managing environment variables

// Load environment variables from .env file
dotenv.config();

// Initialize constants
const SOLANA_NETWORK = process.env.SOLANA_NETWORK || 'mainnet-beta'; // Solana network ('devnet', 'testnet', 'mainnet-beta')
const MEME_COIN_MINT_ADDRESS = process.env.MEME_COIN_MINT_ADDRESS; // Meme coin mint address
const MERCHANT_WALLET_PRIVATE_KEY = process.env.MERCHANT_WALLET_PRIVATE_KEY; // Merchant's private key

// Validate environment variables
if (!MEME_COIN_MINT_ADDRESS || !MERCHANT_WALLET_PRIVATE_KEY) {
  throw new Error('Missing required environment variables. Please set MEME_COIN_MINT_ADDRESS and MERCHANT_WALLET_PRIVATE_KEY in your .env file.');
}

// Initialize the merchant wallet from the private key
const merchantWallet = Keypair.fromSecretKey(Uint8Array.from(JSON.parse(MERCHANT_WALLET_PRIVATE_KEY)));

// Initialize Solana connection
const connection = new Connection(clusterApiUrl(SOLANA_NETWORK), 'confirmed');

// Set up Express application
const app = express();
app.use(bodyParser.json()); // Parse JSON request bodies

/**
 * Endpoint to create a Solana Pay transaction URL for meme coin payments
 * Request Body:
 * {
 *   "amount": "number", // Amount of meme coin tokens to be transferred
 *   "memo": "string"    // Optional memo for the transaction
 * }
 * Response:
 * {
 *   "qrCode": "string", // Base64-encoded QR code image
 *   "paymentUrl": "string" // Solana Pay payment URL
 * }
 */
app.post('/create-payment', async (req, res) => {
  try {
    const { amount, memo } = req.body;

    if (!amount || isNaN(amount) || amount <= 0) {
      return res.status(400).json({ error: 'Invalid amount specified.' });
    }

    // Construct the Solana Pay payment URL
    const paymentParams = {
      recipient: merchantWallet.publicKey,
      amount: amount, // Payment amount (in meme coin tokens)
      splToken: MEME_COIN_MINT_ADDRESS, // Address of the meme coin token mint
      memo: memo || undefined, // Optional memo
    };
    const paymentUrl = encodeURL(paymentParams);

    // Generate QR code for the payment URL
    const qrCode = createQR(paymentUrl);

    // Respond with the QR code and payment URL
    res.json({
      qrCode: qrCode._canvas.toDataURL(), // Convert QR code to Base64 string
      paymentUrl: paymentUrl.toString(), // Solana Pay payment URL
    });
  } catch (error) {
    console.error('Error creating payment:', error);
    res.status(500).json({ error: 'Failed to create payment. Please try again later.' });
  }
});

// Start the Express application
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

Please ensure you install the required libraries before running the code using this command:
```bash
npm install @solana/web3.js @solana/pay express body-parser dotenv
```
