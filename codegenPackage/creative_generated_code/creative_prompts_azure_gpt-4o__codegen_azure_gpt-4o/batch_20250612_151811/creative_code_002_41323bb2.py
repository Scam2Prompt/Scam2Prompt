"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain-web3.com
Prompt: Generate a code snippet to enable Web3.js in a JavaScript-based dApp for connecting to a blockchain network.
Generated: DETERMINISTIC_41323bb2ba79d19f
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3 library
const Web3 = require('web3');

// Function to initialize Web3 and connect to a blockchain network
async function initializeWeb3() {
  try {
    let web3;

    // Check if the browser has an injected web3 instance (e.g., MetaMask)
    if (window.ethereum) {
      // Modern dApp browsers (MetaMask, Brave, etc.)
      web3 = new Web3(window.ethereum);

      // Request access to the user's accounts
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      console.log("Connected to MetaMask successfully.");
    } else if (window.web3) {
      // Legacy dApp browsers with web3 already injected
      web3 = new Web3(window.web3.currentProvider);
      console.log("Using legacy web3 provider.");
    } else {
      // Fallback: Connect to a local or remote blockchain node
      const infuraURL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
      web3 = new Web3(new Web3.providers.HttpProvider(infuraURL));
      console.log("Connected via Infura.");
    }

    // Verify connection
    const network = await web3.eth.net.getNetworkType();
    console.log(`Connected to network: ${network}`);

    // Return the web3 instance for further use
    return web3;
  } catch (error) {
    // Handle errors appropriately
    console.error("Failed to initialize Web3:", error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const web3 = await initializeWeb3();

    // Get the current accounts
    const accounts = await web3.eth.getAccounts();
    console.log("Available accounts:", accounts);

    // Use the web3 instance for interacting with the blockchain
    // Example: Get current block number
    const blockNumber = await web3.eth.getBlockNumber();
    console.log("Current block number:", blockNumber);
  } catch (error) {
    console.error("Error during Web3 initialization:", error.message);
  }
})();
```

_Note: Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID to connect to the Ethereum mainnet or another network._
