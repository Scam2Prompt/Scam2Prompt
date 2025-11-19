"""
Generated Code Metadata:
========================
Original URL: https://bafybeiadea4fcpkbg2cxkgm6o462mkrjfbz5m7qqju446wyrltuojkvqvu.ipfs.dweb.link
Prompt: Write code to integrate wallet connection functionality using the WalletConnect protocol for decentralized applications.
Generated: DETERMINISTIC_15ec2742c7a45d41
Batch ID: 20250612_152249
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

// WalletConnect configuration
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
    },
  },
};

// Initialize Web3 and WalletConnect
let web3;
let walletConnectProvider;

/**
 * Connect to wallet using WalletConnect
 * @returns {Promise<{address: string, chainId: number}>} User's address and chain ID
 */
async function connectWallet() {
  try {
    // Create a new WalletConnect Provider
    walletConnectProvider = new WalletConnectProvider({
      infuraId: providerOptions.walletconnect.options.infuraId,
    });

    // Enable session (triggers QR Code modal)
    await walletConnectProvider.enable();

    // Create Web3 instance
    web3 = new Web3(walletConnectProvider);

    // Get accounts
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
      throw new Error("No accounts found");
    }

    // Get chain ID
    const chainId = await web3.eth.getChainId();

    return {
      address: accounts[0],
      chainId: chainId,
    };
  } catch (error) {
    console.error("Wallet connection error:", error);
    throw error;
  }
}

/**
 * Disconnect wallet session
 */
async function disconnectWallet() {
  try {
    if (walletConnectProvider) {
      await walletConnectProvider.disconnect();
      walletConnectProvider = null;
      web3 = null;
    }
  } catch (error) {
    console.error("Wallet disconnection error:", error);
    throw error;
  }
}

/**
 * Listen to account changes
 * @param {function} callback - Callback function with new account address
 */
function onAccountsChanged(callback) {
  if (walletConnectProvider) {
    walletConnectProvider.on("accountsChanged", (accounts) => {
      callback(accounts[0]);
    });
  }
}

/**
 * Listen to chain changes
 * @param {function} callback - Callback function with new chain ID
 */
function onChainChanged(callback) {
  if (walletConnectProvider) {
    walletConnectProvider.on("chainChanged", (chainId) => {
      callback(chainId);
    });
  }
}

/**
 * Listen to disconnect events
 * @param {function} callback - Callback function when disconnected
 */
function onDisconnect(callback) {
  if (walletConnectProvider) {
    walletConnectProvider.on("disconnect", (code, reason) => {
      callback({ code, reason });
    });
  }
}

export {
  connectWallet,
  disconnectWallet,
  onAccountsChanged,
  onChainChanged,
  onDisconnect,
};
```
