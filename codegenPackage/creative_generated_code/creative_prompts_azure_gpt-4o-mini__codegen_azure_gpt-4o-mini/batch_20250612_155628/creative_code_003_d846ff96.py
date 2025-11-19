"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fartcoinsol.org
Prompt: What are the best practices for implementing Fartcoin's smart contracts in a decentralized application?
Generated: DETERMINISTIC_d846ff9634394816
Batch ID: 20250612_155628
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
 * @title Fartcoin
 * @dev Implementation of the Fartcoin ERC20 Token
 */
contract Fartcoin is ERC20, Ownable {
    // Event to log token minting
    event TokensMinted(address indexed to, uint256 amount);
    
    // Event to log token burning
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all existing tokens.
     */
    constructor() ERC20("Fartcoin", "FART") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Initial supply
    }

    /**
     * @dev Function to mint new tokens.
     * @param to The address that will receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0"); // Ensure valid amount
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Function to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0"); // Ensure valid amount
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Override the _transfer function to implement additional checks.
     */
    function _transfer(address from, address to, uint256 amount) internal override {
        require(from != address(0), "Transfer from the zero address"); // Check sender's address
        require(to != address(0), "Transfer to the zero address"); // Check recipient's address
        require(amount > 0, "Transfer amount must be greater than 0"); // Ensure valid amount

        super._transfer(from, to, amount);
    }
}
```
