"""
Generated Code Metadata:
========================
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: "Generate code to render upgrades off-chain and update NFTs on-chain using Meta Blocks' protocol."
Generated: DETERMINISTIC_afc7b32f1f426b3b
Batch ID: 20250622_211342
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.meta-blocks.io": {
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
// Import required libraries
const { ethers } = require('ethers');
const axios = require('axios');

// Define constants
const META_BLOCKS_PROTOCOL_API = 'https://api.meta-blocks.io';
const NFT_CONTRACT_ADDRESS = '0x...'; // Replace with NFT contract address
const NFT_CONTRACT_ABI = [...]; // Replace with NFT contract ABI

// Define a class to handle off-chain and on-chain upgrades
class MetaBlocksUpgrader {
  /**
   * Initialize the upgrader with provider and wallet
   * @param {ethers.providers.Provider} provider - Ethereum provider
   * @param {ethers.Wallet} wallet - Ethereum wallet
   */
  constructor(provider, wallet) {
    this.provider = provider;
    this.wallet = wallet;
    this.nftContract = new ethers.Contract(NFT_CONTRACT_ADDRESS, NFT_CONTRACT_ABI, wallet);
  }

  /**
   * Render upgrades off-chain using Meta Blocks' protocol
   * @param {string} tokenId - ID of the NFT to upgrade
   * @param {object} upgradeData - Upgrade data (e.g. new metadata)
   * @returns {Promise<object>} - Off-chain upgrade result
   */
  async renderUpgradeOffChain(tokenId, upgradeData) {
    try {
      const response = await axios.post(`${META_BLOCKS_PROTOCOL_API}/render-upgrade`, {
        tokenId,
        upgradeData,
      });
      return response.data;
    } catch (error) {
      throw new Error(`Error rendering upgrade off-chain: ${error.message}`);
    }
  }

  /**
   * Update NFTs on-chain
   * @param {string} tokenId - ID of the NFT to update
   * @param {object} updateData - Update data (e.g. new metadata)
   * @returns {Promise<ethers.Transaction>} - On-chain update transaction
   */
  async updateNftOnChain(tokenId, updateData) {
    try {
      const tx = await this.nftContract.updateToken(tokenId, updateData);
      return tx;
    } catch (error) {
      throw new Error(`Error updating NFT on-chain: ${error.message}`);
    }
  }

  /**
   * Upgrade an NFT using off-chain and on-chain steps
   * @param {string} tokenId - ID of the NFT to upgrade
   * @param {object} upgradeData - Upgrade data (e.g. new metadata)
   * @returns {Promise<object>} - Upgrade result
   */
  async upgradeNft(tokenId, upgradeData) {
    try {
      const offChainResult = await this.renderUpgradeOffChain(tokenId, upgradeData);
      const onChainTx = await this.updateNftOnChain(tokenId, offChainResult);
      await onChainTx.wait();
      return { offChainResult, onChainTx };
    } catch (error) {
      throw new Error(`Error upgrading NFT: ${error.message}`);
    }
  }
}

// Example usage
async function main() {
  // Initialize provider and wallet
  const provider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');
  const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

  // Create an instance of the upgrader
  const upgrader = new MetaBlocksUpgrader(provider, wallet);

  // Upgrade an NFT
  const tokenId = '123';
  const upgradeData = { name: 'New Name', description: 'New Description' };
  const result = await upgrader.upgradeNft(tokenId, upgradeData);
  console.log(result);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
```
