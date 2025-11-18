"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Create a tutorial for using Moxie’s smart contracts to reward downstream influence and organic actions by Farcaster members.
Generated: DETERMINISTIC_ac2ba6c4d8f16ec0
Batch ID: 20250612_151027
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

/// @title Moxie Smart Contracts for Rewarding Downstream Influence
/// @author Your Name
/// @notice This contract allows Farcaster members to reward actions and influence downstream.
/// @dev Ensure to test this contract thoroughly before deploying it in production.

contract MoxieRewards {
    // Event to log reward distribution
    event RewardDistributed(address indexed member, uint256 amount);

    // Mapping to store the balances of each member
    mapping(address => uint256) private balances;

    // Total supply of rewards in the contract
    uint256 public totalSupply;

    // Modifier to check if the caller has sufficient balance
    modifier hasSufficientBalance(uint256 amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        _;
    }

    /// @notice Constructor to initialize total supply of rewards
    /// @param initialSupply Initial amount of rewards to be distributed
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply;
        balances[msg.sender] = initialSupply; // Allocate initial supply to the contract deployer
    }

    /// @notice Function to reward a member for their influence
    /// @param member The address of the member to reward
    /// @param amount The amount of reward to distribute
    /// @dev Only the contract owner can distribute rewards
    function rewardMember(address member, uint256 amount) external hasSufficientBalance(amount) {
        require(member != address(0), "Invalid address");
        require(amount > 0, "Reward amount must be greater than zero");

        balances[msg.sender] -= amount; // Deduct from caller's balance
        balances[member] += amount; // Add to the member's balance

        emit RewardDistributed(member, amount); // Emit event for reward distribution
    }

    /// @notice Function to view the balance of a specific member
    /// @param member The address of the member
    /// @return The balance of the specified member
    function viewBalance(address member) external view returns (uint256) {
        return balances[member];
    }

    /// @notice Function to withdraw rewards from the contract
    /// @dev Allows members to withdraw their accrued rewards
    function withdrawRewards(uint256 amount) external hasSufficientBalance(amount) {
        balances[msg.sender] -= amount; // Deduct from member's balance
        payable(msg.sender).transfer(amount); // Transfer the reward to the member
    }

    /// @notice Fallback function to receive Ether
    receive() external payable {
        // In case Ether needs to be sent to this contract
    }
}
```
