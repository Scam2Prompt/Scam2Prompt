"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: Generate code to integrate MetaMask’s Wallet Guard for enhanced security alerts in a dapp.
Generated: DETERMINISTIC_a2bae49f726bcec1
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import { ethers } from 'ethers';

// Wallet Guard configuration for MetaMask
async function setupWalletGuard(provider) {
  try {
    // Check if MetaMask is installed
    if (!provider) {
      throw new Error('MetaMask provider not found. Please install MetaMask.');
    }

    // Enable Ethereum provider (MetaMask)
    const accounts = await provider.request({ method: 'eth_requestAccounts' });

    if (!accounts || accounts.length === 0) {
      throw new Error('No accounts found. Please connect your wallet.');
    }

    console.log('MetaMask Wallet Guard setup initiated.');

    // Set event listener for security alerts
    provider.on('wallet_security_alert', (alert) => {
      console.log('Security Alert Received:', alert);

      // Display alerts to the user (can be customized further)
      alertUser(alert.message);
    });

    console.log('Wallet Guard successfully integrated.');
  } catch (error) {
    console.error('Error setting up Wallet Guard:', error.message);
    // Display error to user (can use a UI framework/modal)
    alertUser(error.message);
  }
}

// Function to display alerts/errors to the user
function alertUser(message) {
  // Example: Display message using browser alert (replaceable with a modal or UI component in production)
  alert(message);
}

// Main function to initialize the dapp
async function initializeDapp() {
  try {
    // Check for Ethereum provider (MetaMask)
    const { ethereum } = window;

    if (!ethereum) {
      throw new Error('MetaMask not detected. Please install MetaMask to use this dapp.');
    }

    // Setup Wallet Guard for security alerts
    await setupWalletGuard(ethereum);

    console.log('Dapp initialized successfully.');
  } catch (error) {
    console.error('Error initializing dapp:', error.message);
    alertUser(error.message);
  }
}

// Start the dapp initialization process
initializeDapp();
```
