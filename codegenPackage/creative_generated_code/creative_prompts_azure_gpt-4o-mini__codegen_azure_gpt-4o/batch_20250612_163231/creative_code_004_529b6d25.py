"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: Explain how MetaMask integrates with popular web browsers and the benefits of using it for decentralized finance activities.
Generated: DETERMINISTIC_529b6d25c36a2612
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a JavaScript code snippet demonstrating how MetaMask integrates with popular web browsers and facilitates decentralized finance (DeFi) activities. The code is designed as an example of querying account details and checking the balance of Ethereum using MetaMask.

```javascript
// Importing the ethers library for interacting with Ethereum blockchain
// Install ethers using: npm install ethers
const { ethers } = require("ethers");

/**
 * Function to check if MetaMask is installed and accessible
 * @returns {boolean} - True if MetaMask is available, false otherwise
 */
function isMetaMaskInstalled() {
  return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
}

/**
 * Function to request access to MetaMask and get the user's account
 * @returns {Promise<string>} - The connected Ethereum account address
 */
async function connectMetaMask() {
  try {
    // Requesting account connection from the user
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    if (accounts.length === 0) {
      throw new Error("No accounts found. Please connect an account in MetaMask.");
    }

    console.log("Connected account:", accounts[0]);
    return accounts[0];
  } catch (err) {
    console.error("Error connecting to MetaMask:", err.message);
    throw new Error("Failed to connect to MetaMask. Please ensure MetaMask is installed and unlocked.");
  }
}

/**
 * Function to fetch the balance of the connected account
 * @param {string} accountAddress - The Ethereum account address
 * @returns {Promise<string>} - The balance in Ether (ETH)
 */
async function getAccountBalance(accountAddress) {
  try {
    // Using ethers.js provider to query the blockchain
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Fetching balance in wei
    const balanceWei = await provider.getBalance(accountAddress);

    // Converting balance to Ether (human-readable format)
    const balanceEther = ethers.utils.formatEther(balanceWei);

    console.log(`Balance of ${accountAddress}: ${balanceEther} ETH`);
    return balanceEther;
  } catch (err) {
    console.error("Error fetching account balance:", err.message);
    throw new Error("Failed to fetch account balance. Please try again later.");
  }
}

/**
 * Main function demonstrating MetaMask integration
 * Connects to MetaMask, fetches the user's account, and retrieves the balance
 * @returns {Promise<void>}
 */
async function main() {
  try {
    // Check if MetaMask is installed
    if (!isMetaMaskInstalled()) {
      throw new Error("MetaMask is not installed in your browser. Please install MetaMask to continue.");
    }

    console.log("MetaMask is installed!");

    // Connect to the user's account
    const accountAddress = await connectMetaMask();

    // Fetch and display the connected account's balance
    const balance = await getAccountBalance(accountAddress);
    console.log(`The connected account (${accountAddress}) has a balance of ${balance} ETH.`);
  } catch (err) {
    console.error(err.message);
  }
}

// Run the main function to initiate MetaMask integration
main();

```

### Prerequisites:
1. Ensure MetaMask is installed in your web browser.
2. Run the code on a website or local server with HTTPS enabled since MetaMask requires secure contexts.
3. Install the `ethers.js` library if you are using Node.js (`npm install ethers`).

This code integrates with MetaMask, connects the user's account, and fetches the balance in Ether. It handles errors gracefully and follows best practices for production-ready JavaScript.
