"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-cosmicnetwork.pages.dev
Prompt: Develop a function in Solidity that applies a 15% penalty for early unstaking of $Cosmic tokens and updates the user's balance accordingly.
Generated: DETERMINISTIC_4f15c47e14971dc8
Batch ID: 20250612_151333
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

contract CosmicTokenStaking {

    // Define a mapping to track user's staked balances
    mapping(address => uint256) private stakedBalances;

    // Define a mapping to track the timestamps of user's stakes
    mapping(address => uint256) private stakeTimestamps;

    // Define the penalty percentage for early unstaking
    uint256 constant PENALTY_PERCENTAGE = 15;

    // Event to log the unstaking process
    event Unstaked(address indexed user, uint256 amount, uint256 penaltyAmount);

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Assume transferFrom is called to transfer the tokens to this contract
        stakedBalances[msg.sender] += amount;
        stakeTimestamps[msg.sender] = block.timestamp; // Record the time of staking
    }

    // Function to unstake tokens with a penalty for early unstaking
    function unstake(uint256 amount) external {
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate the time since the stake
        uint256 stakingDuration = block.timestamp - stakeTimestamps[msg.sender];

        // Check if the user is unstaking early (before a certain duration, e.g., 30 days)
        if (stakingDuration < 30 days) {
            // Calculate the penalty amount
            uint256 penaltyAmount = (amount * PENALTY_PERCENTAGE) / 100;
            uint256 amountAfterPenalty = amount - penaltyAmount;

            // Update the staked balance
            stakedBalances[msg.sender] -= amount;

            // Emit an event for the unstaking process
            emit Unstaked(msg.sender, amount, penaltyAmount);

            // Transfer the remaining amount after penalty to the user
            // Assume transfer is a function to transfer the tokens back to the user
            transfer(msg.sender, amountAfterPenalty);
        } else {
            // No penalty for late unstaking
            stakedBalances[msg.sender] -= amount;
            emit Unstaked(msg.sender, amount, 0);
            transfer(msg.sender, amount);
        }
    }

    // Placeholder function for token transfer logic
    function transfer(address to, uint256 amount) internal {
        // Logic to transfer $Cosmic tokens to the user
        // This would typically call the ERC20 transfer function
    }

    // Function to check the staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}
```
