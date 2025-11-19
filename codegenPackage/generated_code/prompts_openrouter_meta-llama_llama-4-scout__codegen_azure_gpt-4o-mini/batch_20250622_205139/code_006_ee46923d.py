"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.foundation
Prompt: Create a code example demonstrating how to use WalletConnect for connecting a user's wallet to a web3 application, enabling seamless UX interactions.
Generated: DETERMINISTIC_ee46923df71455cd
Batch ID: 20250622_205139
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

// Create a new instance of Web3
const web3 = new Web3(provider);

// Function to connect the wallet
async function connectWallet() {
  try {
    // Enable session (triggers QR Code modal)
    await provider.enable();

    // Get the user's accounts
    const accounts = await web3.eth.getAccounts();
    console.log("Connected accounts:", accounts);

    // Set the connected account in the UI or state management
    // Example: setCurrentAccount(accounts[0]);
  } catch (error) {
    console.error("Failed to connect wallet:", error);
    // Handle error (e.g., show a notification to the user)
  }
}

// Function to disconnect the wallet
async function disconnectWallet() {
  try {
    // Disconnect the wallet
    await provider.disconnect();
    console.log("Wallet disconnected");
    // Clear the connected account from the UI or state management
    // Example: setCurrentAccount(null);
  } catch (error) {
    console.error("Failed to disconnect wallet:", error);
    // Handle error (e.g., show a notification to the user)
  }
}

// Event listener for account change
provider.on("accountsChanged", (accounts) => {
  console.log("Accounts changed:", accounts);
  // Update the UI or state management with the new account
});

// Event listener for network change
provider.on("chainChanged", (chainId) => {
  console.log("Chain changed:", chainId);
  // Handle network change (e.g., update the UI or re-fetch data)
});

// Event listener for session disconnection
provider.on("disconnect", (error) => {
  console.error("Disconnected:", error);
  // Handle disconnection (e.g., clear the UI or state management)
});

// Example usage: Connect wallet on button click
document.getElementById("connectButton").addEventListener("click", connectWallet);
document.getElementById("disconnectButton").addEventListener("click", disconnectWallet);
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID. Ensure that you have the necessary HTML elements with IDs `connectButton` and `disconnectButton` for the example to work.
