"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Develop a Solidity contract that implements the tokenomics for $BCB, including features for burning tokens and managing circulating supply.
Generated: DETERMINISTIC_4d8625d79442a01a
Batch ID: 20250612_163616
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BCBToken
 * @dev Implementation of the BCB token with burn functionality and circulating supply management.
 */
contract BCBToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply) ERC20("BCB Token", "BCB") {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to burn tokens, reducing the total supply.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amount);
        
        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Override the _burn function to ensure proper accounting of total supply.
     * @param account The account from which to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function _burn(address account, uint256 amount) internal override {
        super._burn(account, amount);
    }

    /**
     * @dev Function to mint new tokens, can only be called by the owner.
     * @param account The account to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the tokens
        _mint(account, amount);
    }
}
```
