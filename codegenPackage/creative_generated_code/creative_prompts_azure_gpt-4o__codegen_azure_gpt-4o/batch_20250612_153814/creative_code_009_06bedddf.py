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

/// @title DeFi Pledge Mining Contract
/// @notice This contract allows users to stake assets and earn rewards based on their pledged amount.
/// @dev Inspired by Trust Base's "DeFi Pledge" concept.

contract PledgeMining {
    // State variables
    uint256 public rewardRate; // Reward rate per block
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount staked by the user
        uint256 rewardDebt; // Rewards already paid out or due
        uint256 lastStakedBlock; // Block number at the time of last stake
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their stake information

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier validateStake(uint256 amount) {
        require(amount > 0, "Stake amount must be greater than zero");
        _;
    }

    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /// @notice Stake assets in the contract to start earning rewards.
    /// @param amount The amount to stake.
    function stake(uint256 amount) external payable validateStake(amount) {
        Stake storage userStake = stakes[msg.sender];

        // Calculate any pending rewards and update user's stake
        uint256 pendingReward = calculateReward(msg.sender);
        userStake.rewardDebt += pendingReward;
        userStake.amount += amount;
        userStake.lastStakedBlock = block.number;

        emit Staked(msg.sender, amount);
    }

    /// @notice Withdraw staked assets from the contract.
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake
        uint256 pendingReward = calculateReward(msg.sender);
        userStake.rewardDebt += pendingReward;
        userStake.amount -= amount;
        userStake.lastStakedBlock = block.number;

        // Transfer the withdrawn amount back to the user
        payable(msg.sender).transfer(amount);

        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Claim accumulated rewards based on the staked assets and elapsed blocks.
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = calculateReward(msg.sender);

        require(pendingReward > 0, "No rewards available to claim");

        // Update user's stake
        userStake.rewardDebt = 0;
        userStake.lastStakedBlock = block.number;

        // Transfer rewards to the user
        payable(msg.sender).transfer(pendingReward);

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /// @notice Calculate the pending rewards for a user.
    /// @param user The user address to calculate rewards for.
    /// @return The pending reward amount.
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 blocksElapsed = block.number - userStake.lastStakedBlock;
        uint256 reward = (userStake.amount * rewardRate * blocksElapsed) / 1 ether;
        return reward + userStake.rewardDebt;
    }

    /// @notice Update the reward rate per block.
    /// @param newRate The new reward rate.
    /// @dev Only the contract owner can update the reward rate.
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }
}
```
