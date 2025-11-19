"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-bridge-and-tx-hi-d503e2-offchain-labs.vercel.app
Prompt: Generate code to integrate NFT minting functionality into a project using the Arbitrum SDK, leveraging the decentralized L2 infrastructure.
Generated: DETERMINISTIC_6187b1f48afda552
Batch ID: 20250612_150440
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://arb1.arbitrum.io/rpc": {
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
const { Wallet, providers, utils } = require('ethers');
const { ArbitrumSDK } = require('@arbitrum/sdk');
const { StandardMerkleTree } = require('@openzeppelin/merkle-tree');
const NFT_ABI = require('./NFT_ABI.json'); // Your NFT contract ABI

// Configuration
const config = {
  arbitrumRpcUrl: 'https://arb1.arbitrum.io/rpc',
  mainnetRpcUrl: 'https://mainnet.infura.io/v3/YOUR_INFURA_KEY',
  privateKey: 'YOUR_PRIVATE_KEY',
  nftContractAddress: 'YOUR_NFT_CONTRACT_ADDRESS',
  gasLimit: 500000,
  gasPrice: utils.parseUnits('0.1', 'gwei')
};

// Initialize providers and wallet
const l1Provider = new providers.JsonRpcProvider(config.mainnetRpcUrl);
const l2Provider = new providers.JsonRpcProvider(config.arbitrumRpcUrl);
const wallet = new Wallet(config.privateKey, l2Provider);

// Initialize Arbitrum SDK
const arbitrumSdk = new ArbitrumSDK({
  l1Provider,
  l2Provider,
  wallet
});

// NFT Minting Service
class NFTMinter {
  constructor() {
    this.nftContract = new ethers.Contract(
      config.nftContractAddress,
      NFT_ABI,
      wallet
    );
  }

  /**
   * Mint NFT on Arbitrum
   * @param {string} recipient - Address to receive the NFT
   * @param {string} tokenURI - Metadata URI for the NFT
   * @returns {Promise<string>} Transaction hash
   */
  async mintNFT(recipient, tokenURI) {
    try {
      // Estimate gas
      const gasEstimate = await this.nftContract.estimateGas.safeMint(
        recipient,
        tokenURI
      );

      // Execute mint
      const tx = await this.nftContract.safeMint(recipient, tokenURI, {
        gasLimit: gasEstimate.mul(12).div(10), // 20% buffer
        gasPrice: config.gasPrice
      });

      await tx.wait();
      return tx.hash;
    } catch (error) {
      console.error('Error minting NFT:', error);
      throw new Error('Failed to mint NFT');
    }
  }

  /**
   * Batch mint NFTs using Merkle tree for whitelist
   * @param {Array} recipients - Array of recipient addresses
   * @param {Array} tokenURIs - Array of token URIs
   * @param {Array} proofs - Array of Merkle proofs
   * @returns {Promise<Array<string>>} Array of transaction hashes
   */
  async batchMintNFTs(recipients, tokenURIs, proofs) {
    if (recipients.length !== tokenURIs.length || recipients.length !== proofs.length) {
      throw new Error('Input arrays must have the same length');
    }

    const txHashes = [];
    
    for (let i = 0; i < recipients.length; i++) {
      try {
        const txHash = await this.mintNFTWithProof(
          recipients[i],
          tokenURIs[i],
          proofs[i]
        );
        txHashes.push(txHash);
      } catch (error) {
        console.error(`Error minting NFT for ${recipients[i]}:`, error);
        txHashes.push(null); // Mark failed mint
      }
    }

    return txHashes;
  }

  /**
   * Mint NFT with Merkle proof verification
   * @param {string} recipient - Address to receive the NFT
   * @param {string} tokenURI - Metadata URI for the NFT
   * @param {Array<string>} proof - Merkle proof
   * @returns {Promise<string>} Transaction hash
   */
  async mintNFTWithProof(recipient, tokenURI, proof) {
    try {
      const gasEstimate = await this.nftContract.estimateGas.mintWithProof(
        recipient,
        tokenURI,
        proof
      );

      const tx = await this.nftContract.mintWithProof(
        recipient,
        tokenURI,
        proof,
        {
          gasLimit: gasEstimate.mul(12).div(10),
          gasPrice: config.gasPrice
        }
      );

      await tx.wait();
      return tx.hash;
    } catch (error) {
      console.error('Error minting NFT with proof:', error);
      throw new Error('Failed to mint NFT with proof');
    }
  }

  /**
   * Generate Merkle tree for whitelist
   * @param {Array} addresses - Array of whitelisted addresses
   * @returns {Object} Merkle tree and root
   */
  generateMerkleTree(addresses) {
    const leaves = addresses.map(addr => [addr]);
    const tree = StandardMerkleTree.of(leaves, ['address']);
    return {
      root: tree.root,
      tree: tree
    };
  }
}

// Utility functions
async function checkL2Balance(address) {
  const balance = await l2Provider.getBalance(address);
  return utils.formatEther(balance);
}

async function depositETHToL2(amount) {
  const deposit = await arbitrumSdk.l1ToL2.depositEth({
    amount: utils.parseEther(amount.toString()),
    l2Provider
  });
  await deposit.wait();
  return deposit.hash;
}

module.exports = {
  NFTMinter,
  checkL2Balance,
  depositETHToL2
};
```
