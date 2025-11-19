"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-nexchain.net
Prompt: Illustrate how to implement a wallet connection feature in a web application similar to the Nexchain Dashboard.
Generated: DETERMINISTIC_7ccad40c9c047b80
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation of a wallet connection feature using JavaScript and the popular Ethereum library `ethers.js`:

```javascript
// Import the ethers library
import { ethers } from "ethers";

// WalletConnection.js
class WalletConnection {
  constructor() {
    this.provider = null; // The provider will be set once the wallet is connected
    this.signer = null;   // The signer will be used to interact with the wallet
  }

  /**
   * Connect to the user's wallet.
   * @returns {Promise<string>} The connected wallet's address.
   */
  async connectWallet() {
    try {
      // Check if window.ethereum is available (MetaMask/Wallet support)
      if (!window.ethereum) {
        throw new Error("No crypto wallet found. Please install MetaMask or another wallet provider.");
      }

      // Initialize the provider using ethers
      this.provider = new ethers.providers.Web3Provider(window.ethereum);

      // Request access to the user's wallet
      await window.ethereum.request({ method: "eth_requestAccounts" });

      // Get the signer (user who owns the wallet)
      this.signer = this.provider.getSigner();

      // Get the user's wallet address
      const address = await this.signer.getAddress();
      console.log("Wallet connected successfully:", address);

      return address;
    } catch (error) {
      console.error("Error connecting to wallet:", error.message);
      throw error; // Propagate the error for further handling
    }
  }

  /**
   * Disconnect from the wallet.
   * This simply resets the provider and signer instances.
   */
  disconnectWallet() {
    this.provider = null;
    this.signer = null;
    console.log("Wallet disconnected.");
  }

  /**
   * Get the current wallet address.
   * @returns {Promise<string>} The connected wallet address.
   */
  async getWalletAddress() {
    if (!this.signer) {
      throw new Error("No wallet connected.");
    }

    return await this.signer.getAddress();
  }

  /**
   * Send Ether from the connected wallet to a recipient.
   * @param {string} recipientAddress - The recipient's wallet address.
   * @param {string} amount - Amount of Ether to send (in Ether, not Wei).
   * @returns {Promise<string>} Transaction hash of the transfer.
   */
  async sendEther(recipientAddress, amount) {
    try {
      if (!this.signer) {
        throw new Error("No wallet connected.");
      }

      // Validate recipient address
      if (!ethers.utils.isAddress(recipientAddress)) {
        throw new Error("Invalid recipient address.");
      }

      // Convert Ether amount to Wei (smallest unit of Ether)
      const amountInWei = ethers.utils.parseEther(amount);

      // Create and send the transaction
      const tx = await this.signer.sendTransaction({
        to: recipientAddress,
        value: amountInWei,
      });

      console.log("Transaction sent:", tx);
      return tx.hash; // Return transaction hash for tracking
    } catch (error) {
      console.error("Error sending Ether:", error.message);
      throw error; // Propagate the error for further handling
    }
  }
}

// Example usage:
// Instantiate the WalletConnection class
const walletConnection = new WalletConnection();

// Connect the wallet
document.getElementById("connectWalletButton").addEventListener("click", async () => {
  try {
    const address = await walletConnection.connectWallet();
    alert(`Connected Wallet Address: ${address}`);
  } catch (error) {
    alert(`Error: ${error.message}`);
  }
});

// Disconnect the wallet
document.getElementById("disconnectWalletButton").addEventListener("click", () => {
  walletConnection.disconnectWallet();
  alert("Wallet disconnected.");
});

// Sending Ether
document.getElementById("sendEtherButton").addEventListener("click", async () => {
  try {
    const recipientAddress = prompt("Enter recipient's wallet address:");
    const amount = prompt("Enter amount of Ether to send:");
    const txHash = await walletConnection.sendEther(recipientAddress, amount);
    alert(`Transaction sent successfully! Tx Hash: ${txHash}`);
  } catch (error) {
    alert(`Error: ${error.message}`);
  }
});

export default WalletConnection;
```

### Required Setup:
1. Install `ethers.js`: `npm install ethers`
2. Integrate this code into your application and ensure you have a basic HTML structure with buttons (`connectWalletButton`, `disconnectWalletButton`, `sendEtherButton`) to trigger actions.

This implementation covers basic wallet connection, disconnection, and Ether transfer features, with proper error handling and comments.
