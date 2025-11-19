"""
Generated Code Metadata:
========================
Original URL: https://widget-builder-ef3hbs3sz-superfluid-finance.vercel.app
Prompt: Write code to integrate the Superfluid Checkout Builder into a Web3 subscription platform, ensuring payment details are defined and exported in the provided format.
Generated: DETERMINISTIC_96d886d124c7e81e
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { SuperfluidCheckout } from '@superfluid-finance/checkout';
const Web3 = require('web3');

// Define constants for Superfluid Checkout and Web3
const SUPERFLUID_CHECKOUT_API_KEY = 'YOUR_SUPERFLUID_CHECKOUT_API_KEY';
const WEB3_PROVIDER_URL = 'YOUR_WEB3_PROVIDER_URL';

// Initialize Superfluid Checkout and Web3
const superfluidCheckout = new SuperfluidCheckout({
  apiKey: SUPERFLUID_CHECKOUT_API_KEY,
});

// Initialize Web3 provider
const web3 = new Web3(new Web3.providers.HttpProvider(WEB3_PROVIDER_URL));

// Define function to create subscription
async function createSubscription(subscriptionDetails) {
  try {
    // Validate subscription details
    if (!subscriptionDetails || !subscriptionDetails.paymentDetails) {
      throw new Error('Invalid subscription details');
    }

    const { paymentDetails } = subscriptionDetails;

    // Validate payment details
    if (!paymentDetails || !paymentDetails.chainId || !paymentDetails.tokenAddress) {
      throw new Error('Invalid payment details');
    }

    // Create Superfluid Checkout session
    const session = await superfluidCheckout.createSession({
      paymentDetails: {
        chainId: paymentDetails.chainId,
        tokenAddress: paymentDetails.tokenAddress,
        paymentMethod: paymentDetails.paymentMethod,
      },
    });

    // Get subscription details
    const subscription = await session.getSubscription();

    // Export subscription details in the required format
    return {
      subscriptionId: subscription.id,
      paymentDetails: {
        chainId: paymentDetails.chainId,
        tokenAddress: paymentDetails.tokenAddress,
        paymentMethod: paymentDetails.paymentMethod,
      },
    };
  } catch (error) {
    console.error('Error creating subscription:', error);
    throw error;
  }
}

// Define function to get subscription status
async function getSubscriptionStatus(subscriptionId) {
  try {
    // Get Superfluid Checkout session
    const session = await superfluidCheckout.getSession(subscriptionId);

    // Get subscription status
    const subscriptionStatus = await session.getSubscriptionStatus();

    return subscriptionStatus;
  } catch (error) {
    console.error('Error getting subscription status:', error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    // Define subscription details
    const subscriptionDetails = {
      paymentDetails: {
        chainId: 1, // Ethereum mainnet
        tokenAddress: '0x...', // Token address
        paymentMethod: 'erc-20', // Payment method
      },
    };

    // Create subscription
    const subscription = await createSubscription(subscriptionDetails);
    console.log('Subscription created:', subscription);

    // Get subscription status
    const subscriptionStatus = await getSubscriptionStatus(subscription.subscriptionId);
    console.log('Subscription status:', subscriptionStatus);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
