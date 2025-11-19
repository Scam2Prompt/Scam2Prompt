"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate a Solidity contract for managing token economy distribution schedules for $GGG tokens, based on the metrics outlined in the Good Games Guild documentation.
Generated: DETERMINISTIC_665ab507d3a5cdb3
Batch ID: 20250612_153820
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title GGGTokenDistribution
 * @dev Manages the distribution schedule for $GGG tokens according to predefined metrics
 */
contract GGGTokenDistribution is Ownable, ReentrancyGuard {
    IERC20 public gggToken;

    // Distribution categories
    enum DistributionCategory {
        PRIVATE_SALE,
        PUBLIC_SALE,
        TEAM,
        ADVISORS,
        MARKETING,
        ECOSYSTEM,
        LIQUIDITY,
        TREASURY,
        STAKING_REWARDS
    }

    // Distribution schedule for each category
    struct DistributionSchedule {
        uint256 totalAllocation;       // Total tokens allocated
        uint256 claimedTokens;         // Tokens already claimed
        uint256 startTime;             // When distribution starts
        uint256 cliffDuration;         // Cliff period in seconds
        uint256 vestingDuration;       // Total vesting duration in seconds
        uint256 releaseInterval;       // Interval between releases in seconds
        bool isLinear;                 // True for linear, false for cliff then linear
    }

    mapping(DistributionCategory => DistributionSchedule) public distributionSchedules;
    mapping(address => mapping(DistributionCategory => uint256)) public userClaims;

    event TokensClaimed(address indexed recipient, DistributionCategory category, uint256 amount);
    event ScheduleUpdated(DistributionCategory category, DistributionSchedule schedule);

    /**
     * @dev Constructor
     * @param _gggToken Address of the GGG token contract
     */
    constructor(address _gggToken) {
        require(_gggToken != address(0), "Invalid token address");
        gggToken = IERC20(_gggToken);
    }

    /**
     * @dev Set distribution schedule for a category
     * @param category Distribution category
     * @param schedule Distribution schedule parameters
     */
    function setDistributionSchedule(
        DistributionCategory category,
        DistributionSchedule calldata schedule
    ) external onlyOwner {
        require(schedule.totalAllocation > 0, "Allocation must be positive");
        require(schedule.vestingDuration > 0, "Vesting duration must be positive");
        
        if (schedule.isLinear) {
            require(schedule.releaseInterval > 0, "Interval must be positive for linear vesting");
        } else {
            require(schedule.cliffDuration <= schedule.vestingDuration, "Cliff exceeds vesting");
        }

        distributionSchedules[category] = schedule;
        emit ScheduleUpdated(category, schedule);
    }

    /**
     * @dev Calculate claimable tokens for a user in a category
     * @param user User address
     * @param category Distribution category
     * @return claimableAmount Number of tokens currently claimable
     */
    function calculateClaimable(address user, DistributionCategory category) public view returns (uint256 claimableAmount) {
        DistributionSchedule storage schedule = distributionSchedules[category];
        if (schedule.totalAllocation == 0 || block.timestamp < schedule.startTime) {
            return 0;
        }

        uint256 elapsed = block.timestamp - schedule.startTime;

        if (elapsed < schedule.cliffDuration) {
            return 0;
        }

        uint256 vestedAmount;
        if (elapsed >= schedule.vestingDuration) {
            vestedAmount = schedule.totalAllocation;
        } else if (schedule.isLinear) {
            uint256 intervalsPassed = elapsed / schedule.releaseInterval;
            vestedAmount = (schedule.totalAllocation * intervalsPassed * schedule.releaseInterval) / schedule.vestingDuration;
        } else {
            // Cliff then linear vesting
            uint256 vestingElapsed = elapsed - schedule.cliffDuration;
            vestedAmount = (schedule.totalAllocation * vestingElapsed) / (schedule.vestingDuration - schedule.cliffDuration);
        }

        uint256 userAllocation = vestedAmount - schedule.claimedTokens;
        uint256 userRemaining = userAllocation - userClaims[user][category];
        
        return userRemaining > 0 ? userRemaining : 0;
    }

    /**
     * @dev Claim tokens from a distribution category
     * @param category Distribution category to claim from
     */
    function claimTokens(DistributionCategory category) external nonReentrant {
        address recipient = msg.sender;
        uint256 claimableAmount = calculateClaimable(recipient, category);
        require(claimableAmount > 0, "No tokens available to claim");

        DistributionSchedule storage schedule = distributionSchedules[category];
        require(gggToken.balanceOf(address(this)) >= claimableAmount, "Insufficient contract balance");

        userClaims[recipient][category] += claimableAmount;
        schedule.claimedTokens += claimableAmount;

        require(gggToken.transfer(recipient, claimableAmount), "Token transfer failed");
        emit TokensClaimed(recipient, category, claimableAmount);
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token contract
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(gggToken), "Cannot recover GGG tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
