"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://627d8bea.soiletdemo.pages.dev
Prompt: Illustrate how to implement staking for winnings from the Meme Games using Web3Toolkit technology in a smart contract.
Generated: DETERMINISTIC_f20216a12f3f1aee
Batch ID: 20250612_161039
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/// @title Staking Contract for Meme Games Winnings
/// @notice This contract allows users to stake their winnings from the Meme Games
/// @dev Uses ERC20 tokens for staking and implements basic staking functionalities
contract MemeGamesStaking is Ownable {
    using SafeMath for uint256;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Struct to represent each user's stake information
    struct StakeInfo {
        uint256 amount; // Amount staked
        uint256 startTime; // Timestamp when the stake started
    }

    // Mapping to keep track of each user's stake information
    mapping(address => StakeInfo) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    /// @param _stakingToken The address of the ERC20 token to be used for staking
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /// @notice Allows a user to stake a specified amount of tokens
    /// @param amount The amount of tokens to stake
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /// @notice Allows a user to unstake their tokens
    function unstake() external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake information
        userStake.amount = 0;
        userStake.startTime = 0;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amountToUnstake);

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /// @notice Allows users to claim their rewards based on the staking duration
    function claimRewards() external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");

        // Transfer rewards to user (assumes contract has enough balance)
        stakingToken.transfer(msg.sender, rewardAmount);

        // Reset user's stake rewards
        userStake.startTime = block.timestamp; // Update start time for next reward calculation

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /// @notice Calculates rewards based on the amount staked and the time staked
    /// @param user The address of the user
    /// @return reward The calculated reward amount
    function calculateRewards(address user) internal view returns (uint256) {
        StakeInfo storage userStake = stakes[user];
        uint256 stakingDuration = block.timestamp.sub(userStake.startTime);
        
        // Example reward calculation: 1 token per second per staked token
        return userStake.amount.mul(stakingDuration);
    }
}
```
