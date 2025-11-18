"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a smart contract in Solidity for staking AITECH tokens with compounding rewards, similar to the staking pools described on the Solidus AI Tech platform. Include parameters for reward composition, lock term, and investor tier boosts.
Generated: DETERMINISTIC_445047af36da93a6
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title AITECH Staking Contract
 * @author Developer X
 * @notice A smart contract for staking AITECH tokens with compounding rewards.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract AITECHStaking is Ownable, ReentrancyGuard {
    // Token being staked
    IERC20 public immutable aitechToken;

    // Struct to hold user staking information
    struct StakeInfo {
        uint256 amount;         // Amount of tokens staked
        uint256 stakeTime;      // Timestamp when the stake was made
        uint256 lockTerm;       // Lock term in seconds
        uint256 compoundedRewards; // Rewards compounded so far
    }

    // Mapping of address to its staking info
    mapping(address => StakeInfo) public stakes;

    // Reward parameters
    uint256 public baseRewardRate; // Base reward rate in percentage (e.g., 5 for 5%)
    uint256 public compoundingInterval; // Interval for compounding rewards in seconds
    uint256 public investorTierBoost; // Additional reward percentage boost for investors in higher tiers

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockTerm);
    event RewardsClaimed(address indexed user, uint256 rewards);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param tokenAddress Address of the AITECH token.
     * @param rewardRate Base reward rate in percentage (e.g., 5 for 5%).
     * @param interval Compounding interval in seconds.
     * @param tierBoost Investor tier boost in percentage.
     */
    constructor(
        address tokenAddress,
        uint256 rewardRate,
        uint256 interval,
        uint256 tierBoost
    ) {
        require(tokenAddress != address(0), "Invalid token address");
        require(rewardRate > 0, "Reward rate must be greater than 0");
        require(interval > 0, "Compounding interval must be greater than 0");

        aitechToken = IERC20(tokenAddress);
        baseRewardRate = rewardRate;
        compoundingInterval = interval;
        investorTierBoost = tierBoost;
    }

    /**
     * @dev Stake a certain amount of tokens.
     * @param amount Amount of tokens to stake.
     * @param lockTerm Lock term in seconds.
     */
    function stake(uint256 amount, uint256 lockTerm) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than 0");
        require(lockTerm > 0, "Lock term must be greater than 0");

        // Transfer tokens from user to contract
        require(
            aitechToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update staking info
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakeTime = block.timestamp;
        stakes[msg.sender].lockTerm = lockTerm;

        emit Staked(msg.sender, amount, lockTerm);
    }

    /**
     * @dev Claim rewards for the user.
     */
    function claimRewards() external nonReentrant {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Calculate rewards based on time elapsed and reward rate
        uint256 rewards = calculateRewards(msg.sender);

        // Reset rewards
        userStake.compoundedRewards = 0;
        userStake.stakeTime = block.timestamp;

        // Transfer rewards to user
        require(
            aitechToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Unstake user's tokens after lock term.
     */
    function unstake() external nonReentrant {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");
        require(
            block.timestamp >= userStake.stakeTime + userStake.lockTerm,
            "Lock term has not expired"
        );

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;
        userStake.compoundedRewards = 0;

        // Transfer tokens back to user
        require(
            aitechToken.transfer(msg.sender, amountToUnstake),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Calculate the rewards for a given user.
     * @param user Address of the user.
     * @return Rewards.
     */
    function calculateRewards(address user) public view returns (uint256) {
        StakeInfo storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.stakeTime;
        uint256 intervals = timeElapsed / compoundingInterval;

        uint256 rewardRate = baseRewardRate + investorTierBoost; // Apply tier boost
        uint256 rewards = userStake.amount * rewardRate / 100 * intervals;

        return rewards + userStake.compoundedRewards;
    }

    /**
     * @dev Update reward parameters by the owner.
     * @param rewardRate New base reward rate in percentage.
     * @param interval New compounding interval in seconds.
     * @param tierBoost New investor tier boost percentage.
     */
    function updateRewardParameters(
        uint256 rewardRate,
        uint256 interval,
        uint256 tierBoost
    ) external onlyOwner {
        require(rewardRate > 0, "Reward rate must be greater than 0");
        require(interval > 0, "Compounding interval must be greater than 0");

        baseRewardRate = rewardRate;
        compoundingInterval = interval;
        investorTierBoost = tierBoost;
    }
}
```
