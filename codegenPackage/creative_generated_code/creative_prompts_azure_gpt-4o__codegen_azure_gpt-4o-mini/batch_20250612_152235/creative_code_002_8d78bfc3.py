"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Create a Solidity function that calculates and distributes compounding staking rewards based on APY and lock term, as described in the SidusPad staking pools.
Generated: DETERMINISTIC_8d78bfc38179ff78
Batch ID: 20250612_152235
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
    struct Stake {
        uint256 amount;            // Amount of tokens staked
        uint256 startTime;         // The time the stake was created
        uint256 lockTerm;          // The lock term in seconds
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    uint256 public annualPercentageYield;      // Annual percentage yield (APY) in basis points (e.g., 500 for 5%)
    
    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockTerm);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to set initial APY
    constructor(uint256 _apy) {
        require(_apy > 0, "APY must be greater than 0");
        annualPercentageYield = _apy;
    }

    // Function to stake tokens
    function stakeTokens(uint256 _amount, uint256 _lockTerm) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_lockTerm > 0, "Lock term must be greater than zero");

        // Create a new stake for the user
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            lockTerm: _lockTerm
        });

        // Emit event for staking
        emit Staked(msg.sender, _amount, _lockTerm);
    }

    // Function to calculate rewards based on the stake
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];

        // Ensure the user has an active stake
        require(userStake.amount > 0, "No active stake found");

        // Calculate the elapsed time since staking
        uint256 elapsedTime = block.timestamp - userStake.startTime;

        // Check if the stake is still locked
        require(elapsedTime >= userStake.lockTerm, "Stake is still locked");

        // Calculate the rewards using the formula: rewards = (amount * APY * elapsedTime) / (365 days * 10000)
        uint256 rewards = (userStake.amount * annualPercentageYield * elapsedTime) / (365 days * 10000);
        return rewards;
    }

    // Function to unstake tokens and claim rewards
    function unstakeTokens() external {
        Stake memory userStake = stakes[msg.sender];

        // Ensure the user has an active stake
        require(userStake.amount > 0, "No active stake found");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);

        // Reset the user's stake
        delete stakes[msg.sender];

        // Emit event for unstaking
        emit Unstaked(msg.sender, userStake.amount, rewards);

        // Here you would transfer the staked amount and rewards back to the user
        // For example:
        // token.transfer(msg.sender, userStake.amount + rewards);
    }
}
```
