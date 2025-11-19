"""
Generated Code Metadata:
========================
Original URL: https://pepeofelon-swap-1.dexkit.app
Prompt: Generate a smart contract code for creating a new token on the Pepeofelon platform using Solidity.
Generated: DETERMINISTIC_2110221f07b56d7e
Batch ID: 20250622_204716
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

// Importing the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for creating a new token on the Pepeofelon platform
contract PepeofelonToken is ERC20, Ownable {
    // Initial supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("PepeofelonToken", "PEPE") {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to mint new tokens
    // Only the owner can mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the specified amount of tokens to the given address
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        // Burn the specified amount of tokens from the caller's account
        _burn(msg.sender, amount);
    }

    // Function to burn tokens from a specified account
    // Only the owner can burn tokens from another account
    function burnFrom(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot burn from the zero address");
        require(amount > 0, "Burn amount must be greater than zero");
        
        // Allowance check to ensure the owner has enough tokens to burn
        uint256 currentAllowance = allowance(account, msg.sender);
        require(currentAllowance >= amount, "Burn amount exceeds allowance");

        // Burn the specified amount of tokens from the given account
        _burn(account, amount);
        _approve(account, msg.sender, currentAllowance - amount);
    }
}
```
