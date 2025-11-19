"""
Generated Code Metadata:
========================
Original URL: https://blockchain-metamask.mobiloitte.org
Prompt: How can I use MetaMask to enable secure and transparent ownership verification for digital artworks on a blockchain-based platform?
Generated: DETERMINISTIC_8ad096376d119c25
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**MetaMask Integration for Secure Ownership Verification**
===========================================================

**Prerequisites**
---------------

* MetaMask installed on user's browser
* Web3 library (e.g., Web3.js or Ethers.js)
* Blockchain-based platform with smart contract functionality

**Code**
------

```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Set up Web3 provider with MetaMask
const provider = new ethers.providers.Web3Provider(window.ethereum);

// Connect to user's MetaMask account
async function connectToMetaMask() {
  try {
    // Request user's permission to access their MetaMask account
    await provider.send('eth_requestAccounts', []);

    // Get user's Ethereum address
    const address = await provider.getSigner().getAddress();
    console.log(`Connected to MetaMask account: ${address}`);

    return address;
  } catch (error) {
    console.error('Error connecting to MetaMask:', error);
    throw error;
  }
}

// Verify ownership of digital artwork
async function verifyOwnership(artworkId, ownerAddress) {
  try {
    // Define the smart contract ABI and address
    const contractAbi = [
      {
        inputs: [],
        stateMutability: 'nonpayable',
        type: 'constructor',
      },
      {
        anonymous: false,
        inputs: [
          {
            indexed: true,
            name: 'owner',
            type: 'address',
          },
          {
            indexed: true,
            name: 'artworkId',
            type: 'uint256',
          },
        ],
        name: 'OwnershipVerified',
        type: 'event',
      },
      {
        inputs: [
          {
            name: 'artworkId',
            type: 'uint256',
          },
        ],
        name: 'getOwner',
        outputs: [
          {
            name: '',
            type: 'address',
          },
        ],
        stateMutability: 'view',
        type: 'function',
      },
      {
        inputs: [
          {
            name: 'artworkId',
            type: 'uint256',
          },
          {
            name: 'owner',
            type: 'address',
          },
        ],
        name: 'verifyOwnership',
        outputs: [],
        stateMutability: 'nonpayable',
        type: 'function',
      },
    ];
    const contractAddress = '0x...'; // Replace with your contract address
    const contract = new ethers.Contract(contractAddress, contractAbi, provider);

    // Verify ownership on the blockchain
    await contract.verifyOwnership(artworkId, ownerAddress);

    // Emit event to confirm ownership verification
    contract.emit('OwnershipVerified', ownerAddress, artworkId);
  } catch (error) {
    console.error('Error verifying ownership:', error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    // Connect to MetaMask
    const address = await connectToMetaMask();

    // Verify ownership of digital artwork
    const artworkId = 123; // Replace with your artwork ID
    await verifyOwnership(artworkId, address);

    console.log(`Ownership of artwork ${artworkId} verified for address ${address}`);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```

**Smart Contract (Solidity)**
---------------------------

```solidity
pragma solidity ^0.8.0;

contract OwnershipVerifier {
  // Mapping of artwork IDs to their owners
  mapping(uint256 => address) public artworkOwners;

  // Event emitted when ownership is verified
  event OwnershipVerified(address indexed owner, uint256 indexed artworkId);

  // Constructor
  constructor() {}

  // Verify ownership of digital artwork
  function verifyOwnership(uint256 _artworkId, address _owner) public {
    require(_owner != address(0), 'Invalid owner address');
    artworkOwners[_artworkId] = _owner;
  }

  // Get owner of digital artwork
  function getOwner(uint256 _artworkId) public view returns (address) {
    return artworkOwners[_artworkId];
  }
}
```
