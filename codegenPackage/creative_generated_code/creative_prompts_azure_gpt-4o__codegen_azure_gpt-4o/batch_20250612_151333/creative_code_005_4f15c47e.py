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

/**
 * @title CosmicTokenStaking
 * @dev Contract to handle staking and early unstaking with penalties for Cosmic tokens ($Cosmic)
 */
contract CosmicTokenStaking {
    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Penalty percentage for early unstaking (15%)
    uint256 public constant EARLY_UNSTAKING_PENALTY = 15;

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount, uint256 penalty);

    /**
     * @dev Function to unstake tokens with an early unstaking penalty.
     * @param amount The amount of tokens the user wants to unstake.
     */
    function unstake(uint256 amount) external {
        // Ensure the user has enough balance to unstake
        require(balances[msg.sender] >= amount, "Insufficient balance to unstake");

        // Calculate the penalty amount
        uint256 penalty = (amount * EARLY_UNSTAKING_PENALTY) / 100;

        // Calculate the amount to be returned to the user after applying the penalty
        uint256 amountAfterPenalty = amount - penalty;

        // Update the user's balance
        balances[msg.sender] -= amount;

        // Emit an event with details about the unstaking
        emit Unstaked(msg.sender, amount, penalty);

        // Transfer the remaining tokens back to the user
        // (Assuming transfer logic is implemented elsewhere)
        _transferTokens(msg.sender, amountAfterPenalty);
    }

    /**
     * @dev Internal function to handle token transfers.
     * Note: Replace this with actual ERC20 transfer logic in production.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function _transferTokens(address to, uint256 amount) internal {
        // In a real implementation, this would interact with the token contract
        // For example: ERC20(tokenAddress).transfer(to, amount);
    }

    /**
     * @dev Function to deposit tokens into the staking contract.
     * Note: This is a placeholder function for demonstration.
     * @param amount The amount of tokens the user wants to deposit.
     */
    function deposit(uint256 amount) external {
        // Add tokens to the user's balance
        balances[msg.sender] += amount;

        // In a real implementation, transferFrom logic would be used to move tokens from the user to the contract
    }

    /**
     * @dev Function to get the balance of the user.
     * @param user The address of the user.
     * @return The balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
