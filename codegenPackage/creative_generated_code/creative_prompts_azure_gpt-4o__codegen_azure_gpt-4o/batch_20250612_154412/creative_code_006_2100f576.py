"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Create a Solidity function to distribute staking rewards in a decentralized network, inspired by the "코인을 맡기면 이자가 나온다고?" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_2100f5765b146c7f
Batch ID: 20250612_154412
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
 * @dev A contract to distribute staking rewards in a decentralized network.
 */
contract StakingRewards {
    // State variables
    address public owner; // Owner of the contract
    uint256 public rewardRatePerSecond; // Rewards distributed per second per staked token
    uint256 public totalStaked; // Total staked tokens in the contract

    struct StakerInfo {
        uint256 stakedAmount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Rewards already paid out or pending
        uint256 lastUpdated; // Timestamp of the last reward update
    }

    mapping(address => StakerInfo) public stakers; // Mapping of staker address to their staking information

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 reward);

    // Constructor
    constructor(uint256 _rewardRatePerSecond) {
        owner = msg.sender;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Modifier to ensure only the owner can call certain functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Modifier to validate non-zero amounts.
     * @param _amount The amount to validate.
     */
    modifier validAmount(uint256 _amount) {
        require(_amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Stake tokens to receive rewards.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external validAmount(_amount) {
        // Update rewards before any state changes
        _updateRewards(msg.sender);

        // Update staker information
        StakerInfo storage staker = stakers[msg.sender];
        staker.stakedAmount += _amount;
        totalStaked += _amount;
        staker.lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim pending rewards.
     * @param _amount The amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external validAmount(_amount) {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= _amount, "Insufficient staked amount");

        // Update rewards before state changes
        _updateRewards(msg.sender);

        // Update staker information
        staker.stakedAmount -= _amount;
        totalStaked -= _amount;
        staker.lastUpdated = block.timestamp;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim all pending rewards.
     */
    function claimRewards() external {
        // Update rewards before state changes
        _updateRewards(msg.sender);

        StakerInfo storage staker = stakers[msg.sender];
        uint256 pendingRewards = staker.rewardDebt;
        require(pendingRewards > 0, "No rewards available to claim");

        // Reset reward debt
        staker.rewardDebt = 0;

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Update rewards for a given staker.
     * @param _staker The address of the staker.
     */
    function _updateRewards(address _staker) internal {
        StakerInfo storage staker = stakers[_staker];
        if (staker.stakedAmount == 0 || staker.lastUpdated == block.timestamp) {
            return;
        }

        // Calculate rewards since the last update
        uint256 timeElapsed = block.timestamp - staker.lastUpdated;
        uint256 rewards = timeElapsed * staker.stakedAmount * rewardRatePerSecond;

        // Update reward debt and timestamp
        staker.rewardDebt += rewards;
        staker.lastUpdated = block.timestamp;
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRewardRatePerSecond The new reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRatePerSecond) external onlyOwner {
        require(_newRewardRatePerSecond > 0, "Reward rate must be greater than zero");
        rewardRatePerSecond = _newRewardRatePerSecond;
    }

    /**
     * @dev Emergency withdraw of all staked tokens. Only callable by the owner.
     */
    function emergencyWithdraw() external onlyOwner {
        totalStaked = 0;
        // Reset all stakers' information
        // NOTE: In a production contract, this would involve returning tokens to stakers.
    }
}
```
