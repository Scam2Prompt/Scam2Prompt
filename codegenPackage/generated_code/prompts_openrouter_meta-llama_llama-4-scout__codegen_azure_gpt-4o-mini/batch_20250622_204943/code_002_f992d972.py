"""
Generated Code Metadata:
========================
Original URL: https://swiftmultiauths.pages.dev
Prompt: "Generate a smart contract code for a staking pool that allows multiple stakeholders to combine their computational resources and increase their chances of being rewarded."
Generated: DETERMINISTIC_f992d9729c73b811
Batch ID: 20250622_204943
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingPool contract allows multiple stakeholders to stake tokens and share rewards
contract StakingPool is Ownable {
    // Struct to hold information about each stakeholder's stake
    struct Stakeholder {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the stakeholder
    }

    // Mapping of stakeholder addresses to their information
    mapping(address => Stakeholder) public stakeholders;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // Reward token contract
    IERC20 public rewardToken;

    // Reward per token staked (in reward tokens)
    uint256 public rewardPerToken;

    // Event emitted when a stakeholder stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a stakeholder withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking pool with the reward token
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    // Function to stake tokens in the pool
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update the stakeholder's information
        Stakeholder storage stakeholder = stakeholders[msg.sender];
        stakeholder.amount += amount;
        stakeholder.rewardDebt = calculateRewardDebt(stakeholder.amount);

        // Update total staked amount
        totalStaked += amount;

        // Transfer tokens from the stakeholder to the contract
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens from the pool
    function withdraw(uint256 amount) external {
        Stakeholder storage stakeholder = stakeholders[msg.sender];
        require(stakeholder.amount >= amount, "Insufficient staked amount");

        // Update the stakeholder's information
        stakeholder.amount -= amount;
        stakeholder.rewardDebt = calculateRewardDebt(stakeholder.amount);

        // Update total staked amount
        totalStaked -= amount;

        // Transfer tokens back to the stakeholder
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards based on the current stake
    function claimRewards() external {
        Stakeholder storage stakeholder = stakeholders[msg.sender];
        uint256 pendingReward = calculatePendingReward(stakeholder);

        require(pendingReward > 0, "No rewards to claim");

        // Update the reward debt
        stakeholder.rewardDebt = calculateRewardDebt(stakeholder.amount);

        // Transfer rewards to the stakeholder
        require(rewardToken.transfer(msg.sender, pendingReward), "Transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    // Internal function to calculate the reward debt for a given stake
    function calculateRewardDebt(uint256 amount) internal view returns (uint256) {
        return (amount * rewardPerToken);
    }

    // Internal function to calculate pending rewards for a stakeholder
    function calculatePendingReward(Stakeholder storage stakeholder) internal view returns (uint256) {
        return (stakeholder.amount * rewardPerToken) - stakeholder.rewardDebt;
    }

    // Function to update the reward per token (can only be called by the owner)
    function updateRewardPerToken(uint256 newRewardPerToken) external onlyOwner {
        rewardPerToken = newRewardPerToken;
    }

    // Function to get the staked amount of a stakeholder
    function getStakedAmount(address stakeholderAddress) external view returns (uint256) {
        return stakeholders[stakeholderAddress].amount;
    }
}
```
