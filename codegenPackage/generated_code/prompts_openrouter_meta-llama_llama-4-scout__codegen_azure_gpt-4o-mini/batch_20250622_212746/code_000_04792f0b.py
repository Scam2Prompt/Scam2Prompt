"""
Generated Code Metadata:
========================
Original URL: https://pepe-tokens.com
Prompt: Write a Solidity smart contract for a token with a 420T supply and 0% tax, similar to the Pepe Coin tokenomics.
Generated: DETERMINISTIC_04792f0b472668a1
Batch ID: 20250622_212746
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

// Contract for the PepeCoin token
contract PepeCoin is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 420 * 10**12 * 10**18; // 420 trillion tokens with 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("PepeCoin", "PEPE") {
        // Mint the total supply to the contract deployer
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to mint new tokens (only owner can mint)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the specified amount of tokens to the recipient
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
