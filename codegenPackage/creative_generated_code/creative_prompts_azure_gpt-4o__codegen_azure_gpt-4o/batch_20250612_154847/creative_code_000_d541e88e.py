"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pi-airdrop.io
Prompt: Write a script to connect a MetaMask wallet to a website using Web3.js, similar to the functionality described on the Pi Network AirDrop site.
Generated: DETERMINISTIC_d541e88ebbf2a6f0
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3.js library
// Ensure you have installed web3.js via npm: npm install web3
const Web3 = require('web3');

// Create a global variable for the Web3 instance
let web3;

// Function to connect MetaMask wallet
async function connectMetaMask() {
  try {
    // Check if MetaMask is installed in the browser
    if (typeof window.ethereum !== 'undefined') {
      console.log('MetaMask is detected.');

      // Create a new Web3 instance using MetaMask's provider
      web3 = new Web3(window.ethereum);

      // Request account access from the user
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Get the connected accounts
      const accounts = await web3.eth.getAccounts();

      if (accounts.length > 0) {
        // Print the connected account to the console
        console.log('Connected account:', accounts[0]);
        return accounts[0]; // Return the connected account address
      } else {
        console.error('No accounts found.');
        return null;
      }
    } else {
      // MetaMask is not installed
      console.error('MetaMask is not detected. Please install MetaMask.');
      return null;
    }
  } catch (error) {
    // Handle errors during connection
    console.error('Error connecting to MetaMask:', error.message);
    return null;
  }
}

// Example usage of the connectMetaMask function
(async () => {
  const connectedAccount = await connectMetaMask();
  if (connectedAccount) {
    console.log('Successfully connected to MetaMask:', connectedAccount);
  } else {
    console.log('Failed to connect to MetaMask.');
  }
})();

// Note:
// 1. To run this script, include it in an HTML file and serve it in a browser environment.
// 2. The Web3.js library interacts with Ethereum-compatible wallets such as MetaMask.
// 3. Ensure MetaMask is installed and accessible in your browser.
```
