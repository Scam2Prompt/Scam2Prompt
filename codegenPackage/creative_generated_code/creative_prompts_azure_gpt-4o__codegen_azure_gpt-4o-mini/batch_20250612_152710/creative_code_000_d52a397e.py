"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonedge-finance-io.web.app
Prompt: Write a smart contract in Solidity for a staking portal based on the features described on MoonEdge, including tier-based staking rewards and project validation mechanisms.
Generated: DETERMINISTIC_d52a397e042e1808
Batch ID: 20250612_152710
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

contract StakingPortal {
    // Struct to represent a staker
    struct Staker {
        uint256 amountStaked;
        uint256 tier;
        uint256 rewardBalance;
        uint256 lastStakeTime;
    }

    // Mapping of addresses to their staking data
    mapping(address => Staker) public stakers;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount, uint256 tier);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    // Tier thresholds and rewards
    uint256[] public tierThresholds = [1 ether, 5 ether, 10 ether]; // Staking amount thresholds
    uint256[] public tierRewards = [5, 10, 15]; // Rewards based on tiers (in %)

    // Function to stake tokens
    function stake() external payable {
        require(msg.value > 0, "Must stake a positive amount");
        
        // Determine the tier based on the amount staked
        uint256 tier = getTier(msg.value);

        // Update staker information
        stakers[msg.sender].amountStaked += msg.value;
        stakers[msg.sender].tier = tier;
        stakers[msg.sender].lastStakeTime = block.timestamp;

        emit Staked(msg.sender, msg.value, tier);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update the staker's staked amount
        staker.amountStaked -= amount;

        // Transfer the staked amount back to the user
        payable(msg.sender).transfer(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateRewards(msg.sender);

        require(reward > 0, "No rewards available");
        
        // Update reward balance
        staker.rewardBalance += reward;

        emit Claimed(msg.sender, reward);
    }

    // Function to get the tier based on staked amount
    function getTier(uint256 amount) internal view returns (uint256) {
        for (uint256 i = 0; i < tierThresholds.length; i++) {
            if (amount < tierThresholds[i]) {
                return i; // Return tier index
            }
        }
        return tierThresholds.length; // Highest tier
    }

    // Function to calculate the rewards for a staker
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 tier = staker.tier;

        // Calculate reward based on staked amount and tier rewards
        uint256 reward = (staker.amountStaked * tierRewards[tier]) / 100; // Assuming rewards in percentage
        return reward;
    }

    // Fallback function to accept Ether
    receive() external payable {
        stake();
    }
}
```
