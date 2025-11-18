"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Create a staking platform in Solidity with two pools: one offering higher returns with a locked schedule and another allowing flexible withdrawals, inspired by Popo's War Chest.
Generated: DETERMINISTIC_8d968daa1c043967
Batch ID: 20250612_145706
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
 * @title Staking Platform
 * @dev A staking platform with two pools:
 * - Flexible Pool: Users can withdraw anytime but earn lower rewards.
 * - Locked Pool: Higher rewards, but funds are locked for a fixed period.
 */
contract StakingPlatform {
    // Struct to store staking information
    struct StakeInfo {
        uint256 amount;         // Amount staked
        uint256 timestamp;      // Timestamp of staking
    }

    // Constants
    uint256 public constant FLEXIBLE_REWARD_RATE = 5;   // 5% annual reward
    uint256 public constant LOCKED_REWARD_RATE = 15;    // 15% annual reward
    uint256 public constant LOCKED_PERIOD = 90 days;    // Lock duration for Locked Pool

    // Mappings to store user stakes for each pool
    mapping(address => StakeInfo) public flexiblePool;
    mapping(address => StakeInfo) public lockedPool;

    // Events
    event Staked(address indexed user, uint256 amount, string poolType);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward, string poolType);

    // Modifier to validate stake amount
    modifier validStakeAmount(uint256 amount) {
        require(amount > 0, "Stake amount must be greater than zero");
        _;
    }

    /**
     * @dev Stake tokens in the Flexible Pool.
     * @param amount Amount to stake.
     */
    function stakeFlexible(uint256 amount) external validStakeAmount(amount) {
        // Update stake amount
        flexiblePool[msg.sender].amount += amount;
        flexiblePool[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount, "Flexible");
    }

    /**
     * @dev Stake tokens in the Locked Pool.
     * @param amount Amount to stake.
     */
    function stakeLocked(uint256 amount) external validStakeAmount(amount) {
        // Update stake amount
        lockedPool[msg.sender].amount += amount;
        lockedPool[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount, "Locked");
    }

    /**
     * @dev Calculate rewards for a specific pool.
     * @param amount Staked amount.
     * @param rate Reward rate (annual).
     * @param duration Duration for which funds were staked.
     * @return Rewards earned.
     */
    function calculateReward(uint256 amount, uint256 rate, uint256 duration) internal pure returns (uint256) {
        // Annual reward calculation (rate * duration / 365 days)
        return (amount * rate * duration) / (365 days * 100);
    }

    /**
     * @dev Withdraw funds and rewards from the Flexible Pool.
     */
    function withdrawFlexible() external {
        StakeInfo storage stake = flexiblePool[msg.sender];
        require(stake.amount > 0, "No funds to withdraw");

        // Calculate rewards
        uint256 duration = block.timestamp - stake.timestamp;
        uint256 reward = calculateReward(stake.amount, FLEXIBLE_REWARD_RATE, duration);

        // Store amount to transfer
        uint256 amountToTransfer = stake.amount + reward;

        // Reset stake
        stake.amount = 0;
        stake.timestamp = 0;

        // Transfer funds (placeholder for actual token transfer logic)
        // Assuming a payable fallback for simplicity
        payable(msg.sender).transfer(amountToTransfer);

        emit Withdrawn(msg.sender, stake.amount, reward, "Flexible");
    }

    /**
     * @dev Withdraw funds and rewards from the Locked Pool.
     */
    function withdrawLocked() external {
        StakeInfo storage stake = lockedPool[msg.sender];
        require(stake.amount > 0, "No funds to withdraw");
        require(block.timestamp >= stake.timestamp + LOCKED_PERIOD, "Funds are locked");

        // Calculate rewards
        uint256 duration = block.timestamp - stake.timestamp;
        uint256 reward = calculateReward(stake.amount, LOCKED_REWARD_RATE, duration);

        // Store amount to transfer
        uint256 amountToTransfer = stake.amount + reward;

        // Reset stake
        stake.amount = 0;
        stake.timestamp = 0;

        // Transfer funds (placeholder for actual token transfer logic)
        // Assuming a payable fallback for simplicity
        payable(msg.sender).transfer(amountToTransfer);

        emit Withdrawn(msg.sender, stake.amount, reward, "Locked");
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}

    /**
     * @dev Helper function to check balance of the contract.
     * @return Contract balance.
     */
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
