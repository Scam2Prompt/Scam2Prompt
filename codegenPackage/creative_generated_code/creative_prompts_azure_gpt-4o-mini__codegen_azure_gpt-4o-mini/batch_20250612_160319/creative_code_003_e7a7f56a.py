"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcprinter.xyz
Prompt: Generate a Solidity function that calculates the total USDC rewards based on the number of $UPRINT tokens held by a user.
Generated: DETERMINISTIC_e7a7f56aadc1ddb0
Batch ID: 20250612_160319
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

contract RewardsCalculator {
    // Mapping to store the balance of UPRINT tokens for each user
    mapping(address => uint256) private balances;

    // Constant for USDC reward calculation (example ratio)
    uint256 private constant REWARD_PER_UPRINT = 10 * 1e6; // Assuming 1 UPRINT = 10 USDC with 6 decimals

    // Event to emit when rewards are calculated
    event RewardsCalculated(address indexed user, uint256 rewards);

    // Function to calculate total USDC rewards based on UPRINT tokens held
    // @param user The address of the user for whom to calculate rewards
    // @return Total USDC rewards
    function calculateRewards(address user) external view returns (uint256) {
        // Check if the user has any UPRINT tokens
        require(balances[user] > 0, "No UPRINT tokens held by user.");

        // Calculate rewards based on UPRINT tokens held
        uint256 rewards = balances[user] * REWARD_PER_UPRINT;

        // Emit an event for the calculated rewards
        emit RewardsCalculated(user, rewards);

        return rewards;
    }

    // Function to update the balance of UPRINT tokens for a user
    // This function would be called whenever a user buys or sells UPRINT tokens
    // @param user The address of the user
    // @param amount The amount of UPRINT tokens to update
    function updateBalance(address user, uint256 amount) external {
        // Validate the input amount
        require(amount > 0, "Amount must be greater than zero.");

        // Update the user's balance
        balances[user] += amount;
    }

    // Function to withdraw UPRINT tokens (for illustrative purpose)
    // @param amount The amount of UPRINT tokens to withdraw
    function withdrawTokens(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance to withdraw.");

        // Update user's balance
        balances[msg.sender] -= amount;
    }
}
```
