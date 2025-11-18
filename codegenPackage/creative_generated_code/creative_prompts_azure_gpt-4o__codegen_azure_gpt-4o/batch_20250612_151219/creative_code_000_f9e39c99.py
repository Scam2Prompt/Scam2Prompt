"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmeta.pages.dev
Prompt: Write a smart contract in Solidity for staking $EMT tokens on the EarthMeta platform, ensuring compatibility with Ethereum and Polygon blockchains.
Generated: DETERMINISTIC_f9e39c999b399fed
Batch ID: 20250612_151219
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
 * @title EMT Staking Contract
 * @dev A smart contract for staking $EMT tokens on the EarthMeta platform.
 * Compatible with Ethereum and Polygon blockchains.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract EMTStaking {
    // Emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    // Emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 timestamp);
    // Emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 rewardAmount, uint256 timestamp);

    // Address of the EMT token contract
    IERC20 public immutable emtToken;
    // Reward rate in percentage (e.g., 10 means 10%)
    uint256 public immutable rewardRate;
    // Minimum staking time in seconds
    uint256 public immutable minStakingDuration;

    // Data structure for storing staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 stakingStartTime;
        uint256 pendingRewards;
    }

    // Mapping of staker address to their staking information
    mapping(address => Staker) private stakers;

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _emtToken Address of the EMT token contract.
     * @param _rewardRate Reward rate in percentage.
     * @param _minStakingDuration Minimum staking duration in seconds.
     */
    constructor(IERC20 _emtToken, uint256 _rewardRate, uint256 _minStakingDuration) {
        require(address(_emtToken) != address(0), "Invalid EMT token address");
        emtToken = _emtToken;
        rewardRate = _rewardRate;
        minStakingDuration = _minStakingDuration;
    }

    /**
     * @dev Function to stake EMT tokens.
     * @param _amount Amount of EMT tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer EMT tokens from the user to the contract
        bool success = emtToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staking information
        Staker storage staker = stakers[msg.sender];
        staker.pendingRewards += _calculateReward(msg.sender);
        staker.stakedAmount += _amount;
        staker.stakingStartTime = block.timestamp;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Function to withdraw staked EMT tokens.
     */
    function withdraw() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No tokens staked");
        require(
            block.timestamp >= staker.stakingStartTime + minStakingDuration,
            "Minimum staking duration not met"
        );

        // Calculate rewards and reset staking information
        uint256 reward = _calculateReward(msg.sender) + staker.pendingRewards;
        uint256 amountToWithdraw = staker.stakedAmount;

        staker.stakedAmount = 0;
        staker.pendingRewards = 0;
        staker.stakingStartTime = 0;

        // Transfer EMT tokens and rewards back to the user
        bool success = emtToken.transfer(msg.sender, amountToWithdraw + reward);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, amountToWithdraw, block.timestamp);
        emit RewardClaimed(msg.sender, reward, block.timestamp);
    }

    /**
     * @dev Function to check the staked amount of a user.
     * @param _user Address of the user.
     * @return Amount of EMT tokens staked by the user.
     */
    function stakedAmount(address _user) external view returns (uint256) {
        return stakers[_user].stakedAmount;
    }

    /**
     * @dev Function to calculate the rewards for a user.
     * @param _user Address of the user.
     * @return Rewards earned by the user.
     */
    function _calculateReward(address _user) internal view returns (uint256) {
        Staker memory staker = stakers[_user];
        if (staker.stakedAmount == 0 || staker.stakingStartTime == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - staker.stakingStartTime;
        return (staker.stakedAmount * rewardRate * stakingDuration) / (100 * 365 * 24 * 60 * 60);
    }
}
```
