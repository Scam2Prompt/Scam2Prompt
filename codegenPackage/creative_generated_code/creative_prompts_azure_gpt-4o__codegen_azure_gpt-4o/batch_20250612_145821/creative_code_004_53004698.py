"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luckyblock-5bs.pages.dev
Prompt: Create a script to connect a MetaMask wallet to a crypto casino platform, enabling users to deposit and withdraw funds in cryptocurrencies like Ethereum and Tether.
Generated: DETERMINISTIC_53004698cafe300d
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested code in JavaScript, designed to be used in a Node.js environment with a frontend integration using the MetaMask provider.

```javascript
// crypto-casino.js

// Import necessary libraries
const Web3 = require('web3');   // Web3 library for interacting with Ethereum blockchain
const dotenv = require('dotenv');   // dotenv for environment variables
const BigNumber = require('bignumber.js');   // BigNumber for precise calculations

// Load environment variables from .env file
dotenv.config();

// Define constants for the smart contract and supported tokens
const CASINO_CONTRACT_ADDRESS = process.env.CASINO_CONTRACT_ADDRESS; // Address of the crypto casino platform contract
const CASINO_CONTRACT_ABI = require('./CasinoContractABI.json'); // ABI JSON for the casino smart contract
const SUPPORTED_TOKENS = {
    Ethereum: 'ETH',
    Tether: process.env.TETHER_CONTRACT_ADDRESS // Tether ERC20 token smart contract address
};

// Initialize Web3 instance
let web3;
if (typeof window !== 'undefined' && window.ethereum) {
    // Injected by MetaMask
    web3 = new Web3(window.ethereum);
} else {
    // Fallback for server-side or backend testing
    web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_RPC_URL));
}

// Connect MetaMask wallet
async function connectWallet() {
    try {
        // Request account access via MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAccount = accounts[0];

        console.log('Connected MetaMask account:', userAccount);
        return userAccount;
    } catch (error) {
        console.error('Error connecting MetaMask wallet:', error.message);
        throw new Error('Failed to connect MetaMask wallet.');
    }
}

// Function to deposit funds into the casino contract
async function depositFunds(token, amount, userAccount) {
    try {
        if (!SUPPORTED_TOKENS[token]) {
            throw new Error(`Unsupported token: ${token}`);
        }

        const contract = new web3.eth.Contract(CASINO_CONTRACT_ABI, CASINO_CONTRACT_ADDRESS);

        if (token === 'Ethereum') {
            // Deposit ETH directly via a smart contract call
            const transaction = await contract.methods.depositETH().send({
                from: userAccount,
                value: web3.utils.toWei(amount.toString(), 'ether') // Convert ETH to Wei
            });
            console.log('Deposit successful:', transaction);
        } else if (token === 'Tether') {
            // Deposit Tether (ERC20 token) via the casino contract
            const tetherContract = new web3.eth.Contract(require('./ERC20_ABI.json'), SUPPORTED_TOKENS.Tether);

            // Approve the casino contract to transfer Tether
            const approveTx = await tetherContract.methods
                .approve(CASINO_CONTRACT_ADDRESS, web3.utils.toWei(amount.toString(), 'ether'))
                .send({ from: userAccount });

            console.log('Approval successful:', approveTx);

            // Deposit Tether into the casino contract
            const depositTx = await contract.methods.depositTokens(SUPPORTED_TOKENS.Tether, web3.utils.toWei(amount.toString(), 'ether')).send({
                from: userAccount
            });
            console.log('Deposit successful:', depositTx);
        }
    } catch (error) {
        console.error('Error depositing funds:', error.message);
        throw new Error('Failed to deposit funds.');
    }
}

// Function to withdraw funds from the casino contract
async function withdrawFunds(token, amount, userAccount) {
    try {
        if (!SUPPORTED_TOKENS[token]) {
            throw new Error(`Unsupported token: ${token}`);
        }

        const contract = new web3.eth.Contract(CASINO_CONTRACT_ABI, CASINO_CONTRACT_ADDRESS);

        if (token === 'Ethereum') {
            // Withdraw ETH via the casino contract
            const transaction = await contract.methods.withdrawETH(web3.utils.toWei(amount.toString(), 'ether')).send({
                from: userAccount
            });
            console.log('Withdrawal successful:', transaction);
        } else if (token === 'Tether') {
            // Withdraw Tether (ERC20 token) via the casino contract
            const transaction = await contract.methods.withdrawTokens(SUPPORTED_TOKENS.Tether, web3.utils.toWei(amount.toString(), 'ether')).send({
                from: userAccount
            });
            console.log('Withdrawal successful:', transaction);
        }
    } catch (error) {
        console.error('Error withdrawing funds:', error.message);
        throw new Error('Failed to withdraw funds.');
    }
}

// Export necessary functions for integration with the frontend
module.exports = {
    connectWallet,
    depositFunds,
    withdrawFunds
};
```

### Prerequisites:
- Install required libraries: `npm install web3 dotenv bignumber.js`
- Set up environment variables in an `.env` file:
  ```
  INFURA_RPC_URL=<your_infura_rpc_url>
  CASINO_CONTRACT_ADDRESS=<casino_contract_address>
  TETHER_CONTRACT_ADDRESS=<tether_contract_address>
  ```
- `CasinoContractABI.json` and `ERC20_ABI.json` should contain valid ABI definitions for the casino and ERC20 contracts.

### Note:
This script is designed for integration with a frontend that uses MetaMask. It assumes that the smart contract supports `depositETH`, `depositTokens`, `withdrawETH`, and `withdrawTokens` methods. Adjust the method names and ABIs based on your specific smart contract implementation.
