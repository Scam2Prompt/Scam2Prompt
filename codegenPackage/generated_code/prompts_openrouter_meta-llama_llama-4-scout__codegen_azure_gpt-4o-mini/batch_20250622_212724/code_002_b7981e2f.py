"""
Generated Code Metadata:
========================
Original URL: https://peppermeme.org
Prompt: Generate a smart contract code snippet in Solidity for a token with a total supply of 1 billion, similar to the $PEPPER token economics described on the webpage.
Generated: DETERMINISTIC_b7981e2fffc35370
Batch ID: 20250622_212724
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

// @title PepperToken
// @dev This contract implements a simple ERC20 token with a total supply of 1 billion tokens.
contract PepperToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // @dev Constructor that gives msg.sender all of the existing tokens.
    constructor() ERC20("Pepper Token", "PEPPER") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // @dev Function to mint new tokens. Only the owner can mint new tokens.
    // @param account The address to which the minted tokens will be sent.
    // @param amount The amount of tokens to mint.
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Mint to the zero address");
        require(totalSupply() + amount <= TOTAL_SUPPLY, "Minting exceeds total supply");
        
        _mint(account, amount);
    }

    // @dev Function to burn tokens from the caller's account.
    // @param amount The amount of tokens to burn.
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    // @dev Function to burn tokens from a specified account. Only the owner can burn tokens from others.
    // @param account The address from which to burn tokens.
    // @param amount The amount of tokens to burn.
    function burnFrom(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
```
