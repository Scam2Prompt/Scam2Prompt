"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancake-eat-about.at
Prompt: Develop code to automate staking and unstaking CAKE tokens on PancakeSwap Syrup Pools, ensuring flexibility in managing funds.
Generated: DETERMINISTIC_bd023a937eadbfc1
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const { Contract } = require('web3-eth-contract');

// Configure web3 and PancakeSwap contract addresses
const web3 = new Web3(new Web3.providers.HttpProvider('<YOUR_INFURA_OR_ETHEREUM_NODE_URL>'));
const CAKE_TOKEN_ADDRESS = '<CAKE_TOKEN_CONTRACT_ADDRESS>';
const SYRUP_POOL_ADDRESS = '<SYRUP_POOL_CONTRACT_ADDRESS>';
const PRIVATE_KEY = '<YOUR_PRIVATE_KEY>'; // Use environment variable for security
const MY_ADDRESS = '<YOUR_WALLET_ADDRESS>';

// Load ABI files for CAKE Token and Syrup Pool
const cakeTokenABI = require('./CakeTokenABI.json'); // Replace with actual ABI JSON file
const syrupPoolABI = require('./SyrupPoolABI.json'); // Replace with actual ABI JSON file

// Create contract instances
const cakeToken = new Contract(cakeTokenABI, CAKE_TOKEN_ADDRESS);
const syrupPool = new Contract(syrupPoolABI, SYRUP_POOL_ADDRESS);

// Function to stake CAKE tokens
const stakeTokens = async (amount) => {
    try {
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Approve the Syrup Pool to spend CAKE tokens
        const approveTx = await cakeToken.methods.approve(SYRUP_POOL_ADDRESS, amountInWei).send({ from: MY_ADDRESS });
        console.log(`Approve Transaction Hash: ${approveTx.transactionHash}`);

        // Stake CAKE tokens in the Syrup Pool
        const stakeTx = await syrupPool.methods.stake(amountInWei).send({ from: MY_ADDRESS });
        console.log(`Stake Transaction Hash: ${stakeTx.transactionHash}`);
    } catch (error) {
        console.error('Error staking tokens:', error);
    }
};

// Function to unstake CAKE tokens
const unstakeTokens = async (amount) => {
    try {
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Unstake CAKE tokens from the Syrup Pool
        const unstakeTx = await syrupPool.methods.unstake(amountInWei).send({ from: MY_ADDRESS });
        console.log(`Unstake Transaction Hash: ${unstakeTx.transactionHash}`);
    } catch (error) {
        console.error('Error unstaking tokens:', error);
    }
};

// Example usage
const main = async () => {
    const stakeAmount = 1; // Specify amount to stake
    const unstakeAmount = 0.5; // Specify amount to unstake

    await stakeTokens(stakeAmount);
    await unstakeTokens(unstakeAmount);
};

// Run the main function
main().catch((error) => {
    console.error('Error in main execution:', error);
});
```

Make sure to replace placeholder values like `<YOUR_INFURA_OR_ETHEREUM_NODE_URL>`, `<CAKE_TOKEN_CONTRACT_ADDRESS>`, `<SYRUP_POOL_CONTRACT_ADDRESS>`, `<YOUR_PRIVATE_KEY>`, and `<YOUR_WALLET_ADDRESS>` with actual values before running the code. Additionally, save the correct ABI files for the CAKE token and Syrup Pool in the same directory or update the paths accordingly. Always handle your private key securely and consider using environment variables to load sensitive information.
