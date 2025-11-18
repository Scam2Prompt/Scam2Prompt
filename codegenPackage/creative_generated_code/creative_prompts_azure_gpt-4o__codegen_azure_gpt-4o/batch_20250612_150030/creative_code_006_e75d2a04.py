"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: Provide an example of handling wallet connection errors using Web3Modal in a Web3 project.
Generated: DETERMINISTIC_e75d2a046f71c6ed
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import Web3Modal from 'web3modal';

// Import providers for Web3Modal (e.g., WalletConnect)
import WalletConnectProvider from "@walletconnect/web3-provider";

// Custom function to handle wallet connection
async function connectWallet() {
  // Define Web3Modal configuration options
  const providerOptions = {
    walletconnect: {
      package: WalletConnectProvider, // WalletConnect provider
      options: {
        infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
      },
    },
  };

  // Initialize Web3Modal
  const web3Modal = new Web3Modal({
    cacheProvider: true, // Enable caching for previously used wallet
    providerOptions, // Wallet provider options
  });

  let web3; // Web3 instance
  let provider; // Wallet provider instance

  try {
    // Open Web3Modal dialog to connect wallet
    provider = await web3Modal.connect();

    // Listen for provider events (e.g., disconnect, accounts change)
    provider.on("disconnect", () => {
      console.error("Wallet disconnected.");
    });

    provider.on("accountsChanged", (accounts) => {
      console.log("Accounts changed:", accounts);
    });

    provider.on("chainChanged", (chainId) => {
      console.log("Chain changed:", chainId);
    });

    // Create Web3 instance using the connected provider
    web3 = new Web3(provider);

    // Fetch connected accounts
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
      console.error("No accounts found.");
      return; // Exit if no accounts are connected
    }

    console.log("Connected account:", accounts[0]);

    // Fetch current chain ID
    const chainId = await web3.eth.getChainId();
    console.log("Connected chain ID:", chainId);
  } catch (error) {
    // Handle connection errors
    console.error("Failed to connect wallet:", error.message || error);
  } finally {
    // Cleanup logic if needed
    if (!web3) {
      console.log("Web3 instance not initialized.");
      return;
    }

    console.log("Web3 instance successfully initialized.");
  }
}

// Example usage of wallet connection
connectWallet();
```
