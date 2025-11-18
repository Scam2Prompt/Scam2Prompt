"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain-frontend.vercel.app
Prompt: Create a function that checks if a wallet is connected to Berachain and retrieves the block number using MetaMask integration.
Generated: DETERMINISTIC_268af0ea014eeaf3
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if a wallet is connected to Berachain and retrieve the current block number.
 * Uses MetaMask and assumes the presence of an Ethereum-compatible browser.
 */

// Import ethers.js (assuming a build environment with npm)
const { ethers } = require("ethers");

/**
 * Asynchronous function to check wallet connection and retrieve block number.
 * @returns {Promise<number>} - The current block number on Berachain.
 * @throws Will throw an error if MetaMask is not installed, the user is not connected, 
 *         or if the network is not Berachain.
 */
async function getBerachainBlockNumber() {
  try {
    // Check if MetaMask (Ethereum provider) is available in the browser
    if (typeof window.ethereum === "undefined") {
      throw new Error("MetaMask is not installed. Please install MetaMask to proceed.");
    }

    // Request user accounts from MetaMask
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

    if (!accounts || accounts.length === 0) {
      throw new Error("No accounts connected. Please connect a wallet.");
    }

    // Initialize ethers.js provider using MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the current network details
    const network = await provider.getNetwork();

    // Replace `BERACHAIN_CHAIN_ID` with the actual chain ID of Berachain
    const BERACHAIN_CHAIN_ID = 12345; // Example chain ID, update this accordingly

    if (network.chainId !== BERACHAIN_CHAIN_ID) {
      throw new Error(`Connected to the wrong network. Please switch to Berachain.`);
    }

    // Retrieve the current block number
    const blockNumber = await provider.getBlockNumber();

    // Return the block number
    return blockNumber;
  } catch (error) {
    // Log the error to the console and rethrow it
    console.error("Error retrieving block number:", error.message);
    throw error;
  }
}

// Example usage:
getBerachainBlockNumber()
  .then((blockNumber) => {
    console.log("Current block number on Berachain:", blockNumber);
  })
  .catch((error) => {
    console.error("Failed to get block number:", error.message);
  });
```
