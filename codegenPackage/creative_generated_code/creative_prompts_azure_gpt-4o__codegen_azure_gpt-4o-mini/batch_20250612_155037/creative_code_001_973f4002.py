"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Generate a Solidity smart contract example that implements a reward system based on social media follower milestones, similar to the $WING tokenomics structure.
Generated: DETERMINISTIC_973f400262e7104a
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for the ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract RewardSystem {
    // State variable to store the ERC20 token contract
    IERC20 public rewardToken;

    // Mapping to hold user follower counts
    mapping(address => uint256) public followerCounts;

    // Mapping to hold user rewards
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to set the reward token address
    constructor(IERC20 _rewardToken) {
        // Ensure the token address is valid
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    // Function to update follower count
    function updateFollowerCount(uint256 newCount) external {
        // Update the follower count for the sender
        followerCounts[msg.sender] = newCount;

        // Check for milestones and distribute rewards accordingly
        distributeRewards(msg.sender, newCount);
    }

    // Internal function to handle reward distribution
    function distributeRewards(address user, uint256 count) internal {
        uint256 rewardAmount = calculateReward(count);
        
        // Ensure that there are enough tokens to transfer
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient reward tokens");

        // Update the user's rewards
        rewards[user] += rewardAmount;

        // Emit event for rewards distribution
        emit RewardsDistributed(user, rewardAmount);

        // Transfer the reward tokens to the user
        require(rewardToken.transfer(user, rewardAmount), "Transfer failed");
    }

    // Function to calculate rewards based on follower count
    function calculateReward(uint256 count) internal pure returns (uint256) {
        if (count >= 1000) {
            return 10 * 10 ** 18; // 10 tokens for 1000 followers
        } else if (count >= 500) {
            return 5 * 10 ** 18; // 5 tokens for 500 followers
        } else if (count >= 100) {
            return 1 * 10 ** 18; // 1 token for 100 followers
        }
        return 0; // No reward for less than 100 followers
    }

    // Function to withdraw remaining tokens in the contract
    function withdrawTokens(uint256 amount) external {
        // Only the contract owner should be able to withdraw tokens
        require(msg.sender == address(this), "Only contract can withdraw tokens");
        
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");

        // Transfer tokens to the owner
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
