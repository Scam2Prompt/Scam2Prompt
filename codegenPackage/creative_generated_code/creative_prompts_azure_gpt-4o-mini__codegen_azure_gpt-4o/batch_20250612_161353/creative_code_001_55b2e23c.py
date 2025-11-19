"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-we.pages.dev
Prompt: How can I implement a smart contract to manage staking rewards for AITECH with compounding options?
Generated: DETERMINISTIC_55b2e23c3dda516d
Batch ID: 20250612_161353
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
 * @dev Smart contract to manage staking rewards for AITECH with compounding options.
 */
contract StakingRewards {
    // State variables
    address public owner; // Owner of the contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount staked

    struct Staker {
        uint256 balance; // Amount staked by the staker
        uint256 rewardDebt; // Rewards already claimed or compounded
        uint256 lastUpdated; // Timestamp of the last update
    }

    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardsCompounded(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier updateRewards(address _staker) {
        if (stakers[_staker].balance > 0) {
            uint256 pendingRewards = calculateRewards(_staker);
            stakers[_staker].rewardDebt += pendingRewards;
        }
        stakers[_staker].lastUpdated = block.timestamp;
        _;
    }

    // Constructor
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    // Functions

    /**
     * @dev Stake AITECH tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");
        stakers[msg.sender].balance += _amount;
        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake AITECH tokens, optionally claiming rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakers[msg.sender].balance >= _amount, "Insufficient staked balance");

        stakers[msg.sender].balance -= _amount;
        totalStaked -= _amount;
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards earned from staking.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = stakers[msg.sender].rewardDebt;
        require(rewards > 0, "No rewards to claim");
        stakers[msg.sender].rewardDebt = 0;
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Compound rewards by adding them back to the staked balance.
     */
    function compoundRewards() external updateRewards(msg.sender) {
        uint256 rewards = stakers[msg.sender].rewardDebt;
        require(rewards > 0, "No rewards to compound");

        stakers[msg.sender].balance += rewards;
        stakers[msg.sender].rewardDebt = 0;
        totalStaked += rewards;
        emit RewardsCompounded(msg.sender, rewards);
    }

    /**
     * @dev Calculate pending rewards for a staker.
     * @param _staker Address of the staker.
     * @return Pending rewards amount.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker memory staker = stakers[_staker];
        uint256 elapsedTime = block.timestamp - staker.lastUpdated;
        return (staker.balance * rewardRate * elapsedTime) / 1e18;
    }

    /**
     * @dev Update reward rate. Only callable by the contract owner.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
