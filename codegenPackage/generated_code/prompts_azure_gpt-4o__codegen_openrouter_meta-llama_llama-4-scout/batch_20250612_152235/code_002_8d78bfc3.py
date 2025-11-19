"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Create a Solidity function that calculates and distributes compounding staking rewards based on APY and lock term, as described in the SidusPad staking pools.
Generated: DETERMINISTIC_8d78bfc38179ff78
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title SidusPad Staking Rewards Calculator
 * @author [Your Name]
 * @notice Calculates and distributes compounding staking rewards based on APY and lock term.
 */
contract SidusPadStakingRewards {
    // Mapping of staking pool configurations
    mapping(address => StakingPoolConfig) public stakingPools;

    // Mapping of user staking information
    mapping(address => mapping(address => UserStakingInfo)) public userStakingInfo;

    // Event emitted when staking rewards are distributed
    event StakingRewardsDistributed(address indexed user, address indexed pool, uint256 rewards);

    // Struct to represent staking pool configuration
    struct StakingPoolConfig {
        uint256 apy; // Annual percentage yield (APY)
        uint256 lockTerm; // Lock term in seconds
        uint256 totalStaked; // Total staked amount
        uint256 totalRewards; // Total rewards accumulated
    }

    // Struct to represent user staking information
    struct UserStakingInfo {
        uint256 stakedAmount; // User's staked amount
        uint256 stakedAt; // Timestamp when user staked
    }

    /**
     * @notice Adds a new staking pool configuration
     * @param pool Address of the staking pool
     * @param apy Annual percentage yield (APY)
     * @param lockTerm Lock term in seconds
     */
    function addStakingPool(address pool, uint256 apy, uint256 lockTerm) public {
        require(apy > 0, "APY must be greater than 0");
        require(lockTerm > 0, "Lock term must be greater than 0");
        stakingPools[pool] = StakingPoolConfig(apy, lockTerm, 0, 0);
    }

    /**
     * @notice Stakes an amount in a staking pool
     * @param pool Address of the staking pool
     * @param amount Amount to stake
     */
    function stake(address pool, uint256 amount) public {
        require(stakingPools[pool].apy > 0, "Staking pool not found");
        require(amount > 0, "Staking amount must be greater than 0");

        // Update user's staking information
        userStakingInfo[msg.sender][pool].stakedAmount += amount;
        userStakingInfo[msg.sender][pool].stakedAt = block.timestamp;

        // Update staking pool's total staked amount
        stakingPools[pool].totalStaked += amount;
    }

    /**
     * @notice Calculates and distributes staking rewards
     * @param pool Address of the staking pool
     */
    function distributeRewards(address pool) public {
        require(stakingPools[pool].apy > 0, "Staking pool not found");

        // Calculate staking rewards
        uint256 rewards = calculateRewards(pool);

        // Update staking pool's total rewards
        stakingPools[pool].totalRewards += rewards;

        // Distribute rewards to user
        address user = msg.sender;
        userStakingInfo[user][pool].stakedAmount = 0; // Reset staked amount

        // Emit event
        emit StakingRewardsDistributed(user, pool, rewards);

        // Transfer rewards (assuming rewards are in the same token as staked amount)
        // payable(user).transfer(rewards); // Uncomment and adjust according to your token's transfer logic
    }

    /**
     * @notice Calculates staking rewards based on APY and lock term
     * @param pool Address of the staking pool
     * @return rewards Staking rewards
     */
    function calculateRewards(address pool) internal view returns (uint256) {
        uint256 apy = stakingPools[pool].apy;
        uint256 lockTerm = stakingPools[pool].lockTerm;
        uint256 stakedAmount = userStakingInfo[msg.sender][pool].stakedAmount;
        uint256 stakedAt = userStakingInfo[msg.sender][pool].stakedAt;
        uint256 timeElapsed = block.timestamp - stakedAt;

        // Calculate reward multiplier
        uint256 rewardMultiplier = (timeElapsed * apy) / (lockTerm * 100);

        // Calculate rewards
        uint256 rewards = (stakedAmount * rewardMultiplier) / 10000;

        return rewards;
    }
}
```
