"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enkixyz.vercel.app
Prompt: How can I implement staking for Metis using the ENKI Protocol on the testnet?
Generated: DETERMINISTIC_50691ca855ef1254
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Necessary imports
const { ethers } = require("ethers"); // Ethereum library for interacting with blockchain
require('dotenv').config();          // For managing environment variables

// Configuration
const provider = new ethers.providers.JsonRpcProvider(process.env.TESTNET_RPC_URL); // Connect to Metis testnet RPC
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);               // Wallet for signing transactions

// ENKI Protocol staking contract ABI (Simplified example, use actual contract ABI from ENKI documentation)
const stakingAbi = [
  "function stake(uint256 amount) public",
  "function claimRewards() public",
  "function withdraw(uint256 amount) public",
  "function getStakedAmount(address account) public view returns (uint256)"
];

// ENKI Protocol staking contract address on Metis testnet
const stakingContractAddress = "0xYourStakingContractAddressHere";

// Instantiate staking contract
const stakingContract = new ethers.Contract(stakingContractAddress, stakingAbi, wallet);

/**
 * Stake tokens in the ENKI Protocol.
 * @param {string} tokenAddress - Address of the token to stake.
 * @param {number} amount - Amount of tokens to stake in wei (smallest unit of token).
 */
async function stakeTokens(tokenAddress, amount) {
  try {
    console.log("Approving tokens for staking...");

    // ERC-20 token ABI (Simplified, use full ABI for production)
    const erc20Abi = [
      "function approve(address spender, uint256 amount) public returns (bool)"
    ];

    // Instantiate token contract
    const tokenContract = new ethers.Contract(tokenAddress, erc20Abi, wallet);

    // Approve staking contract to spend the tokens
    const approveTx = await tokenContract.approve(stakingContractAddress, amount);
    await approveTx.wait(); // Wait for transaction confirmation

    console.log("Tokens approved. Staking now...");

    // Stake tokens into the ENKI Protocol
    const stakeTx = await stakingContract.stake(amount);
    await stakeTx.wait(); // Wait for transaction confirmation

    console.log("Successfully staked tokens.");
  } catch (error) {
    console.error("Error staking tokens:", error);
  }
}

/**
 * Claim staking rewards.
 */
async function claimRewards() {
  try {
    console.log("Claiming rewards...");

    // Claim rewards from the staking contract
    const claimTx = await stakingContract.claimRewards();
    await claimTx.wait(); // Wait for transaction confirmation

    console.log("Successfully claimed rewards.");
  } catch (error) {
    console.error("Error claiming rewards:", error);
  }
}

/**
 * Withdraw staked tokens.
 * @param {number} amount - Amount of tokens to withdraw in wei (smallest unit of token).
 */
async function withdrawTokens(amount) {
  try {
    console.log("Withdrawing staked tokens...");

    // Withdraw tokens from the staking contract
    const withdrawTx = await stakingContract.withdraw(amount);
    await withdrawTx.wait(); // Wait for transaction confirmation

    console.log("Successfully withdrew staked tokens.");
  } catch (error) {
    console.error("Error withdrawing tokens:", error);
  }
}

/**
 * Get the amount of staked tokens for a specific account.
 * @param {string} account - Address of the account to check staked tokens for.
 */
async function getStakedAmount(account) {
  try {
    console.log(`Getting staked amount for account: ${account} ...`);

    // Call the staking contract to retrieve the staked amount
    const stakedAmount = await stakingContract.getStakedAmount(account);

    console.log(`Staked amount for account ${account}: ${ethers.utils.formatUnits(stakedAmount, 18)} tokens`);
    return stakedAmount;
  } catch (error) {
    console.error("Error retrieving staked amount:", error);
  }
}

// Example usage:

// Replace with your token address and desired staking amount in wei
const tokenAddress = "0xYourTokenAddressHere";
const stakeAmount = ethers.utils.parseUnits("10", 18); // Staking 10 tokens

(async () => {
  await stakeTokens(tokenAddress, stakeAmount);
  await claimRewards();
  await withdrawTokens(stakeAmount);
  await getStakedAmount(wallet.address);
})();
```

**Notes:**
1. Replace `process.env.TESTNET_RPC_URL`, `process.env.PRIVATE_KEY`, and contract addresses with actual values.
2. Update the ABI definitions with the official ABI from the ENKI Protocol documentation.
3. Install necessary dependencies (`ethers` and `dotenv`) by running `npm install ethers dotenv`.
