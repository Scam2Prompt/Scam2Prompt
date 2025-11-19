"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Write a code snippet to interact with the zkSwap Finance smart contracts for staking and farming on the zkSync Era.
Generated: DETERMINISTIC_026599e25c80dd81
Batch ID: 20250612_160742
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.zksync.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
const { ethers } = require("ethers");

// Define constants for zkSwap Finance smart contract address and ABI
const ZKSWAP_CONTRACT_ADDRESS = "0xYourZkSwapContractAddressHere"; // Replace with actual contract address
const ZKSWAP_ABI = [
    // Add ABI details here
    "function stake(uint256 amount) external",
    "function withdraw(uint256 amount) external",
    "function harvest() external",
    "event Staked(address indexed user, uint256 amount)",
    "event Withdrawn(address indexed user, uint256 amount)",
    "event Harvested(address indexed user, uint256 amount)"
];

// Set up provider and signer
const provider = new ethers.providers.JsonRpcProvider("https://rpc.zksync.io"); // Replace with actual RPC URL
const privateKey = "0xYourPrivateKeyHere"; // Replace with user's private key
const wallet = new ethers.Wallet(privateKey, provider);
const zkSwapContract = new ethers.Contract(ZKSWAP_CONTRACT_ADDRESS, ZKSWAP_ABI, wallet);

/**
 * Function to stake tokens in zkSwap
 * @param {number} amount - The amount of tokens to stake
 */
async function stakeTokens(amount) {
    try {
        // Convert amount to wei
        const weiAmount = ethers.utils.parseUnits(amount.toString(), 18); // Assuming 18 decimals
        const tx = await zkSwapContract.stake(weiAmount);
        await tx.wait(); // Wait for transaction to be mined
        console.log(`Successfully staked ${amount} tokens.`);
    } catch (error) {
        console.error("Error staking tokens:", error);
    }
}

/**
 * Function to withdraw tokens from zkSwap
 * @param {number} amount - The amount of tokens to withdraw
 */
async function withdrawTokens(amount) {
    try {
        const weiAmount = ethers.utils.parseUnits(amount.toString(), 18);
        const tx = await zkSwapContract.withdraw(weiAmount);
        await tx.wait();
        console.log(`Successfully withdrawn ${amount} tokens.`);
    } catch (error) {
        console.error("Error withdrawing tokens:", error);
    }
}

/**
 * Function to harvest rewards from zkSwap
 */
async function harvestRewards() {
    try {
        const tx = await zkSwapContract.harvest();
        await tx.wait();
        console.log("Successfully harvested rewards.");
    } catch (error) {
        console.error("Error harvesting rewards:", error);
    }
}

// Example usage
(async () => {
    await stakeTokens(10); // Replace with desired stake amount
    await withdrawTokens(5); // Replace with desired withdraw amount
    await harvestRewards();
})();
```

**Notes:**
- Replace `ZKSWAP_CONTRACT_ADDRESS`, `RPC URL`, and `privateKey` with actual values.
- The ABI should include the necessary methods for staking, withdrawing, and harvesting; you need to fill it with the actual ABI of the zkSwap contract.
