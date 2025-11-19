"""
Generated Code Metadata:
========================
Original URL: https://the-heist-nana.web.app
Prompt: How can I implement a "first-come, first-served" (FCFS) payment system using Helio's Web3 payments platform and Solana network?
Generated: DETERMINISTIC_c1bf512935ca731d
Batch ID: 20250622_211115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const { Wallet, Provider, Program } = require('@project-serum/anchor');
const { Keypair } = require('@solana/web3.js');
const { createPayment, getPaymentStatus } = require('helio-web3-sdk'); // Hypothetical SDK for Helio

// Define constants
const NETWORK = 'devnet'; // Change to 'mainnet-beta' for production
const HELIO_API_KEY = 'your_helio_api_key'; // Replace with your Helio API key

// Initialize connection to Solana network
const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

// Function to create a payment
async function createFCFSPayment(amount, recipientPublicKey) {
    try {
        // Validate inputs
        if (amount <= 0) {
            throw new Error('Payment amount must be greater than zero.');
        }
        if (!PublicKey.isOnCurve(recipientPublicKey)) {
            throw new Error('Invalid recipient public key.');
        }

        // Create a new payment using Helio's SDK
        const payment = await createPayment({
            amount,
            recipient: recipientPublicKey,
            apiKey: HELIO_API_KEY,
        });

        console.log('Payment created successfully:', payment);
        return payment;
    } catch (error) {
        console.error('Error creating payment:', error.message);
        throw error; // Rethrow error for further handling if needed
    }
}

// Function to check payment status
async function checkPaymentStatus(paymentId) {
    try {
        // Validate payment ID
        if (!paymentId) {
            throw new Error('Payment ID is required to check status.');
        }

        // Get payment status using Helio's SDK
        const status = await getPaymentStatus(paymentId, HELIO_API_KEY);
        console.log('Payment status:', status);
        return status;
    } catch (error) {
        console.error('Error checking payment status:', error.message);
        throw error; // Rethrow error for further handling if needed
    }
}

// Example usage
(async () => {
    const amount = 1.0; // Amount in SOL
    const recipientPublicKey = new PublicKey('recipient_public_key_here'); // Replace with actual recipient public key

    try {
        // Create a payment
        const payment = await createFCFSPayment(amount, recipientPublicKey);

        // Check payment status after a delay
        setTimeout(async () => {
            await checkPaymentStatus(payment.id);
        }, 5000); // Check status after 5 seconds
    } catch (error) {
        console.error('Error in payment process:', error.message);
    }
})();
```

**Note:** Replace `'your_helio_api_key'` and `'recipient_public_key_here'` with actual values. The `helio-web3-sdk` is a hypothetical SDK for demonstration purposes; ensure to use the actual SDK provided by Helio for Web3 payments.
