"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highdappsync.pages.dev
Prompt: Generate a sample code for managing non-custodial wallets in a Dapp with Connect Dapp Web.
Generated: DETERMINISTIC_992e0b48e6135b1d
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script for managing non-custodial wallets in a Dapp using Connect Dapp Web.
 * This sample code includes wallet connection, disconnection, and transaction handling.
 */

// Import required libraries
import { ethers } from "ethers"; // Ethers.js for blockchain interactions
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider

// Constants
const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura project ID
const NETWORK = "mainnet"; // Blockchain network to connect to (e.g., mainnet, rinkeby)

// Global variables
let provider; // Web3 provider instance
let signer; // Signer instance for sending transactions

/**
 * Initializes the WalletConnect provider and connects the wallet.
 */
async function connectWallet() {
  try {
    // Configure WalletConnect provider
    const walletConnectProvider = new WalletConnectProvider({
      infuraId: INFURA_PROJECT_ID, // Use Infura for connecting to the Ethereum network
    });

    // Enable provider (opens wallet modal for user interaction)
    await walletConnectProvider.enable();

    // Create an Ethers.js Web3 provider instance
    provider = new ethers.providers.Web3Provider(walletConnectProvider);

    // Retrieve the user's wallet address
    const accounts = await provider.listAccounts();
    const walletAddress = accounts[0]; // Assuming only one wallet connected

    // Create signer instance for transactions
    signer = provider.getSigner();

    console.log(`Wallet connected: ${walletAddress}`);
    return walletAddress; // Optionally return the wallet address
  } catch (error) {
    console.error("Failed to connect wallet:", error);
    throw new Error("Could not connect wallet. Please try again.");
  }
}

/**
 * Disconnects the wallet session.
 */
function disconnectWallet() {
  try {
    if (provider?.provider?.disconnect) {
      provider.provider.disconnect(); // Disconnect WalletConnect session
    }
    console.log("Wallet disconnected successfully.");
  } catch (error) {
    console.error("Failed to disconnect wallet:", error);
  }
}

/**
 * Sends a transaction from the connected wallet.
 * @param {string} to - The recipient's wallet address.
 * @param {string} value - The amount of ETH to send (in ethers).
 */
async function sendTransaction(to, value) {
  try {
    if (!signer) {
      throw new Error("Wallet is not connected. Please connect a wallet first.");
    }

    // Validate recipient address
    if (!ethers.utils.isAddress(to)) {
      throw new Error("Invalid recipient address.");
    }

    // Prepare transaction data
    const transaction = {
      to, // Recipient's wallet address
      value: ethers.utils.parseEther(value.toString()), // Convert ETH value to Wei
    };

    // Send the transaction
    const txResponse = await signer.sendTransaction(transaction);
    console.log("Transaction sent. Waiting for confirmation...");

    // Wait for the transaction to be mined
    const receipt = await txResponse.wait();
    console.log("Transaction confirmed:", receipt);
    return receipt; // Return transaction receipt
  } catch (error) {
    console.error("Failed to send transaction:", error);
    throw new Error("Could not send transaction. Please try again.");
  }
}

// Example Usage:
// Uncomment the lines below and replace with real values to test the functions.
// (Ensure you have a valid Infura project ID and wallet available.)
//
// connectWallet().then((walletAddress) => {
//   console.log("Connected wallet address:", walletAddress);
//   sendTransaction("0xRecipientWalletAddress", "0.01").then((receipt) => {
//     console.log("Transaction receipt:", receipt);
//   });
// });
//
// // Later disconnect the wallet:
// disconnectWallet();

export { connectWallet, disconnectWallet, sendTransaction };
```
