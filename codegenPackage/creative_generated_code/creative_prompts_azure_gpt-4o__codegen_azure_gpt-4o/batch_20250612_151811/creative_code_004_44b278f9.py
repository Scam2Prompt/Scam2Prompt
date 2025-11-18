"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain-web3.com
Prompt: Provide a code example for initializing a Web3 provider in a dApp using JavaScript.
Generated: DETERMINISTIC_44b278f9f1553488
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3 library
import Web3 from 'web3';

/**
 * Initializes a Web3 provider for a decentralized application (dApp).
 * @returns {Promise<Web3>} Instance of Web3 connected to the provider.
 * @throws Will throw an error if no Web3 provider is found.
 */
async function initializeWeb3Provider() {
  try {
    // Check if the browser has an Ethereum provider injected (e.g., MetaMask)
    if (window.ethereum) {
      // Use the browser's injected Ethereum provider
      const provider = window.ethereum;

      // Request permission to access the user's accounts
      await provider.request({ method: 'eth_requestAccounts' });

      // Initialize Web3 with the provider
      const web3 = new Web3(provider);

      console.log('Web3 provider initialized successfully.');
      return web3;
    } else if (window.web3) {
      // Legacy Web3 provider detection (e.g., older versions of MetaMask)
      console.warn('Legacy Web3 detected. Consider upgrading.');
      const web3 = new Web3(window.web3.currentProvider);

      console.log('Web3 provider initialized successfully.');
      return web3;
    } else {
      // No Web3 provider found
      throw new Error(
        'No Ethereum browser extension detected. Please install MetaMask or another wallet.'
      );
    }
  } catch (error) {
    console.error('Failed to initialize Web3 provider:', error);
    throw error; // Rethrow the error for handling downstream
  }
}

// Example usage
(async () => {
  try {
    const web3 = await initializeWeb3Provider();

    // Perform any Web3 operations after initialization
    console.log('Connected to Ethereum network:', await web3.eth.net.getId());
  } catch (error) {
    console.error('Error during Web3 initialization:', error.message);
  }
})();
```
