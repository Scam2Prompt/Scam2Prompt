"""
Generated Code Metadata:
========================
Original URL: https://launchpad.seedify.de
Prompt: Write a function in Solidity to calculate staking rewards for users participating in a launchpad's token staking program.
Generated: DETERMINISTIC_3cb521a45e3a8312
Batch ID: 20250612_151858
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

contract StakingRewards {
    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 lastRewardTime; // Last time rewards were calculated
        uint256 rewards; // Total rewards earned
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update the staker's rewards before staking
        updateRewards(msg.sender);

        // Update the staker's information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].lastRewardTime = block.timestamp;
        totalStaked += amount;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update the staker's rewards before withdrawing
        updateRewards(msg.sender);

        // Update the staker's information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 reward = stakers[msg.sender].rewards;
        require(reward > 0, "No rewards to claim");

        // Reset the rewards to zero after claiming
        stakers[msg.sender].rewards = 0;

        // Transfer the rewards to the user (assuming the contract has enough balance)
        payable(msg.sender).transfer(reward);

        // Emit the RewardsClaimed event
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 timeStaked = block.timestamp - staker.lastRewardTime;

        // Calculate rewards based on the time staked and the reward rate
        uint256 newRewards = (staker.amountStaked * rewardRate * timeStaked) / 1e18;
        staker.rewards += newRewards;

        // Update the last reward time
        staker.lastRewardTime = block.timestamp;
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
