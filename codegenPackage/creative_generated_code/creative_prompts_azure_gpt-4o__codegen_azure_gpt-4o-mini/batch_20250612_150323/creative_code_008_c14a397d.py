"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.creatorlink.net
Prompt: Write code to implement cross-platform compatibility for Wallet Connect in a dApp, ensuring seamless integration with multiple wallets.
Generated: DETERMINISTIC_c14a397d3fb203a6
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletConnect.js
import WalletConnectProvider from "@walletconnect/web3-provider"; // Import WalletConnect provider
import Web3 from "web3"; // Import Web3 library
import { ethers } from "ethers"; // Import ethers for easier wallet interaction

/**
 * WalletConnectManager class to handle WalletConnect integration for dApp
 */
class WalletConnectManager {
  constructor() {
    this.provider = null; // WalletConnect provider
    this.web3 = null; // Web3 instance
  }

  /**
   * Initializes the WalletConnect provider
   */
  async init() {
    try {
      // Create a new WalletConnect provider
      this.provider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_PROJECT_ID", // Required: Infura project ID
      });

      // Enable session (triggers QR Code modal)
      await this.provider.enable();

      // Create Web3 instance with WalletConnect provider
      this.web3 = new Web3(this.provider);

      console.log("WalletConnect initialized");
    } catch (error) {
      console.error("Failed to initialize WalletConnect:", error);
      throw new Error("WalletConnect initialization failed");
    }
  }

  /**
   * Fetches the user's Ethereum accounts
   * @returns {Promise<string[]>} List of user Ethereum accounts
   */
  async getAccounts() {
    try {
      const accounts = await this.web3.eth.getAccounts();
      return accounts;
    } catch (error) {
      console.error("Failed to fetch accounts:", error);
      throw new Error("Fetching accounts failed");
    }
  }

  /**
   * Signs a message with the user's wallet
   * @param {string} message - The message to sign
   * @returns {Promise<string>} The signed message
   */
  async signMessage(message) {
    try {
      const accounts = await this.getAccounts();
      const signature = await this.web3.eth.personal.sign(message, accounts[0]);
      return signature;
    } catch (error) {
      console.error("Failed to sign message:", error);
      throw new Error("Signing message failed");
    }
  }

  /**
   * Disconnects from the WalletConnect session
   */
  async disconnect() {
    if (this.provider) {
      await this.provider.disconnect();
      console.log("WalletConnect disconnected");
    }
  }
}

/**
 * Main function to demonstrate usage of WalletConnectManager
 */
(async function main() {
  const walletConnectManager = new WalletConnectManager();

  try {
    await walletConnectManager.init(); // Initializes WalletConnect

    const accounts = await walletConnectManager.getAccounts(); // Fetch accounts
    console.log("Connected accounts:", accounts); 

    const message = "Sign this message to verify your account"; // Message to be signed
    const signature = await walletConnectManager.signMessage(message); // Sign message
    console.log("Message signed:", signature);

    // Call disconnect method when done
    await walletConnectManager.disconnect();
  } catch (error) {
    console.error("An error occurred:", error);
  }
})();
```

**Notes:**
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
- This code assumes that the user has the necessary wallet installed and configured. 
- Ensure you have the necessary dependencies installed (`@walletconnect/web3-provider`, `web3`, and `ethers`).
