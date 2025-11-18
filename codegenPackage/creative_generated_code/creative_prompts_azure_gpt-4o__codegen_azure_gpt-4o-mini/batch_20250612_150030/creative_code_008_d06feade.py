"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: Write code to detect wallet disconnection events using Web3Modal in a decentralized application.
Generated: DETERMINISTIC_d06feadea87b3026
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import Web3Modal from 'web3modal';

// Initialize Web3Modal instance
const web3Modal = new Web3Modal({
  // Configure connection options
  cacheProvider: true, // optional
  providerOptions: {} // Add specific provider options here if needed
});

// Variable to hold the Web3 instance
let web3;

// Function to connect the wallet
async function connectWallet() {
  try {
    // Open wallet connection modal
    const provider = await web3Modal.connect();
    
    // Create a new Web3 instance with the provider
    web3 = new Web3(provider);
    
    // Handle accounts change
    provider.on('accountsChanged', (accounts) => {
      console.log('Accounts changed:', accounts);
      // Implement any logic needed to update the application state
    });

    // Handle network change
    provider.on('chainChanged', (chainId) => {
      console.log('Chain changed:', chainId);
      // Implement any logic needed to update the application state
    });

    // Handle disconnection events
    provider.on('disconnect', (error) => {
      console.error('Disconnected:', error);
      // Implement any logic needed to handle disconnection
    });

  } catch (error) {
    console.error('Failed to connect wallet:', error);
    alert('Could not connect to wallet. Please try again.');
  }
}

// Function to disconnect the wallet
async function disconnectWallet() {
  try {
    // Clear cached provider
    await web3Modal.clearCachedProvider();
    web3 = null; // Set web3 instance to null
    console.log('Wallet disconnected');
  } catch (error) {
    console.error('Failed to disconnect wallet:', error);
    alert('Could not disconnect wallet. Please try again.');
  }
}

// Example usage: connect wallet on button click
document.getElementById('connectButton').addEventListener('click', connectWallet);
document.getElementById('disconnectButton').addEventListener('click', disconnectWallet);
```

Make sure to include HTML for buttons with IDs `connectButton` and `disconnectButton` in your application for this code to function properly.
