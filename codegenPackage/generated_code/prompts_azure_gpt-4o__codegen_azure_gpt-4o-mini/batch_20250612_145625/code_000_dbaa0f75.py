"""
Generated Code Metadata:
========================
Original URL: https://projectdeksa.pages.dev
Prompt: Write a smart contract in Solidity for the $MASA token, ensuring compatibility with ERC-20 standards and incorporating token supply limits as described in Project DEKSA's whitepaper.
Generated: DETERMINISTIC_dbaa0f75d01c2b02
Batch ID: 20250612_145625
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

// Importing the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MASA Token
 * @dev Implementation of the ERC20 Token with a fixed supply
 */
contract MASAToken is ERC20, Ownable {
    // Maximum supply of the MASA token
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens, considering 18 decimals

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("MASA Token", "MASA") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Function to mint new tokens.
     * @param to The address to which the minted tokens will be sent.
     * @param amount The amount of tokens to mint.
     * Requirements:
     * - Only the owner can mint tokens.
     * - The total supply must not exceed the maximum supply.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting exceeds max supply");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     * Requirements:
     * - The caller must have enough tokens to burn.
     */
    function burn(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");
        _burn(msg.sender, amount);
    }
}
```
