"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Develop a Solidity contract that implements the tokenomics for $BCB, including features for burning tokens and managing circulating supply.
Generated: DETERMINISTIC_4d8625d79442a01a
Batch ID: 20250612_163616
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
 * @title BCBToken
 * @dev Implementation of the $BCB token with burn functionality and circulating supply management.
 */
contract BCBToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Total supply of tokens
    uint256 private _totalSupply;

    /**
     * @dev Constructor that gives the deployer all initial tokens.
     * @param initialSupply The initial supply of tokens to deploy.
     */
    constructor(uint256 initialSupply) ERC20("BCB Token", "BCB") {
        require(initialSupply > 0, "Initial supply must be greater than zero.");
        _mint(msg.sender, initialSupply);
        _totalSupply = initialSupply;
    }

    /**
     * @dev Override the totalSupply method to return the correct circulating supply.
     * @return The total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Function to burn tokens.
     * @param amount The amount of tokens to be burned.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn.");

        // Reducing the total supply and burning the tokens from the sender's balance
        _burn(msg.sender, amount);
        _totalSupply -= amount;

        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Function to retrieve the circulating supply.
     * @return The circulating supply of the token.
     */
    function circulatingSupply() public view returns (uint256) {
        return totalSupply() - balanceOf(address(this)); // Adjusting for tokens held by the contract itself
    }

    /**
     * @dev Function to mint new tokens (only owner).
     * @param amount The amount of new tokens to mint.
     */
    function mint(uint256 amount) external onlyOwner {
        require(amount > 0, "Minting amount must be greater than zero.");

        // Minting new tokens and increasing total supply
        _mint(msg.sender, amount);
        _totalSupply += amount;
    }
}
```
