"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-etftoken.web.app
Prompt: Create a function in Solidity to calculate staking rewards for BTCETF tokens based on the total tokens staked by the community and individual contributions.
Generated: DETERMINISTIC_4046b4d950c1cd5b
Batch ID: 20250612_152410
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

contract BTCETFStaking {
    // State variables
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    mapping(address => uint256) public stakes; // Mapping to track individual stakes
    uint256 public rewardRate; // Reward rate in percentage (e.g., 5 for 5%)

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with a reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero.");
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        
        // Update the total staked tokens and individual stake
        totalStaked += amount;
        stakes[msg.sender] += amount;

        // Logic to handle the actual transfer of tokens would go here
        // Example: ERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);
    }

    // Function to calculate rewards based on the total staked and individual contribution
    function calculateRewards(address user) external view returns (uint256) {
        uint256 userStake = stakes[user];
        require(userStake > 0, "No tokens staked by user.");

        // Calculate the user's share of the total staked tokens
        uint256 userShare = (userStake * 100) / totalStaked;

        // Calculate rewards based on the user's share and the total reward pool
        uint256 totalRewards = (totalStaked * rewardRate) / 100;
        uint256 userReward = (totalRewards * userShare) / 100;

        return userReward;
    }

    // Function to withdraw tokens and rewards
    function withdraw(uint256 amount) external {
        uint256 userStake = stakes[msg.sender];
        require(userStake >= amount, "Insufficient staked amount.");

        // Logic to handle the actual transfer of tokens would go here
        // Example: ERC20(tokenAddress).transfer(msg.sender, amount);

        // Update the total and user's stake
        totalStaked -= amount;
        stakes[msg.sender] -= amount;
    }
}
```
