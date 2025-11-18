"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-svd.vercel.app
Prompt: Write a script in Solidity to implement a minting function for a token named "FREE SHAVACADOO" that allows users to mint tokens to their wallet address.
Generated: DETERMINISTIC_2fbbb37b79954f10
Batch ID: 20250612_150440
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

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FREE SHAVACADOO Token
 * @dev Implementation of the ERC20 token with a minting function
 */
contract FreeShavacadoToken is ERC20, Ownable {
    // Token supply cap
    uint256 public constant MAX_SUPPLY = 1000000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("FREE SHAVACADOO", "SHAVA") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Mint new tokens to the specified address.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting exceeds max supply");

        // Mint the tokens
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }
}
```
