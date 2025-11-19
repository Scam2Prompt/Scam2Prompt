"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-coinbase-com.kagiproxy.com
Prompt: Draft a JavaScript example that shows how to implement a fiat-to-crypto solution using Coinbase's Onramp service.
Generated: DETERMINISTIC_b0c12eee918cbd57
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Example implementation of a fiat-to-crypto solution using Coinbase's Onramp service

// Ensure you have imported and included the Coinbase Onramp SDK in your project.
// Installation: npm install @coinbase/onramp

// Import the Coinbase Onramp module
import { CoinbaseOnramp } from '@coinbase/onramp';

// Initialize the Onramp SDK
const initializeOnramp = async () => {
  try {
    // Configuration settings for Onramp integration
    const config = {
      clientId: 'your-client-id', // Replace with your Coinbase Client ID
      onSuccess: (transaction) => {
        console.log('Transaction Successful:', transaction);
        // Handle success (e.g., update the UI or database)
      },
      onFailure: (error) => {
        console.error('Transaction Failed:', error);
        // Handle failure (e.g., show an error message to the user)
      },
      onExit: () => {
        console.log('User exited Onramp flow');
        // Handle user exit (e.g., clean up resources or reset state)
      },
    };

    // Create an Onramp instance
    const onrampInstance = await CoinbaseOnramp.create(config);

    return onrampInstance;
  } catch (error) {
    console.error('Error initializing Onramp SDK:', error);
    throw new Error('Could not initialize Coinbase Onramp.');
  }
};

// Function to start the fiat-to-crypto flow
const startOnrampFlow = async () => {
  try {
    // Initialize the Onramp SDK
    const onrampInstance = await initializeOnramp();

    // Launch the Onramp UI for the user
    onrampInstance.open();
  } catch (error) {
    console.error('Error starting Onramp flow:', error);
    alert('Failed to start the fiat-to-crypto transaction flow.');
  }
};

// Event listener to trigger the Onramp flow (e.g., button click)
document.getElementById('start-onramp-btn').addEventListener('click', async () => {
  await startOnrampFlow();
});

// HTML Example for the button (can be included in your HTML file)
/*
<button id="start-onramp-btn">Buy Crypto</button>
*/
```

Make sure to replace `your-client-id` with your actual Coinbase Client ID and handle sensitive data securely.
