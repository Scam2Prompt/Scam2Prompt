"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.metamaske.com.cn
Prompt: Create a tutorial for developing a decentralized application (DApp) that leverages MetaMask for user authentication and transaction signing, based on the features outlined on the Metamask Wallet page.
Generated: DETERMINISTIC_7c2e479d35e8dad0
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a tutorial on developing a simple decentralized application (DApp) that leverages MetaMask for user authentication and transaction signing. The example uses JavaScript and the web3.js library.

```javascript
// Import Web3.js library
const Web3 = require("web3");

// Set up the DApp core functionality
class DApp {
  /**
   * Initialize the DApp
   * Sets up Web3 instance and checks MetaMask installation.
   */
  constructor() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === "undefined") {
      throw new Error("MetaMask is not installed. Please install MetaMask to use this DApp.");
    }
    // Initialize Web3 instance using MetaMask's provider
    this.web3 = new Web3(window.ethereum);
  }

  /**
   * Connect to MetaMask and retrieve user's account address
   * @returns {Promise<string>} The account address
   */
  async connectToMetaMask() {
    try {
      // Request access to MetaMask
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
      if (accounts.length === 0) {
        throw new Error("No accounts found. Please make sure MetaMask is unlocked.");
      }

      // Return the first account (default account)
      return accounts[0];
    } catch (error) {
      // Handle errors (e.g., user denies access)
      console.error("Error connecting to MetaMask:", error.message);
      throw error;
    }
  }

  /**
   * Sign a transaction using MetaMask
   * @param {Object} transactionData - The transaction data
   * @param {string} fromAddress - The sender's address
   * @returns {Promise<string>} The transaction hash
   */
  async signAndSendTransaction(transactionData, fromAddress) {
    try {
      // Add the sender's address to the transaction data
      transactionData.from = fromAddress;

      // Send the transaction
      const txHash = await window.ethereum.request({
        method: "eth_sendTransaction",
        params: [transactionData],
      });

      return txHash; // Return the transaction hash
    } catch (error) {
      // Handle errors (e.g., insufficient funds, rejected transaction)
      console.error("Error signing and sending transaction:", error.message);
      throw error;
    }
  }

  /**
   * Get the current balance of an account
   * @param {string} accountAddress - The account address
   * @returns {Promise<string>} The balance in Ether
   */
  async getBalance(accountAddress) {
    try {
      // Fetch the balance in Wei (smallest denomination of Ether)
      const balanceWei = await this.web3.eth.getBalance(accountAddress);

      // Convert Wei to Ether using Web3 utility method
      const balanceEther = Web3.utils.fromWei(balanceWei, "ether");

      return balanceEther; // Return the balance in Ether
    } catch (error) {
      console.error("Error fetching balance:", error.message);
      throw error;
    }
  }
}

// Example Usage
(async () => {
  try {
    // Create a new instance of the DApp
    const dApp = new DApp();

    // Connect to MetaMask and get the user's account
    console.log("Connecting to MetaMask...");
    const userAccount = await dApp.connectToMetaMask();
    console.log("Connected Account:", userAccount);

    // Fetch the user's balance
    console.log("Fetching account balance...");
    const balance = await dApp.getBalance(userAccount);
    console.log("Account Balance (Ether):", balance);

    // Send a transaction (example)
    console.log("Sending a transaction...");
    const txHash = await dApp.signAndSendTransaction(
      {
        to: "0xRecipientAddressHere", // Replace with recipient address
        value: Web3.utils.toWei("0.01", "ether"), // Sending 0.01 Ether
      },
      userAccount
    );
    console.log("Transaction Hash:", txHash);
  } catch (error) {
    console.error("DApp Error:", error.message);
  }
})();
```

### Notes:
- Replace `"0xRecipientAddressHere"` with a valid Ethereum recipient address.
- Ensure MetaMask is installed and the user is logged in before running the code.
- Install the web3.js library via `npm install web3` before executing this code.
