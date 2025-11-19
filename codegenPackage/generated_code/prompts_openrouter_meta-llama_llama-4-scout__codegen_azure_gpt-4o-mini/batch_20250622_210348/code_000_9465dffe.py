"""
Generated Code Metadata:
========================
Original URL: https://app-dogecoin20.pages.dev
Prompt: Write a smart contract in Solidity for a staking system that distributes rewards to stakers over a period of two years, similar to the Dogecoin20 project.
Generated: DETERMINISTIC_9465dffeec24eca6
Batch ID: 20250622_210348
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

contract StakingRewards {
    // State variables
    address public owner;
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward rate per second
    uint256 public startTime;
    uint256 public endTime;
    
    // Mapping of staker addresses to their staked amounts
    mapping(address => uint256) public stakedAmounts;
    // Mapping of staker addresses to their reward amounts
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier stakingActive() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Staking is not active");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _rewardRate, uint256 _duration) {
        owner = msg.sender;
        rewardRate = _rewardRate;
        startTime = block.timestamp;
        endTime = block.timestamp + _duration; // Duration in seconds
    }

    // Function to stake tokens
    function stake(uint256 amount) external stakingActive {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update staked amounts
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external stakingActive {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amounts
        stakedAmounts[msg.sender] -= amount;
        totalStaked -= amount;

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address staker) public view returns (uint256) {
        if (block.timestamp < startTime || block.timestamp > endTime) {
            return 0; // No rewards outside of staking period
        }
        uint256 stakedAmount = stakedAmounts[staker];
        return (stakedAmount * rewardRate * (block.timestamp - startTime)) / totalStaked;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update rewards mapping
        rewards[msg.sender] += reward;

        // Emit reward paid event
        emit RewardPaid(msg.sender, reward);
    }

    // Function to withdraw contract balance (only for owner)
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
