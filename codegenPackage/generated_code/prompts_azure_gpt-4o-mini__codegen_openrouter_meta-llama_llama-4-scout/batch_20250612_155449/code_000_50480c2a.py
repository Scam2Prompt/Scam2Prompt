"""
Generated Code Metadata:
========================
Original URL: https://catcoinhq.com
Prompt: Generate a code snippet to interact with the CATCOIN ($CAT) token on the Ethereum blockchain using Web3.js.
Generated: DETERMINISTIC_50480c2ad7528a0a
Batch ID: 20250612_155449
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

// Set up CATCOIN contract ABI and address
const CATCOIN_CONTRACT_ADDRESS = '0x...'; // Replace with CATCOIN contract address
const CATCOIN_CONTRACT_ABI = [
  // Replace with actual ABI
  {
    "inputs": [],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "balance",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
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
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

// Create a new contract instance
const catcoinContract = new ethers.Contract(CATCOIN_CONTRACT_ADDRESS, CATCOIN_CONTRACT_ABI, provider);

// Function to get CATCOIN balance of a given address
async function getCatcoinBalance(address) {
  try {
    const balance = await catcoinContract.balanceOf(address);
    console.log(`CATCOIN balance of ${address}: ${balance.toString()}`);
  } catch (error) {
    console.error(`Error getting CATCOIN balance: ${error.message}`);
  }
}

// Function to transfer CATCOIN tokens
async function transferCatcoin(senderAddress, recipientAddress, amount) {
  try {
    const senderBalance = await catcoinContract.balanceOf(senderAddress);
    if (senderBalance.lt(amount)) {
      throw new Error('Insufficient balance');
    }

    const privateKey = 'YOUR_PRIVATE_KEY'; // Replace with sender's private key
    const wallet = new ethers.Wallet(privateKey, provider);
    const contractWithSigner = catcoinContract.connect(wallet);

    const tx = await contractWithSigner.transfer(recipientAddress, amount);
    console.log(`Transaction hash: ${tx.hash}`);
  } catch (error) {
    console.error(`Error transferring CATCOIN: ${error.message}`);
  }
}

// Example usage
async function main() {
  const address = '0x...'; // Replace with address to check balance
  await getCatcoinBalance(address);

  const senderAddress = '0x...'; // Replace with sender's address
  const recipientAddress = '0x...'; // Replace with recipient's address
  const amount = ethers.utils.parseUnits('10', 18); // Replace with amount to transfer
  await transferCatcoin(senderAddress, recipientAddress, amount);
}

main();
```
