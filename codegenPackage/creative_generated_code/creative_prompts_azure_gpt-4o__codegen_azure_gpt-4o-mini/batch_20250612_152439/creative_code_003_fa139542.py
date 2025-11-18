"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prism-61a.pages.dev
Prompt: Write a smart contract to enable staking on the Prism platform, considering the tokenomics described in the whitepaper.
Generated: DETERMINISTIC_fa139542ee771b4c
Batch ID: 20250612_152439
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PrismStaking
 * @dev A smart contract for staking on the Prism platform.
 * This contract allows users to stake their tokens, earn rewards, and withdraw their staked tokens.
 */
contract PrismStaking is ReentrancyGuard, Ownable {
    // The token being staked
    IERC20 public stakingToken;

    // Struct to hold information about each user's stake
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 rewardDebt;   // Rewards debt for the user
    }

    // Mapping of user addresses to their stake data
    mapping(address => Stake) public stakes;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward rate per token staked (can be adjusted)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are updated
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken The address of the ERC20 token to be staked.
     * @param _rewardRate The initial reward rate per token staked.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to stake a specified amount of tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer the tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake information
        Stake storage stake = stakes[msg.sender];
        stake.amount += amount;
        stake.rewardDebt += calculatePendingRewards(msg.sender);

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake information
        stake.amount -= amount;
        stake.rewardDebt += calculatePendingRewards(msg.sender);

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);
        
        // Update total staked amount
        totalStaked -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to update the reward rate.
     * Only the owner can call this function.
     * @param newRate The new reward rate per token staked.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Function to calculate pending rewards for a user.
     * @param user The address of the user.
     * @return The pending rewards for the user.
     */
    function calculatePendingRewards(address user) internal view returns (uint256) {
        Stake storage stake = stakes[user];
        return stake.amount * rewardRate; // Simplified reward calculation
    }

    /**
     * @dev Function to view the user's stake information.
     * @return The amount staked and the pending rewards.
     */
    function viewStake() external view returns (uint256 amountStaked, uint256 pendingRewards) {
        Stake storage stake = stakes[msg.sender];
        amountStaked = stake.amount;
        pendingRewards = calculatePendingRewards(msg.sender);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
