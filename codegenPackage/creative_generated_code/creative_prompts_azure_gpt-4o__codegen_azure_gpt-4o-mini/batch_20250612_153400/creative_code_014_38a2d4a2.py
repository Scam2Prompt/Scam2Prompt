"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinuairdrop.pages.dev
Prompt: Write a script using ethers.js to fetch the $POODL token balance and staking rewards for a connected wallet address.
Generated: DETERMINISTIC_38a2d4a270d2d1bc
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

// Define the ERC20 token and staking contract addresses
const POODL_TOKEN_ADDRESS = "0xYourPoodlTokenAddress"; // Replace with actual $POODL token address
const STAKING_CONTRACT_ADDRESS = "0xYourStakingContractAddress"; // Replace with actual staking contract address

// ABI for ERC20 token to fetch balance
const ERC20_ABI = [
    "function balanceOf(address owner) view returns (uint256)",
];

// ABI for staking contract to fetch rewards
const STAKING_ABI = [
    "function earned(address account) view returns (uint256)",
];

// Main function to get balance and staking rewards
async function fetchPoodlData(walletAddress) {
    try {
        // Check if wallet address is provided
        if (!walletAddress) {
            throw new Error("Wallet address is required.");
        }

        // Connect to Ethereum provider (e.g., Infura, Alchemy)
        const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID"); // Replace with your Infura Project ID

        // Create contract instances
        const poodlTokenContract = new ethers.Contract(POODL_TOKEN_ADDRESS, ERC20_ABI, provider);
        const stakingContract = new ethers.Contract(STAKING_CONTRACT_ADDRESS, STAKING_ABI, provider);

        // Fetch token balance
        const balance = await poodlTokenContract.balanceOf(walletAddress);
        const formattedBalance = ethers.utils.formatUnits(balance, 18); // Assuming $POODL has 18 decimal places

        // Fetch staking rewards
        const rewards = await stakingContract.earned(walletAddress);
        const formattedRewards = ethers.utils.formatUnits(rewards, 18); // Adjust based on staking contract decimals if different

        // Output results
        console.log(`$POODL Token Balance: ${formattedBalance}`);
        console.log(`Staking Rewards: ${formattedRewards}`);
        
    } catch (error) {
        console.error("Error fetching data:", error.message);
    }
}

// Replace with the wallet address you want to check
const walletAddress = "0xYourWalletAddress"; // Replace with the actual wallet address

// Execute the function
fetchPoodlData(walletAddress);
```

### Notes:
- Ensure to replace `0xYourPoodlTokenAddress`, `0xYourStakingContractAddress`, and `0xYourWalletAddress` with actual addresses.
- Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID to connect to the Ethereum network.
- The code is structured to handle errors gracefully and provides clear output on the token balance and staking rewards.
