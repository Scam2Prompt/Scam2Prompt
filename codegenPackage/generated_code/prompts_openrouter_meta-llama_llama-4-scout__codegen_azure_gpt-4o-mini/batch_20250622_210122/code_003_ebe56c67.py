"""
Generated Code Metadata:
========================
Original URL: https://defisyncapps.pages.dev
Prompt: "Design a staking mechanism for a DeFi platform that allows users to redeem assets and return them to their spot wallet within a day, including a function for harvesting rewards."
Generated: DETERMINISTIC_ebe56c67ae503487
Batch ID: 20250622_210122
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A contract for staking tokens with a mechanism to redeem assets and harvest rewards.
 */
contract StakingContract is ReentrancyGuard, Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Token to be staked
    IERC20 public stakingToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user redeems tokens
    event Redeemed(address indexed user, uint256 amount);

    // Event emitted when rewards are harvested
    event RewardsHarvested(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token to be staked.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to redeem staked tokens.
     */
    function redeem() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");
        require(block.timestamp >= userStake.timestamp + 1 days, "Redeem only after 1 day");

        uint256 amountToRedeem = userStake.amount;
        userStake.amount = 0; // Reset user's stake

        require(stakingToken.transfer(msg.sender, amountToRedeem), "Transfer failed");
        emit Redeemed(msg.sender, amountToRedeem);
    }

    /**
     * @dev Function to harvest rewards.
     */
    function harvest() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");

        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to harvest");

        userStake.rewards = 0; // Reset rewards
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsHarvested(msg.sender, reward);
    }

    /**
     * @dev Function to calculate rewards for a user.
     * @param user Address of the user.
     * @return uint256 Amount of rewards.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeStaked = block.timestamp - userStake.timestamp;
        return (userStake.amount * rewardRate * timeStaked) / 1e18; // Adjust for reward rate precision
    }

    /**
     * @dev Function to withdraw tokens in case of emergency.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
