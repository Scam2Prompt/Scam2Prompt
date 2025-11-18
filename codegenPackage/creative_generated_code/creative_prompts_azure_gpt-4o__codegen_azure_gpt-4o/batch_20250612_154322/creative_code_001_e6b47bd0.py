"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erc20-creator.pages.dev
Prompt: Generate code to integrate Ethereum Wallet Connect functionality for creating and managing ERC-20 tokens, as outlined on the https://erc20-creator.pages.dev website.
Generated: DETERMINISTIC_e6b47bd096ac0030
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider';

// Configure Wallet Connect Provider
const provider = new WalletConnectProvider({
  infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
});

// Initialize Web3 instance
const web3 = new Web3(provider);

// ERC-20 Token Contract ABI
const ERC20_ABI = [
  {
    "constant": true,
    "inputs": [],
    "name": "name",
    "outputs": [{"name": "", "type": "string"}],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}],
    "name": "approve",
    "outputs": [{"name": "", "type": "bool"}],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "totalSupply",
    "outputs": [{"name": "", "type": "uint256"}],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{"name": "_from", "type": "address"}, {"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
    "name": "transferFrom",
    "outputs": [{"name": "", "type": "bool"}],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "decimals",
    "outputs": [{"name": "", "type": "uint8"}],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "symbol",
    "outputs": [{"name": "", "type": "string"}],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
    "name": "transfer",
    "outputs": [{"name": "", "type": "bool"}],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [{"name": "_owner", "type": "address"}],
    "name": "balanceOf",
    "outputs": [{"name": "balance", "type": "uint256"}],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{"name": "_owner", "type": "address"}, {"name": "_spender", "type": "address"}],
    "name": "allowance",
    "outputs": [{"name": "", "type": "uint256"}],
    "type": "function"
  },
  {
    "inputs": [{"name": "_name", "type": "string"}, {"name": "_symbol", "type": "string"}, {"name": "_decimals", "type": "uint8"}, {"name": "_totalSupply", "type": "uint256"}],
    "type": "constructor"
  },
  {
    "payable": false,
    "type": "fallback"
  },
  {
    "anonymous": false,
    "inputs": [{"indexed": true, "name": "owner", "type": "address"}, {"indexed": true, "name": "spender", "type": "address"}, {"indexed": false, "name": "value", "type": "uint256"}],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [{"indexed": true, "name": "from", "type": "address"}, {"indexed": true, "name": "to", "type": "address"}, {"indexed": false, "name": "value", "type": "uint256"}],
    "name": "Transfer",
    "type": "event"
  }
];

// Function to connect wallet
async function connectWallet() {
  try {
    // Enable provider
    await provider.enable();

    // Get connected accounts
    const accounts = await web3.eth.getAccounts();
    console.log('Connected accounts:', accounts);

    return accounts[0]; // Return first account
  } catch (error) {
    console.error('Error connecting wallet:', error);
    throw error;
  }
}

// Function to deploy ERC-20 token contract
async function deployTokenContract(name, symbol, decimals, totalSupply, fromAddress) {
  try {
    // Define ERC-20 contract bytecode and arguments
    const ERC20_BYTECODE = "YOUR_CONTRACT_BYTECODE_HERE"; // Replace with actual bytecode
    const erc20Contract = new web3.eth.Contract(ERC20_ABI);

    // Deploy contract
    const deployedContract = await erc20Contract.deploy({
      data: ERC20_BYTECODE,
      arguments: [name, symbol, decimals, totalSupply],
    }).send({
      from: fromAddress,
      gas: 1500000,
      gasPrice: '30000000000',
    });

    console.log('Contract deployed at:', deployedContract.options.address);
    return deployedContract.options.address; // Return contract address
  } catch (error) {
    console.error('Error deploying token contract:', error);
    throw error;
  }
}

// Example usage
(async function main() {
  try {
    console.log('Connecting wallet...');
    const userAddress = await connectWallet();

    console.log('Deploying ERC-20 contract...');
    const contractAddress = await deployTokenContract(
      'MyToken',     // Token name
      'MTK',         // Token symbol
      18,            // Decimals
      web3.utils.toWei('1000000', 'ether'), // Total supply (1 million tokens)
      userAddress    // Wallet address to deploy from
    );

    console.log('ERC-20 Contract Address:', contractAddress);
  } catch (error) {
    console.error('Error in main function:', error);
  }
})();
```

### Notes:
1. Replace `"YOUR_INFURA_PROJECT_ID"` with your Infura project ID.
2. Replace `"YOUR_CONTRACT_BYTECODE_HERE"` with the bytecode of the ERC-20 token smart contract.
3. Ensure you have enough Ether in your wallet to cover gas fees for deploying the contract.
