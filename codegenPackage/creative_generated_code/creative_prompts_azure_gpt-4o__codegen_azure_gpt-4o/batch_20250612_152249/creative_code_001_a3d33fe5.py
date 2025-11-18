"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spaceconnect.tistory.com
Prompt: Recommend a JavaScript library for connecting cryptocurrency wallets and explain how to use it to replicate the "Connect Wallet" feature mentioned on the SpaceConnect page.
Generated: DETERMINISTIC_a3d33fe53f02b1d5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the WalletConnect library via npm or CDN
// npm installation: npm install @walletconnect/web3-provider
// This library allows users to connect to various cryptocurrency wallets

// Import necessary dependencies
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Function to initialize the "Connect Wallet" feature
async function connectWallet() {
  try {
    // Create a new WalletConnect provider instance
    const provider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
    });

    // Enable the WalletConnect provider
    await provider.enable();

    // Initialize Web3 with the WalletConnect provider
    const web3 = new Web3(provider);

    // Get the list of accounts connected to the wallet
    const accounts = await web3.eth.getAccounts();

    // Check if any account is returned
    if (accounts.length === 0) {
      console.log("No accounts found. Please connect a wallet.");
    } else {
      console.log("Connected account:", accounts[0]); // Log the first account
    }

    // Optionally, you can fetch chainId to know which network the wallet is connected to
    const chainId = await web3.eth.getChainId();
    console.log("Connected chain ID:", chainId);

    // Subscribe to events (e.g., disconnect or account change)
    provider.on("disconnect", (code, reason) => {
      console.log("Wallet disconnected:", code, reason);
    });

    provider.on("accountsChanged", (changedAccounts) => {
      console.log("Accounts changed:", changedAccounts);
    });

    provider.on("chainChanged", (changedChainId) => {
      console.log("Chain changed:", changedChainId);
    });
  } catch (error) {
    // Handle errors gracefully
    console.error("Failed to connect wallet:", error.message);
  }
}

// Example usage: Connect Wallet button
document.getElementById("connect-wallet-btn").addEventListener("click", connectWallet);

/*
  HTML Example for the "Connect Wallet" button:
  <button id="connect-wallet-btn">Connect Wallet</button>
*/

/*
  Notes:
  - Replace "YOUR_INFURA_PROJECT_ID" with your actual Infura project ID to connect to Ethereum mainnet or testnets.
  - Alternatively, you can use other providers or configurations depending on your blockchain network needs.
  - Make sure to install "@walletconnect/web3-provider" and "web3" via npm before running the code.
*/
```
