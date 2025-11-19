"""
Generated Code Metadata:
========================
Original URL: https://itsnottestingitstestingblockusa.pages.dev
Prompt: Provide an example of a smart contract that could be used to manage credits earned through social media engagement in a blockchain-based gamification system.
Generated: DETERMINISTIC_82be936ff7850b88
Batch ID: 20250612_151246
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

/// @title Social Media Engagement Credit Manager
/// @notice This contract manages credits earned through social media engagement
/// @dev The contract allows users to earn, redeem, and transfer credits
contract SocialMediaCredits {
    // Mapping from user address to their credit balance
    mapping(address => uint256) private _balances;

    // Event emitted when credits are earned
    event CreditsEarned(address indexed user, uint256 amount);

    // Event emitted when credits are redeemed
    event CreditsRedeemed(address indexed user, uint256 amount);

    // Event emitted when credits are transferred
    event CreditsTransferred(address indexed from, address indexed to, uint256 amount);

    /// @notice Earn credits for social media engagement
    /// @param amount The amount of credits to be earned
    /// @dev Only positive amounts are allowed
    function earnCredits(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update the user's balance
        _balances[msg.sender] += amount;

        // Emit an event for the earned credits
        emit CreditsEarned(msg.sender, amount);
    }

    /// @notice Redeem credits for rewards
    /// @param amount The amount of credits to be redeemed
    /// @dev The user must have enough credits to redeem
    function redeemCredits(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient credits");

        // Deduct the credits from the user's balance
        _balances[msg.sender] -= amount;

        // Emit an event for the redeemed credits
        emit CreditsRedeemed(msg.sender, amount);
    }

    /// @notice Transfer credits to another user
    /// @param to The address of the recipient
    /// @param amount The amount of credits to transfer
    /// @dev The sender must have enough credits to transfer
    function transferCredits(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient credits");

        // Update balances
        _balances[msg.sender] -= amount;
        _balances[to] += amount;

        // Emit an event for the transferred credits
        emit CreditsTransferred(msg.sender, to, amount);
    }

    /// @notice Get the credit balance of a user
    /// @param user The address of the user
    /// @return The credit balance of the user
    function getBalance(address user) external view returns (uint256) {
        return _balances[user];
    }
}
```
