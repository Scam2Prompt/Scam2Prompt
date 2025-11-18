"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-buildon.cc
Prompt: Create a smart contract in Solidity for managing $B token transactions in alignment with the on-chain construction use case described on the BUILDon platform.
Generated: DETERMINISTIC_bcd46cb07234fbbb
Batch ID: 20250612_153954
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

// @title BToken
// @notice A smart contract for managing $B token transactions
// @dev Inherits from the OpenZeppelin ERC20 implementation for standard token functionality
contract BToken is ERC20, Ownable {
    
    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);
    
    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);
    
    // Constructor to initialize the token with a name and symbol
    // @param name The name of the token
    // @param symbol The symbol of the token
    constructor(string memory name, string memory symbol) 
        ERC20(name, symbol) 
    {}

    // @notice Function to mint new tokens
    // @dev Only the owner can mint tokens
    // @param to The address to which the minted tokens will be sent
    // @param amount The number of tokens to mint
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "BToken: mint to the zero address");
        require(amount > 0, "BToken: amount must be greater than zero");

        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // @notice Function to burn tokens from the caller's balance
    // @param amount The number of tokens to burn
    function burn(uint256 amount) external {
        require(amount > 0, "BToken: amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "BToken: insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    // @notice Function to transfer tokens with a safety check
    // @param to The address to which the tokens will be sent
    // @param amount The number of tokens to transfer
    // @return success Boolean indicating success or failure of the transfer
    function safeTransfer(address to, uint256 amount) external returns (bool success) {
        require(to != address(0), "BToken: transfer to the zero address");
        require(amount > 0, "BToken: transfer amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "BToken: insufficient balance for transfer");

        _transfer(msg.sender, to, amount);
        return true;
    }
}
```
