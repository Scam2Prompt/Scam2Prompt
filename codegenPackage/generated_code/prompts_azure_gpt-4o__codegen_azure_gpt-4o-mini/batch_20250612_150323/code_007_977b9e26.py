"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.foundation
Prompt: Provide an example of how to use WalletConnect to enable cross-platform wallet connections for a decentralized finance (DeFi) application.
Generated: DETERMINISTIC_977b9e2677958325
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Initialize a provider for WalletConnect
const provider = new WalletConnectProvider({
  infuraId: "YOUR_INFURA_PROJECT_ID", // Required: Infura project ID
});

// Create a new Web3 instance
const web3 = new Web3(provider);

// Function to connect to the wallet
async function connectWallet() {
  try {
    // Enable session (triggers QR Code modal)
    await provider.enable();

    // Get the user's accounts
    const accounts = await web3.eth.getAccounts();
    console.log("Connected accounts:", accounts);

    // Set the connected account in your application state
    // Example: setCurrentAccount(accounts[0]);
  } catch (error) {
    console.error("Failed to connect wallet:", error);
  }
}

// Function to disconnect the wallet
async function disconnectWallet() {
  try {
    // Kill the session
    await provider.disconnect();
    console.log("Wallet disconnected");
  } catch (error) {
    console.error("Failed to disconnect wallet:", error);
  }
}

// Function to send a transaction
async function sendTransaction(to, value) {
  try {
    const accounts = await web3.eth.getAccounts();
    const tx = {
      from: accounts[0],
      to: to,
      value: web3.utils.toWei(value, "ether"), // Convert value to Wei
      gas: 2000000, // Set gas limit
    };

    // Send the transaction
    const receipt = await web3.eth.sendTransaction(tx);
    console.log("Transaction receipt:", receipt);
  } catch (error) {
    console.error("Transaction failed:", error);
  }
}

// Example usage
document.getElementById("connectButton").onclick = connectWallet;
document.getElementById("disconnectButton").onclick = disconnectWallet;
document.getElementById("sendButton").onclick = () => {
  const toAddress = document.getElementById("toAddress").value;
  const amount = document.getElementById("amount").value;
  sendTransaction(toAddress, amount);
};

// Handle session updates
provider.on("accountsChanged", (accounts) => {
  console.log("Accounts changed:", accounts);
});

provider.on("chainChanged", (chainId) => {
  console.log("Chain changed:", chainId);
});

provider.on("disconnect", (error) => {
  console.error("Disconnected:", error);
});
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID. Ensure you have the necessary HTML elements with IDs `connectButton`, `disconnectButton`, `toAddress`, and `amount` for the example usage to work.
