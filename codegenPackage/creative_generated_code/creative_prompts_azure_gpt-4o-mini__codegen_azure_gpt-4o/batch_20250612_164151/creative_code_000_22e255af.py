"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accountvalidators.com
Prompt: Generate code to integrate WalletConnect with a DApp using the Hybrid SDK for Ethereum.
Generated: DETERMINISTIC_22e255af7ab63bce
Batch ID: 20250612_164151
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import required modules and dependencies
import WalletConnectProvider from "@walletconnect/web3-provider"; // Web3 WalletConnect provider
import Web3 from "web3"; // Web3 library

// Configuration for WalletConnect
const walletConnectConfig = {
  rpc: {
    1: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Ethereum Mainnet RPC
    4: "https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Rinkeby Testnet RPC
  },
  chainId: 1, // Default chain ID (Ethereum Mainnet)
};

// Function to initialize WalletConnect and establish connection with the DApp
async function connectWallet() {
  try {
    // Initialize WalletConnect provider
    const provider = new WalletConnectProvider(walletConnectConfig);

    // Enable session (connect to wallet)
    await provider.enable();

    // Create Web3 instance using the WalletConnect provider
    const web3 = new Web3(provider);

    // Get connected accounts
    const accounts = await web3.eth.getAccounts();
    console.log("Connected Accounts:", accounts);

    // Get chain ID
    const chainId = await web3.eth.getChainId();
    console.log("Connected Chain ID:", chainId);

    // Listen for events like account changes or chain updates
    provider.on("accountsChanged", (newAccounts) => {
      console.log("Accounts Changed:", newAccounts);
    });

    provider.on("chainChanged", (newChainId) => {
      console.log("Chain Changed:", newChainId);
    });

    provider.on("disconnect", (code, reason) => {
      console.log("Wallet Disconnected:", code, reason);
    });

    return { provider, web3, accounts, chainId };
  } catch (error) {
    console.error("Error connecting wallet:", error);
    throw new Error("Failed to connect to WalletConnect");
  }
}

// Function to disconnect the wallet
async function disconnectWallet(provider) {
  try {
    if (provider) {
      await provider.disconnect();
      console.log("Wallet disconnected successfully");
    } else {
      console.log("No provider instance found");
    }
  } catch (error) {
    console.error("Error disconnecting wallet:", error);
    throw new Error("Failed to disconnect WalletConnect");
  }
}

// Example usage
(async () => {
  try {
    const { provider, web3, accounts, chainId } = await connectWallet();

    // Perform DApp interactions with Web3 instance here
    console.log("Web3 instance is ready for DApp interaction!");

    // Disconnect the wallet when done
    await disconnectWallet(provider);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
})();
```

> **Note**: Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID. Ensure you have installed `@walletconnect/web3-provider` and `web3` packages using npm before running this code (`npm install @walletconnect/web3-provider web3`).
