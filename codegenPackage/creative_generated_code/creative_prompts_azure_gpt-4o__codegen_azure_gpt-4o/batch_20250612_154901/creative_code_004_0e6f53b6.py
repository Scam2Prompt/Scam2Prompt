"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensys-demos.vercel.app
Prompt: Create a step-by-step guide in code to set up an Infura project and integrate it with MetaMask for web3 application development.
Generated: DETERMINISTIC_0e6f53b6d4bfabf3
Batch ID: 20250612_154901
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`;": {
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
/**
 * Step-by-step guide to set up an Infura project and integrate it with MetaMask for web3 application development.
 * This code demonstrates connecting a web3 application to the Ethereum blockchain
 * using Infura and MetaMask. Ensure you have Node.js installed and an existing Infura project.
 */

// Step 1: Install dependencies
// Run the following command in your project directory:
// npm install web3

// Step 2: Import Web3 library
const Web3 = require('web3');

// Step 3: Initialize Infura connection
// Replace 'YOUR_INFURA_PROJECT_ID' with your actual Infura project ID.
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID';
const infuraUrl = `https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`;

// Step 4: Create a Web3 instance using Infura as the provider
const web3 = new Web3(new Web3.providers.HttpProvider(infuraUrl));

// Step 5: MetaMask integration
// Detect MetaMask (or any Ethereum-compatible wallet) and use it as the provider
if (typeof window.ethereum !== 'undefined') {
  console.log('MetaMask is detected');
  
  // Step 6: Prompt user to connect MetaMask
  // Request account access for MetaMask
  window.ethereum.request({ method: 'eth_requestAccounts' })
    .then((accounts) => {
      console.log('Connected account:', accounts[0]);
      
      // Use MetaMask as the web3 provider
      web3.setProvider(window.ethereum);
    })
    .catch((error) => {
      console.error('Error connecting to MetaMask:', error);
    });
} else {
  console.error('MetaMask not detected. Please install MetaMask to use this application.');
}

// Step 7: Basic example: Fetch Ethereum block number
async function fetchBlockNumber() {
  try {
    const blockNumber = await web3.eth.getBlockNumber();
    console.log('Current Ethereum block number:', blockNumber);
  } catch (error) {
    console.error('Error fetching block number:', error);
  }
}

// Call the function to fetch block number
fetchBlockNumber();

/**
 * Additional Notes:
 * - Make sure you replace 'YOUR_INFURA_PROJECT_ID' with the actual project ID obtained from Infura.
 * - Ensure MetaMask is installed as a browser extension and the user is logged in.
 * - This code snippet assumes that you're running it in a browser environment with MetaMask installed.
 */
```
