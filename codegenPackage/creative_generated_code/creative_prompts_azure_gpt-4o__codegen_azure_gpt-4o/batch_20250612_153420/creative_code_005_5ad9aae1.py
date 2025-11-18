"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accept-gummyonsol.pages.dev
Prompt: Develop a Solidity smart contract that mimics the tokenomics structure of $GUMMY, including the specific allocation percentages (e.g., 30% for CEX liquidity, 10% for market makers).
Generated: DETERMINISTIC_5ad9aae1dcf6d494
Batch ID: 20250612_153420
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
 * @dev A smart contract to manage the tokenomics structure of $GUMMY.
 * Allocations:
 * - 30% for CEX liquidity
 * - 10% for market makers
 * - Remaining tokens managed by the contract owner.
 */
contract GummyTokenomics {

    // State variables
    address public owner; // Contract owner
    uint256 public totalSupply; // Total supply of tokens

    // Allocation percentages
    uint256 public constant CEX_LIQUIDITY_PERCENTAGE = 30; // 30% for CEX liquidity
    uint256 public constant MARKET_MAKERS_PERCENTAGE = 10; // 10% for market makers

    // Balances
    uint256 public cexLiquidityAllocation; // Tokens allocated for CEX liquidity
    uint256 public marketMakersAllocation; // Tokens allocated for market makers
    uint256 public ownerAllocation; // Remaining tokens allocated to the owner

    // Events
    event AllocationSet(
        uint256 cexLiquidityAllocation,
        uint256 marketMakersAllocation,
        uint256 ownerAllocation
    );
    event TokensDistributed(address recipient, uint256 amount);

    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");

        // Set owner
        owner = msg.sender;

        // Set total supply
        totalSupply = _totalSupply;

        // Calculate allocations
        cexLiquidityAllocation = (totalSupply * CEX_LIQUIDITY_PERCENTAGE) / 100;
        marketMakersAllocation = (totalSupply * MARKET_MAKERS_PERCENTAGE) / 100;
        ownerAllocation = totalSupply - cexLiquidityAllocation - marketMakersAllocation;

        emit AllocationSet(
            cexLiquidityAllocation,
            marketMakersAllocation,
            ownerAllocation
        );
    }

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to distribute tokens to a specific recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to distribute.
     */
    function distributeTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= ownerAllocation, "Insufficient owner allocation");

        // Deduct the amount from the owner allocation
        ownerAllocation -= amount;

        // Emit the transfer event
        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Function to update the contract owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
