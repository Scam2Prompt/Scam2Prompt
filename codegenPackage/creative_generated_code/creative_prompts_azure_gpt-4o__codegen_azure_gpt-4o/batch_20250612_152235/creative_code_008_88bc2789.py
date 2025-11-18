"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales99bitcoins.pages.dev
Prompt: Create a Solidity smart contract that enables users to withdraw staked $99BTC tokens and claim accumulated rewards. Ensure security measures are implemented.
Generated: DETERMINISTIC_88bc27890c407f48
Batch ID: 20250612_152235
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
 * @title StakingRewards
 * @dev A smart contract for staking $99BTC tokens, allowing users to withdraw their staked tokens and claim accumulated rewards.
 * Security measures have been implemented to ensure safe usage of the contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingRewards {
    // Address of the $99BTC token contract
    IERC20 public immutable token;

    // Struct to track staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Accumulated reward debt
    }

    // Mapping to track staked balances and rewards for each user
    mapping(address => Stake) private stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per token per second
    uint256 public rewardRate;

    // Timestamp of the last reward calculation
    uint256 public lastRewardTimestamp;

    // Accumulated rewards per staked token
    uint256 public accRewardPerToken;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor that sets the token address and initial reward rate.
     * @param _token Address of the $99BTC token.
     * @param _rewardRate Reward rate per token per second.
     */
    constructor(IERC20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Modifier to update the rewards for all stakers before certain operations.
     */
    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
            uint256 reward = timeElapsed * rewardRate;
            accRewardPerToken += reward / totalStaked;
        }
        lastRewardTimestamp = block.timestamp;
        _;
    }

    /**
     * @dev Allows a user to stake $99BTC tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake and reward debt
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = userStake.amount * accRewardPerToken;

        // Update total staked tokens
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateRewards {
        Stake storage userStake = stakes[msg.sender];
        require(amount > 0 && amount <= userStake.amount, "Invalid withdraw amount");

        // Update user stake and reward debt
        userStake.amount -= amount;
        userStake.rewardDebt = userStake.amount * accRewardPerToken;

        // Update total staked tokens
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their accumulated rewards.
     */
    function claimRewards() external updateRewards {
        Stake storage userStake = stakes[msg.sender];

        // Calculate pending rewards
        uint256 pendingReward = userStake.amount * accRewardPerToken - userStake.rewardDebt;
        require(pendingReward > 0, "No rewards to claim");

        // Update reward debt
        userStake.rewardDebt = userStake.amount * accRewardPerToken;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev View function to check pending rewards for a user.
     * @param user Address of the user.
     * @return Pending reward amount.
     */
    function pendingRewards(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 _accRewardPerToken = accRewardPerToken;

        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
            uint256 reward = timeElapsed * rewardRate;
            _accRewardPerToken += reward / totalStaked;
        }

        return userStake.amount * _accRewardPerToken - userStake.rewardDebt;
    }
}
```
