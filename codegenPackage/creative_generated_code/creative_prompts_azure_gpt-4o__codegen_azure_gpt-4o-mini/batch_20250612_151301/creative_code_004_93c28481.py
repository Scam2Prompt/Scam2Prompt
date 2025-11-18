"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://belegends.pages.dev
Prompt: Write a function in Solidity to calculate staking rewards for `$LEGEND` tokens based on the duration of staking and the amount staked.
Generated: DETERMINISTIC_93c28481b3138168
Batch ID: 20250612_151301
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
    // State variables
    address public owner;
    uint256 public rewardRate; // Reward rate per second for staked tokens
    mapping(address => uint256) private stakes; // Amount of tokens staked by each address
    mapping(address => uint256) private stakingStart; // Staking start timestamp for each address

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set initial values
    constructor(uint256 _rewardRate) {
        owner = msg.sender; // Set contract creator as owner
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update staked amount and start time
        stakes[msg.sender] += amount;
        stakingStart[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        uint256 amountStaked = stakes[msg.sender];
        require(amountStaked > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);

        // Reset staking data
        stakes[msg.sender] = 0;
        stakingStart[msg.sender] = 0;

        // Transfer staked amount and rewards (assuming the contract has enough tokens)
        payable(msg.sender).transfer(amountStaked + reward);
        
        emit Unstaked(msg.sender, amountStaked);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate staking rewards based on duration
    function calculateReward(address user) public view returns (uint256) {
        uint256 stakedAmount = stakes[user];
        uint256 duration = block.timestamp - stakingStart[user];

        // Calculate reward based on reward rate and duration
        return (stakedAmount * rewardRate * duration) / 1 ether; // Assuming rewardRate is in wei
    }

    // Function to allow the owner to withdraw funds from the contract (if needed)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient balance");
        payable(owner).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
