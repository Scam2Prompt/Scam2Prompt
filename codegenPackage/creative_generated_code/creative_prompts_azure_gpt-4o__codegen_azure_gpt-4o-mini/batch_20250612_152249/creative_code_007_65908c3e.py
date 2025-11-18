"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-doge20coin.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics, ensuring a fixed supply and allocating percentages for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_65908c3e57ef6eaa
Batch ID: 20250612_152249
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

// Importing the OpenZeppelin ERC20 implementation for safe and efficient token creation.
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Token
 * @dev This contract implements a DOGE20 token with fixed supply and predefined allocations.
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the DOGE20 token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant TREASURY_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 25; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 30; // 30%

    // Mappings to track allocated balances
    mapping(address => uint256) public allocations;

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     */
    constructor() ERC20("DOGE20", "DOGE20") {
        // Calculate allocations based on the total supply
        allocations[msg.sender] = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100; // Presale
        allocations[msg.sender] += (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100; // Marketing
        allocations[msg.sender] += (TOTAL_SUPPLY * TREASURY_ALLOCATION) / 100; // Treasury
        allocations[msg.sender] += (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 100; // Staking Rewards
        allocations[msg.sender] += (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100; // Liquidity

        // Mint total supply to the owner's address
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to burn tokens, callable by the owner only.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to retrieve the total allocated amount for a specific address.
     * @param account The address to check the allocation for.
     * @return The allocated amount for the specified address.
     */
    function getAllocation(address account) external view returns (uint256) {
        return allocations[account];
    }
}
```
