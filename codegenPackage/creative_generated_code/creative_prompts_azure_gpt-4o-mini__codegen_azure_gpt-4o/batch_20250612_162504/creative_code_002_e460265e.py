"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solmeme-io.pages.dev
Prompt: What are the steps to integrate Solana Pay for immediate USDC transactions in a Shopify app?
Generated: DETERMINISTIC_e460265ed9784fe0
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation of integrating Solana Pay for immediate USDC transactions in a Shopify app. This assumes a Node.js + Express backend and the Solana Pay SDK:

```javascript
// Dependencies
const express = require('express');
const { Keypair, Connection, clusterApiUrl, PublicKey } = require('@solana/web3.js');
const { encodeURL } = require('@solana/pay');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Solana Configuration
const SOLANA_NETWORK = 'mainnet-beta'; // Use 'devnet' for testing
const USDC_MINT_ADDRESS = new PublicKey('Es9vMFrzaCxdjhfybKrxn3LeG8cFRZ5i7E7zL2Xq7iV'); // USDC Mint Address
const MERCHANT_PUBLIC_KEY = new PublicKey('<Your Merchant Wallet Address>'); // Replace with your wallet address
const connection = new Connection(clusterApiUrl(SOLANA_NETWORK));

// Endpoint to generate Solana Pay payment link
app.post('/generate-solana-pay-link', async (req, res) => {
    try {
        const { amount, shopifyOrderId } = req.body;

        // Validate input
        if (!amount || isNaN(amount)) {
            return res.status(400).json({ error: 'Invalid amount provided.' });
        }
        if (!shopifyOrderId) {
            return res.status(400).json({ error: 'Shopify Order ID is required.' });
        }

        // Create payment URL
        const paymentDetails = {
            recipient: MERCHANT_PUBLIC_KEY, // Merchant wallet address
            mint: USDC_MINT_ADDRESS,       // Specify USDC as the token
            amount,                        // Payment amount in USDC
            reference: Keypair.generate().publicKey, // Unique reference for transaction (can track orders)
            label: 'Shopify Payment',      // Label for the transaction
            message: `Payment for order #${shopifyOrderId}` // Message for the transaction
        };

        const paymentURL = encodeURL(paymentDetails);

        // Respond with the Solana Pay link
        res.status(200).json({ solanaPayLink: paymentURL });
    } catch (error) {
        console.error('Error generating Solana Pay link:', error);
        res.status(500).json({ error: 'Failed to generate Solana Pay link.' });
    }
});

// Endpoint to validate Solana payment
app.post('/validate-solana-payment', async (req, res) => {
    try {
        const { shopifyOrderId, transactionSignature } = req.body;

        // Validate input
        if (!shopifyOrderId) {
            return res.status(400).json({ error: 'Shopify Order ID is required.' });
        }
        if (!transactionSignature) {
            return res.status(400).json({ error: 'Transaction signature is required.' });
        }

        // Fetch transaction details from Solana
        const transaction = await connection.getTransaction(transactionSignature, { commitment: 'confirmed' });

        // Check if transaction exists
        if (!transaction) {
            return res.status(404).json({ error: 'Transaction not found.' });
        }

        // Validate transaction recipient, mint, and amount
        const instruction = transaction.transaction.message.instructions.find(inst => inst.programId.equals(new PublicKey('TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA')));
        if (!instruction) {
            return res.status(400).json({ error: 'No valid token transfer instruction found.' });
        }

        const transactionRecipient = instruction.keys[1].pubkey;
        const transactionMint = instruction.keys[2].pubkey;
        const transactionAmount = instruction.data.readUIntLE(0); // Amount in smallest denomination (lamports)

        if (!transactionRecipient.equals(MERCHANT_PUBLIC_KEY)) {
            return res.status(400).json({ error: 'Payment was not made to the correct recipient.' });
        }
        if (!transactionMint.equals(USDC_MINT_ADDRESS)) {
            return res.status(400).json({ error: 'Payment was not in USDC.' });
        }
        if (transactionAmount !== amount * (10 ** 6)) { // Convert USDC to lamports
            return res.status(400).json({ error: 'Incorrect payment amount.' });
        }

        // Payment is valid
        res.status(200).json({ success: true, message: 'Payment validated successfully.' });
    } catch (error) {
        console.error('Error validating Solana payment:', error);
        res.status(500).json({ error: 'Failed to validate payment.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Replace `<Your Merchant Wallet Address>` with your Solana wallet public key.
- Use `clusterApiUrl('devnet')` for testing purposes.
- Ensure you install necessary dependencies: `npm install express @solana/web3.js @solana/pay body-parser`.
- Use HTTPS for secure communication when deploying.
