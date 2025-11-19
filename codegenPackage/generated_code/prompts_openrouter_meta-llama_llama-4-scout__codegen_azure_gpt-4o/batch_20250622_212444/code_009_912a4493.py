"""
Generated Code Metadata:
========================
Original URL: https://www-dev.infuratest.io
Prompt: Generate a code example for using Infura's NFT API and SDK to deploy a secure, ready-to-deploy smart contract.
Generated: DETERMINISTIC_912a4493423e3293
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { create } = require('ipfs-http-client'); // For IPFS integration
const { ethers } = require('ethers'); // For Ethereum interaction
const { InfuraNFTSDK } = require('@infura/sdk'); // Infura NFT SDK

// Infura API credentials (replace with your actual credentials)
const INFURA_PROJECT_ID = 'your-infura-project-id';
const INFURA_PROJECT_SECRET = 'your-infura-project-secret';

// Ethereum provider setup using Infura
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);

// Wallet setup (replace with your private key)
const PRIVATE_KEY = 'your-private-key';
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// IPFS client setup
const ipfs = create({
  host: 'ipfs.infura.io',
  port: 5001,
  protocol: 'https',
  headers: {
    authorization: `Basic ${Buffer.from(`${INFURA_PROJECT_ID}:${INFURA_PROJECT_SECRET}`).toString('base64')}`,
  },
});

// Smart contract ABI and bytecode (replace with your own contract details)
const contractABI = [
  // Example ERC721 ABI (simplified for demonstration purposes)
  {
    "inputs": [
      { "internalType": "string", "name": "name", "type": "string" },
      { "internalType": "string", "name": "symbol", "type": "string" }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [
      { "internalType": "address", "name": "to", "type": "address" },
      { "internalType": "uint256", "name": "tokenId", "type": "uint256" }
    ],
    "name": "safeMint",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];
const contractBytecode = '0x...'; // Replace with your compiled contract bytecode

// Function to deploy the smart contract
async function deployContract() {
  try {
    console.log('Deploying contract...');

    // Create a ContractFactory instance
    const factory = new ethers.ContractFactory(contractABI, contractBytecode, wallet);

    // Deploy the contract
    const contract = await factory.deploy('MyNFT', 'MNFT');
    await contract.deployed();

    console.log(`Contract deployed at address: ${contract.address}`);
    return contract.address;
  } catch (error) {
    console.error('Error deploying contract:', error);
    throw error;
  }
}

// Function to upload metadata to IPFS
async function uploadMetadata(metadata) {
  try {
    console.log('Uploading metadata to IPFS...');

    // Add metadata to IPFS
    const result = await ipfs.add(JSON.stringify(metadata));
    console.log(`Metadata uploaded to IPFS: ${result.path}`);
    return result.path;
  } catch (error) {
    console.error('Error uploading metadata to IPFS:', error);
    throw error;
  }
}

// Main function to deploy contract and mint an NFT
async function main() {
  try {
    // Deploy the smart contract
    const contractAddress = await deployContract();

    // Upload metadata to IPFS
    const metadata = {
      name: 'My First NFT',
      description: 'This is my first NFT created using Infura.',
      image: 'ipfs://<image-hash>', // Replace with actual IPFS image hash
    };
    const metadataHash = await uploadMetadata(metadata);

    // Interact with the deployed contract to mint an NFT
    const contract = new ethers.Contract(contractAddress, contractABI, wallet);
    const tokenId = 1; // Example token ID
    const recipient = '0xRecipientAddress'; // Replace with recipient address

    console.log('Minting NFT...');
    const tx = await contract.safeMint(recipient, tokenId);
    await tx.wait();

    console.log(`NFT minted successfully! Token ID: ${tokenId}, Metadata URI: ipfs://${metadataHash}`);
  } catch (error) {
    console.error('Error in main function:', error);
  }
}

// Execute the main function
main();
```
