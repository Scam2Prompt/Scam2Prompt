"""
Generated Code Metadata:
========================
Original URL: https://suipassport.vercel.app
Prompt: Create a smart contract that interacts with the Sui Passport platform to unlock rewards for community engagement.
Generated: DETERMINISTIC_c38544ecfd661734
Batch ID: 20250612_153832
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for interacting with the Sui Passport platform
contract CommunityEngagementRewards is Ownable {
    // Event to log reward distribution
    event RewardDistributed(address indexed user, uint256 amount);

    // Mapping to track user engagement scores
    mapping(address => uint256) public engagementScores;

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Minimum engagement score required to unlock rewards
    uint256 public constant MIN_ENGAGEMENT_SCORE = 100;

    // Constructor to initialize the contract with the reward token address
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    // Function to update engagement score for a user
    function updateEngagementScore(address user, uint256 score) external onlyOwner {
        require(user != address(0), "Invalid user address");
        engagementScores[user] += score;
    }

    // Function to unlock rewards based on engagement score
    function unlockRewards() external {
        uint256 score = engagementScores[msg.sender];
        require(score >= MIN_ENGAGEMENT_SCORE, "Insufficient engagement score");

        // Calculate reward amount (1 token per engagement score point)
        uint256 rewardAmount = score;

        // Ensure the contract has enough tokens to distribute
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");

        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, rewardAmount);

        // Emit event for reward distribution
        emit RewardDistributed(msg.sender, rewardAmount);

        // Reset the user's engagement score after rewards are unlocked
        engagementScores[msg.sender] = 0;
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        rewardToken.transfer(msg.sender, amount);
    }

    // Function to check the engagement score of a user
    function getEngagementScore(address user) external view returns (uint256) {
        return engagementScores[user];
    }
}
```
