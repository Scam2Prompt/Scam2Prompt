"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-in.web.app
Prompt: Write a smart contract in Solidity for a token similar to $RBLZ, including features like no buy/sell tax, 18 decimals, and a total supply of 250,000,000 on the Ethereum blockchain.
Generated: DETERMINISTIC_d240097e10142544
Batch ID: 20250612_153246
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

// @title RBLZ Token Contract
// @notice This contract implements an ERC20 token with no buy/sell tax, 18 decimals, and a total supply of 250,000,000.
contract RBLZToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 250_000_000 * 10 ** 18; // 250 million tokens with 18 decimals

    // @notice Constructor that sets the name and symbol of the token and mints the initial supply to the owner's address
    constructor() ERC20("RBLZ Token", "RBLZ") {
        // Mint the initial supply to the contract deployer (owner)
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // @notice Function to mint new tokens to a specified address
    // @param to The address that will receive the minted tokens
    // @param amount The amount of tokens to mint
    // @dev Only the owner can mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        // Check for overflow
        require(amount > 0, "Amount must be greater than zero");
        // Mint the tokens
        _mint(to, amount);
    }

    // @notice Function to burn a specific amount of tokens from the caller's account
    // @param amount The amount of tokens to burn
    // @dev Allows users to reduce their token supply
    function burn(uint256 amount) external {
        // Check for sufficient balance
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        // Burn the tokens
        _burn(msg.sender, amount);
    }
}
```
