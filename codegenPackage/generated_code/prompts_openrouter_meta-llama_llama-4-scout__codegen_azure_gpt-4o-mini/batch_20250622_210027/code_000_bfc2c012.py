"""
Generated Code Metadata:
========================
Original URL: https://pepe20-vip.web.app
Prompt: Write a Solidity smart contract for a token named PEPE 2.0 with a fixed supply of 469,000,000,000,000 tokens.
Generated: DETERMINISTIC_bfc2c012d4e9ce16
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

// PEPE 2.0 Token Contract
contract PEPE2Token is ERC20, Ownable {
    // Fixed supply of tokens
    uint256 private constant INITIAL_SUPPLY = 469_000_000_000_000 * 10 ** 18; // 18 decimals

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("PEPE 2.0", "PEPE2") {
        // Mint the total supply to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to mint new tokens (only owner can mint)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        // Mint the specified amount of tokens to the given address
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can burn)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens from the owner's balance
        _burn(msg.sender, amount);
    }
}
```
