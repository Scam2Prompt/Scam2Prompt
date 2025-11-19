"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20ai.pages.dev
Prompt: Write a smart contract in Solidity for a staking system that distributes rewards to stakers over a period of two years, similar to Dogecoin20's staking mechanism.
Generated: DETERMINISTIC_f0c3d11f271cc2dc
Batch ID: 20250622_210803
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

contract Staking {
    // State variables
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
    }

    mapping(address => Stake) public stakes; // Mapping of staker addresses to their stakes
    uint256 public totalStaked; // Total amount staked in the contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public constant DURATION = 63072000; // 2 years in seconds

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        if (stakedDuration > DURATION) {
            stakedDuration = DURATION; // Cap the duration to 2 years
        }

        return (userStake.amount * rewardRate * stakedDuration) / 1e18; // Adjust for decimals
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        
        // Reset user's stake
        totalStaked -= userStake.amount;
        delete stakes[msg.sender];

        // Transfer staked amount and rewards to the user
        // Note: In a real contract, you would transfer tokens here
        // e.g., token.transfer(msg.sender, userStake.amount + reward);

        // Emit the Unstaked and RewardPaid events
        emit Unstaked(msg.sender, userStake.amount);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
