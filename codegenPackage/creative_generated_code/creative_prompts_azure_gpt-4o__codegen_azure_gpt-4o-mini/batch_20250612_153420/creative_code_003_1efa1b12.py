"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safergf.pages.dev
Prompt: Demonstrate how to use the Onramp Kit from Safe CORE to enable fiat payments via Stripe for Ethereum smart account funding.
Generated: DETERMINISTIC_1efa1b1241bdd712
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Stripe and Safe CORE SDK
const { SafeFactory, SafeAccountConfig } = require('@safe-global/protocol-kit');
const Stripe = require('stripe');
const express = require('express');

// Initialize Express app
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Initialize Stripe with your secret key
const stripe = new Stripe('YOUR_STRIPE_SECRET_KEY');

// Create a Safe account
async function createSafeAccount() {
    const safeFactory = await SafeFactory.create({ ethersProvider: YOUR_ETHEREUM_PROVIDER });
    const safeAccountConfig = {
        owners: ['YOUR_ETHEREUM_ADDRESS'], // Replace with your Ethereum address
        threshold: 1, // Set the threshold for transactions
    };

    try {
        const safeAccount = await safeFactory.deploySafe(safeAccountConfig);
        console.log(`Safe account created: ${safeAccount.getAddress()}`);
        return safeAccount;
    } catch (error) {
        console.error('Error creating Safe account:', error);
        throw new Error('Failed to create Safe account');
    }
}

// Endpoint to create a payment intent
app.post('/create-payment-intent', async (req, res) => {
    const { amount, currency } = req.body;

    // Validate input
    if (!amount || !currency) {
        return res.status(400).json({ error: 'Amount and currency are required' });
    }

    try {
        // Create a payment intent with Stripe
        const paymentIntent = await stripe.paymentIntents.create({
            amount,
            currency,
            payment_method_types: ['card'],
        });
        // Respond with the client secret to confirm the payment
        res.json({ clientSecret: paymentIntent.client_secret });
    } catch (error) {
        console.error('Error creating payment intent:', error);
        res.status(500).json({ error: 'Failed to create payment intent' });
    }
});

// Endpoint to fund the Safe account (mock implementation)
app.post('/fund-safe-account', async (req, res) => {
    const { safeAddress, amount } = req.body;

    // Validate input
    if (!safeAddress || !amount) {
        return res.status(400).json({ error: 'Safe address and amount are required' });
    }

    try {
        // Here you would implement logic to transfer funds to the Safe account
        // For demonstration, we assume the funds were transferred successfully
        console.log(`Funding Safe account ${safeAddress} with amount ${amount}`);
        res.json({ message: 'Funding successful' });
    } catch (error) {
        console.error('Error funding Safe account:', error);
        res.status(500).json({ error: 'Failed to fund Safe account' });
    }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Call the createSafeAccount function to create a Safe account on startup
createSafeAccount().catch(error => {
    console.error('Failed to initialize Safe account:', error);
});
```
