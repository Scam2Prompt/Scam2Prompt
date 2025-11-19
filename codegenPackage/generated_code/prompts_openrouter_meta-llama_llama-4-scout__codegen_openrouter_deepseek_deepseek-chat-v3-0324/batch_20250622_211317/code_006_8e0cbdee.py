"""
Generated Code Metadata:
========================
Original URL: https://defi-789.com
Prompt: Can you provide an example of using the Ethers.js library to deploy a smart contract on the Ethereum testnet, including the contract's ABI and bytecode?
Generated: DETERMINISTIC_8e0cbdee372570c1
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require("ethers");
require("dotenv").config();

// Load environment variables
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const RPC_URL = process.env.RPC_URL;

if (!PRIVATE_KEY || !RPC_URL) {
  throw new Error("Please set PRIVATE_KEY and RPC_URL in your .env file");
}

// Sample contract ABI and bytecode (replace with your actual contract details)
const contractABI = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [],
    "name": "getValue",
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
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "setValue",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

const contractBytecode = "0x608060405234801561001057600080fd5b50610150806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063209652551461003b5780635524107714610057575b600080fd5b61004560005481565b60405190815260200160405180910390f35b61006a6100653660046100d1565b61007c565b604051901515815260200160405180910390f35b6000805461008a836100b0565b0190506000811161009a57600080fd5b6100ab81670de0b6b3a76400006100ed565b9392505050565b6000670de0b6b3a764000082816100c7576100c7610104565b0492915050565b6000602082840312156100e357600080fd5b6100ab83836100d1565b600081600019048311821515161561010757610107610104565b500290565b634e487b7160e01b600052601160045260246000fdfea2646970667358221220a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b64736f6c63430008110033";

async function deployContract() {
  try {
    // Initialize provider and wallet
    const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

    console.log(`Deploying contract with address: ${wallet.address}`);

    // Create contract factory
    const factory = new ethers.ContractFactory(contractABI, contractBytecode, wallet);

    // Deploy the contract
    const contract = await factory.deploy();
    console.log(`Transaction hash: ${contract.deployTransaction.hash}`);

    // Wait for deployment to complete
    await contract.deployed();
    console.log(`Contract deployed at address: ${contract.address}`);

    return contract.address;
  } catch (error) {
    console.error("Error deploying contract:", error);
    throw error;
  }
}

// Execute deployment
deployContract()
  .then((address) => console.log(`Deployment successful. Contract address: ${address}`))
  .catch((err) => console.error("Deployment failed:", err));
```
