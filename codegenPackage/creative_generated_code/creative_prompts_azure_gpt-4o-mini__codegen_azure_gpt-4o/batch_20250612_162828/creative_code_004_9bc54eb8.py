"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-gnosis.net
Prompt: What are the steps to create a staking rewards feature in a dapp using MetaMask's capabilities?
Generated: DETERMINISTIC_9bc54eb81cc9ad8f
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Staking Rewards Feature in a DApp using MetaMask.
 * This code assumes you have a smart contract deployed that handles staking and rewards (e.g., ERC-20 compatible).
 * The code interacts with MetaMask and the smart contract using ethers.js.
 * Ensure you replace placeholder values (e.g., contract address, ABI) with actual values from your setup.
 */

// Import ethers.js for interacting with Ethereum blockchain
const { ethers } = require('ethers');

// Constants and setup
const CONTRACT_ADDRESS = "0xYourSmartContractAddress"; // Replace with your deployed contract address
const CONTRACT_ABI = [/* Your Contract ABI */]; // Replace with your contract ABI
const STAKING_AMOUNT = ethers.utils.parseEther("1.0"); // Example staking amount (1 ETH)
const REWARD_FETCH_INTERVAL = 60000; // Frequency to check rewards (in milliseconds)
let provider, signer, contract; // To hold provider, signer, and contract instance

// Initialize connection to MetaMask
async function connectMetaMask() {
    try {
        if (window.ethereum) {
            await window.ethereum.request({ method: "eth_requestAccounts" }); // Request account access
            provider = new ethers.providers.Web3Provider(window.ethereum); // MetaMask provider
            signer = provider.getSigner(); // Signer instance for transactions
            contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer); // Contract interface
            console.log("MetaMask connected successfully!");
        } else {
            throw new Error("MetaMask is not installed or available!");
        }
    } catch (error) {
        console.error("Error connecting to MetaMask:", error.message);
    }
}

// Stake tokens
async function stakeTokens() {
    try {
        const tx = await contract.stakeTokens(STAKING_AMOUNT); // Call staking function in the contract
        console.log("Transaction sent:", tx.hash);
        await tx.wait(); // Wait for transaction to be mined
        console.log("Staking complete!");
    } catch (error) {
        console.error("Error staking tokens:", error.message);
    }
}

// Claim rewards
async function claimRewards() {
    try {
        const tx = await contract.claimRewards(); // Call rewards claim function in the contract
        console.log("Transaction sent:", tx.hash);
        await tx.wait(); // Wait for transaction to be mined
        console.log("Rewards claimed successfully!");
    } catch (error) {
        console.error("Error claiming rewards:", error.message);
    }
}

// Fetch current rewards (read-only function)
async function fetchRewards() {
    try {
        const rewards = await contract.getRewards(); // Call rewards fetch function in the contract
        console.log("Current rewards:", ethers.utils.formatEther(rewards));
        return rewards;
    } catch (error) {
        console.error("Error fetching rewards:", error.message);
    }
}

// Periodically check rewards
function startRewardPolling() {
    try {
        setInterval(async () => {
            const rewards = await fetchRewards();
            console.log("Updated rewards:", ethers.utils.formatEther(rewards));
        }, REWARD_FETCH_INTERVAL); // Fetch rewards every REWARD_FETCH_INTERVAL
    } catch (error) {
        console.error("Error with reward polling:", error.message);
    }
}

// Main function to execute staking and polling
async function main() {
    await connectMetaMask(); // Connect to MetaMask
    await stakeTokens(); // Stake tokens
    startRewardPolling(); // Start checking rewards periodically
}

// Execute the main function
main().catch((error) => console.error("Error in main function:", error.message));
```

Ensure the smart contract you deploy has the functions `stakeTokens`, `claimRewards`, and `getRewards` implemented. Replace placeholders like `CONTRACT_ADDRESS` and `CONTRACT_ABI` with the actual values from your contract deployment.
