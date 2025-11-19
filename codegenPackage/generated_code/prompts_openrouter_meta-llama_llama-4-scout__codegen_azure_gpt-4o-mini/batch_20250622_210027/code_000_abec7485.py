"""
Generated Code Metadata:
========================
Original URL: https://spyro-io.pages.dev
Prompt: Write a Solidity contract for an ERC-20 token with a supply of 1,000,000,000,000 and 0% taxes, similar to $SPYRO.
Generated: DETERMINISTIC_abec7485f925c16d
Batch ID: 20250622_210027
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

// Importing the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the ERC20 token
contract SpyroToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000_000_000 * 10 ** 18; // 1 trillion tokens with 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("Spyro Token", "SPYRO") {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to mint new tokens (only owner can call this)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the specified amount of tokens
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can call this)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
    }
}
```
