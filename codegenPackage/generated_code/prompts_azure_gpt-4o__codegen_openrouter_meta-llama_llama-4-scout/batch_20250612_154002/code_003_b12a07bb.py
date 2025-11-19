"""
Generated Code Metadata:
========================
Original URL: https://erc20-eth.vip
Prompt: Provide an example of JavaScript code that interacts with an ERC-20 token contract using Web3.js, focusing on token transfers in a DeFi context.
Generated: DETERMINISTIC_b12a07bb4b895a34
Batch ID: 20250612_154002
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

// Set up ERC-20 token contract ABI and address
const ERC20_ABI = [
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
        "name": "authority",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "operator",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "isAuthorized",
        "type": "bool"
      }
    ],
    "name": "LogSetAuthorized",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "authority",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "LogSetOwner",
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
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
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
        "name": "spender",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "inputs": [
      {
        "name": "symbol_",
        "type": "string"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function",
    "name": "setSymbol"
  },
  {
    "inputs": [
      {
        "name": "authority_",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function",
    "name": "setAuthority"
  },
  {
    "inputs": [
      {
        "name": "owner_",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function",
    "name": "setOwner"
  },
  {
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "authority",
    "outputs": [
      {
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
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
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
    "name": "owner",
    "outputs": [
      {
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
        "name": "from",
        "type": "address"
      },
      {
        "name": "to",
        "type": "address"
      },
      {
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "owner",
        "type": "address"
      },
      {
        "name": "spender",
        "type": "address"
      }
    ],
    "name": "allowance",
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
        "name": "spender",
        "type": "address"
      },
      {
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "to",
        "type": "address"
      },
      {
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "totalSupply",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

const ERC20_CONTRACT_ADDRESS = '0x...'; // Replace with actual contract address

// Create a new ERC-20 token contract instance
const contract = new ethers.Contract(ERC20_CONTRACT_ADDRESS, ERC20_ABI, provider);

// Set up wallet and signer
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY';
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
const signer = wallet.connect(provider);

// Function to transfer ERC-20 tokens
async function transferTokens(toAddress, amount) {
  try {
    // Get current balance
    const balance = await contract.balanceOf(signer.address);
    console.log(`Current balance: ${balance}`);

    // Check if sufficient balance
    if (balance.lt(amount)) {
      throw new Error('Insufficient balance');
    }

    // Approve and transfer tokens
    const tx = await contract.transfer(toAddress, amount, { gasLimit: 20000 });
    console.log(`Transaction hash: ${tx.hash}`);

    // Wait for transaction confirmation
    await tx.wait();
    console.log('Tokens transferred successfully');
  } catch (error) {
    console.error('Error transferring tokens:', error);
  }
}

// Example usage
async function main() {
  const toAddress = '0x...'; // Replace with recipient address
  const amount = ethers.utils.parseEther('1'); // 1 token

  await transferTokens(toAddress, amount);
}

main().catch((error) => console.error('Error:', error));
```
