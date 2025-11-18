"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enkixyz.vercel.app
Prompt: Write a script to automate the process of staking and unstaking Metis tokens on the ENKI Protocol testnet using Web3.js.
Generated: DETERMINISTIC_6756cfc1645a0f4b
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');
const { abi: stakingAbi } = require('./StakingContractABI.json'); // Ensure ABI JSON file is in the same directory
require('dotenv').config(); // Load environment variables from .env

// Environment variables
const RPC_URL = process.env.RPC_URL; // Testnet RPC URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key
const STAKING_CONTRACT_ADDRESS = process.env.STAKING_CONTRACT_ADDRESS; // ENKI Protocol staking contract address

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(RPC_URL));

// Get wallet account from private key
const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
web3.eth.accounts.wallet.add(account);
web3.eth.defaultAccount = account.address;

// Load staking contract
const stakingContract = new web3.eth.Contract(stakingAbi, STAKING_CONTRACT_ADDRESS);

/**
 * Stakes Metis tokens on the ENKI Protocol.
 * @param {string} amount - Amount of Metis tokens to stake (in wei).
 */
async function stake(amount) {
    try {
        console.log(`Staking ${web3.utils.fromWei(amount, 'ether')} Metis tokens...`);

        const tx = stakingContract.methods.stake(amount);
        const gas = await tx.estimateGas({ from: account.address });
        const gasPrice = await web3.eth.getGasPrice();

        const transaction = tx.send({
            from: account.address,
            gas,
            gasPrice,
        });

        transaction.on('transactionHash', (hash) => {
            console.log(`Transaction sent. Hash: ${hash}`);
        });

        transaction.on('receipt', (receipt) => {
            console.log(`Transaction confirmed. Receipt:`, receipt);
        });

        transaction.on('error', (error) => {
            console.error(`Error during staking:`, error);
        });

    } catch (error) {
        console.error(`Failed to stake:`, error);
    }
}

/**
 * Unstakes Metis tokens from the ENKI Protocol.
 */
async function unstake() {
    try {
        console.log(`Unstaking Metis tokens...`);

        const tx = stakingContract.methods.unstake();
        const gas = await tx.estimateGas({ from: account.address });
        const gasPrice = await web3.eth.getGasPrice();

        const transaction = tx.send({
            from: account.address,
            gas,
            gasPrice,
        });

        transaction.on('transactionHash', (hash) => {
            console.log(`Transaction sent. Hash: ${hash}`);
        });

        transaction.on('receipt', (receipt) => {
            console.log(`Transaction confirmed. Receipt:`, receipt);
        });

        transaction.on('error', (error) => {
            console.error(`Error during unstaking:`, error);
        });

    } catch (error) {
        console.error(`Failed to unstake:`, error);
    }
}

// Example usage: Replace with the actual amount to stake (in wei).
(async () => {
    const amountToStake = web3.utils.toWei('1', 'ether'); // Stake 1 Metis token

    await stake(amountToStake);
    // Uncomment below line to unstake (ensure staking has been done before this step).
    // await unstake();
})();
```

**Instructions for Deployment:**
1. Install dependencies: `npm install web3 dotenv`.
2. Ensure `.env` file is properly configured with:
   - `RPC_URL` (Metis testnet RPC URL),
   - `PRIVATE_KEY` (your wallet private key),
   - `STAKING_CONTRACT_ADDRESS` (ENKI Protocol staking contract address).
3. Save the staking contract ABI in `StakingContractABI.json` (in the script's directory).
4. Run the script using `node script.js`.
