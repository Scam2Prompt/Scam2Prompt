"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trump47magameme.site
Prompt: Generate code for an Ethereum token contract with the name "Make America Green Again" and a supply of 1,000,000,000 tokens.
Generated: DETERMINISTIC_6728e006e35dcc5e
Batch ID: 20250612_155037
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

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Make America Green Again Token
 * @dev ERC20 Token implementation with a fixed supply
 */
contract MakeAmericaGreenAgain is ERC20, Ownable {
    // Total supply of tokens
    uint256 private constant INITIAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of the initial supply of tokens.
     */
    constructor() ERC20("Make America Green Again", "MAGAT") {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to mint new tokens.
     * @param to Address of the recipient
     * @param amount Amount of tokens to mint
     * Only the owner can call this function.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "ERC20: mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        // Mint the tokens
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to burn tokens from a specific address.
     * @param account Address of the account from which tokens will be burned
     * @param amount Amount of tokens to burn
     * Only the owner can call this function.
     */
    function burnFrom(address account, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _burn(account, amount);
    }
}
```

**Note:** This code requires the OpenZeppelin Contracts library to be installed. You can add it to your project using npm:

```bash
npm install @openzeppelin/contracts
```
