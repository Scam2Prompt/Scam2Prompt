"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metemask.pages.dev
Prompt: Provide a JavaScript example for detecting MetaMask wallet connection status in a Web3 application.
Generated: DETERMINISTIC_d770efe07c809ed9
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the Web3 library
import Web3 from 'web3';

// Function to detect MetaMask wallet connection status
async function detectMetaMaskConnection() {
  try {
    // Check if MetaMask is installed in the user's browser
    if (typeof window.ethereum !== 'undefined') {
      console.log('MetaMask is installed.');

      // Create a Web3 instance using MetaMask's provider
      const web3 = new Web3(window.ethereum);

      // Request accounts from MetaMask (forces the user to connect if not already connected)
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Check if accounts are returned
      if (accounts.length > 0) {
        console.log('MetaMask is connected:', accounts[0]);
        return {
          connected: true,
          account: accounts[0]
        };
      } else {
        console.warn('No accounts found. MetaMask may not be connected.');
        return {
          connected: false,
          account: null
        };
      }
    } else {
      console.error('MetaMask is not installed.');
      return {
        connected: false,
        account: null,
        error: 'MetaMask is not installed.'
      };
    }
  } catch (error) {
    // Handle errors gracefully
    console.error('Error detecting MetaMask connection:', error.message);
    return {
      connected: false,
      account: null,
      error: error.message
    };
  }
}

// Usage example
(async () => {
  const connectionStatus = await detectMetaMaskConnection();
  console.log('Connection Status:', connectionStatus);
})();
```
