"""
Generated Code Metadata:
========================
Original URL: https://wallstreet-pepe.vercel.app
Prompt: Generate a smart contract code snippet in Solidity to create a simple tokenomics system for $WEPE Token with a total supply of 200,000,000,000 $WEPE.
Generated: DETERMINISTIC_1d5823ca0c111694
Batch ID: 20250622_212351
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

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the $WEPE Token
contract WEPE is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 200_000_000_000 * 10 ** 18; // 200 billion tokens with 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("$WEPE Token", "WEPE") {
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
