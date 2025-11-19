"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Develop a solution to issue and manage Masa Soulbound Tokens (SBTs) for blockchain-based rewards, including integration with Masa's wallet connection feature.
Generated: DETERMINISTIC_76875c20125ab231
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title MasaSoulboundToken
 * @dev ERC721 token that is soulbound (non-transferable) with Masa wallet integration
 */
contract MasaSoulboundToken is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Mapping from address to whether they've been issued an SBT
    mapping(address => bool) private _hasSBT;

    // Event emitted when a new SBT is issued
    event SBTIssued(address indexed recipient, uint256 tokenId, string tokenURI);

    /**
     * @dev Initializes the contract by setting name and symbol
     */
    constructor() ERC721("MasaSoulboundToken", "MSBT") {}

    /**
     * @dev Issues a new SBT to the specified recipient
     * @param recipient The address to receive the SBT
     * @param tokenURI The metadata URI for the SBT
     */
    function issueSBT(address recipient, string memory tokenURI) external onlyOwner {
        require(recipient != address(0), "MasaSBT: recipient is zero address");
        require(!_hasSBT[recipient], "MasaSBT: recipient already has an SBT");
        require(bytes(tokenURI).length > 0, "MasaSBT: tokenURI cannot be empty");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _safeMint(recipient, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _hasSBT[recipient] = true;

        emit SBTIssued(recipient, tokenId, tokenURI);
    }

    /**
     * @dev Sets the token URI for a given token ID
     * @param tokenId The ID of the token to set URI for
     * @param tokenURI The URI to assign
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal virtual {
        require(_exists(tokenId), "MasaSBT: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The ID of the token to query
     * @return The token URI
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "MasaSBT: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Overrides transfer functions to make token soulbound (non-transferable)
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 batchSize
    ) internal virtual override {
        require(from == address(0) || to == address(0), "MasaSBT: token is soulbound and non-transferable");
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }

    /**
     * @dev Checks if an address has been issued an SBT
     * @param account The address to check
     * @return True if the address has an SBT, false otherwise
     */
    function hasSBT(address account) external view returns (bool) {
        return _hasSBT[account];
    }

    /**
     * @dev Returns the total number of SBTs issued
     * @return The total count of SBTs
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

```javascript
// masa-sbt-manager.js
const { ethers } = require('ethers');
const MasaSoulboundTokenABI = require('./MasaSoulboundTokenABI.json');

class MasaSBTManager {
  /**
   * @param {ethers.providers.Web3Provider} provider - Web3 provider
   * @param {string} contractAddress - MasaSoulboundToken contract address
   */
  constructor(provider, contractAddress) {
    this.provider = provider;
    this.contractAddress = contractAddress;
    this.contract = new ethers.Contract(
      contractAddress,
      MasaSoulboundTokenABI,
      provider.getSigner()
    );
  }

  /**
   * Issues a new SBT to a recipient
   * @param {string} recipientAddress - Recipient wallet address
   * @param {string} tokenURI - Metadata URI for the SBT
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async issueSBT(recipientAddress, tokenURI) {
    try {
      const tx = await this.contract.issueSBT(recipientAddress, tokenURI);
      return await tx.wait();
    } catch (error) {
      console.error('Error issuing SBT:', error);
      throw new Error('Failed to issue SBT');
    }
  }

  /**
   * Checks if an address has an SBT
   * @param {string} addressToCheck - Address to check
   * @returns {Promise<boolean>} True if address has SBT
   */
  async checkHasSBT(addressToCheck) {
    try {
      return await this.contract.hasSBT(addressToCheck);
    } catch (error) {
      console.error('Error checking SBT status:', error);
      throw new Error('Failed to check SBT status');
    }
  }

  /**
   * Gets total number of SBTs issued
   * @returns {Promise<number>} Total SBT count
   */
  async getTotalSupply() {
    try {
      return (await this.contract.totalSupply()).toNumber();
    } catch (error) {
      console.error('Error getting total supply:', error);
      throw new Error('Failed to get total SBT supply');
    }
  }

  /**
   * Gets token URI for a specific SBT
   * @param {number} tokenId - SBT token ID
   * @returns {Promise<string>} Token metadata URI
   */
  async getTokenURI(tokenId) {
    try {
      return await this.contract.tokenURI(tokenId);
    } catch (error) {
      console.error('Error getting token URI:', error);
      throw new Error('Failed to get token URI');
    }
  }

  /**
   * Connects to Masa wallet and returns signer
   * @returns {Promise<ethers.Signer>} Connected signer
   */
  async connectWallet() {
    try {
      await this.provider.send('eth_requestAccounts', []);
      return this.provider.getSigner();
    } catch (error) {
      console.error('Error connecting wallet:', error);
      throw new Error('Failed to connect wallet');
    }
  }
}

module.exports = MasaSBTManager;
```

```json
// MasaSoulboundTokenABI.json
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
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "approved",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
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
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "operator",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "bool",
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
        "internalType": "address",
        "name": "previousOwner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "
