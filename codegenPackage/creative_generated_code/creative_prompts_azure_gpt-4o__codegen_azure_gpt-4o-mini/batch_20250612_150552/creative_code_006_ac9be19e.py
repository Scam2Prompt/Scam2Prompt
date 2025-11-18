"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omikanmitoken-buy.pages.dev
Prompt: Write a Solidity smart contract for staking Omikami tokens, including features for rewards distribution and liquidity locking.
Generated: DETERMINISTIC_ac9be19e708e9699
Batch ID: 20250612_150552
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Omikami Staking Contract
 * @dev This contract allows users to stake Omikami tokens and earn rewards.
 */
contract OmikamiStaking is Ownable, ReentrancyGuard {
    // The Omikami token contract
    IERC20 public omikamiToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 reward;        // Accumulated reward
        uint256 lastUpdated;   // Last update timestamp
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate (for example, rewards per second)
    uint256 public rewardRate;

    // Event for staking action
    event Staked(address indexed user, uint256 amount);
    
    // Event for withdrawing stake
    event Withdrawn(address indexed user, uint256 amount);

    // Event for claiming rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _omikamiToken Address of the Omikami token contract.
     * @param _rewardRate Rate of rewards per second.
     */
    constructor(IERC20 _omikamiToken, uint256 _rewardRate) {
        omikamiToken = _omikamiToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake a specified amount of Omikami tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than 0");
        
        // Update the user's reward before staking new amount
        updateReward(msg.sender);

        // Transfer tokens from user to contract
        omikamiToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked Omikami tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's reward before withdrawing
        updateReward(msg.sender);

        // Update user's stake information
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        omikamiToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards for the user.
     */
    function claimRewards() external nonReentrant {
        updateReward(msg.sender);
        uint256 reward = stakes[msg.sender].reward;
        require(reward > 0, "No rewards available to claim");

        // Reset user's reward
        stakes[msg.sender].reward = 0;

        // Transfer rewards to the user
        omikamiToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Update the reward for a user.
     * @param user Address of the user to update rewards for.
     */
    function updateReward(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            // Calculate the new reward based on the time since last update
            uint256 newReward = (block.timestamp - userStake.lastUpdated) * rewardRate * userStake.amount;
            userStake.reward += newReward;
        }
        // Update last updated timestamp
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Set a new reward rate (only owner).
     * @param _rewardRate New reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Get the total amount of rewards earned by a user.
     * @param user Address of the user.
     * @return Total rewards earned.
     */
    function getTotalRewards(address user) external view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 currentReward = (block.timestamp - userStake.lastUpdated) * rewardRate * userStake.amount;
        return userStake.reward + currentReward;
    }

    /**
     * @dev Get the staked amount for a user.
     * @param user Address of the user.
     * @return Amount staked.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
