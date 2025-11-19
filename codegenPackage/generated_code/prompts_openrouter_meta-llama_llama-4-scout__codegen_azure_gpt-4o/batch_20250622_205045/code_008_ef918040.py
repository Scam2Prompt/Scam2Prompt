"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.web.app
Prompt: Propose a smart contract upgrade to introduce a new feature for BTCETF, such as auto-compounding of staking rewards.
Generated: DETERMINISTIC_ef91804010e6f6cc
Batch ID: 20250622_205045
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
 * @title BTCETF Staking Contract with Auto-Compounding
 * @dev This contract introduces an auto-compounding feature for staking rewards.
 */
contract BTCETFStaking {
    // State variables
    address public owner;
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastRewardBlock;

    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for auto-compounding
    }

    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsCompounded(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateRewards(address _staker) {
        if (lastRewardBlock > 0) {
            uint256 pendingReward = calculatePendingReward(_staker);
            if (pendingReward > 0) {
                stakers[_staker].rewardDebt += pendingReward;
            }
        }
        lastRewardBlock = block.number;
        _;
    }

    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount The amount to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount The amount to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        staker.amount -= _amount;
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Compound rewards into the staked amount.
     */
    function compoundRewards() external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;
        require(reward > 0, "No rewards to compound");

        staker.amount += reward;
        staker.rewardDebt = 0;
        totalStaked += reward;

        emit RewardsCompounded(msg.sender, reward);
    }

    /**
     * @dev Calculate pending rewards for a staker.
     * @param _staker The address of the staker.
     * @return The pending reward amount.
     */
    function calculatePendingReward(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (staker.amount == 0 || lastRewardBlock == 0) {
            return 0;
        }

        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 reward = (staker.amount * rewardRate * blocksSinceLastReward) / 1e18;
        return reward;
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
