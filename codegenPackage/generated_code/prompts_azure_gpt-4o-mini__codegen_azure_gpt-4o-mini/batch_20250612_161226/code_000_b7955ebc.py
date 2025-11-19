"""
Generated Code Metadata:
========================
Original URL: https://aptekaimed.ru
Prompt: Explain how to use Beefy Finance for automated investment strategies in DeFi, including steps to connect a wallet and choose liquidity pools.
Generated: DETERMINISTIC_b7955ebccc2a8524
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';
import BeefyFinance from 'beefy-sdk'; // Hypothetical SDK for Beefy Finance

// Initialize Web3 and Beefy Finance
const web3 = new Web3(window.ethereum);
const beefy = new BeefyFinance();

// Function to connect to the user's wallet
async function connectWallet() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Error connecting to wallet:', error);
        throw new Error('Wallet connection failed');
    }
}

// Function to fetch available liquidity pools
async function fetchLiquidityPools() {
    try {
        const pools = await beefy.getLiquidityPools();
        console.log('Available Liquidity Pools:', pools);
        return pools;
    } catch (error) {
        console.error('Error fetching liquidity pools:', error);
        throw new Error('Failed to fetch liquidity pools');
    }
}

// Function to select a liquidity pool and invest
async function investInPool(poolId, amount, account) {
    try {
        // Check if the poolId is valid
        const pool = await beefy.getPoolById(poolId);
        if (!pool) {
            throw new Error('Invalid pool ID');
        }

        // Convert amount to the appropriate format (e.g., wei)
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Approve the token transfer
        const tokenContract = new web3.eth.Contract(pool.tokenABI, pool.tokenAddress);
        await tokenContract.methods.approve(beefy.contractAddress, amountInWei).send({ from: account });

        // Invest in the selected pool
        const tx = await beefy.invest(poolId, amountInWei, { from: account });
        console.log('Investment transaction:', tx);
        return tx;
    } catch (error) {
        console.error('Error investing in pool:', error);
        throw new Error('Investment failed');
    }
}

// Main function to execute the investment strategy
async function main() {
    try {
        const account = await connectWallet();
        const pools = await fetchLiquidityPools();

        // Example: Automatically invest in the first available pool
        if (pools.length > 0) {
            const poolId = pools[0].id; // Select the first pool
            const amount = 1; // Amount to invest in ETH
            await investInPool(poolId, amount, account);
        } else {
            console.log('No liquidity pools available for investment.');
        }
    } catch (error) {
        console.error('Error in main execution:', error);
    }
}

// Execute the main function
main();
```

**Note:** This code assumes the existence of a hypothetical `beefy-sdk` for interacting with Beefy Finance. Adjustments may be necessary based on the actual SDK or API used.
