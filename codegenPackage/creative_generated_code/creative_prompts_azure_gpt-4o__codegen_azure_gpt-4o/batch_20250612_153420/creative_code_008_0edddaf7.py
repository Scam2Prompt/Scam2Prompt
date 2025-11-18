"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Provide code in Solidity for implementing yield farming functionality for $HEHE tokens, including reward distribution based on staking duration.
Generated: DETERMINISTIC_0edddaf7bf263f65
Batch ID: 20250612_153420
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
 * @title YieldFarming
 * @dev A smart contract for yield farming $HEHE tokens, with rewards distributed based on staking duration.
 */
contract YieldFarming {
    // ERC20 token used for staking and rewards
    IERC20 public immutable HEHEToken;

    // Annual reward rate (in percentage points, e.g., 20 for 20%)
    uint256 public immutable annualRewardRate;

    // Data structure to track staker information
    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked
        uint256 stakingStartTimestamp; // Timestamp of when staking started
        uint256 accumulatedRewards; // Total rewards accumulated to date
    }

    // Mapping from address to staker information
    mapping(address => Staker) private stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the yield farming contract.
     * @param _HEHEToken Address of the $HEHE ERC20 token contract.
     * @param _annualRewardRate Annual reward rate in percentage points (e.g., 20 for 20%).
     */
    constructor(IERC20 _HEHEToken, uint256 _annualRewardRate) {
        require(address(_HEHEToken) != address(0), "Invalid token address");
        require(_annualRewardRate > 0, "Annual reward rate must be positive");

        HEHEToken = _HEHEToken;
        annualRewardRate = _annualRewardRate;
    }

    /**
     * @dev Stake $HEHE tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from user to contract
        HEHEToken.transferFrom(msg.sender, address(this), amount);

        // Update staking information
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        staker.stakedAmount += amount;
        if (staker.stakingStartTimestamp == 0) {
            staker.stakingStartTimestamp = block.timestamp;
        }

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated yield farming rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        uint256 reward = staker.accumulatedRewards;
        require(reward > 0, "No rewards to claim");

        staker.accumulatedRewards = 0;

        // Transfer rewards to user
        HEHEToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        uint256 amount = staker.stakedAmount;
        require(amount > 0, "No tokens to unstake");

        uint256 reward = staker.accumulatedRewards;

        staker.stakedAmount = 0;
        staker.stakingStartTimestamp = 0;
        staker.accumulatedRewards = 0;

        // Transfer staked tokens back to user
        HEHEToken.transfer(msg.sender, amount);

        // Transfer any accumulated rewards to user
        if (reward > 0) {
            HEHEToken.transfer(msg.sender, reward);
            emit RewardsClaimed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the current accumulated rewards for a staker.
     * @param user Address of the staker.
     */
    function getRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 pendingRewards = _calculateRewards(staker);
        return staker.accumulatedRewards + pendingRewards;
    }

    /**
     * @dev Internal function to update the rewards for a staker.
     * @param user Address of the staker.
     */
    function _updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 pendingRewards = _calculateRewards(staker);
        staker.accumulatedRewards += pendingRewards;
        staker.stakingStartTimestamp = block.timestamp;
    }

    /**
     * @dev Internal function to calculate pending rewards for a staker.
     * @param staker Staker struct containing staking information.
     * @return The pending rewards based on staking duration and amount.
     */
    function _calculateRewards(Staker storage staker) internal view returns (uint256) {
        if (staker.stakedAmount == 0 || staker.stakingStartTimestamp == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - staker.stakingStartTimestamp; // in seconds
        uint256 yearlyReward = (staker.stakedAmount * annualRewardRate) / 100; // yearly reward
        uint256 reward = (yearlyReward * stakingDuration) / 365 days; // pro-rata rewards
        return reward;
    }
}

/**
 * @dev Minimal ERC20 interface for the $HEHE token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
