"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderly.finance
Prompt: Write code to integrate wallet connection functionality into a decentralized finance platform using the MetaMask API, similar to the features on wonderly.finance.
Generated: DETERMINISTIC_cf13742809caca0e
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import Web3 from 'web3';

// Define the WalletConnector class
class WalletConnector {
  constructor() {
    // Initialize Web3 instance
    this.web3 = null;

    // Store the connected wallet address
    this.account = null;

    // MetaMask provider check
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install it to use this feature.");
    }
  }

  /**
   * Connect to the MetaMask wallet.
   * @returns {Promise<string>} The connected wallet address.
   */
  async connect() {
    try {
      // Request account access from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Save the first account as the connected wallet
      this.account = accounts[0];

      // Initialize Web3 with MetaMask's provider
      this.web3 = new Web3(window.ethereum);

      console.log("Wallet connected:", this.account);
      return this.account;
    } catch (error) {
      console.error("Error connecting to wallet:", error.message);
      throw new Error("Failed to connect wallet. Please try again.");
    }
  }

  /**
   * Get the current connected account.
   * @returns {string|null} The currently connected account address or null if not connected.
   */
  getAccount() {
    return this.account;
  }

  /**
   * Listen for account changes and execute a callback.
   * @param {Function} callback A function to call when the account changes.
   */
  listenForAccountChanges(callback) {
    if (!window.ethereum) return;

    // Listen to account change events
    window.ethereum.on('accountsChanged', (accounts) => {
      console.log("Account changed:", accounts);
      this.account = accounts[0] || null;
      callback(this.account);
    });
  }

  /**
   * Listen for network changes and execute a callback.
   * @param {Function} callback A function to call when the network changes.
   */
  listenForNetworkChanges(callback) {
    if (!window.ethereum) return;

    // Listen to network change events
    window.ethereum.on('chainChanged', (chainId) => {
      console.log("Network changed:", chainId);
      callback(chainId);
    });
  }

  /**
   * Disconnect the wallet by clearing local state.
   */
  disconnect() {
    this.account = null;
    this.web3 = null;
    console.log("Wallet disconnected.");
  }
}

// Example usage for integration
(async () => {
  const walletConnector = new WalletConnector();

  try {
    // Attempt to connect the wallet
    const connectedAccount = await walletConnector.connect();
    console.log("Connected account:", connectedAccount);

    // Listen for account changes
    walletConnector.listenForAccountChanges((newAccount) => {
      console.log("Account updated:", newAccount);
    });

    // Listen for network changes
    walletConnector.listenForNetworkChanges((newChainId) => {
      console.log("Network updated to chain ID:", newChainId);
    });
  } catch (error) {
    console.error("Wallet connection failed:", error.message);
  }
})();
```

This code is a production-ready implementation for integrating MetaMask wallet connection functionality into a decentralized finance platform. It includes error handling, clear documentation, and event listeners to handle account and network changes.
