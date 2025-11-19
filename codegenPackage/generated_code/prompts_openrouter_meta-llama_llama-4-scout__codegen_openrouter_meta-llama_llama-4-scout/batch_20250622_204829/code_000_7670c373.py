"""
Generated Code Metadata:
========================
Original URL: https://imltovken.com
Prompt: How can I implement an Ethereum pledge system using JavaScript and Web3.js library?
Generated: DETERMINISTIC_7670c373dc5d0af7
Batch ID: 20250622_204829
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
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID';
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);

// Set up contract ABI and address
const PLEDGE_CONTRACT_ABI = [
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
        "indexed": true,
        "name": "pledgeAmount",
        "type": "uint256"
      }
    ],
    "name": "PledgeMade",
    "type": "event"
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
        "indexed": true,
        "name": "unpledgeAmount",
        "type": "uint256"
      }
    ],
    "name": "UnpledgeMade",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "getPledgeBalance",
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
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "makePledge",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "unpledge",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];
const PLEDGE_CONTRACT_ADDRESS = 'YOUR_PLEDGE_CONTRACT_ADDRESS';

// Create contract instance
const contract = new ethers.Contract(PLEDGE_CONTRACT_ADDRESS, PLEDGE_CONTRACT_ABI, provider);

// Connect to Ethereum wallet
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY';
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
const contractWithSigner = contract.connect(wallet);

// Pledge system functions
async function makePledge(amount) {
  try {
    // Validate amount
    if (typeof amount !== 'number' || amount <= 0) {
      throw new Error('Invalid pledge amount');
    }

    // Convert amount to wei
    const weiAmount = ethers.utils.parseEther(amount.toString());

    // Make pledge
    const tx = await contractWithSigner.makePledge(weiAmount);
    await tx.wait();

    console.log(`Pledge made: ${amount} ETH`);
  } catch (error) {
    console.error('Error making pledge:', error);
  }
}

async function unpledge(amount) {
  try {
    // Validate amount
    if (typeof amount !== 'number' || amount <= 0) {
      throw new Error('Invalid unpledge amount');
    }

    // Convert amount to wei
    const weiAmount = ethers.utils.parseEther(amount.toString());

    // Unpledge
    const tx = await contractWithSigner.unpledge(weiAmount);
    await tx.wait();

    console.log(`Unpledge made: ${amount} ETH`);
  } catch (error) {
    console.error('Error unpledging:', error);
  }
}

async function getPledgeBalance() {
  try {
    const balance = await contract.getPledgeBalance();
    const etherBalance = ethers.utils.formatEther(balance);

    console.log(`Current pledge balance: ${etherBalance} ETH`);
  } catch (error) {
    console.error('Error getting pledge balance:', error);
  }
}

// Example usage
async function main() {
  await makePledge(1);
  await getPledgeBalance();
  await unpledge(0.5);
  await getPledgeBalance();
}

main();
```
