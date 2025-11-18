"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brokensea-dapp.pages.dev
Prompt: Create a JavaScript function to check for Web3 provider availability and initialize a connection for a dApp like "Broken Sea."
Generated: DETERMINISTIC_c58525d349520cb3
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Initializes a Web3 connection and checks for provider availability.
 * This function is intended to be used in a dApp like "Broken Sea."
 */

// Import the required dependencies (ensure these are installed in your project)
import Web3 from 'web3';

/**
 * Function to check for Web3 provider availability and initialize a connection
 * @returns {Object} An object containing the Web3 instance and provider details
 */
async function initializeWeb3() {
  try {
    // Check if the browser has an injected Web3 provider (like MetaMask)
    if (typeof window.ethereum !== 'undefined') {
      // Modern dApp browsers
      const provider = window.ethereum;

      // Request user's permission to connect
      await provider.request({ method: 'eth_requestAccounts' });

      // Create a new Web3 instance
      const web3 = new Web3(provider);

      // Return the Web3 instance and provider details
      return {
        web3Instance: web3,
        provider: provider,
        message: 'Web3 provider initialized successfully'
      };
    } else if (typeof window.web3 !== 'undefined') {
      // Legacy dApp browsers
      const provider = window.web3.currentProvider;

      // Create a new Web3 instance
      const web3 = new Web3(provider);

      // Return the Web3 instance and provider details
      return {
        web3Instance: web3,
        provider: provider,
        message: 'Legacy Web3 provider initialized successfully'
      };
    } else {
      // No Web3 provider found
      return {
        web3Instance: null,
        provider: null,
        message: 'No Web3 provider detected. Please install a Web3 wallet like MetaMask.'
      };
    }
  } catch (error) {
    // Handle any errors during initialization
    console.error('Failed to initialize Web3:', error);
    return {
      web3Instance: null,
      provider: null,
      message: `Error initializing Web3: ${error.message}`
    };
  }
}

// Export the function for use in other parts of your application
export default initializeWeb3;
```
