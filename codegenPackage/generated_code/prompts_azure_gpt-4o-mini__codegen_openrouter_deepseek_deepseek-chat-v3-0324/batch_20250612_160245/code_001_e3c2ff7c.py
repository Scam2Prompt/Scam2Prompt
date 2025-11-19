"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a code snippet that demonstrates how to use WalletConnect to connect wallets to DApps as described in the Dapp Starter documentation.
Generated: DETERMINISTIC_e3c2ff7cfabfde71
Batch ID: 20250612_160245
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Initialize WalletConnect Provider
const provider = new WalletConnectProvider({
  rpc: {
    1: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
    56: "https://bsc-dataseed.binance.org/",
    // Add other chains as needed
  },
});

// Enable session (triggers QR Code modal)
async function connectWallet() {
  try {
    // Enable provider
    await provider.enable();

    // Create Web3 instance
    const web3 = new Web3(provider);

    // Get accounts
    const accounts = await web3.eth.getAccounts();
    console.log("Connected accounts:", accounts);

    // Get chainId
    const chainId = await web3.eth.getChainId();
    console.log("Connected chain ID:", chainId);

    // Subscribe to accounts change
    provider.on("accountsChanged", (accounts) => {
      console.log("Accounts changed:", accounts);
    });

    // Subscribe to chain change
    provider.on("chainChanged", (chainId) => {
      console.log("Chain changed:", chainId);
    });

    // Subscribe to disconnect
    provider.on("disconnect", (code, reason) => {
      console.log("Disconnected:", code, reason);
    });

    return { web3, provider, accounts, chainId };
  } catch (error) {
    console.error("WalletConnect connection error:", error);
    throw error;
  }
}

// Disconnect wallet
async function disconnectWallet() {
  try {
    await provider.disconnect();
    console.log("Wallet disconnected");
  } catch (error) {
    console.error("WalletConnect disconnection error:", error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    // Connect wallet
    const { web3, accounts } = await connectWallet();

    // Example: Get balance
    const balance = await web3.eth.getBalance(accounts[0]);
    console.log("Account balance:", balance);

    // Disconnect after some time (for demo)
    setTimeout(disconnectWallet, 10000);
  } catch (error) {
    console.error("Error in main:", error);
  }
}

// Uncomment to run example
// main();
```
