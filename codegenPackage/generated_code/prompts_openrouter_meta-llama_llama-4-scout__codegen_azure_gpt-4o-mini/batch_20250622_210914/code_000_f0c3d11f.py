"""
Generated Code Metadata:
========================
Original URL: https://dodgecoiin20.pages.dev
Prompt: Write a smart contract in Solidity for a staking system that distributes rewards to stakers over a period of two years, similar to Dogecoin20's staking mechanism.
Generated: DETERMINISTIC_f0c3d11f271cc2dc
Batch ID: 20250622_210914
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

contract StakingSystem {
    // State variables
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Time when the stake was made
    }

    mapping(address => Stake) public stakes; // Mapping of staker addresses to their stakes
    uint256 public totalStaked; // Total amount staked in the contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public constant DURATION = 2 * 365 days; // Staking duration of 2 years
    uint256 public startTime; // Start time of the staking period

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
        startTime = block.timestamp; // Set the start time to the current block timestamp
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(block.timestamp < startTime + DURATION, "Staking period has ended");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0; // No stake, no reward

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        if (stakingDuration > DURATION) {
            stakingDuration = DURATION; // Cap the duration to the staking period
        }

        return (userStake.amount * rewardRate * stakingDuration) / 1e18; // Calculate reward
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);
        uint256 amountToUnstake = userStake.amount;

        // Reset the user's stake
        userStake.amount = 0;
        totalStaked -= amountToUnstake;

        // Transfer the staked amount and reward to the user
        // Note: In a real contract, you would use an ERC20 token transfer here
        // ERC20(tokenAddress).transfer(msg.sender, amountToUnstake);
        // ERC20(tokenAddress).transfer(msg.sender, reward);

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to get the user's stake information
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }
}
```
unction to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
