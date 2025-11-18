"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Write a smart contract in Solidity to implement a staking pool similar to the AITECH staking tiers described on the webpage, including features like compounding rewards, NFT boosts, and tier-based reward percentages.
Generated: DETERMINISTIC_d0b6ba2b13ed8f8e
Batch ID: 20250612_152620
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
 * @title StakingPool
 * @author Expert Programmer
 * @notice Implements a tier-based staking pool with compounding rewards and optional NFT boosts.
 */
contract StakingPool {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount;       // Amount staked
        uint256 rewardDebt;   // Reward debt for compounding
        uint256 lastUpdated;  // Timestamp of last update
        uint256 tier;         // Tier of the user based on staking amount
        uint256 nftBoost;     // Boost percentage from NFT (0-100)
    }

    // Reward percentages based on tiers (as basis points, e.g., 500 = 5%)
    uint256[] public tierRewardPercentages = [500, 1000, 1500, 2000];
    uint256 public constant MAX_NFT_BOOST = 100; // Maximum NFT boost percentage

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Total staked amount in the pool
    uint256 public totalStaked;

    // Reward pool balance
    uint256 public rewardPool;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 tier);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Modifier to check if a user has staked
    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No stake found for user");
        _;
    }

    /**
     * @notice Allows a user to stake tokens in the pool.
     * @param _amount Amount of tokens to stake.
     * @param _nftBoost Optional boost percentage from owning an NFT (0-100).
     */
    function stake(uint256 _amount, uint256 _nftBoost) external {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(_nftBoost <= MAX_NFT_BOOST, "NFT boost exceeds maximum allowed");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        _compoundRewards(msg.sender); // Compound rewards before updating
        userStake.amount += _amount;
        userStake.lastUpdated = block.timestamp;
        userStake.nftBoost = _nftBoost;

        // Determine tier based on total staked amount
        userStake.tier = _calculateTier(userStake.amount);

        // Update global variables
        totalStaked += _amount;

        emit Staked(msg.sender, _amount, userStake.tier);
    }

    /**
     * @notice Allows a user to withdraw their staked tokens.
     */
    function withdraw() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        _compoundRewards(msg.sender); // Compound rewards before withdrawal

        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0; // Reset staking amount
        userStake.rewardDebt = 0; // Reset reward debt
        userStake.tier = 0; // Reset tier
        userStake.nftBoost = 0; // Reset NFT boost

        totalStaked -= amountToWithdraw;
        emit Withdrawn(msg.sender, amountToWithdraw);

        // Transfer tokens back to the user (dummy transfer logic here)
        // Example: token.transfer(msg.sender, amountToWithdraw);
    }

    /**
     * @notice Allows a user to claim their staking rewards.
     */
    function claimRewards() external hasStake(msg.sender) {
        _compoundRewards(msg.sender); // Calculate latest rewards
        uint256 rewards = _pendingRewards(msg.sender); // Get pending rewards
        require(rewards > 0, "No rewards available to claim");

        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += rewards; // Update reward debt

        emit RewardsClaimed(msg.sender, rewards);

        // Transfer rewards to the user (dummy transfer logic here)
        // Example: token.transfer(msg.sender, rewards);
    }

    /**
     * @notice Internal function to compound rewards for a user.
     * @param user Address of the user to compound rewards for.
     */
    function _compoundRewards(address user) internal {
        uint256 rewards = _pendingRewards(user);
        if (rewards > 0) {
            Stake storage userStake = stakes[user];
            userStake.rewardDebt += rewards; // Add rewards to reward debt
            userStake.amount += rewards;     // Compound rewards into stake amount
            totalStaked += rewards;          // Update total staked in the pool
        }
    }

    /**
     * @notice Internal function to calculate pending rewards for a user.
     * @param user Address of the user to calculate rewards for.
     * @return Pending rewards for the user.
     */
    function _pendingRewards(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        uint256 baseReward = (userStake.amount * tierRewardPercentages[userStake.tier] * timeElapsed) / (365 days * 10000);
        uint256 boostedReward = baseReward + (baseReward * userStake.nftBoost / 100);
        return boostedReward - userStake.rewardDebt;
    }

    /**
     * @notice Internal function to calculate the staking tier based on the amount.
     * @param amount Staked amount for the user.
     * @return Staking tier.
     */
    function _calculateTier(uint256 amount) internal view returns (uint256) {
        if (amount >= 1000 ether) {
            return 3; // Highest tier
        } else if (amount >= 500 ether) {
            return 2;
        } else if (amount >= 100 ether) {
            return 1;
        } else {
            return 0; // Lowest tier
        }
    }
}
```
