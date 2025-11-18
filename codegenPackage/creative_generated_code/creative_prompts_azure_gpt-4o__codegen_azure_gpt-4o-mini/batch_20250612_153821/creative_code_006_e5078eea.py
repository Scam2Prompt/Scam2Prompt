"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralisednetwork.pages.dev
Prompt: Create a staking pool smart contract that combines resources to increase staking rewards, as outlined on Decentralised Networks.
Generated: DETERMINISTIC_e5078eeaff5ef7a1
Batch ID: 20250612_153821
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

/**
 * @title StakingPool
 * @dev This contract allows users to stake ERC20 tokens in a pool to earn rewards.
 */
contract StakingPool is Ownable {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the user staked
    }

    // Mapping of user addresses to their respective stakes
    mapping(address => Stake) private stakes;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // The ERC20 token that can be staked
    IERC20 public stakingToken;

    // Reward rate - rewards per second per token
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stakes a specified amount of tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the staking contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraws staked tokens and claims rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the rewards
        uint256 reward = calculateReward(msg.sender);

        // Reset user's stake before transferring tokens
        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;
        totalStaked -= amountToWithdraw;

        // Transfer staked tokens back to the user
        stakingToken.transfer(msg.sender, amountToWithdraw);

        // Transfer rewards to the user
        if (reward > 0) {
            // Safely transfer rewards to user (assumed to be in a separate token)
            stakingToken.transfer(msg.sender, reward);
        }

        emit Withdrawn(msg.sender, amountToWithdraw);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward for the specified user.
     * @param user The address of the user for whom to calculate rewards.
     * @return The calculated reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        return (stakingDuration * userStake.amount * rewardRate) / 1e18; // Assuming rewardRate is scaled for precision
    }

    /**
     * @dev Returns the stake details of a user.
     * @param user The address of the user.
     * @return amount Staked amount by the user.
     * @return timestamp Timestamp of the last stake.
     */
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }

    /**
     * @dev Updates the reward rate. Only callable by the contract owner.
     * @param newRewardRate The new reward rate to set.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
