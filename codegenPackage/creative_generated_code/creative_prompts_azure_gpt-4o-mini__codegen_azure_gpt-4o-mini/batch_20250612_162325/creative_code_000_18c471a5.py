"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edrfrtertertertc.web.app
Prompt: Generate a code snippet for integrating Helio's Web3 payment platform using the Solana network for a decentralized application.
Generated: DETERMINISTIC_18c471a5458b06f3
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { HelioPayment } from '@helio/web3-sdk'; // Assuming Helio SDK is available

// Constants for Solana network and Helio configuration
const SOLANA_NETWORK = 'mainnet-beta'; // Change to 'devnet' for testing
const HELIO_API_KEY = 'YOUR_HELIO_API_KEY'; // Replace with your actual API key

// Initialize connection to Solana network
const connection = new Connection(clusterApiUrl(SOLANA_NETWORK), 'confirmed');

// Initialize Helio payment with the provided API key
const helioPayment = new HelioPayment(HELIO_API_KEY);

// Function to create a payment request
async function createPaymentRequest(amount, recipientAddress) {
    try {
        // Validate input parameters
        if (!amount || amount <= 0) {
            throw new Error('Invalid payment amount. It must be greater than zero.');
        }
        if (!PublicKey.isOnCurve(recipientAddress)) {
            throw new Error('Invalid recipient address.');
        }

        // Create a payment request using the Helio API
        const paymentRequest = await helioPayment.createPayment({
            amount,
            currency: 'SOL', // Currency in SOL
            recipient: recipientAddress,
        });

        // Return the payment request details
        return paymentRequest;
    } catch (error) {
        console.error('Error creating payment request:', error);
        throw new Error('Failed to create payment request. Please try again later.');
    }
}

// Function to check payment status
async function checkPaymentStatus(transactionId) {
    try {
        // Retrieve payment status from Helio API
        const status = await helioPayment.getPaymentStatus(transactionId);

        // Return the payment status details
        return status;
    } catch (error) {
        console.error('Error checking payment status:', error);
        throw new Error('Failed to retrieve payment status. Please try again later.');
    }
}

// Example usage
(async () => {
    const recipient = 'RecipientPublicKeyHere'; // Replace with the actual recipient's public key
    const amount = 0.1; // Amount in SOL

    try {
        const paymentRequest = await createPaymentRequest(amount, recipient);
        console.log('Payment request created:', paymentRequest);

        // You can store paymentRequest.id and check its status later
        const paymentStatus = await checkPaymentStatus(paymentRequest.id);
        console.log('Payment status:', paymentStatus);
    } catch (error) {
        console.error('Error during payment process:', error.message);
    }
})();
```

**Note:** Ensure to replace `YOUR_HELIO_API_KEY` and `RecipientPublicKeyHere` with actual values before running the code. The Helio SDK implementation should be referenced from its documentation for accurate usage.
