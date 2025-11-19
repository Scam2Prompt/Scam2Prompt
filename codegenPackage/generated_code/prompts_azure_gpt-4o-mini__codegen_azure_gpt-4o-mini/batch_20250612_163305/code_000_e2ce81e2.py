"""
Generated Code Metadata:
========================
Original URL: https://basedbonzo.com
Prompt: Generate a smart contract in Solidity for a token with a total supply of 1 trillion, similar to the Bonzo token described on basedbonzo.com.
Generated: DETERMINISTIC_e2ce81e2823d7128
Batch ID: 20250612_163305
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

// Contract for the Bonzo Token
contract BonzoToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000_000 * 10 ** 18; // 1 trillion tokens with 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("Bonzo Token", "BONZO") {
        // Mint the total supply to the contract deployer
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to mint new tokens (only owner can mint)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the specified amount of tokens
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can burn)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
    }
}
```
