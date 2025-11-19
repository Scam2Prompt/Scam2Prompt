"""
Generated Code Metadata:
========================
Original URL: https://dappass.neocities.org
Prompt: Create a library for interacting with the Dapp Pass smart contract, including functions for minting, transferring, and checking ownership of the digital asset.
Generated: DETERMINISTIC_abf376150060de72
Batch ID: 20250622_211012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// DappPass.js

/**
 * DappPass library for interacting with the Dapp Pass smart contract.
 * @module DappPass
 */

const Web3 = require('web3');
const { DappPassABI } = require('./DappPassABI.json');

/**
 * DappPass class.
 */
class DappPass {
  /**
   * Creates a new DappPass instance.
   * @param {string} contractAddress - The address of the Dapp Pass smart contract.
   * @param {string} web3Provider - The Web3 provider URL.
   */
  constructor(contractAddress, web3Provider) {
    this.contractAddress = contractAddress;
    this.web3 = new Web3(new Web3.providers.HttpProvider(web3Provider));
    this.contract = new this.web3.eth.Contract(DappPassABI, contractAddress);
  }

  /**
   * Mints a new digital asset.
   * @param {string} to - The address to mint the asset to.
   * @param {string} tokenURI - The URI of the token.
   * @param {number} tokenId - The ID of the token.
   * @returns {Promise<string>} The transaction hash.
   */
  async mint(to, tokenURI, tokenId) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const from = accounts[0];
      const tx = await this.contract.methods.mint(to, tokenURI, tokenId).send({ from });
      return tx.transactionHash;
    } catch (error) {
      throw new Error(`Error minting token: ${error.message}`);
    }
  }

  /**
   * Transfers a digital asset.
   * @param {string} from - The address to transfer the asset from.
   * @param {string} to - The address to transfer the asset to.
   * @param {number} tokenId - The ID of the token.
   * @returns {Promise<string>} The transaction hash.
   */
  async transfer(from, to, tokenId) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const tx = await this.contract.methods.transfer(from, to, tokenId).send({ from });
      return tx.transactionHash;
    } catch (error) {
      throw new Error(`Error transferring token: ${error.message}`);
    }
  }

  /**
   * Checks ownership of a digital asset.
   * @param {string} owner - The address to check ownership for.
   * @param {number} tokenId - The ID of the token.
   * @returns {Promise<boolean>} Whether the owner owns the token.
   */
  async isOwner(owner, tokenId) {
    try {
      const ownerOf = await this.contract.methods.ownerOf(tokenId).call();
      return ownerOf.toLowerCase() === owner.toLowerCase();
    } catch (error) {
      throw new Error(`Error checking ownership: ${error.message}`);
    }
  }

  /**
   * Gets the URI of a digital asset.
   * @param {number} tokenId - The ID of the token.
   * @returns {Promise<string>} The URI of the token.
   */
  async getTokenURI(tokenId) {
    try {
      const tokenURI = await this.contract.methods.tokenURI(tokenId).call();
      return tokenURI;
    } catch (error) {
      throw new Error(`Error getting token URI: ${error.message}`);
    }
  }
}

module.exports = DappPass;
```

```json
// DappPassABI.json

[
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
      },
      {
        "internalType": "address",
        "name": "approved",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
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
    "name": "getApproved",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "operator",
        "type": "address"
      }
    ],
    "name": "isApprovedForAll",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "string",
        "name": "tokenURI",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "mint",
    "outputs": [],
    "stateMutability": "nonpayable",
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
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "safeTransferFrom",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "internalType": "bytes",
        "name": "_data",
        "type": "bytes"
      }
    ],
    "name": "safeTransferFrom",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function
