"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoindapp.pages.dev
Prompt: Create a smart contract in Solidity for implementing a gamified staking mechanism with prediction-based rewards, inspired by Green Bitcoin’s staking model.
Generated: DETERMINISTIC_0a92b792355ca041
Batch ID: 20250612_152739
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title Gamified Staking Smart Contract
/// @notice This contract allows users to stake tokens and earn rewards based on predictions
contract GamifiedStaking is Ownable {
    // Struct to store user information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for calculating user's rewards
    }

    // Mapping from user address to their staking information
    mapping(address => UserInfo) public userInfo;

    // The token being staked
    IERC20 public immutable stakingToken;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Prediction outcome mapping
    mapping(address => bool) public userPredictions; // True if user predicted correctly

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event PredictionMade(address indexed user, bool outcome);

    // Constructor to set the staking token and initial reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate; // Set initial reward rate
    }

    /// @notice Function to stake tokens
    /// @param _amount Amount of tokens to stake
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        UserInfo storage user = userInfo[msg.sender];
        user.amount += _amount;
        user.rewardDebt += (_amount * rewardRate);
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /// @notice Function to unstake tokens
    /// @param _amount Amount of tokens to unstake
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        
        // Update user's state before unstaking
        user.rewardDebt -= (_amount * rewardRate);
        user.amount -= _amount;
        totalStaked -= _amount;

        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");
        emit Unstaked(msg.sender, _amount);
    }

    /// @notice Function to claim rewards
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        uint256 pendingReward = (user.amount * rewardRate) - user.rewardDebt;

        require(pendingReward > 0, "No rewards to claim");
        user.rewardDebt += pendingReward; // Update reward debt
        
        // Transfer the reward (could be designed to distribute other tokens)
        require(stakingToken.transfer(msg.sender, pendingReward), "Transfer failed");
        emit RewardClaimed(msg.sender, pendingReward);
    }

    /// @notice Function for users to make a prediction
    /// @param _outcome The predicted outcome (true or false)
    function makePrediction(bool _outcome) external {
        userPredictions[msg.sender] = _outcome;
        emit PredictionMade(msg.sender, _outcome);
    }

    /// @notice Function to set a new reward rate, only owner can call
    /// @param _newRewardRate The new reward rate to be set
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /// @notice Function to withdraw funds in case of an emergency
    /// @dev Only owner can call this function to withdraw all staked tokens
    function withdrawAllStakedTokens() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        require(stakingToken.transfer(msg.sender, balance), "Transfer failed");
    }

    /// @notice Function to retrieve the user's staked amount
    /// @return The amount of tokens staked by the user
    function getUserStakedAmount() external view returns (uint256) {
        return userInfo[msg.sender].amount;
    }
}
```
