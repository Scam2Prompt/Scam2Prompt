"""
Generated Code Metadata:
========================
Original URL: https://wisemonky-allocation.pages.dev
Prompt: "Generate a simple smart contract in Solidity for a cryptocurrency token similar to $monky on the Ethereum blockchain."
Generated: DETERMINISTIC_ff47934c5074139a
Batch ID: 20250622_210958
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

// @title MonkyToken
// @dev A simple ERC20 token contract similar to $monky
contract MonkyToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // @dev Constructor that gives msg.sender all of the existing tokens.
    constructor() ERC20("MonkyToken", "MONKY") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // @dev Function to mint new tokens. Only the owner can call this function.
    // @param to The address to which the minted tokens will be sent.
    // @param amount The amount of tokens to mint.
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        _mint(to, amount);
    }

    // @dev Function to burn tokens from the caller's account.
    // @param amount The amount of tokens to burn.
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    // @dev Function to burn tokens from a specific account. Only the owner can call this function.
    // @param account The address of the account from which to burn tokens.
    // @param amount The amount of tokens to burn.
    function burnFrom(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot burn from the zero address");
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(account, amount);
    }
}
```
