"""
Generated Code Metadata:
========================
Original URL: https://smog-tokens-en.pages.dev
Prompt: Design a simple smart contract on Ethereum that allows users to stake $SMOG tokens and earn rewards in the form of additional tokens or other cryptocurrencies.
Generated: DETERMINISTIC_12d9bfb210943058
Batch ID: 20250622_210231
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking $SMOG tokens
contract StakingContract is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // The token being staked
    IERC20 public smogToken;

    // Reward token (could be another ERC20 token)
    IERC20 public rewardToken;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward per token staked (in reward tokens)
    uint256 public rewardPerToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the staking and reward tokens
    constructor(IERC20 _smogToken, IERC20 _rewardToken) {
        smogToken = _smogToken;
        rewardToken = _rewardToken;
    }

    // Function to stake $SMOG tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(smogToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked $SMOG tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update the staker's information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(smogToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        require(reward > 0, "No rewards to claim");
        staker.rewardDebt += reward;

        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a staker
    function calculateReward(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amountStaked * rewardPerToken) - staker.rewardDebt;
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRewardPerToken) external onlyOwner {
        rewardPerToken = newRewardPerToken;
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address stakerAddress) external view returns (uint256) {
        return stakers[stakerAddress].amountStaked;
    }

    // Function to get the pending rewards of a user
    function getPendingRewards(address stakerAddress) external view returns (uint256) {
        return calculateReward(stakerAddress);
    }
}
```
