"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfdbull.pages.dev
Prompt: Write a Solidity smart contract for handling the vesting of staked $BTFD tokens and rewards, ensuring tokens are locked for a set period before becoming claimable.
Generated: DETERMINISTIC_e93bf34789994589
Batch ID: 20250612_154236
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

/**
 * @title TokenVesting
 * @dev A smart contract for handling vesting of staked $BTFD tokens and rewards.
 * The contract locks tokens for a specific vesting period before they become claimable.
 */
contract TokenVesting {
    // Structure to store vesting information
    struct VestingSchedule {
        uint256 amount;        // Amount of tokens staked
        uint256 rewards;       // Rewards accrued
        uint256 startTime;     // Start time of the vesting period (timestamp)
        uint256 unlockTime;    // When the tokens can be claimed (timestamp)
        bool claimed;          // Whether the tokens have been claimed
    }

    // Mapping from address to vesting schedules
    mapping(address => VestingSchedule[]) public vestingSchedules;

    // Address of the $BTFD token contract
    IERC20 public immutable token;

    // Events
    event TokensStaked(address indexed user, uint256 amount, uint256 rewards, uint256 unlockTime);
    event TokensClaimed(address indexed user, uint256 amount, uint256 rewards);

    /**
     * @dev Constructor to initialize the token address.
     * @param tokenAddress Address of the $BTFD token contract.
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(tokenAddress);
    }

    /**
     * @dev Function to stake tokens and start a vesting schedule.
     * @param amount Amount of tokens to stake.
     * @param vestingDuration Duration of the vesting period in seconds.
     * @param rewards Rewards to be distributed after the vesting period.
     */
    function stakeTokens(uint256 amount, uint256 vestingDuration, uint256 rewards) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(vestingDuration > 0, "Vesting duration must be greater than zero");
        require(rewards >= 0, "Rewards cannot be negative");

        // Transfer staked tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Create a new vesting schedule
        VestingSchedule memory schedule = VestingSchedule({
            amount: amount,
            rewards: rewards,
            startTime: block.timestamp,
            unlockTime: block.timestamp + vestingDuration,
            claimed: false
        });

        // Store the vesting schedule for the user
        vestingSchedules[msg.sender].push(schedule);

        emit TokensStaked(msg.sender, amount, rewards, schedule.unlockTime);
    }

    /**
     * @dev Function to claim vested tokens and rewards.
     * Claims all vested schedules that are unlocked for the caller.
     */
    function claimTokens() external {
        VestingSchedule[] storage schedules = vestingSchedules[msg.sender];
        uint256 totalAmount = 0;
        uint256 totalRewards = 0;

        for (uint256 i = 0; i < schedules.length; i++) {
            VestingSchedule storage schedule = schedules[i];
            if (!schedule.claimed && block.timestamp >= schedule.unlockTime) {
                totalAmount += schedule.amount;
                totalRewards += schedule.rewards;
                schedule.claimed = true;
            }
        }

        require(totalAmount > 0 || totalRewards > 0, "No tokens or rewards available to claim");

        // Transfer tokens and rewards to the user
        if (totalAmount > 0) {
            require(token.transfer(msg.sender, totalAmount), "Token transfer failed");
        }

        emit TokensClaimed(msg.sender, totalAmount, totalRewards);
    }

    /**
     * @dev Function to get the vesting schedules of a user.
     * @param user Address of the user to query.
     * @return Array of vesting schedules for the user.
     */
    function getVestingSchedules(address user) external view returns (VestingSchedule[] memory) {
        return vestingSchedules[user];
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
