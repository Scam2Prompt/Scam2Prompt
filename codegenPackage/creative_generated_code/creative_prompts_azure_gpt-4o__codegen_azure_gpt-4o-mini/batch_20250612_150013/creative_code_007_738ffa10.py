"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogs.pages.dev
Prompt: Write code in Solidity for a staking mechanism that supports two pools: one with locked schedules for higher returns and another with flexible withdrawal options, as described in "The War Chest."
Generated: DETERMINISTIC_738ffa1022fc0498
Batch ID: 20250612_150013
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

/**
 * @title StakingContract
 * @dev This contract allows users to stake tokens in two different pools: a locked schedule pool for higher returns 
 * and a flexible withdrawal pool. 
 */
contract StakingContract is ReentrancyGuard {
    // Define the structure for each staking pool
    enum PoolType { Locked, Flexible }

    // Represents a user's stake
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 duration; // Applicable for locked pool
        PoolType poolType;
    }
    
    // Mapping from user address to their stakes
    mapping(address => Stake[]) public stakes;

    // Token being staked
    IERC20 public stakingToken;

    // Events for logging deposits and withdrawals
    event Staked(address indexed user, uint256 amount, PoolType poolType);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the staking token address
    constructor(IERC20 _stakingToken) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        stakingToken = _stakingToken;
    }

    /**
     * @dev Allows users to stake tokens in either the locked or flexible pool.
     * @param amount The amount of tokens to stake.
     * @param poolType The type of pool to stake into (Locked or Flexible).
     * @param duration The duration for which the tokens will be locked (only for Locked pool).
     */
    function stake(uint256 amount, PoolType poolType, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Create a new stake
        stakes[msg.sender].push(Stake({
            amount: amount,
            startTime: block.timestamp,
            duration: poolType == PoolType.Locked ? duration : 0,
            poolType: poolType
        }));

        emit Staked(msg.sender, amount, poolType);
    }

    /**
     * @dev Allows users to withdraw their staked tokens based on the pool type.
     * @param stakeIndex The index of the stake to withdraw.
     */
    function withdraw(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");
        
        Stake storage userStake = stakes[msg.sender][stakeIndex];
        require(userStake.amount > 0, "No stake found at index");

        // Handle withdrawal based on pool type
        if (userStake.poolType == PoolType.Locked) {
            require(block.timestamp >= userStake.startTime + userStake.duration, "Stake is still locked");
        }

        // Transfer the staked amount back to the user
        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0; // Prevent re-entrancy
        require(stakingToken.transfer(msg.sender, amountToWithdraw), "Transfer failed");

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Returns the stakes of a user.
     * @param user The address of the user.
     * @return An array of Stake structs representing the user's stakes.
     */
    function getUserStakes(address user) external view returns (Stake[] memory) {
        return stakes[user];
    }

    /**
     * @dev Returns the total number of stakes for a user.
     * @param user The address of the user.
     * @return The total number of stakes.
     */
    function getStakesCount(address user) external view returns (uint256) {
        return stakes[user].length;
    }
}
```
