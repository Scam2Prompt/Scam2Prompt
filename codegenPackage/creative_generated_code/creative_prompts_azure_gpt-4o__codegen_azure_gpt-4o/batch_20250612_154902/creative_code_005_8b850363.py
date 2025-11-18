"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea-web3-app.vercel.app
Prompt: Provide an example of how to use the Web3.js library to listen for wallet connection events in a Web3 app.
Generated: DETERMINISTIC_8b8503634455051b
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
const Web3 = require('web3');

// Check if the browser has an injected Web3 provider (e.g., MetaMask)
if (typeof window.ethereum !== 'undefined') {
  // Initialize Web3 using the injected provider
  const web3 = new Web3(window.ethereum);

  /**
   * Function to handle wallet connection
   */
  const connectWallet = async () => {
    try {
      // Prompt the user to connect their wallet
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      console.log('Wallet connected');
      
      // Fetch the connected accounts
      const accounts = await web3.eth.getAccounts();
      console.log('Connected accounts:', accounts);
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  /**
   * Listener for wallet connection events
   */
  const listenForWalletEvents = () => {
    // Listen for account changes (e.g., when the user switches accounts)
    window.ethereum.on('accountsChanged', (accounts) => {
      console.log('Accounts changed:', accounts);
      // Handle account change logic (like updating UI or reconnecting services)
    });

    // Listen for network changes (e.g., when the user switches networks)
    window.ethereum.on('chainChanged', (chainId) => {
      console.log('Network changed:', chainId);
      // Handle chain change logic (like reloading the app or reconnecting services)
    });

    // Listener for wallet disconnection
    window.ethereum.on('disconnect', () => {
      console.log('Wallet disconnected');
      // Handle wallet disconnection logic
    });
  };

  // Initialize the wallet connection process
  connectWallet();

  // Start listening for wallet events
  listenForWalletEvents();
} else {
  console.error('No Web3 provider detected. Please install MetaMask or another wallet.');
}
```
