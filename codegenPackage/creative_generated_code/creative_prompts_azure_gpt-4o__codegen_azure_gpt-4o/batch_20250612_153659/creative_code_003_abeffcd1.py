"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helripairdrop.web.app
Prompt: Create a Solana-based payment gateway that supports QR code scanning and ensures funds are sent directly to the merchant, as described in Helio's platform.
Generated: DETERMINISTIC_abeffcd1676e84b0
Batch ID: 20250612_153659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
// Import necessary libraries
const { Connection, PublicKey, Keypair, Transaction, SystemProgram } = require("@solana/web3.js");
const QRCode = require("qrcode");

// Constants
const SOLANA_NETWORK = "https://api.mainnet-beta.solana.com"; // Solana Mainnet Endpoint
const MERCHANT_PUBLIC_KEY = "your_merchant_public_key_here"; // Replace with merchant's Solana wallet address
const PAYMENT_AMOUNT = 0.01; // Amount in SOL to transfer per transaction

/**
 * Initializes the Solana connection.
 * @returns {Connection} Solana blockchain connection instance.
 */
function initializeConnection() {
  return new Connection(SOLANA_NETWORK, "confirmed");
}

/**
 * Generates a QR code for the payment transaction.
 * @param {string} merchantAddress Merchant's Solana public address.
 * @param {number} amount Payment amount in SOL.
 * @returns {Promise<string>} A string representation of the generated QR code.
 */
async function generateQRCode(merchantAddress, amount) {
  try {
    const paymentURI = `solana:${merchantAddress}?amount=${amount}`;
    return await QRCode.toDataURL(paymentURI);
  } catch (error) {
    throw new Error(`Failed to generate QR Code: ${error.message}`);
  }
}

/**
 * Processes a payment transaction.
 * @param {Connection} connection Solana blockchain connection instance.
 * @param {Keypair} payer Wallet of the person making the payment (payer).
 * @param {string} merchantAddress Merchant's Solana public address.
 * @param {number} amount Payment amount in SOL.
 * @returns {Promise<string>} Transaction ID of the completed transaction.
 */
async function processPayment(connection, payer, merchantAddress, amount) {
  try {
    const merchantPubKey = new PublicKey(merchantAddress);

    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: payer.publicKey,
        toPubkey: merchantPubKey,
        lamports: amount * 1000000000, // Convert SOL to lamports (1 SOL = 10^9 lamports)
      })
    );

    const signature = await connection.sendTransaction(transaction, [payer]);
    await connection.confirmTransaction(signature, "confirmed");

    return signature;
  } catch (error) {
    throw new Error(`Payment failed: ${error.message}`);
  }
}

// Example usage (ensure Keypair is securely managed in production)
(async () => {
  try {
    const connection = initializeConnection();

    // Replace with actual payer Keypair (e.g., loaded from environment variables or a secure wallet manager)
    const payer = Keypair.generate();

    // Generate QR Code for payment
    const qrCodeData = await generateQRCode(MERCHANT_PUBLIC_KEY, PAYMENT_AMOUNT);
    console.log("Generated QR Code:", qrCodeData);

    // Process payment (this should be triggered after the payer scans the QR and confirms)
    const transactionId = await processPayment(connection, payer, MERCHANT_PUBLIC_KEY, PAYMENT_AMOUNT);
    console.log("Payment Successful! Transaction ID:", transactionId);
  } catch (error) {
    console.error("Error:", error.message);
  }
})();
```

**Note:** Replace `your_merchant_public_key_here` with the merchant's actual Solana wallet address.
