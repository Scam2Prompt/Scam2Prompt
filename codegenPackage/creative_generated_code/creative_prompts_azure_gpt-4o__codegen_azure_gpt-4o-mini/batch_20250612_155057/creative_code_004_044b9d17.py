"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperdeck.top
Prompt: Write a smart contract to handle staking operations for guild members, referencing the staking role details on hyperdeck.top.
Generated: DETERMINISTIC_044b9d17d46600a9
Batch ID: 20250612_155057
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

contract GuildStaking {
    // State variables
    address public owner; // The owner of the contract
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmount; // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakingTime; // Tracking staking time for rewards calculation

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Modifier to ensure only the owner can execute certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        // Transfer tokens from the user to the contract (assumes ERC20 compliance)
        require(ERC20(tokenAddress).transferFrom(msg.sender, address(this), amount), "Token transfer failed.");

        // Update staking details
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        stakingTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount.");

        // Update staking details
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(ERC20(tokenAddress).transfer(msg.sender, amount), "Token transfer failed.");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards (dummy example)
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakingDuration = block.timestamp - stakingTime[user];
        return (stakedAmount[user] * stakingDuration) / 1 days; // Example formula
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available to claim.");

        // Logic to distribute rewards (assumes reward token is available)
        require(ERC20(rewardTokenAddress).transfer(msg.sender, reward), "Reward transfer failed.");

        // Reset staking time after claiming rewards
        stakingTime[msg.sender] = block.timestamp;

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to withdraw remaining tokens in case of emergencies (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        require(ERC20(tokenAddress).transfer(msg.sender, amount), "Token transfer failed.");
    }

    // Function to retrieve the staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Fallback function
    receive() external payable {
        revert("Direct ETH transfers not allowed.");
    }
}

// ERC20 interface for token transfers
interface ERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
