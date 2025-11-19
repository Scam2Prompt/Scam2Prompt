"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Develop a Solidity smart contract to manage the Meme Index's staking rewards, distributing the 25% supply dedicated to staking rewards among $MEMEX holders.
Generated: DETERMINISTIC_6f2289a5a06fc372
Batch ID: 20250622_211639
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

/**
 * @title MemeIndexStakingRewards
 * @dev A smart contract to manage staking rewards for $MEMEX holders.
 *      Distributes 25% of the total supply dedicated to staking rewards.
 */
contract MemeIndexStakingRewards {
    // Total supply of $MEMEX tokens
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18; // Example: 1 million tokens with 18 decimals
    uint256 public constant REWARD_POOL = (TOTAL_SUPPLY * 25) / 100; // 25% of total supply for rewards

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track rewards earned by users
    mapping(address => uint256) public rewards;

    // Total staked amount
    uint256 public totalStaked;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to ensure non-zero staking amounts
    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Stake $MEMEX tokens to participate in rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonZeroAmount(amount) {
        // Update staked balance and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $MEMEX tokens.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external nonZeroAmount(amount) {
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Calculate and distribute rewards to the caller.
     */
    function claimRewards() external {
        uint256 userStake = stakedBalances[msg.sender];
        require(userStake > 0, "No staked balance");

        // Calculate reward based on user's stake proportion
        uint256 reward = (userStake * REWARD_POOL) / totalStaked;
        require(reward > 0, "No rewards available");

        // Update rewards mapping
        rewards[msg.sender] += reward;

        // Emit reward claim event
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev View function to check the rewards of a user.
     * @param user The address of the user.
     * @return The amount of rewards earned by the user.
     */
    function viewRewards(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
