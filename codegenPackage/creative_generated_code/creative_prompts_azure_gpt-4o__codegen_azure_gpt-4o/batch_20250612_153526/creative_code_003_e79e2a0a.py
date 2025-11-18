"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asd-45l.pages.dev
Prompt: Provide an example of using the Onramp Kit to implement fiat-to-crypto payments via Stripe in a web3 application.
Generated: DETERMINISTIC_e79e2a0a003532b6
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example implementation of fiat-to-crypto payments using Onramp Kit and Stripe in a web3 application.
 * 
 * This code assumes you have `@stripe/stripe-js`, `@web3modal/react`, and `@onramp-kit/core` packages installed.
 * Additionally, it assumes you have Stripe account credentials and a backend server set up for handling Stripe Payment Intents.
 */

// Import required modules
import React, { useState } from 'react';
import { loadStripe } from '@stripe/stripe-js'; // Stripe.js for client-side integration
import { Web3Modal } from '@web3modal/react'; // Web3Modal for wallet connection
import { createOnrampSession } from '@onramp-kit/core'; // Onramp Kit for crypto purchase session creation

// Load Stripe instance with your public key
const stripePromise = loadStripe('your-stripe-public-key'); // Replace with your actual public key

/**
 * Main React component for fiat-to-crypto payments
 */
const FiatToCryptoPayments = () => {
  const [walletAddress, setWalletAddress] = useState(null);
  const [paymentIntentId, setPaymentIntentId] = useState(null);
  const [cryptoAmount, setCryptoAmount] = useState('');
  const [loading, setLoading] = useState(false);

  /**
   * Handler to connect the user's wallet
   */
  const connectWallet = async () => {
    try {
      const web3Modal = new Web3Modal();
      const provider = await web3Modal.connect();
      const accounts = await provider.request({ method: 'eth_accounts' });
      setWalletAddress(accounts[0]); // Set the connected wallet address
    } catch (error) {
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  /**
   * Handler to initiate the payment process
   */
  const handlePayment = async () => {
    if (!walletAddress) {
      alert('Please connect your wallet first.');
      return;
    }

    if (!cryptoAmount || isNaN(cryptoAmount) || parseFloat(cryptoAmount) <= 0) {
      alert('Please enter a valid crypto amount.');
      return;
    }

    setLoading(true);

    try {
      // Step 1: Create a Stripe Payment Intent via your backend
      const response = await fetch('/create-payment-intent', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount: cryptoAmount, walletAddress }),
      });

      if (!response.ok) {
        throw new Error('Failed to create payment intent.');
      }

      const { paymentIntentId: intentId, clientSecret } = await response.json();
      setPaymentIntentId(intentId);

      // Step 2: Redirect user to Stripe checkout or use Stripe Elements
      const stripe = await stripePromise;
      const result = await stripe.confirmCardPayment(clientSecret);

      if (result.error) {
        throw new Error(result.error.message);
      }

      // Step 3: Use Onramp Kit to create a crypto purchase session
      const onrampSession = await createOnrampSession({
        walletAddress,
        paymentIntentId: intentId,
      });

      console.log('Onramp session created:', onrampSession);
      alert('Payment successful! Crypto will be delivered to your wallet.');
    } catch (error) {
      console.error('Error during payment:', error);
      alert('Payment failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Fiat-to-Crypto Payment</h1>
      <p>
        Wallet Address: <strong>{walletAddress || 'Not connected'}</strong>
      </p>
      <button onClick={connectWallet} disabled={loading}>
        {walletAddress ? 'Wallet Connected' : 'Connect Wallet'}
      </button>
      <div>
        <label htmlFor="cryptoAmount">Crypto Amount:</label>
        <input
          type="number"
          id="cryptoAmount"
          value={cryptoAmount}
          onChange={(e) => setCryptoAmount(e.target.value)}
          disabled={loading}
        />
      </div>
      <button onClick={handlePayment} disabled={loading}>
        {loading ? 'Processing...' : 'Buy Crypto'}
      </button>
    </div>
  );
};

export default FiatToCryptoPayments;
```

**Backend Node.js Example for Stripe Payment Intent Creation:**
```javascript
/**
 * Simple Express.js backend for handling Stripe Payment Intent creation.
 */

const express = require('express');
const bodyParser = require('body-parser');
const Stripe = require('stripe');
const cors = require('cors');

// Initialize Stripe with your secret key
const stripe = new Stripe('your-stripe-secret-key'); // Replace with your actual secret key

const app = express();
app.use(cors());
app.use(bodyParser.json()); // Parse JSON requests

/**
 * Endpoint to create a Stripe Payment Intent
 */
app.post('/create-payment-intent', async (req, res) => {
  try {
    const { amount, walletAddress } = req.body;

    if (!amount || !walletAddress) {
      return res.status(400).send('Amount and wallet address are required.');
    }

    // Convert amount to smallest currency unit (e.g., cents for USD)
    const convertedAmount = Math.round(parseFloat(amount) * 100);

    // Create a Payment Intent
    const paymentIntent = await stripe.paymentIntents.create({
      amount: convertedAmount,
      currency: 'usd',
      metadata: { walletAddress }, // Attach wallet address for tracking
    });

    res.status(200).json({
      paymentIntentId: paymentIntent.id,
      clientSecret: paymentIntent.client_secret,
    });
  } catch (error) {
    console.error('Error creating payment intent:', error);
    res.status(500).send('Failed to create payment intent.');
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

**Notes:**
- Replace `your-stripe-public-key` and `your-stripe-secret-key` with your actual Stripe keys.
- Ensure your backend server is secured and properly configured for production with HTTPS and environment variables.
- Test thoroughly in both development and production environments before deployment.
