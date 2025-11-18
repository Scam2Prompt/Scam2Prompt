"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itsnottestingitstestingblockusa.pages.dev
Prompt: Provide an example of a smart contract that could be used to manage credits earned through social media engagement in a blockchain-based gamification system.
Generated: DETERMINISTIC_82be936ff7850b88
Batch ID: 20250612_151246
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
 * @title SocialMediaEngagementCredits
 * @dev A smart contract to manage credits earned through social media engagement in a gamification system.
 */
contract SocialMediaEngagementCredits {
    // Owner of the contract
    address public owner;

    // Mapping to store user credits
    mapping(address => uint256) public credits;

    // Events to log important actions
    event CreditsEarned(address indexed user, uint256 amount);
    event CreditsTransferred(address indexed from, address indexed to, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add credits to a user's balance. Only the owner can call this function.
     * @param user The address of the user to whom credits are being added.
     * @param amount The amount of credits to be added.
     */
    function addCredits(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address.");
        require(amount > 0, "Credit amount must be greater than zero.");

        credits[user] += amount;
        emit CreditsEarned(user, amount);
    }

    /**
     * @dev Function for users to transfer credits to another user.
     * @param to The address of the recipient.
     * @param amount The amount of credits to transfer.
     */
    function transferCredits(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address.");
        require(credits[msg.sender] >= amount, "Insufficient credits.");
        require(amount > 0, "Transfer amount must be greater than zero.");

        credits[msg.sender] -= amount;
        credits[to] += amount;
        emit CreditsTransferred(msg.sender, to, amount);
    }

    /**
     * @dev Function to check the credit balance of a user.
     * @param user The address of the user to check the balance for.
     * @return The credit balance of the user.
     */
    function getCreditBalance(address user) external view returns (uint256) {
        require(user != address(0), "Invalid user address.");
        return credits[user];
    }
}
```
