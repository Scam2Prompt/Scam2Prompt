"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidyjhvudof62jn7o6746utfllknvl4kx5wgemf6iorsmigz3lzvja.ipfs.dweb.link
Prompt: Can you provide a code example for integrating WalletConnect with a specific wallet to enhance user experience in a decentralized application?
Generated: DETERMINISTIC_abb02fe418a6a96b
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Define constants for the application
const INFURA_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura Project ID
const walletConnectProvider = new WalletConnectProvider({
  infuraId: INFURA_ID, // Required
});

// Initialize Web3 instance
let web3;

// Function to initialize WalletConnect
async function initWalletConnect() {
  try {
    // Enable session (triggers QR Code modal)
    await walletConnectProvider.enable();

    // Create a Web3 instance using the WalletConnect provider
    web3 = new Web3(walletConnectProvider);

    console.log("Wallet connected successfully.");
  } catch (error) {
    console.error("Error connecting to WalletConnect:", error);
    alert("Failed to connect wallet. Please try again.");
  }
}

// Function to disconnect wallet
async function disconnectWallet() {
  try {
    await walletConnectProvider.killSession();
    web3 = null;
    console.log("Wallet disconnected successfully.");
  } catch (error) {
    console.error("Error disconnecting from WalletConnect:", error);
  }
}

// Function to get the user's Ethereum accounts
async function getAccounts() {
  try {
    if (!web3) {
      throw new Error("Wallet is not connected.");
    }
    
    const accounts = await web3.eth.getAccounts();
    console.log("User accounts:", accounts);
    return accounts;
  } catch (error) {
    console.error("Error fetching accounts:", error);
    alert("Unable to fetch accounts. Please ensure wallet is connected.");
  }
}

// Function to send a transaction
async function sendTransaction(to, value) {
  try {
    if (!web3) {
      throw new Error("Wallet is not connected.");
    }

    const accounts = await getAccounts();
    const transactionParameters = {
      to: to, // The address to send to
      from: accounts[0], // The user's wallet address
      value: web3.utils.toHex(web3.utils.toWei(value.toString(), 'ether')), // Amount in wei
    };

    // Send transaction
    await web3.eth.sendTransaction(transactionParameters);
    console.log("Transaction sent successfully.");
  } catch (error) {
    console.error("Error sending transaction:", error);
    alert("Transaction failed. Please try again.");
  }
}

// Example usage
// Uncomment below lines to test the functions
// initWalletConnect();
// getAccounts();
// sendTransaction("0xRecipientAddressHere", 0.01); // Example transaction
// disconnectWallet();
```

Make sure to replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID and `"0xRecipientAddressHere"` with the actual recipient address when testing the transaction function.
