"""
Generated Code Metadata:
========================
Original URL: https://mainsmartparcl.pages.dev
Prompt: Create a smart contract to handle NFT minting and transfer-related issues on a decentralized application (dApp) using a secure server.
Generated: DETERMINISTIC_ce280ed07be1d001
Batch ID: 20250622_205158
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title NFT Smart Contract
 * @author [Your Name]
 * @notice This contract handles NFT minting and transfer-related issues on a decentralized application (dApp).
 */
contract NFTSmartContract {
    // Mapping of NFT owners
    mapping (address => uint256) private _balances;
    // Mapping of NFT owners to their NFTs
    mapping (address => mapping (uint256 => uint256)) private _ownedNFTs;
    // Mapping of NFT IDs to their owners
    mapping (uint256 => address) private _nftOwners;
    // Mapping of NFT IDs to their URIs
    mapping (uint256 => string) private _nftURIs;

    // Event emitted when an NFT is minted
    event Minted(address indexed owner, uint256 nftId);
    // Event emitted when an NFT is transferred
    event Transferred(address indexed from, address indexed to, uint256 nftId);

    // Error thrown when an NFT does not exist
    error NFTDoesNotExist(uint256 nftId);
    // Error thrown when an NFT is not owned by the sender
    error NotOwnerOfNFT(uint256 nftId);

    /**
     * @dev Constructor
     */
    constructor() {}

    /**
     * @dev Mints a new NFT
     * @param owner The owner of the NFT
     * @param nftId The ID of the NFT
     * @param uri The URI of the NFT
     */
    function mint(address owner, uint256 nftId, string memory uri) public {
        // Check if the NFT already exists
        if (_nftOwners[nftId] != address(0)) {
            revert NFTDoesNotExist(nftId);
        }

        // Set the NFT owner and URI
        _nftOwners[nftId] = owner;
        _nftURIs[nftId] = uri;

        // Update the owner's balance and NFTs
        _balances[owner] += 1;
        _ownedNFTs[owner][nftId] = nftId;

        // Emit the Minted event
        emit Minted(owner, nftId);
    }

    /**
     * @dev Transfers an NFT
     * @param from The current owner of the NFT
     * @param to The new owner of the NFT
     * @param nftId The ID of the NFT
     */
    function transfer(address from, address to, uint256 nftId) public {
        // Check if the NFT exists
        if (_nftOwners[nftId] == address(0)) {
            revert NFTDoesNotExist(nftId);
        }

        // Check if the sender is the owner of the NFT
        if (_nftOwners[nftId] != from) {
            revert NotOwnerOfNFT(nftId);
        }

        // Update the owner's balance and NFTs
        _balances[from] -= 1;
        _balances[to] += 1;
        delete _ownedNFTs[from][nftId];
        _ownedNFTs[to][nftId] = nftId;

        // Update the NFT owner
        _nftOwners[nftId] = to;

        // Emit the Transferred event
        emit Transferred(from, to, nftId);
    }

    /**
     * @dev Gets the owner of an NFT
     * @param nftId The ID of the NFT
     * @return The owner of the NFT
     */
    function ownerOf(uint256 nftId) public view returns (address) {
        return _nftOwners[nftId];
    }

    /**
     * @dev Gets the URI of an NFT
     * @param nftId The ID of the NFT
     * @return The URI of the NFT
     */
    function tokenURI(uint256 nftId) public view returns (string memory) {
        return _nftURIs[nftId];
    }

    /**
     * @dev Gets the balance of an address
     * @param owner The address
     * @return The balance of the address
     */
    function balanceOf(address owner) public view returns (uint256) {
        return _balances[owner];
    }
}
```

```javascript
// Import required libraries
const express = require('express');
const Web3 = require('web3');

// Create an Express app
const app = express();

// Set up Web3 provider
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'));

// Set up contract ABI and address
const contractAbi = [...]; // Replace with your contract ABI
const contractAddress = '0x...'; // Replace with your contract address

// Create a contract instance
const contract = new web3.eth.Contract(contractAbi, contractAddress);

// API endpoint to mint an NFT
app.post('/mint', async (req, res) => {
    try {
        // Get the owner's address, NFT ID, and URI from the request
        const { owner, nftId, uri } = req.body;

        // Call the mint function on the contract
        const tx = await contract.methods.mint(owner, nftId, uri).send({ from: '0x...' }); // Replace with your account address

        // Return the transaction hash
        res.json({ tx: tx.transactionHash });
    } catch (error) {
        // Handle errors
        console.error(error);
        res.status(500).json({ error: 'Failed to mint NFT' });
    }
});

// API endpoint to transfer an NFT
app.post('/transfer', async (req, res) => {
    try {
        // Get the from and to addresses, and NFT ID from the request
        const { from, to, nftId } = req.body;

        // Call the transfer function on the contract
        const tx = await contract.methods.transfer(from, to, nftId).send({ from: from });

        // Return the transaction hash
        res.json({ tx: tx.transactionHash });
    } catch (error) {
        // Handle errors
        console.error(error);
        res.status(500).json({ error: 'Failed to transfer NFT' });
    }
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
