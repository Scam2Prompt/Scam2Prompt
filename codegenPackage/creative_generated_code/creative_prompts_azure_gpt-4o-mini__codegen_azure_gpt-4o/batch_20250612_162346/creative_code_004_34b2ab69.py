"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummyu.pages.dev
Prompt: Generate a Solidity contract that outlines the tokenomics for $Gummy, including distribution percentages for team and founders.
Generated: DETERMINISTIC_34b2ab694453e2e3
Batch ID: 20250612_162346
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
 * @title GummyTokenomics
 * @dev A Solidity contract that outlines the tokenomics for the $Gummy token.
 */
contract GummyTokenomics {
    // Constants for token distribution percentages
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    uint256 public constant TEAM_SUPPLY_PERCENTAGE = 20; // 20% reserved for the team
    uint256 public constant FOUNDERS_SUPPLY_PERCENTAGE = 10; // 10% reserved for founders

    // State variables to track allocated tokens
    uint256 public teamSupply;
    uint256 public foundersSupply;
    uint256 public remainingSupply;

    address public owner;

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the token distribution based on percentages.
     */
    constructor() {
        owner = msg.sender;

        // Calculate token allocations
        teamSupply = (TOTAL_SUPPLY * TEAM_SUPPLY_PERCENTAGE) / 100;
        foundersSupply = (TOTAL_SUPPLY * FOUNDERS_SUPPLY_PERCENTAGE) / 100;
        remainingSupply = TOTAL_SUPPLY - teamSupply - foundersSupply;

        // Emit initial allocations as events
        emit TokensDistributed(address(0), teamSupply);    // Team allocation
        emit TokensDistributed(address(0), foundersSupply); // Founders allocation
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Distribute tokens to a recipient address.
     * @param recipient The address to receive the tokens.
     * @param amount The number of tokens to distribute.
     */
    function distributeTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(amount <= remainingSupply, "Insufficient remaining supply");

        // Deduct from remaining supply
        remainingSupply -= amount;

        // Emit distribution event
        emit TokensDistributed(recipient, amount);
    }
}
```
