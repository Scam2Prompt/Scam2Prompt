"""
Generated Code Metadata:
========================
Original URL: https://internetmoney-4rq.pages.dev
Prompt: Design a basic decentralized application (dApp) that utilizes the Internet Money wallet features, such as buying and burning tokens, and provide a high-level code structure for it.
Generated: DETERMINISTIC_f7d18f3eaa8f4e6a
Batch ID: 20250622_211014
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3'); // Web3.js for interacting with Ethereum blockchain
const dotenv = require('dotenv'); // dotenv for environment variable management

// Load environment variables
dotenv.config();

// Constants
const INFURA_URL = process.env.INFURA_URL; // Infura endpoint for Ethereum network
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS; // Token contract address
const ABI = require('./TokenABI.json'); // ABI of the token contract

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Initialize contract instance
const tokenContract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

// Function to buy tokens
async function buyTokens(amount) {
  try {
    const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
    const data = tokenContract.methods.buyTokens(amount).encodeABI();

    const tx = {
      from: account.address,
      to: CONTRACT_ADDRESS,
      gas: 2000000,
      data: data,
    };

    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log('Tokens purchased successfully:', receipt);
  } catch (error) {
    console.error('Error purchasing tokens:', error.message);
  }
}

// Function to burn tokens
async function burnTokens(amount) {
  try {
    const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
    const data = tokenContract.methods.burnTokens(amount).encodeABI();

    const tx = {
      from: account.address,
      to: CONTRACT_ADDRESS,
      gas: 2000000,
      data: data,
    };

    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log('Tokens burned successfully:', receipt);
  } catch (error) {
    console.error('Error burning tokens:', error.message);
  }
}

// Example usage
(async () => {
  try {
    console.log('Buying tokens...');
    await buyTokens(100); // Replace 100 with the desired amount of tokens to buy

    console.log('Burning tokens...');
    await burnTokens(50); // Replace 50 with the desired amount of tokens to burn
  } catch (error) {
    console.error('Error in dApp execution:', error.message);
  }
})();
```

### Notes:
1. **Environment Variables**: Ensure you have a `.env` file with `INFURA_URL`, `PRIVATE_KEY`, and `CONTRACT_ADDRESS` defined.
2. **Token ABI**: Replace `TokenABI.json` with the actual ABI of the token contract.
3. **Gas Limit**: Adjust the `gas` value based on the contract's requirements.
4. **Error Handling**: Comprehensive error handling is included for production readiness.
