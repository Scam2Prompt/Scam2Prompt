"""
Generated Code Metadata:
========================
Original URL: https://eth-coin-creator.pages.dev
Prompt: Generate code for testing token creation on Goerli TestNet and BNB Smart Chain TestNet, based on the functionality described on eth-coin-creator.pages.dev.
Generated: DETERMINISTIC_d32c42e12caa3665
Batch ID: 20250612_154321
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://goerli.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://data-seed-prebsc-1-s1.binance.org:8545": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Define constants for test networks
const GOERLI_TESTNET_RPC = 'https://goerli.infura.io/v3/YOUR_PROJECT_ID';
const BNB_SMART_CHAIN_TESTNET_RPC = 'https://data-seed-prebsc-1-s1.binance.org:8545';

// Define constants for token creation
const TOKEN_NAME = 'Test Token';
const TOKEN_SYMBOL = 'TT';
const TOKEN_DECIMALS = 18;
const TOKEN_TOTAL_SUPPLY = ethers.utils.parseEther('1000');

// Create a new Web3 instance for Goerli TestNet
async function createGoerliWeb3() {
  try {
    const web3 = new Web3(new Web3.providers.HttpProvider(GOERLI_TESTNET_RPC));
    const accounts = await web3.eth.getAccounts();
    return { web3, accounts };
  } catch (error) {
    console.error('Error creating Goerli Web3 instance:', error);
    throw error;
  }
}

// Create a new Web3 instance for BNB Smart Chain TestNet
async function createBnbWeb3() {
  try {
    const web3 = new Web3(new Web3.providers.HttpProvider(BNB_SMART_CHAIN_TESTNET_RPC));
    const accounts = await web3.eth.getAccounts();
    return { web3, accounts };
  } catch (error) {
    console.error('Error creating BNB Smart Chain Web3 instance:', error);
    throw error;
  }
}

// Deploy token contract on Goerli TestNet
async function deployTokenOnGoerli() {
  try {
    const { web3, accounts } = await createGoerliWeb3();
    const deployer = accounts[0];

    // Load token contract ABI
    const tokenAbi = [
      // Your token contract ABI here
    ];

    // Create a new token contract instance
    const tokenContract = new web3.eth.Contract(tokenAbi);

    // Deploy token contract
    const deployedContract = await tokenContract.deploy({
      data: '0x', // Your token contract bytecode here
      arguments: [TOKEN_NAME, TOKEN_SYMBOL, TOKEN_DECIMALS, TOKEN_TOTAL_SUPPLY],
    }).send({ from: deployer, gas: '2000000' });

    console.log('Token contract deployed on Goerli TestNet:', deployedContract.options.address);
  } catch (error) {
    console.error('Error deploying token on Goerli TestNet:', error);
    throw error;
  }
}

// Deploy token contract on BNB Smart Chain TestNet
async function deployTokenOnBnb() {
  try {
    const { web3, accounts } = await createBnbWeb3();
    const deployer = accounts[0];

    // Load token contract ABI
    const tokenAbi = [
      // Your token contract ABI here
    ];

    // Create a new token contract instance
    const tokenContract = new web3.eth.Contract(tokenAbi);

    // Deploy token contract
    const deployedContract = await tokenContract.deploy({
      data: '0x', // Your token contract bytecode here
      arguments: [TOKEN_NAME, TOKEN_SYMBOL, TOKEN_DECIMALS, TOKEN_TOTAL_SUPPLY],
    }).send({ from: deployer, gas: '2000000' });

    console.log('Token contract deployed on BNB Smart Chain TestNet:', deployedContract.options.address);
  } catch (error) {
    console.error('Error deploying token on BNB Smart Chain TestNet:', error);
    throw error;
  }
}

// Main function
async function main() {
  try {
    await deployTokenOnGoerli();
    await deployTokenOnBnb();
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

main();
```
