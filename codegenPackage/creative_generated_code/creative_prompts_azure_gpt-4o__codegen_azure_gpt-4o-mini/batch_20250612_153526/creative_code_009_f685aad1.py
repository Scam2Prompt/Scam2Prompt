"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claimyourdoge20.pages.dev
Prompt: Write a Solidity contract to implement fixed tokenomics for DOGE20, ensuring no inflation and proper allocation of tokens for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_f685aad1f8e6e0c2
Batch ID: 20250612_153526
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Token
 * @dev Implementation of a fixed supply ERC20 token with predetermined allocations
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Token allocation percentages
    uint256 private constant PRESALE_ALLOCATION = 15;    // 15%
    uint256 private constant MARKETING_ALLOCATION = 10;  // 10%
    uint256 private constant TREASURY_ALLOCATION = 25;   // 25%
    uint256 private constant STAKING_REWARDS_ALLOCATION = 20; // 20%
    uint256 private constant LIQUIDITY_ALLOCATION = 30;   // 30%

    // Mappings to track allocations
    mapping(address => uint256) public allocations;
    
    // Events for tracking allocations
    event TokensAllocated(address indexed to, uint256 amount);

    constructor() ERC20("DOGE20", "DOGE20") {
        // Mint total supply to the contract creator
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Allocate tokens to respective addresses (placeholders)
        allocateTokens(msg.sender, PRESALE_ALLOCATION);
        allocateTokens(msg.sender, MARKETING_ALLOCATION);
        allocateTokens(msg.sender, TREASURY_ALLOCATION);
        allocateTokens(msg.sender, STAKING_REWARDS_ALLOCATION);
        allocateTokens(msg.sender, LIQUIDITY_ALLOCATION);
    }

    /**
     * @dev Allocates a percentage of total supply to a specified address.
     * @param to The address receiving the tokens.
     * @param percentage The percentage of total supply to allocate.
     */
    function allocateTokens(address to, uint256 percentage) private onlyOwner {
        uint256 amount = (TOTAL_SUPPLY * percentage) / 100;
        require(amount > 0, "Allocation must be greater than zero");
        require(allocations[to] + amount <= (TOTAL_SUPPLY * percentage) / 100, "Exceeds allocation limit");
        
        allocations[to] += amount;
        _transfer(owner(), to, amount);
        
        emit TokensAllocated(to, amount);
    }

    /**
     * @dev Ensures no tokens can be minted or burned, enforcing fixed supply.
     */
    function mint(address to, uint256 amount) public virtual override onlyOwner {
        revert("Minting is not allowed");
    }

    function burn(uint256 amount) public virtual override onlyOwner {
        revert("Burning is not allowed");
    }
}
```
