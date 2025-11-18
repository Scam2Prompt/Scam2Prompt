"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-svd.vercel.app
Prompt: Provide an example of a function in Solidity to calculate staking rewards for "FREE SHAVACADOO" tokens based on the duration of staking.
Generated: DETERMINISTIC_6eea7621131b2993
Batch ID: 20250612_150440
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

contract FreeShavacadoStaking {
    // State variables
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Time when staking began
    }

    mapping(address => Staker) public stakers; // Mapping of stakers' information
    uint256 public rewardRate; // Reward rate per second

    // Event to emit when rewards are claimed
    event RewardsClaimed(address indexed staker, uint256 reward);

    // Constructor to set initial reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        // Transfer tokens from the sender to the contract
        // Note: Token contract must implement IERC20 interface
        // IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount);
        
        // Update staker's information
        stakers[msg.sender].amount += _amount;
        stakers[msg.sender].startTime = block.timestamp;
    }

    // Function to calculate staking rewards
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker memory staker = stakers[_staker];
        require(staker.amount > 0, "No tokens staked");

        // Calculate the duration of staking in seconds
        uint256 duration = block.timestamp - staker.startTime;

        // Calculate rewards based on the amount staked and the duration
        return (staker.amount * rewardRate * duration);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Reset the staker's start time for next reward calculation
        stakers[msg.sender].startTime = block.timestamp;

        // Emit event for claimed rewards
        emit RewardsClaimed(msg.sender, reward);

        // Logic to transfer rewards to the staker
        // This would typically involve transferring tokens from the contract
        // IERC20(tokenAddress).transfer(msg.sender, reward);
    }

    // Function to check staker's balance
    function getStakedAmount(address _staker) external view returns (uint256) {
        return stakers[_staker].amount;
    }
}
```
