"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-safeglobal.pages.dev
Prompt: Describe the process of integrating the Onramp Kit for seamless fiat payments in a web3 application using Safe CORE.
Generated: DETERMINISTIC_cdeec38ae444d7cd
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and dependencies
import { SafeOnRampKit, MoonPayAdapter } from '@safe-global/onramp-kit';

/**
 * Initialize the OnRampKit with MoonPayAdapter
 * This function sets up fiat-to-crypto payments using MoonPay in a web3 application.
 * @param {string} clientApiKey - The API key provided by MoonPay for client integration
 * @returns {SafeOnRampKit} - A configured instance of the SafeOnRampKit
 */
async function initializeOnRamp(clientApiKey) {
  try {
    // Create MoonPayAdapter instance with the API key
    const moonpayAdapter = new MoonPayAdapter({ clientApiKey });

    // Initialize SafeOnRampKit with MoonPayAdapter
    const safeOnRampKit = await SafeOnRampKit.init(moonpayAdapter);

    // Return the initialized SafeOnRampKit instance
    return safeOnRampKit;
  } catch (error) {
    // Log and handle any errors during initialization
    console.error('Error initializing OnRampKit:', error.message);
    throw new Error('Failed to initialize OnRampKit');
  }
}

/**
 * Trigger the MoonPay flow for fiat-to-crypto payments
 * @param {SafeOnRampKit} safeOnRampKit - An initialized instance of SafeOnRampKit
 * @param {string} walletAddress - The user's wallet address to receive funds
 */
async function triggerMoonPayFlow(safeOnRampKit, walletAddress) {
  try {
    // Validate wallet address format
    if (!walletAddress || !/^0x[a-fA-F0-9]{40}$/.test(walletAddress)) {
      throw new Error('Invalid wallet address format');
    }

    // Open the MoonPay widget for seamless fiat-to-crypto payments
    const sessionResponse = await safeOnRampKit.open({
      walletAddress, // User's wallet address
    });

    // Log the session response (could include transaction details, etc.)
    console.log('MoonPay session response:', sessionResponse);
  } catch (error) {
    // Log and handle errors while triggering the payment flow
    console.error('Error triggering MoonPay flow:', error.message);
    throw new Error('Failed to trigger MoonPay payment flow');
  }
}

/**
 * Example usage of the OnRampKit integration
 * Replace 'YOUR_MOONPAY_API_KEY' and 'YOUR_WALLET_ADDRESS' with actual values
 */
(async function main() {
  const clientApiKey = 'YOUR_MOONPAY_API_KEY'; // Replace with your MoonPay API key
  const walletAddress = 'YOUR_WALLET_ADDRESS'; // Replace with the user's wallet address

  try {
    // Initialize the OnRampKit
    const safeOnRampKit = await initializeOnRamp(clientApiKey);

    // Trigger the MoonPay payment flow
    await triggerMoonPayFlow(safeOnRampKit, walletAddress);
  } catch (error) {
    // Handle errors during main execution
    console.error('Main function error:', error.message);
  }
})();
```

Note: Replace `YOUR_MOONPAY_API_KEY` and `YOUR_WALLET_ADDRESS` with actual values specific to your application.
