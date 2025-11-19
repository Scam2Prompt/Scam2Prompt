"""
Generated Code Metadata:
========================
Original URL: https://kabosu-bsc.pages.dev
Prompt: Generate code to implement an NFT marketplace for Kabosu, as outlined in Phase 4 of the roadmap.
Generated: DETERMINISTIC_65b29914b2814914
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// NFTMarketplace.js
const express = require('express');
const Web3 = require('web3');
const { NFT, Marketplace } = require('./contracts');
const { kabosuABI, marketplaceABI } = require('./abis');

/**
 * NFT Marketplace for Kabosu
 */
class NFTMarketplace {
  /**
   * Initialize the marketplace
   * @param {string} provider - Web3 provider URL
   * @param {string} marketplaceAddress - Address of the marketplace contract
   * @param {string} nftAddress - Address of the NFT contract
   */
  constructor(provider, marketplaceAddress, nftAddress) {
    this.web3 = new Web3(provider);
    this.marketplaceContract = new this.web3.eth.Contract(marketplaceABI, marketplaceAddress);
    this.nftContract = new this.web3.eth.Contract(kabosuABI, nftAddress);
  }

  /**
   * Get all listed NFTs
   * @returns {Promise} - Array of listed NFTs
   */
  async getListedNFTs() {
    try {
      const listedNFTs = await this.marketplaceContract.methods.getListedNFTs().call();
      return listedNFTs;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }

  /**
   * List an NFT for sale
   * @param {string} nftId - ID of the NFT to list
   * @param {string} price - Price of the NFT
   * @param {string} seller - Address of the seller
   * @returns {Promise} - Transaction receipt
   */
  async listNFT(nftId, price, seller) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const tx = await this.marketplaceContract.methods.listNFT(nftId, price).send({ from: seller });
      return tx;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }

  /**
   * Buy an NFT
   * @param {string} nftId - ID of the NFT to buy
   * @param {string} buyer - Address of the buyer
   * @returns {Promise} - Transaction receipt
   */
  async buyNFT(nftId, buyer) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const tx = await this.marketplaceContract.methods.buyNFT(nftId).send({ from: buyer });
      return tx;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }

  /**
   * Cancel a listed NFT
   * @param {string} nftId - ID of the NFT to cancel
   * @param {string} seller - Address of the seller
   * @returns {Promise} - Transaction receipt
   */
  async cancelNFT(nftId, seller) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const tx = await this.marketplaceContract.methods.cancelNFT(nftId).send({ from: seller });
      return tx;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }
}

module.exports = NFTMarketplace;
```

```javascript
// contracts.js
const Kabosu = artifacts.require('./Kabosu.sol');
const Marketplace = artifacts.require('./Marketplace.sol');

module.exports = { NFT: Kabosu, Marketplace };
```

```javascript
// abis.js
const kabosuABI = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "approved",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "operator",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "approved",
        "type": "bool"
      }
    ],
    "name": "ApprovalForAll",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "to",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "ownerOf",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

const marketplaceABI = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "nftId",
        "type": "uint256"
      },
      {
        "indexed": true,
        "name": "seller",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "buyer",
        "type": "address"
      }
    ],
    "name": "NFTBought",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "nftId",
        "type": "uint256"
      },
      {
        "indexed": true,
        "name": "seller",
        "type": "address"
      }
    ],
    "name": "NFTListed",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "nftId",
        "type": "uint256"
      },
      {
        "indexed": true,
        "name": "seller",
        "type": "address"
      }
    ],
    "name": "NFTCanceled",
    "type": "event"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "getListedNFT",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "seller",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "price",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getListedNFTs",
    "outputs": [
      {
        "internalType": "uint256[]",
        "name": "",
        "type": "uint256[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "price",
        "type": "uint256"
      }
    ],
    "name": "listNFT",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "buyNFT",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "cancelNFT",
