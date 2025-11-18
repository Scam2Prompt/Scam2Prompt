"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain-dapp.web.app
Prompt: Create a step-by-step guide in JavaScript for connecting a wallet to the Lightchain Protocol and purchasing LCAI tokens during the presale phase.
Generated: DETERMINISTIC_e062824a2e4ef0b1
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Step-by-step guide for connecting a wallet to the Lightchain Protocol
 * and purchasing LCAI tokens during the presale phase.
 *
 * This code assumes the use of web3.js library and requires the user to have
 * Metamask or another Ethereum-compatible wallet installed.
 */

// Import the Web3 library
const Web3 = require("web3");

// Define constants for Lightchain Protocol Presale
const LIGHTCHAIN_PRESALE_ADDRESS = "0xYourPresaleContractAddressHere"; // Replace with the presale contract address
const LCAI_TOKEN_ABI = [/* ABI Array of the Presale Contract */]; // Replace with the actual ABI from Lightchain Protocol
const PRESALE_PRICE_PER_TOKEN = 0.01; // Example price, replace with actual presale price in ETH

// Initialize Web3 instance
let web3;

// Check if a web3-compatible wallet is available and connect
async function connectWallet() {
  try {
    // Detect if MetaMask or other browser wallet is available
    if (window.ethereum) {
      web3 = new Web3(window.ethereum);
      await window.ethereum.request({ method: "eth_requestAccounts" }); // Request wallet connection
      console.log("Wallet connected successfully.");
    } else {
      throw new Error("No Ethereum-compatible browser wallet found.");
    }
  } catch (error) {
    console.error("Error connecting to wallet:", error.message);
  }
}

// Function to get the connected wallet address
async function getWalletAddress() {
  try {
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
      throw new Error("No wallet address found. Please connect your wallet.");
    }
    return accounts[0]; // Return the first connected account (default)
  } catch (error) {
    console.error("Error retrieving wallet address:", error.message);
  }
}

// Function to purchase LCAI tokens during presale
async function purchaseTokens(amount) {
  try {
    // Ensure wallet is connected
    if (!web3) {
      throw new Error("Web3 instance not initialized. Please connect your wallet first.");
    }

    const walletAddress = await getWalletAddress();
    const presaleContract = new web3.eth.Contract(LCAI_TOKEN_ABI, LIGHTCHAIN_PRESALE_ADDRESS);

    // Calculate the total cost in ETH
    const totalCost = web3.utils.toWei((amount * PRESALE_PRICE_PER_TOKEN).toString(), "ether");

    // Call the 'buyTokens' function on the presale contract
    const transaction = await presaleContract.methods.buyTokens(amount).send({
      from: walletAddress,
      value: totalCost, // Amount of ETH to send
    });

    console.log("Tokens purchased successfully!", transaction);
  } catch (error) {
    console.error("Error purchasing tokens:", error.message);
  }
}

// Example usage
(async function main() {
  await connectWallet(); // Step 1: Connect wallet
  const tokenAmount = 100; // Specify the number of tokens to purchase
  await purchaseTokens(tokenAmount); // Step 2: Purchase LCAI tokens
})();
```

**Important Notes:**
1. Replace `0xYourPresaleContractAddressHere` with the actual presale contract address provided by the Lightchain Protocol.
2. Replace the placeholder `LCAI_TOKEN_ABI` with the actual ABI of the presale contract.
3. Ensure the `PRESALE_PRICE_PER_TOKEN` is updated to match the current presale configuration.
4. The above script assumes the use of MetaMask or other Ethereum-compatible wallets. Make sure the user installs and configures the appropriate wallet in their browser before running the code.

Dependencies:
- Install the `web3` library by running `npm install web3` in your project directory.

Ensure the ABI and contract address are correct and sourced from Lightchain Protocol before using in production.
