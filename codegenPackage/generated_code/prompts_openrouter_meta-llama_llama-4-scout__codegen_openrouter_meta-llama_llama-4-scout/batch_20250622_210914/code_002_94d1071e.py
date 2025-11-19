"""
Generated Code Metadata:
========================
Original URL: https://bonkrewards-6st.pages.dev
Prompt: Generate a smart contract code in Solidity to implement a similar rewards system with dynamic multipliers based on lock duration.
Generated: DETERMINISTIC_94d1071e8b6f8e1b
Batch ID: 20250622_210914
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title RewardsSystem
 * @author [Your Name]
 * @notice A smart contract implementing a rewards system with dynamic multipliers based on lock duration.
 */
contract RewardsSystem is ReentrancyGuard {
    // Mapping of user lock information
    mapping (address => LockInfo) public userLocks;

    // Mapping of reward multipliers based on lock duration
    mapping (uint256 => uint256) public rewardMultipliers;

    // ERC20 token for rewards
    ERC20 public rewardToken;

    // Event emitted when a user locks tokens
    event Locked(address indexed user, uint256 amount, uint256 lockDuration);

    // Event emitted when a user unlocks tokens
    event Unlocked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to store user lock information
    struct LockInfo {
        uint256 lockedAmount;
        uint256 lockEndTime;
    }

    /**
     * @notice Constructor
     * @param rewardTokenAddress Address of the ERC20 token for rewards
     */
    constructor(address rewardTokenAddress) {
        rewardToken = ERC20(rewardTokenAddress);

        // Initialize reward multipliers (example: 1x for 1 day, 2x for 1 week, 5x for 1 month)
        rewardMultipliers[1 days] = 1;
        rewardMultipliers[7 days] = 2;
        rewardMultipliers[30 days] = 5;
    }

    /**
     * @notice Lock tokens for a specified duration
     * @param amount Amount of tokens to lock
     * @param lockDuration Duration to lock tokens (in seconds)
     */
    function lock(uint256 amount, uint256 lockDuration) public {
        require(amount > 0, "Invalid lock amount");
        require(lockDuration > 0, "Invalid lock duration");
        require(userLocks[msg.sender].lockedAmount == 0, "Tokens are already locked");

        // Check if reward multiplier exists for the given lock duration
        require(rewardMultipliers[lockDuration] > 0, "No reward multiplier for the given lock duration");

        // Transfer tokens from user to contract
        ERC20Burnable(address(rewardToken)).burnFrom(msg.sender, amount);

        // Update user lock information
        userLocks[msg.sender] = LockInfo(amount, block.timestamp + lockDuration);

        emit Locked(msg.sender, amount, lockDuration);
    }

    /**
     * @notice Unlock tokens
     */
    function unlock() public {
        require(userLocks[msg.sender].lockedAmount > 0, "No tokens locked");
        require(userLocks[msg.sender].lockEndTime <= block.timestamp, "Tokens are still locked");

        // Transfer tokens back to user
        ERC20(address(rewardToken)).transfer(msg.sender, userLocks[msg.sender].lockedAmount);

        // Reset user lock information
        delete userLocks[msg.sender];

        emit Unlocked(msg.sender, userLocks[msg.sender].lockedAmount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public nonReentrant {
        require(userLocks[msg.sender].lockedAmount > 0, "No tokens locked");
        require(userLocks[msg.sender].lockEndTime <= block.timestamp, "Tokens are still locked");

        // Calculate reward amount based on lock duration and multiplier
        uint256 rewardAmount = userLocks[msg.sender].lockedAmount * rewardMultipliers[userLocks[msg.sender].lockEndTime - block.timestamp] / 100;

        // Transfer rewards to user
        ERC20(address(rewardToken)).transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Update reward multiplier for a given lock duration
     * @param lockDuration Lock duration (in seconds)
     * @param multiplier Reward multiplier
     */
    function updateRewardMultiplier(uint256 lockDuration, uint256 multiplier) public onlyOwner {
        rewardMultipliers[lockDuration] = multiplier;
    }

    // Restrict function to only be callable by the contract owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Get contract owner
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
