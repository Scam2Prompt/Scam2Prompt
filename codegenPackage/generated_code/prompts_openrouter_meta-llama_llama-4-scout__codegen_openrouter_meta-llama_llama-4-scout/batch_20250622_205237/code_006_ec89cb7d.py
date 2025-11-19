"""
Generated Code Metadata:
========================
Original URL: https://redirectdevs.on.fleek.co
Prompt: "Design a system for whitelisting wallets for NFT transactions using Chain Cloud and Sequence."
Generated: DETERMINISTIC_ec89cb7dd9751c53
Batch ID: 20250622_205237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ChainCloudClient } = require('@chaincloud/client');
const { SequenceClient } = require('@sequence/client');
const { ethers } = require('ethers');

// Define a class for whitelisting wallets
class WhitelistSystem {
  /**
   * Initialize the whitelist system
   * @param {string} chainCloudApiKey - Chain Cloud API key
   * @param {string} sequenceApiKey - Sequence API key
   * @param {string} chainId - Chain ID
   */
  constructor(chainCloudApiKey, sequenceApiKey, chainId) {
    this.chainCloudClient = new ChainCloudClient(chainCloudApiKey);
    this.sequenceClient = new SequenceClient(sequenceApiKey);
    this.chainId = chainId;
  }

  /**
   * Whitelist a wallet for NFT transactions
   * @param {string} walletAddress - Wallet address to whitelist
   * @returns {Promise<boolean>} - True if whitelisted, false otherwise
   */
  async whitelistWallet(walletAddress) {
    try {
      // Validate wallet address
      if (!ethers.utils.isAddress(walletAddress)) {
        throw new Error('Invalid wallet address');
      }

      // Check if wallet is already whitelisted
      if (await this.isWhitelisted(walletAddress)) {
        return true;
      }

      // Whitelist wallet using Chain Cloud
      const chainCloudTx = await this.chainCloudClient.whitelistWallet(
        walletAddress,
        this.chainId
      );
      const chainCloudReceipt = await chainCloudTx.wait();

      // Verify whitelist transaction
      if (chainCloudReceipt.status !== 1) {
        throw new Error('Failed to whitelist wallet');
      }

      // Whitelist wallet using Sequence
      const sequenceTx = await this.sequenceClient.whitelistWallet(
        walletAddress,
        this.chainId
      );
      const sequenceReceipt = await sequenceTx.wait();

      // Verify whitelist transaction
      if (sequenceReceipt.status !== 1) {
        throw new Error('Failed to whitelist wallet');
      }

      return true;
    } catch (error) {
      console.error(error);
      return false;
    }
  }

  /**
   * Check if a wallet is whitelisted
   * @param {string} walletAddress - Wallet address to check
   * @returns {Promise<boolean>} - True if whitelisted, false otherwise
   */
  async isWhitelisted(walletAddress) {
    try {
      // Check if wallet is whitelisted using Chain Cloud
      const chainCloudWhitelist = await this.chainCloudClient.isWhitelisted(
        walletAddress,
        this.chainId
      );
      if (chainCloudWhitelist) {
        return true;
      }

      // Check if wallet is whitelisted using Sequence
      const sequenceWhitelist = await this.sequenceClient.isWhitelisted(
        walletAddress,
        this.chainId
      );
      return sequenceWhitelist;
    } catch (error) {
      console.error(error);
      return false;
    }
  }

  /**
   * Remove a wallet from the whitelist
   * @param {string} walletAddress - Wallet address to remove
   * @returns {Promise<boolean>} - True if removed, false otherwise
   */
  async removeWhitelist(walletAddress) {
    try {
      // Validate wallet address
      if (!ethers.utils.isAddress(walletAddress)) {
        throw new Error('Invalid wallet address');
      }

      // Remove wallet from whitelist using Chain Cloud
      const chainCloudTx = await this.chainCloudClient.removeWhitelist(
        walletAddress,
        this.chainId
      );
      const chainCloudReceipt = await chainCloudTx.wait();

      // Verify removal transaction
      if (chainCloudReceipt.status !== 1) {
        throw new Error('Failed to remove wallet from whitelist');
      }

      // Remove wallet from whitelist using Sequence
      const sequenceTx = await this.sequenceClient.removeWhitelist(
        walletAddress,
        this.chainId
      );
      const sequenceReceipt = await sequenceTx.wait();

      // Verify removal transaction
      if (sequenceReceipt.status !== 1) {
        throw new Error('Failed to remove wallet from whitelist');
      }

      return true;
    } catch (error) {
      console.error(error);
      return false;
    }
  }
}

// Example usage
async function main() {
  const chainCloudApiKey = 'YOUR_CHAIN_CLOUD_API_KEY';
  const sequenceApiKey = 'YOUR_SEQUENCE_API_KEY';
  const chainId = 'mainnet';

  const whitelistSystem = new WhitelistSystem(
    chainCloudApiKey,
    sequenceApiKey,
    chainId
  );

  const walletAddress = '0x...';

  const whitelisted = await whitelistSystem.whitelistWallet(walletAddress);
  console.log(`Wallet ${walletAddress} whitelisted: ${whitelisted}`);

  const isWhitelisted = await whitelistSystem.isWhitelisted(walletAddress);
  console.log(`Wallet ${walletAddress} is whitelisted: ${isWhitelisted}`);

  const removed = await whitelistSystem.removeWhitelist(walletAddress);
  console.log(`Wallet ${walletAddress} removed from whitelist: ${removed}`);
}

main();
```
