"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Create a Solidity function that calculates and distributes compounding staking rewards based on APY and lock term, as described in the SidusPad staking pools.
Generated: DETERMINISTIC_8d78bfc38179ff78
Batch ID: 20250612_152235
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

contract StakingPool {
    // State variables
    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Timestamp when the stake was made
        uint256 lockTerm; // Lock term in seconds
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    uint256 public apy; // Annual Percentage Yield (APY) in basis points (1% = 100 basis points)
    
    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockTerm);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to initialize APY
    constructor(uint256 _apy) {
        require(_apy > 0, "APY must be greater than zero");
        apy = _apy;
    }

    // Function to stake tokens
    function stake(uint256 amount, uint256 lockTerm) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockTerm > 0, "Lock term must be greater than zero");

        // Create a new stake
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            lockTerm: lockTerm
        });

        emit Staked(msg.sender, amount, lockTerm);
    }

    // Function to calculate rewards based on APY and lock term
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        require(userStake.amount > 0, "No active stake found");

        // Calculate the time elapsed since the stake was made
        uint256 timeElapsed = block.timestamp - userStake.startTime;

        // Calculate the total rewards based on APY
        uint256 annualRewards = (userStake.amount * apy * timeElapsed) / (365 days * 10000);
        return annualRewards;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");
        require(block.timestamp >= userStake.startTime + userStake.lockTerm, "Stake is still locked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);
        uint256 totalAmount = userStake.amount + rewards;

        // Reset the user's stake
        delete stakes[msg.sender];

        // Transfer the staked amount and rewards to the user
        // Note: In a real contract, you would transfer tokens here
        // For example: token.transfer(msg.sender, totalAmount);

        emit Unstaked(msg.sender, userStake.amount, rewards);
    }

    // Function to update APY (only owner can call this)
    function updateAPY(uint256 newAPY) external {
        require(newAPY > 0, "APY must be greater than zero");
        apy = newAPY;
    }
}
```
