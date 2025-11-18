"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustbase.one
Prompt: Create a Solidity function for decentralized pledge mining that calculates rewards based on staked assets, inspired by Trust Base's "DeFi Pledge" concept.
Generated: DETERMINISTIC_06bedddfaefb80c0
Batch ID: 20250612_153814
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

contract DecentralizedPledgeMining {
    // Event emitted when a user stakes assets
    event Pledged(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to hold user pledge information
    struct Pledge {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Rewards debt
    }

    // Mapping of user addresses to their pledges
    mapping(address => Pledge) public pledges;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward per staked asset (expressed in wei)
    uint256 public rewardPerToken;

    // Modifier to check if the user has staked assets
    modifier hasPledge() {
        require(pledges[msg.sender].amount > 0, "No assets staked");
        _;
    }

    // Function to stake assets
    function stake(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount, "Value sent must match stake amount");

        // Update total staked and user pledge
        totalStaked += amount;
        pledges[msg.sender].amount += amount;

        // Emit event for user pledge
        emit Pledged(msg.sender, amount);
    }

    // Function to calculate and update rewards for a user
    function updateRewards(address user) internal {
        Pledge storage userPledge = pledges[user];
        uint256 pendingReward = (userPledge.amount * rewardPerToken) - userPledge.rewardDebt;
        userPledge.rewardDebt += pendingReward;
    }

    // Function to claim rewards
    function claimRewards() external hasPledge {
        updateRewards(msg.sender);

        uint256 reward = pledges[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        pledges[msg.sender].rewardDebt = 0;

        // Transfer reward to user
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Transfer failed");

        // Emit event for rewards claimed
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to set the reward per token (can be called by the owner)
    function setRewardPerToken(uint256 newReward) external {
        rewardPerToken = newReward;
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to get user pledge information
    function getUserPledge(address user) external view returns (uint256 amount, uint256 rewardDebt) {
        Pledge storage userPledge = pledges[user];
        return (userPledge.amount, userPledge.rewardDebt);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
