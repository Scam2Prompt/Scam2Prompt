"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: Generate a code snippet that demonstrates how to tokenize shares of Spiko MMFs for storage in a wallet using Ethereum smart contracts.
Generated: DETERMINISTIC_5ad2bc85abbb05eb
Batch ID: 20250612_164305
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

// @title Spiko MMF Token Contract
// @dev This contract allows the creation and management of Spiko MMF tokens
contract SpikoMMFToken is ERC20, Ownable {
    // @dev Event emitted when tokens are minted
    event TokensMinted(address indexed user, uint256 amount);
    
    // @dev Event emitted when tokens are burned
    event TokensBurned(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Spiko MMF Token", "SPMMF") {}

    // @dev Function to mint new tokens
    // @param amount The amount of tokens to mint
    function mintTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _mint(msg.sender, amount);
        emit TokensMinted(msg.sender, amount);
    }

    // @dev Function to burn tokens from the caller's account
    // @param amount The amount of tokens to burn
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }
    
    // @dev Function to transfer tokens between addresses
    // @param to The address to transfer tokens to
    // @param amount The amount of tokens to transfer
    function transferTokens(address to, uint256 amount) external {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to transfer");
        _transfer(msg.sender, to, amount);
    }
}
```
