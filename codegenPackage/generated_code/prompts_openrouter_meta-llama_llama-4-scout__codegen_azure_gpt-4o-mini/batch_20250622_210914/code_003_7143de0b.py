"""
Generated Code Metadata:
========================
Original URL: https://plenafinance.vercel.app
Prompt: Design a smart contract to distribute rewards, such as USDT prizes and whitelist spots, to participants of the $PLENA airdrop campaign, using Solidity and Ethers.js.
Generated: DETERMINISTIC_7143de0ba8a8b5ff
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the interface for ERC20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for distributing rewards in an airdrop campaign
contract AirdropDistributor is Ownable {
    // State variables
    IERC20 public rewardToken; // The token to distribute (e.g., USDT)
    mapping(address => bool) public claimed; // Track if an address has claimed rewards

    // Event to log reward distribution
    event RewardClaimed(address indexed participant, uint256 amount);

    // Constructor to set the reward token address
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    // Function to distribute rewards to participants
    function distributeRewards(address[] calldata participants, uint256[] calldata amounts) external onlyOwner {
        require(participants.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < participants.length; i++) {
            require(participants[i] != address(0), "Invalid participant address");
            require(amounts[i] > 0, "Amount must be greater than zero");
            require(!claimed[participants[i]], "Reward already claimed");

            // Transfer the reward token to the participant
            bool success = rewardToken.transfer(participants[i], amounts[i]);
            require(success, "Token transfer failed");

            // Mark the reward as claimed
            claimed[participants[i]] = true;

            // Emit an event for the claimed reward
            emit RewardClaimed(participants[i], amounts[i]);
        }
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(rewardToken), "Cannot withdraw reward token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }

    // Function to withdraw the remaining reward tokens in the contract
    function withdrawRemainingTokens() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        rewardToken.transfer(owner(), balance);
    }
}
```

```javascript
// JavaScript code using Ethers.js to interact with the AirdropDistributor contract

const { ethers } = require("ethers");

// AirdropDistributor contract ABI
const airdropDistributorABI = [
    // Add the relevant ABI entries here
    "function distributeRewards(address[] calldata participants, uint256[] calldata amounts)",
    "function withdrawRemainingTokens() external",
    "event RewardClaimed(address indexed participant, uint256 amount)"
];

// Function to distribute rewards
async function distributeRewards(provider, contractAddress, participants, amounts) {
    const signer = provider.getSigner();
    const airdropDistributor = new ethers.Contract(contractAddress, airdropDistributorABI, signer);

    try {
        const tx = await airdropDistributor.distributeRewards(participants, amounts);
        console.log("Transaction sent:", tx.hash);
        await tx.wait();
        console.log("Transaction confirmed:", tx.hash);
    } catch (error) {
        console.error("Error distributing rewards:", error);
    }
}

// Example usage
(async () => {
    const provider = new ethers.providers.JsonRpcProvider("YOUR_INFURA_OR_ALCHEMY_URL");
    const contractAddress = "YOUR_AIRDROP_DISTRIBUTOR_CONTRACT_ADDRESS";
    const participants = ["0xAddress1", "0xAddress2"]; // Replace with actual addresses
    const amounts = [1000, 2000]; // Replace with actual amounts

    await distributeRewards(provider, contractAddress, participants, amounts);
})();
```
