"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad.seedify.de
Prompt: Write a function in Solidity to calculate staking rewards for users participating in a launchpad's token staking program.
Generated: DETERMINISTIC_3cb521a45e3a8312
Batch ID: 20250612_151858
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

contract StakingRewards {
    // Struct to hold information about each user's stake
    struct Stake {
        uint256 amount;       // Amount of tokens staked by the user
        uint256 startTime;    // Timestamp when the stake was created
        uint256 rewards;      // Accumulated rewards for the user
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate = 1e18; // 1 token per second for simplicity

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws stakes and rewards
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        
        // Update user's existing stake rewards before adding a new stake
        _updateRewards(msg.sender);

        // Increase the user's stake and total staked amount
        stakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        // Set the start time for rewards calculation
        stakes[msg.sender].startTime = block.timestamp;

        // Emit event for staking
        emit Staked(msg.sender, _amount);
    }

    // Internal function to update rewards for the user
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        
        // Calculate the duration for which rewards should be accrued
        uint256 stakedDuration = block.timestamp - userStake.startTime;

        // Update the rewards based on the staked duration and reward rate
        userStake.rewards += (userStake.amount * stakedDuration * rewardRate) / 1e18;

        // Reset the start time for the next calculation
        userStake.startTime = block.timestamp;
    }

    // Function to withdraw stakes and rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stakes to withdraw");

        // Update rewards before withdrawal
        _updateRewards(msg.sender);

        // Store values to transfer out before resetting
        uint256 amountToWithdraw = userStake.amount;
        uint256 rewardsToWithdraw = userStake.rewards;

        // Reset user's stake information
        userStake.amount = 0;
        userStake.rewards = 0;
        totalStaked -= amountToWithdraw;

        // Transfer staked tokens and rewards to the user
        // Assuming ERC20 token transfer function is called here
        // Replace 'tokenContract' with the actual token contract instance
        // tokenContract.transfer(msg.sender, amountToWithdraw);
        // tokenContract.transfer(msg.sender, rewardsToWithdraw);

        // Emit event for withdrawal
        emit Withdrawn(msg.sender, amountToWithdraw, rewardsToWithdraw);
    }

    // Function to view the staking rewards of a user
    function viewRewards(address _user) external view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 currentRewards = userStake.rewards;

        // Calculate how much more can be earned since the last update
        uint256 stakedDuration = block.timestamp - userStake.startTime;
        currentRewards += (userStake.amount * stakedDuration * rewardRate) / 1e18;

        return currentRewards;
    }
}
```
