"""
Generated Code Metadata:
========================
Original URL: https://ethdrt.com
Prompt: Write JavaScript code to interact with an Ethereum smart contract for pledging funds using Web3.js.
Generated: DETERMINISTIC_ef6d480fac4adae5
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Set up Web3 provider
const INFURA_PROJECT_ID = 'YOUR_PROJECT_ID';
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);

// Set up contract ABI and address
const CONTRACT_ABI = [
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
        "name": "pledger",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "PledgeMade",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "pledgeAmount",
    "outputs": [
      {
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
        "name": "",
        "type": "address"
      }
    ],
    "name": "pledges",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "totalPledged",
    "outputs": [
      {
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
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "makePledge",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];
const CONTRACT_ADDRESS = '0x...';

// Create contract instance
const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, provider);

// Function to make a pledge
async function makePledge(amount) {
  try {
    // Get signer (account making the transaction)
    const signer = await provider.getSigner();

    // Call contract's makePledge function
    const tx = await contract.connect(signer).makePledge(amount);
    await tx.wait();

    console.log(`Pledge of ${amount} made successfully!`);
  } catch (error) {
    console.error('Error making pledge:', error);
  }
}

// Function to get total pledged amount
async function getTotalPledged() {
  try {
    const totalPledged = await contract.totalPledged();
    console.log(`Total pledged: ${totalPledged.toString()}`);
  } catch (error) {
    console.error('Error getting total pledged:', error);
  }
}

// Function to get pledge amount for a specific address
async function getPledge(address) {
  try {
    const pledge = await contract.pledges(address);
    console.log(`Pledge for ${address}: ${pledge.toString()}`);
  } catch (error) {
    console.error('Error getting pledge:', error);
  }
}

// Example usage
async function main() {
  // Make a pledge of 1 ETH
  await makePledge(ethers.utils.parseEther('1'));

  // Get total pledged amount
  await getTotalPledged();

  // Get pledge amount for a specific address
  const address = '0x...';
  await getPledge(address);
}

main();
```
