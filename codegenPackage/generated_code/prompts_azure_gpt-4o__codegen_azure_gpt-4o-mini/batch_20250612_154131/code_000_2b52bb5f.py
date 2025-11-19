"""
Generated Code Metadata:
========================
Original URL: https://ratotheratcoin.com
Prompt: Write a smart contract in Solidity that replicates the tokenomics of Rato the Rat ($RATO), including a supply of 420,690,000,000 tokens, no tax, and the contract address 0xf816507e690f5aa4e29d164885eb5fa7a5627860.
Generated: DETERMINISTIC_2b52bb5ffe7ea34e
Batch ID: 20250612_154131
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

// Importing the OpenZeppelin ERC20 contract for standard token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RatoToken
 * @dev Implementation of the Rato the Rat ($RATO) token
 */
contract RatoToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 420690000000 * 10 ** 18; // 420,690,000,000 tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("Rato the Rat", "$RATO") {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to mint new tokens. Only the owner can call this function.
     * @param account The address to which the minted tokens will be sent.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the specified amount of tokens to the account
        _mint(account, amount);
    }

    /**
     * @dev Function to burn tokens. Only the owner can call this function.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens from the owner's balance
        _burn(msg.sender, amount);
    }
}
```
