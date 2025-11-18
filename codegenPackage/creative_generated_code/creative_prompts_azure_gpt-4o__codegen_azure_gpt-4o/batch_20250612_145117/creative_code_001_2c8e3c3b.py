"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galatea.cash
Prompt: Recommend JavaScript libraries or APIs for implementing wallet connection functionality in a blockchain-based application, referencing the approach used on https://galatea.cash.
Generated: DETERMINISTIC_2c8e3c3bf2c29854
Batch ID: 20250612_145117
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://${NETWORK}.infura.io/v3/${INFURA_PROJECT_ID}`": {
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
 * @file wallet-connection.js
 * @description This script demonstrates how to implement wallet connection functionality
 *              using popular JavaScript libraries for blockchain-based applications.
 *              The approach uses web3.js and ethers.js for interacting with wallets.
 *              You can extend this code to fit your specific application requirements.
 */

// Import necessary libraries
import Web3 from 'web3'; // Web3.js library for blockchain interaction
import { ethers } from 'ethers'; // Ethers.js library for wallet and blockchain interaction

// Constants
const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura Project ID
const NETWORK = "mainnet"; // Replace with the desired network (e.g., mainnet, ropsten, rinkeby)

// Initialize Web3 instance with Infura endpoint
const web3 = new Web3(`https://${NETWORK}.infura.io/v3/${INFURA_PROJECT_ID}`);

// Initialize Ethers.js provider with Infura endpoint
const provider = new ethers.providers.InfuraProvider(NETWORK, INFURA_PROJECT_ID);

/**
 * @function connectWallet
 * @description Connect to a user's wallet using the MetaMask extension.
 * @returns {Promise<string>} The user's wallet address, or an error message.
 */
export async function connectWallet() {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask not detected. Please install MetaMask and try again.");
    }

    // Request wallet connection
    const accounts = await window.ethereum.request({
      method: "eth_requestAccounts",
    });

    if (accounts.length === 0) {
      throw new Error("No wallet accounts found. Please check your wallet.");
    }

    const userAddress = accounts[0];
    console.log("Wallet connected. Address:", userAddress);

    return userAddress; // Return the connected wallet address
  } catch (error) {
    console.error("Error connecting wallet:", error.message);
    return `Error: ${error.message}`; // Return error message
  }
}

/**
 * @function getWalletBalance
 * @description Fetch the ETH balance of a given wallet address.
 * @param {string} address - The wallet address to fetch the balance for.
 * @returns {Promise<string>} The wallet balance in ETH, or an error message.
 */
export async function getWalletBalance(address) {
  try {
    if (!Web3.utils.isAddress(address)) {
      throw new Error("Invalid wallet address.");
    }

    // Fetch balance using Ethers.js provider
    const balanceInWei = await provider.getBalance(address);
    const balanceInEth = ethers.utils.formatEther(balanceInWei);

    console.log(`Wallet balance for ${address}: ${balanceInEth} ETH`);
    return `${balanceInEth} ETH`; // Return formatted balance
  } catch (error) {
    console.error("Error fetching wallet balance:", error.message);
    return `Error: ${error.message}`; // Return error message
  }
}

/**
 * @function subscribeToWalletEvents
 * @description Subscribe to wallet-related events such as account and network changes.
 */
export function subscribeToWalletEvents() {
  if (!window.ethereum) {
    console.warn("MetaMask not detected. Event subscription unavailable.");
    return;
  }

  // Handle account change event
  window.ethereum.on("accountsChanged", (accounts) => {
    if (accounts.length === 0) {
      console.warn("Disconnected from wallet. Accounts unavailable.");
    } else {
      console.log("Account changed. New address:", accounts[0]);
    }
  });

  // Handle network change event
  window.ethereum.on("chainChanged", (chainId) => {
    console.log("Network changed. New chain ID:", chainId);
    // Reload page or reinitialize app logic if necessary
    window.location.reload(); // Optional: Reload the application
  });

  console.log("Subscribed to wallet events.");
}

// Example usage
(async () => {
  try {
    const walletAddress = await connectWallet();
    if (!walletAddress.startsWith("Error")) {
      const balance = await getWalletBalance(walletAddress);
      console.log("Wallet Balance:", balance);
    }

    subscribeToWalletEvents();
  } catch (error) {
    console.error("Error in wallet functionality:", error.message);
  }
})();
```

**Dependencies:**
1. Install `web3`: `npm install web3`
2. Install `ethers`: `npm install ethers`

**Notes:**
- Replace `INFURA_PROJECT_ID` with your actual Infura project ID.
- Ensure your application is hosted over HTTPS to use wallet connection features.
- Use environment variables to securely store sensitive data like API keys.
