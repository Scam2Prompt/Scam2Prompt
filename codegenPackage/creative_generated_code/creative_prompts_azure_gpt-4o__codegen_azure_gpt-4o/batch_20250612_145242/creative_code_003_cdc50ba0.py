"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-96qjy03xf-reown-com.vercel.app
Prompt: Create a wallet configuration for AppKit using Ethers as the driving library, with no email or social integration.
Generated: DETERMINISTIC_cdc50ba0369a36d6
Batch ID: 20250612_145242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary modules from ethers
const { ethers } = require("ethers");

// WalletConfig class to encapsulate wallet-related operations
class WalletConfig {
  /**
   * Constructor to initialize the WalletConfig
   * @param {string} providerUrl - The RPC URL of the blockchain provider
   */
  constructor(providerUrl) {
    // Ensure the provider URL is valid
    if (!providerUrl || typeof providerUrl !== 'string') {
      throw new Error("Invalid provider URL");
    }

    // Create a provider using ethers
    this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
  }

  /**
   * Create a new wallet with a random private key
   * @returns {object} - An object containing the wallet and its mnemonic phrase
   */
  createNewWallet() {
    try {
      // Generate a new random wallet
      const wallet = ethers.Wallet.createRandom();

      return {
        wallet: wallet,
        address: wallet.address,
        mnemonic: wallet.mnemonic.phrase,
      };
    } catch (error) {
      throw new Error(`Failed to create a new wallet: ${error.message}`);
    }
  }

  /**
   * Load a wallet from a mnemonic phrase
   * @param {string} mnemonic - The mnemonic phrase of the wallet
   * @returns {object} - The loaded wallet
   */
  loadWalletFromMnemonic(mnemonic) {
    try {
      // Validate the input mnemonic
      if (!mnemonic || typeof mnemonic !== "string") {
        throw new Error("Invalid mnemonic phrase");
      }

      // Load the wallet using the mnemonic
      const wallet = ethers.Wallet.fromMnemonic(mnemonic);

      return {
        wallet: wallet,
        address: wallet.address,
      };
    } catch (error) {
      throw new Error(`Failed to load wallet from mnemonic: ${error.message}`);
    }
  }

  /**
   * Load a wallet from a private key
   * @param {string} privateKey - The private key of the wallet
   * @returns {object} - The loaded wallet
   */
  loadWalletFromPrivateKey(privateKey) {
    try {
      // Validate the input private key
      if (!privateKey || typeof privateKey !== "string") {
        throw new Error("Invalid private key");
      }

      // Load the wallet using the private key
      const wallet = new ethers.Wallet(privateKey, this.provider);

      return {
        wallet: wallet,
        address: wallet.address,
      };
    } catch (error) {
      throw new Error(`Failed to load wallet from private key: ${error.message}`);
    }
  }

  /**
   * Get the balance of an address
   * @param {string} address - The Ethereum address to check the balance of
   * @returns {Promise<string>} - The balance in Ether
   */
  async getBalance(address) {
    try {
      // Validate the Ethereum address
      if (!ethers.utils.isAddress(address)) {
        throw new Error("Invalid Ethereum address");
      }

      // Get the balance in Wei and convert it to Ether
      const balanceWei = await this.provider.getBalance(address);
      const balanceEther = ethers.utils.formatEther(balanceWei);

      return balanceEther;
    } catch (error) {
      throw new Error(`Failed to get balance: ${error.message}`);
    }
  }
}

// Example usage (for testing purposes only)
// Replace `YOUR_RPC_PROVIDER_URL` with the actual provider URL
const walletConfig = new WalletConfig("YOUR_RPC_PROVIDER_URL");

// Uncomment the following lines to test functionality:
// const newWallet = walletConfig.createNewWallet();
// console.log("New Wallet:", newWallet);

// const loadedWallet = walletConfig.loadWalletFromMnemonic(newWallet.mnemonic);
// console.log("Loaded Wallet:", loadedWallet);
```

This code snippet defines a `WalletConfig` class that provides wallet management utilities using the `ethers` library. It includes methods to create a new wallet, load wallets from mnemonic phrases or private keys, and fetch wallet balances. Error handling is implemented for invalid inputs and operational errors.
